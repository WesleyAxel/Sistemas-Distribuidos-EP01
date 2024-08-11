package ufabc.alunos.sistemas.cliente;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.*;
import ufabc.aluno.sistemas.cliente.*;
import ufabc.alunos.sistemas.cliente.util.Cliente;
import io.grpc.ManagedChannel;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

import java.util.Iterator;
import java.util.Scanner;

public class ClientTests {

    private Cliente cliente;
    private GreeterGrpc.GreeterBlockingStub blockingStubMock;
    private ManagedChannel channelMock;
    private Scanner scannerMock;

    @BeforeEach
    void setUp() {
        channelMock = mock(ManagedChannel.class);
        blockingStubMock = mock(GreeterGrpc.GreeterBlockingStub.class);
        scannerMock = mock(Scanner.class);

        cliente = new Cliente(channelMock);
        cliente.blockingStub = blockingStubMock;
    }

    @Test
    void testValidarNome() {
        assertTrue(Cliente.validarNome("UsuarioValido")); // Nome válido
        assertFalse(Cliente.validarNome("NomeMuitoLongoNaoValidoPorqueTemMaisDeVinteCaracteres")); // Nome muito longo
    }

    @Test
    public void testCriarCanal() {
        when(scannerMock.nextLine()).thenReturn("TestChannel");
        when(scannerMock.nextInt()).thenReturn(0);

        ResponseCriarCanal responseMock = ResponseCriarCanal.newBuilder()
                .setMensagem("Canal criado com sucesso")
                .build();
        when(blockingStubMock.criar(any(CriarCanalRequest.class))).thenReturn(responseMock);

        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n0\n".getBytes()));
        cliente.criarCanal("TestUser");

        ArgumentCaptor<CriarCanalRequest> requestCaptor = ArgumentCaptor.forClass(CriarCanalRequest.class);
        verify(blockingStubMock).criar(requestCaptor.capture());
        CriarCanalRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestChannel", actualRequest.getNome());
        assertEquals(TipoCanal.SIMPLES, actualRequest.getTipoCanal());
        assertEquals("TestUser", actualRequest.getNomeCriador());
    }

    @Test
    public void testRemoverCanal() {
        when(scannerMock.nextLine()).thenReturn("TestChannel");

        RemoverCanalResponse responseMock = RemoverCanalResponse.newBuilder()
                .setMensagem("Canal removido com sucesso")
                .build();
        when(blockingStubMock.remover(any(RemoverCanalRequest.class))).thenReturn(responseMock);

        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n".getBytes()));
        cliente.removerCanal("TestUser");

        ArgumentCaptor<RemoverCanalRequest> requestCaptor = ArgumentCaptor.forClass(RemoverCanalRequest.class);
        verify(blockingStubMock).remover(requestCaptor.capture());
        RemoverCanalRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestChannel", actualRequest.getNome());
        assertEquals("TestUser", actualRequest.getNomeCriador());
    }

    @Test
    public void testAssinarCanal() {
        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n".getBytes()));

        ResponseAssinarCanal responseMock = ResponseAssinarCanal.newBuilder()
                .setMensagem("Assinatura realizada com sucesso")
                .build();
        when(blockingStubMock.assinarCanal(any(AssinarCanalRequest.class))).thenReturn(responseMock);

        cliente.assinarCanal("TestUser");

        ArgumentCaptor<AssinarCanalRequest> requestCaptor = ArgumentCaptor.forClass(AssinarCanalRequest.class);
        verify(blockingStubMock).assinarCanal(requestCaptor.capture());
        AssinarCanalRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestChannel", actualRequest.getNomeCanal());
        assertEquals("TestUser", actualRequest.getNomeCriador());
        assertEquals("Assinatura realizada com sucesso", responseMock.getMensagem());
    }

    @Test
    public void testDesassinarCanal() {
        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n".getBytes()));

        ResponseRemoverAssinaturaCanal responseMock = ResponseRemoverAssinaturaCanal.newBuilder()
                .setMensagem("Assinatura removida com sucesso")
                .build();
        when(blockingStubMock.removerAssinaturaCanal(any(RemoverAssinaturaCanalRequest.class))).thenReturn(responseMock);

        cliente.desassinarCanal("TestUser");

        ArgumentCaptor<RemoverAssinaturaCanalRequest> requestCaptor = ArgumentCaptor.forClass(RemoverAssinaturaCanalRequest.class);
        verify(blockingStubMock).removerAssinaturaCanal(requestCaptor.capture());
        RemoverAssinaturaCanalRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestChannel", actualRequest.getNomeCanal());
        assertEquals("TestUser", actualRequest.getNomeCriador());
        assertEquals("Assinatura removida com sucesso", responseMock.getMensagem());
    }

    @Test
    public void testEnviarMensagem() {
        System.setIn(new java.io.ByteArrayInputStream("TestChannel\nHello, world!\n".getBytes()));

        MensagemResponse responseMock = MensagemResponse.newBuilder()
                .setMensagem("Mensagem enviada com sucesso")
                .build();
        when(blockingStubMock.receberMensagem(any(MensagemRequest.class))).thenReturn(responseMock);

        cliente.enviarMensagem("TestUser");

        ArgumentCaptor<MensagemRequest> requestCaptor = ArgumentCaptor.forClass(MensagemRequest.class);
        verify(blockingStubMock).receberMensagem(requestCaptor.capture());
        MensagemRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestChannel", actualRequest.getNomeCanal());
        assertEquals("TestUser", actualRequest.getNomeCriador());
        assertEquals("Hello, world!", actualRequest.getMensagem());
        assertEquals("Mensagem enviada com sucesso", responseMock.getMensagem());
    }

    @Test
    public void testReceberMensagensMultiplas() {
        MensagemStreamResponse responseMock1 = MensagemStreamResponse.newBuilder()
                .setNomeCanal("Channel1")
                .setMensagem("Mensagem 1")
                .build();
        MensagemStreamResponse responseMock2 = MensagemStreamResponse.newBuilder()
                .setNomeCanal("Channel2")
                .setMensagem("Mensagem 2")
                .build();
        Iterator<MensagemStreamResponse> responseIteratorMock = Mockito.mock(Iterator.class);
        when(responseIteratorMock.hasNext()).thenReturn(true, true, false);
        when(responseIteratorMock.next()).thenReturn(responseMock1, responseMock2);
        when(blockingStubMock.enviarMensagensStream(any(EnviarMensagensStreamRequest.class))).thenReturn(responseIteratorMock);

        cliente.receberMensagensMultiplas("TestUser");

        ArgumentCaptor<EnviarMensagensStreamRequest> requestCaptor = ArgumentCaptor.forClass(EnviarMensagensStreamRequest.class);
        verify(blockingStubMock).enviarMensagensStream(requestCaptor.capture());
        EnviarMensagensStreamRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestUser", actualRequest.getNomeCliente());
    }

    @Test
    public void testReceberMensagemUnica() {
        ResponseMensagemUnica responseMock = ResponseMensagemUnica.newBuilder()
                .setNomeCanal("TestChannel")
                .setMensagem("Mensagem única")
                .build();
        when(blockingStubMock.enviarMensagemUnica(any(EnviarMensagemUnicaRequest.class))).thenReturn(responseMock);

        cliente.receberMensagemUnica("TestUser");

        ArgumentCaptor<EnviarMensagemUnicaRequest> requestCaptor = ArgumentCaptor.forClass(EnviarMensagemUnicaRequest.class);
        verify(blockingStubMock).enviarMensagemUnica(requestCaptor.capture());
        EnviarMensagemUnicaRequest actualRequest = requestCaptor.getValue();

        assertEquals("TestUser", actualRequest.getNomeCliente());
        assertEquals("TestChannel", responseMock.getNomeCanal());
        assertEquals("Mensagem única", responseMock.getMensagem());
    }
}