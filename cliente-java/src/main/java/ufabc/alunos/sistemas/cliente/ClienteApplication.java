package ufabc.alunos.sistemas.cliente;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import ufabc.alunos.sistemas.cliente.util.Cliente;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import ufabc.alunos.sistemas.cliente.*;

import java.util.Scanner;

@SpringBootApplication
public class ClienteApplication {

	public static void main(String[] args) {
		SpringApplication.run(ClienteApplication.class, args);

		System.out.println("Hello and welcome!");
		Scanner scanner = new Scanner(System.in);
		String nomeUsuario;

		ManagedChannel channel = ManagedChannelBuilder.forAddress("localhost", 50051)
				.usePlaintext()
				.build();

		Cliente client = new Cliente(channel);

		while (true) {
			System.out.print("Digite seu nome (até 20 caracteres, sem caracteres especiais): ");
			nomeUsuario = scanner.nextLine();
			if (client.validarNome(nomeUsuario)) {
				break;
			} else {
				System.out.println("Nome inválido. Por favor, tente novamente.");
			}
		}

		while (true) {
			System.out.println("\nMenu:");
			System.out.println("1. Criar canal");
			System.out.println("2. Remover canal");
			System.out.println("3. Assinar canal");
			System.out.println("4. Desassinar canal");
			System.out.println("5. Enviar mensagem");
			System.out.println("6. Sair");
			System.out.print("Escolha uma opção: ");
			String escolha = scanner.nextLine();

			switch (escolha) {
				case "1":
					client.criarCanal(nomeUsuario);
					break;
				case "2":
					client.removerCanal(nomeUsuario);
					break;
				case "3":
					client.assinarCanal();
					break;
				case "4":
					client.desassinarCanal();
					break;
				case "5":
					client.enviarMensagem(nomeUsuario);
					break;
				case "6":
					channel.shutdown();
					return;
				default:
					System.out.println("Opção inválida!");
					break;
			}
		}
	}
}
