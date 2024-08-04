import unittest
from unittest.mock import MagicMock, patch
from cliente_v1 import validar_nome, criar_canal, remover_canal, assinar_canal, desassinar_canal, enviar_mensagem, receber_mensagemMultiplas, receber_mensagemUnica

class TestCliente(unittest.TestCase):
    def test_validar_nome(self):
        self.assertTrue(validar_nome("UsuarioValido"))  # Nome válido
        self.assertFalse(validar_nome("NomeMuitoLongoNaoValidoPorqueTemMaisDeVinteCaracteres"))  # Nome muito longo
        self.assertFalse(validar_nome("Nome_Invalido!"))  # Nome com caracteres especiais

class TestClienteServerInteractions(unittest.TestCase):
    def setUp(self):
        self.stub = MagicMock()
        self.nome_usuario = "UsuarioValido"

    @patch('builtins.input', side_effect=["CanalTeste", "0"])
    def test_criar_canal(self, mock_input):
        self.stub.Criar.return_value = MagicMock(mensagem="Canal criado com sucesso")
        criar_canal(self.stub, self.nome_usuario)
        self.stub.Criar.assert_called_once()

    @patch('builtins.input', return_value="CanalTeste")
    def test_remover_canal(self, mock_input):
        self.stub.Remover.return_value = MagicMock(mensagem="Canal removido com sucesso")
        remover_canal(self.stub, self.nome_usuario)
        self.stub.Remover.assert_called_once()

    @patch('builtins.input', return_value="CanalTeste")
    def test_assinar_canal(self, mock_input):
        self.stub.AssinarCanal.return_value = MagicMock(mensagem="Assinado com sucesso")
        assinar_canal(self.stub, self.nome_usuario)
        self.stub.AssinarCanal.assert_called_once()

    @patch('builtins.input', return_value="CanalTeste")
    def test_desassinar_canal(self, mock_input):
        self.stub.RemoverAssinaturaCanal.return_value = MagicMock(mensagem="Desassinado com sucesso")
        desassinar_canal(self.stub, self.nome_usuario)
        self.stub.RemoverAssinaturaCanal.assert_called_once()


    @patch('builtins.input', side_effect=["CanalTeste", "Mensagem de Teste"])
    def test_enviar_mensagem(self, mock_input):
        self.stub.ReceberMensagem.return_value = MagicMock(mensagem="Mensagem enviada")
        enviar_mensagem(self.stub, self.nome_usuario)
        self.stub.ReceberMensagem.assert_called_once()

    def test_receber_mensagemMultiplas(self):
        self.stub.EnviarMensagensStream.return_value = iter([
            MagicMock(nome_canal="CanalTeste", mensagem="Mensagem 1"),
            MagicMock(nome_canal="CanalTeste", mensagem="Mensagem 2")
        ])
        with patch('builtins.print') as mocked_print:
            receber_mensagemMultiplas(self.stub, self.nome_usuario)
            mocked_print.assert_any_call("Canal: CanalTeste, Mensagem do canal: Mensagem 1")
            mocked_print.assert_any_call("Canal: CanalTeste, Mensagem do canal: Mensagem 2")

    def test_receber_mensagemUnica(self):
        self.stub.EnviarMensagemUnica.return_value = MagicMock(nome_canal="CanalTeste", mensagem="Mensagem única")
        with patch('builtins.print') as mocked_print:
            receber_mensagemUnica(self.stub, self.nome_usuario)
            mocked_print.assert_called_with("Canal: CanalTeste, Mensagem do canal: Mensagem única")

if __name__ == '__main__':
    unittest.main()

