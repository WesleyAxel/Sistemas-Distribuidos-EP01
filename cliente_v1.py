import grpc
import server_pb2
import server_pb2_grpc
import re

# VALIDAÇÃO DO NOME INSERIDO PELO CLIENTE
def validar_nome(nome):
    if len(nome) > 20:
        return False
    if re.search(r'\W', nome):  
        return False
    return True

# FUNÇÃO CRIADA PARA QUE SEJA FEITA A CRIAÇÃO DE CANAL
def criar_canal(stub, nome_usuario):
    nome_canal = input("Digite o nome do canal: ")
    tipo_canal = int(input("Digite o tipo do canal (0 para Simples, 1 para Multiplo): "))
    response = stub.Criar(server_pb2.CriarCanalRequest(nome=nome_canal, tipo_canal=tipo_canal, nome_criador=nome_usuario))
    print(response.mensagem)

# FUNÇÃO CRIADA PARA QUE SEJA FEITA A REMOÇÃO DE CANAL
def remover_canal(stub, nome_usuario):
    nome_canal = input("Digite o nome do canal a ser removido: ")
    response = stub.Remover(server_pb2.RemoverCanalRequest(nome=nome_canal, nome_criador=nome_usuario))
    print(response.mensagem)

# FUNÇÃO CRIADA PARA QUE SEJA FEITA A ASSINATURA DE CANAL
def assinar_canal():
    print('IMPLEMENTAR')

# FUNÇÃO CRIADA PARA QUE SEJA FEITA A REMOÇÃO DA ASSINATURA DE CANAL
def desassinar_canal():
    print('IMPLEMENTAR')

# FUNÇÃO CRIADA PARA QUE SEJA ENVIAR MENSAGEM A UM CANAL
def enviar_mensagem(stub, nome_usuario):
    nome_canal = input("Digite o nome do canal: ")
    mensagem = input("Digite a mensagem: ")
    response = stub.ReceberMensagem(server_pb2.MensagemRequest(nome_canal=nome_canal, nome_criador=nome_usuario, mensagem=mensagem))
    print(response.mensagem)

def run():
    nome_usuario = ""
    while True:
        nome_usuario = input("Digite seu nome (até 20 caracteres, sem caracteres especiais): ")
        if validar_nome(nome_usuario):
            break
        else:
            print("Nome inválido. Por favor, tente novamente.")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = server_pb2_grpc.GreeterStub(channel)
        while True:
            print("\nMenu:")
            print("1. Criar canal")
            print("2. Remover canal")
            print("3. Assinar canal")
            print("4. Desassinar canal")
            print("5. Enviar mensagem")
            print("6. Sair")
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                criar_canal(stub, nome_usuario)
            elif escolha == "2":
                remover_canal(stub, nome_usuario)
            elif escolha == "3":
                assinar_canal()
            elif escolha == "4":
                desassinar_canal()
            elif escolha == "5":
                enviar_mensagem(stub, nome_usuario)
            elif escolha == "6":
                break
            else:
                print("Opção inválida!")

if __name__ == '__main__':
    run()