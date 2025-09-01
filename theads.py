import threading
import time

# Função para a primeira thread - imprime números de 1 a 10
def imprimir_sequencia_1():
    """
    Função executada pela primeira thread.
    Imprime números de 1 a 10 com intervalo de 0.5 segundos entre cada número.
    """
    print("Thread-1 iniciada: imprimindo números de 1 a 10")
    
    # Loop para imprimir números de 1 a 10
    for numero in range(1, 11):
        print(f"Thread-1: {numero}")
        time.sleep(0.5)  # Simula tempo de processamento (0.5 segundos)
    
    print("Thread-1 finalizada!")

# Função para a segunda thread - imprime números de 50 a 60
def imprimir_sequencia_2():
    """
    Função executada pela segunda thread.
    Imprime números de 50 a 60 com intervalo de 0.3 segundos entre cada número.
    """
    print("Thread-2 iniciada: imprimindo números de 50 a 60")
    
    # Loop para imprimir números de 50 a 60
    for numero in range(50, 61):
        print(f"Thread-2: {numero}")
        time.sleep(0.3)  # Simula tempo de processamento (0.3 segundos)
    
    print("Thread-2 finalizada!")

# Função principal do programa
def main():
    """
    Função principal que cria e gerencia as threads.
    """
    print("Programa iniciado: criando threads...")
    
    # Criação das threads
    # target: função que a thread irá executar
    thread1 = threading.Thread(target=imprimir_sequencia_1, name="Thread-1")
    thread2 = threading.Thread(target=imprimir_sequencia_2, name="Thread-2")
    
    # Inicia as threads
    # As threads começam a executar suas funções alvo
    thread1.start()
    thread2.start()
    
    print("Threads iniciadas, aguardando conclusão...")
    
    # Aguarda as threads terminarem
    # join() bloqueia a execução do programa principal até que a thread termine
    thread1.join()
    thread2.join()
    
    print("Todas as threads finalizadas. Programa encerrado.")

# Verifica se este script está sendo executado diretamente
if __name__ == "__main__":
    main()