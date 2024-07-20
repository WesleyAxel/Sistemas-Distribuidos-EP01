
from concurrent import futures
import grpc
import logging
import sqlite3
import server_pb2
import server_pb2_grpc

DATABASE = 'canais.db'

# inicialização do database se ele não existe
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS canais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo_canal INTEGER NOT NULL,
            nome_criador TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Implementando o serviço de criação e remoção de canais
class Greeter(server_pb2_grpc.GreeterServicer):
    def __init__(self):
        # Inicializa a lista de canais
        self.canais = []

    def Criar(self, request, context):
        # Separa variaveis da requisição de criação de canal
        nome = request.nome
        tipo_canal = request.tipo_canal
        nome_criador = request.nome_criador

       # Salva no banco de dados a informação do novo canal criado
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO canais (nome, tipo_canal, nome_criador) VALUES (?, ?, ?)', (nome, tipo_canal, nome_criador))
        conn.commit()
        
        # Consulta todos os canais criados após a criação de um novo
        cursor.execute('SELECT nome, tipo_canal, nome_criador FROM canais')
        canais = cursor.fetchall()
        conn.close()

        mensagem = f"Canal criado: nome={nome}, tipo_canal={tipo_canal}, nome_criador={nome_criador}. Total de canais: {len(canais)}"
        
        # Imprime no console
        print(mensagem)
        print("Lista de canais criados:")
        for canal in canais:
            print(f"Nome: {canal[0]}, Tipo: {canal[1]}, Nome do Criador: {canal[2]}")

        return server_pb2.ResponseCriarCanal(mensagem=mensagem)
    
    def Remover(self, request, context):
        # Separa variaveis da requisição de remoção de canal
        nome = request.nome
        nome_criador = request.nome_criador
        
        # Verifica e remove do banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT nome_criador FROM canais WHERE nome = ?', (nome,))
        result = cursor.fetchone()
        
        if result and result[0] == nome_criador:
            cursor.execute('DELETE FROM canais WHERE nome = ?', (nome,))
            conn.commit()
            mensagem = f"Canal '{nome}' removido com sucesso pelo o autor '{nome_criador}'."
        else:
            mensagem = f"Falha ao remover: Canal '{nome}' não encontrado ou '{nome_criador}' não é o autor do canal."
        
        # Consulta todos os canais criados após remoção
        cursor.execute('SELECT nome, tipo_canal, nome_criador FROM canais')
        canais = cursor.fetchall()
        conn.close()

        # Imprime no console todos os canais
        print(mensagem)
        print("Lista de canais criados:")
        for canal in canais:
            print(f"Nome: {canal[0]}, Tipo: {canal[1]}, Nome do Criador: {canal[2]}")
        
        return server_pb2.RemoverCanalResponse(mensagem=mensagem)

# Inicialização do servidor
def serve():

    init_db()

    porta = "50051"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:" + porta)
    server.start()
    print("Servidor inicializando na porta " + porta)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
