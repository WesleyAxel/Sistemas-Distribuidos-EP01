import grpc
import server_pb2
import server_pb2_grpc

# primeiro teste de cliente que inicializa e envia duas requisiçoes de canais criados

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = server_pb2_grpc.GreeterStub(channel)
        response = stub.Criar(server_pb2.CriarCanalRequest(nome='CANAL_EXEMPLO_1', tipo_canal=server_pb2.SIMPLES, nome_criador='Wesley1'))
        print(f"Resposta do servidor: {response.mensagem}")
        response = stub.Criar(server_pb2.CriarCanalRequest(nome='CANAL_EXEMPLO_2', tipo_canal=server_pb2.MULTIPLO, nome_criador='Wesley2'))
        print(f"Resposta do servidor: {response.mensagem}")

        # Removendo canais
        response = stub.Remover(server_pb2.RemoverCanalRequest(nome='CANAL_EXEMPLO_1', nome_criador='Wesley1'))
        print(f"Response: {response.mensagem}")
        response = stub.Remover(server_pb2.RemoverCanalRequest(nome='CANAL_EXEMPLO_2', nome_criador='Wesley1'))  # Tentativa de remoção por um usuário não criador
        print(f"Response: {response.mensagem}")

if __name__ == '__main__':
    run()