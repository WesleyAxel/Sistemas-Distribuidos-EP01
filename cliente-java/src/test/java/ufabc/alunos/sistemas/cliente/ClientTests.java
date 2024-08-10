package ufabc.alunos.sistemas.cliente;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.ArgumentCaptor;
import org.mockito.InjectMocks;
import ufabc.aluno.sistemas.cliente.*;
import ufabc.alunos.sistemas.cliente.util.Cliente;
import io.grpc.ManagedChannel;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.stubbing.Answer;

import java.util.Iterator;
import java.util.Scanner;

public class ClientTests {
    //@Mock
    //private GreeterGrpc.GreeterBlockingStub blockingStub;

    //@Mock
    //private ManagedChannel channel;

    //@InjectMocks
    //private Cliente cliente;

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
        // Simula as entradas do Scanner
        when(scannerMock.nextLine()).thenReturn("TestChannel");
        when(scannerMock.nextInt()).thenReturn(0);

        // Simula o comportamento do método criar
        ResponseCriarCanal responseMock = ResponseCriarCanal.newBuilder()
                .setMensagem("Canal criado com sucesso")
                .build();
        when(blockingStubMock.criar(any(CriarCanalRequest.class))).thenReturn(responseMock);

        // Substitui o System.in por Scanner simulado e chama o método
        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n0\n".getBytes()));
        cliente.criarCanal("TestUser");

        // Verifica se o método criar foi chamado com os parâmetros corretos
        ArgumentCaptor<CriarCanalRequest> requestCaptor = ArgumentCaptor.forClass(CriarCanalRequest.class);
        verify(blockingStubMock).criar(requestCaptor.capture());
        CriarCanalRequest actualRequest = requestCaptor.getValue();

        // Verifica se o nome do canal e o tipo foram capturados corretamente
        assertEquals("TestChannel", actualRequest.getNome());
        assertEquals(TipoCanal.SIMPLES, actualRequest.getTipoCanal());
        assertEquals("TestUser", actualRequest.getNomeCriador());
    }

    @Test
    public void testRemoverCanal() {
        // Simula as entradas do Scanner
        when(scannerMock.nextLine()).thenReturn("TestChannel");

        // Simula o comportamento do método remover
        RemoverCanalResponse responseMock = RemoverCanalResponse.newBuilder()
                .setMensagem("Canal removido com sucesso")
                .build();
        when(blockingStubMock.remover(any(RemoverCanalRequest.class))).thenReturn(responseMock);

        // Substitui o System.in por Scanner simulado e chama o método
        System.setIn(new java.io.ByteArrayInputStream("TestChannel\n".getBytes()));
        cliente.removerCanal("TestUser");

        // Verifica se o método remover foi chamado com os parâmetros corretos
        ArgumentCaptor<RemoverCanalRequest> requestCaptor = ArgumentCaptor.forClass(RemoverCanalRequest.class);
        verify(blockingStubMock).remover(requestCaptor.capture());
        RemoverCanalRequest actualRequest = requestCaptor.getValue();

        // Verifica se o nome do canal e o criador foram capturados corretamente
        assertEquals("TestChannel", actualRequest.getNome());
        assertEquals("TestUser", actualRequest.getNomeCriador());
    }
}