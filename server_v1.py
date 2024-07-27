
from concurrent import futures
import random
import grpc
import logging
import sqlite3
import server_pb2
import server_pb2_grpc

from collections import defaultdict

DATABASE_CANAIS = 'canais.db'
DATABASE_MENSAGENS = 'mensagens.db'
DATABASE_ASSINATURAS = 'assinaturas.db'

# inicialização do database de canais e criação caso ele não exista
def init_db_canais():
    conn = sqlite3.connect(DATABASE_CANAIS)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS canais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL UNIQUE,
            tipo_canal INTEGER NOT NULL,
            nome_criador TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# inicialização do database de mensagens e criação caso ele não exista
def init_db_mensagens():
    conn = sqlite3.connect(DATABASE_MENSAGENS)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_canal TEXT NOT NULL,
            nome_criador TEXT NOT NULL,
            mensagem TEXT NOT NULL,
            enviada BOOLEAN NOT NULL DEFAULT 0,
            FOREIGN KEY(nome_canal) REFERENCES canais(nome)
        )
    ''')
    conn.commit()
    conn.close()

# inicialização do database de assinaturas de canais
def init_db_assinaturas():
    conn = sqlite3.connect(DATABASE_ASSINATURAS)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS assinaturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_canal TEXT NOT NULL,
            cliente TEXT NOT NULL,
            FOREIGN KEY(nome_canal) REFERENCES canais(nome)
        )
    ''')
    conn.commit()
    conn.close()

# Implementando o serviço do servidor
class Greeter(server_pb2_grpc.GreeterServicer):
    def __init__(self):
        self.assinantes = defaultdict(set)
        self.load_assinaturas()  

    # carrega todas as assinturas já feitas
    def load_assinaturas(self):
        conn = sqlite3.connect(DATABASE_ASSINATURAS)
        cursor = conn.cursor()
        cursor.execute('SELECT nome_canal, cliente FROM assinaturas')
        assinaturas = cursor.fetchall()
        conn.close()
        
        for nome_canal, cliente in assinaturas:
            self.assinantes[nome_canal].add(cliente)

    ## CRIAÇÃO DE CANAL
    def Criar(self, request, context):
        # Separa variaveis da requisição de criação de canal
        nome = request.nome
        tipo_canal = request.tipo_canal
        nome_criador = request.nome_criador

        # Verifica se o canal já existe no banco de dados
        conn = sqlite3.connect(DATABASE_CANAIS)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM canais WHERE nome = ?', (nome,))
        if cursor.fetchone()[0] > 0:
            conn.close()
            return server_pb2.ResponseCriarCanal(mensagem=f"Falha ao criar canal: Canal com nome '{nome}' já existe.")
        
       # Salva no banco de dados a informação do novo canal criado
        cursor.execute('INSERT INTO canais (nome, tipo_canal, nome_criador) VALUES (?, ?, ?)', (nome, tipo_canal, nome_criador))
        conn.commit()
        
        # Consulta todos os canais criados após a criação de um novo
        cursor.execute('SELECT nome, tipo_canal, nome_criador FROM canais')
        canais = cursor.fetchall()
        conn.close()

        mensagem = f"Canal criado: nome={nome}, tipo_canal={tipo_canal}, nome_criador={nome_criador}. Total de canais: {len(canais)}"
        
        # Imprime no console todos os canais para checagem
        print(mensagem)
        print("Lista de canais no servidor:")
        for canal in canais:
            print(f"Nome: {canal[0]}, Tipo: {canal[1]}, Nome do Criador: {canal[2]}")

        return server_pb2.ResponseCriarCanal(mensagem=mensagem)
    
    ## EXCLUIR CANAL CRIADO
    def Remover(self, request, context):
        # Separa variaveis da requisição de remoção de canal
        nome = request.nome
        nome_criador = request.nome_criador
        
        # Verifica e remove do banco de dados
        conn = sqlite3.connect(DATABASE_CANAIS)
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

        # Imprime no console todos os canais para checagem
        print(mensagem)
        print("Lista de canais no servidor:")
        for canal in canais:
            print(f"Nome: {canal[0]}, Tipo: {canal[1]}, Nome do Criador: {canal[2]}")
        
        return server_pb2.RemoverCanalResponse(mensagem=mensagem)
    
    ## ENVIO DE MENSAGEM DO CLIENTE PARA O SERVIDOR
    def ReceberMensagem(self, request, context):
        nome_canal = request.nome_canal
        nome_criador = request.nome_criador
        mensagem = request.mensagem
        
        # Verifica se o canal existe e se o criador é o dono do canal
        conn = sqlite3.connect(DATABASE_CANAIS)
        cursor = conn.cursor()
        cursor.execute('SELECT nome_criador FROM canais WHERE nome = ?', (nome_canal,))
        result = cursor.fetchone()
        
        if result and result[0] == nome_criador:
            # Salva a mensagem no banco de dados
            conn_mensagens = sqlite3.connect(DATABASE_MENSAGENS)
            cursor_mensagens = conn_mensagens.cursor()
            cursor_mensagens.execute('INSERT INTO mensagens (nome_canal, nome_criador, mensagem, enviada) VALUES (?, ?, ?, ?)', (nome_canal, nome_criador, mensagem, 0))
            conn_mensagens.commit()
            conn_mensagens.close()

            resposta = f"Mensagem enviada ao canal '{nome_canal}' por '{nome_criador}'."
        else:
            resposta = f"Falha ao enviar receber mensagem: Canal '{nome_canal}' não encontrado ou '{nome_criador}' não é o autor."
        
        # Imprime no console
        print(resposta)
        
        return server_pb2.MensagemResponse(mensagem=resposta)
    
# Inicialização do servidor
def serve():

    init_db_canais()
    init_db_mensagens()
    init_db_assinaturas()
    
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
