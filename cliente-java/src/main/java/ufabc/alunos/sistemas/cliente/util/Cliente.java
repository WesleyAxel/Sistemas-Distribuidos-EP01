package ufabc.alunos.sistemas.cliente.util;

import java.util.Scanner;
import java.util.Iterator;
import java.util.regex.Pattern;

import io.grpc.ManagedChannel;
import ufabc.alunos.sistemas.cliente.*;

public class Cliente {

    private GreeterGrpc.GreeterBlockingStub blockingStub;

    public Cliente(ManagedChannel channel) {
        blockingStub = GreeterGrpc.newBlockingStub(channel);
    }

    public Boolean validarNome(String nome){
        if(nome.length() > 20){
            return false;
        }
        return true;
    }

    public void criarCanal(String nomeUsuario){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do canal: ");
        String nomeCanal = scanner.nextLine();
        System.out.print("Digite o tipo do canal (0 para Simples, 1 para Multiplo): ");
        int tipoCanal = scanner.nextInt();
        scanner.nextLine(); // consume newline
        CriarCanalRequest request = CriarCanalRequest.newBuilder()
                .setNome(nomeCanal)
                .setTipoCanal(TipoCanal.valueOf(tipoCanal))
                .setNomeCriador(nomeUsuario)
                .build();
        ResponseCriarCanal response = blockingStub.criar(request);
        System.out.println(response.getMensagem());
    }

    public void removerCanal(String nomeUsuario) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do canal a ser removido: ");
        String nomeCanal = scanner.nextLine();
        RemoverCanalRequest request = RemoverCanalRequest.newBuilder()
                .setNome(nomeCanal)
                .setNomeCriador(nomeUsuario)
                .build();
        RemoverCanalResponse response = blockingStub.remover(request);
        System.out.println(response.getMensagem());
    }

    public void assinarCanal(String nomeUsuario){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do canal que deseja assinar o servico de mensagens: ");
        String nomeCanal = scanner.nextLine();
        AssinarCanalRequest request = AssinarCanalRequest.newBuilder()
                .setNomeCanal(nomeCanal)
                .setNomeCriador(nomeUsuario)
                .build();
        ResponseAssinarCanal response = blockingStub.assinarCanal(request);
        System.out.println(response.getMensagem());
    }

    public void desassinarCanal(String nomeUsuario){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do canal que deseja remover a assinatura do servico de mensagens: ");
        String nomeCanal = scanner.nextLine();
        RemoverAssinaturaCanalRequest request = RemoverAssinaturaCanalRequest.newBuilder()
                .setNomeCanal(nomeCanal)
                .setNomeCriador(nomeUsuario)
                .build();
        ResponseRemoverAssinaturaCanal response = blockingStub.removerAssinaturaCanal(request);
        System.out.println(response.getMensagem());
    }

    public void enviarMensagem(String nomeUsuario) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o nome do canal: ");
        String nomeCanal = scanner.nextLine();
        System.out.print("Digite a mensagem: ");
        String mensagem = scanner.nextLine();
        MensagemRequest request = MensagemRequest.newBuilder()
                .setNomeCanal(nomeCanal)
                .setNomeCriador(nomeUsuario)
                .setMensagem(mensagem)
                .build();
        MensagemResponse response = blockingStub.receberMensagem(request);
        System.out.println(response.getMensagem());
    }

    public void receberMensagensMultiplas(String nomeUsuario){
        EnviarMensagensStreamRequest request = EnviarMensagensStreamRequest.newBuilder()
                .setNomeCliente(nomeUsuario)
                .build();
        Iterator<MensagemStreamResponse> responses = blockingStub.enviarMensagensStream(request);
        while (responses.hasNext()) {
            MensagemStreamResponse response = responses.next();
            System.out.println("Canal: " + response.getNomeCanal() + ", Mensagem do canal: " + response.getMensagem());
        }
    }

    public void receberMensagemUnica(String nomeUsuario){
        EnviarMensagemUnicaStreamRequest request = EnviarMensagemUnicaStreamRequest.newBuilder()
                .setNomeCliente(nomeUsuario)
                .build();
        ResponseMensagemUnica response = blockingStub.enviarMensagemUnica(request);
        System.out.println("Canal: " + response.getNomeCanal() + ", Mensagem do canal: " + response.getMensagem());
    }
}
