from pergunta import Pergunta
from jogador import Jogador
from ranking import Ranking
import os
import random

def main():
    # Sinaliza a execução do programa
    executando = True

    # Conta o número de linhas e de participantes do ranking se o arquivo ranking existir
    if os.path.isfile("./ranking.txt"):
        with open("ranking.txt", "r") as arquivoRanking:
            tamanhoArquivo = sum(1 for linha in arquivoRanking)

        arquivoRanking.close()
        tamanhoArquivo = int(tamanhoArquivo/2)

        # Separa os participantes do ranking salvos no arquivo em objetos do tipo Ranking em uma lista
        arquivoRanking = open("ranking.txt", "r")
        ranking = []
        for i in range(tamanhoArquivo):
            ranking.append(Ranking(arquivoRanking.readline().strip("\n"), int(arquivoRanking.readline().strip("\n"))))
        arquivoRanking.close()
    else:
        tamanhoArquivo = 0
        ranking = []

    # Menu inicial do jogo
    opcoes = ("1", "2", "3")
    print(" Show do Milhão \n [1] Iniciar jogo \n [2] Ver ranking \n [3] Fechar jogo")
    comando = input("Digite o número da opção: ")

    # Verifica se a entrada indicada pelo usuário é válida
    while comando not in opcoes:
        comando = input("Comando inválido. Tente novamente: ")

    # Laço de execução do programa
    while executando:
        # Inicia jogo
        if comando == "1":
            # Inicializa jogador
            print("Bem-vindo ao Show do Milhão!")
            nome = input("Digite seu nome: ")
            jogador = Jogador(nome, 3, 1000, 0, 5000, False)
            jogador.jogando = True

            # Conta o número de linhas no arquivo
            with open("perguntas.txt", "r") as arquivoPerguntas:
                tamanhoPerguntas = sum(1 for linha in arquivoPerguntas)
            arquivoPerguntas.close()

            # Tranforma o número de linhas em número de perguntas e cria uma lista do número de perguntas
            # em ordem aleatória
            quantidadePerguntas = int(tamanhoPerguntas / 6)
            ordemExibicao = list(range(quantidadePerguntas))
            random.shuffle(ordemExibicao)

            # Cria uma lista de elementos do tipo Pergunta com as perguntas lidas do arquivo
            arquivoPerguntas = open("perguntas.txt", "r")
            perguntas = []
            for i in range(quantidadePerguntas):
                perguntas.append(Pergunta(arquivoPerguntas.readline().strip("\n"), arquivoPerguntas.readline().strip("\n"),
                                          arquivoPerguntas.readline().strip("\n"), arquivoPerguntas.readline().strip("\n"),
                                          arquivoPerguntas.readline().strip("\n"), arquivoPerguntas.readline().strip("\n")))
            arquivoPerguntas.close()

            # Escreve as perguntas da lista em um arquivo auxilinar na ordem aleatória gerada anteriormente
            auxiliarPerguntas = open("aux.txt", "w")

            for i in range(quantidadePerguntas):
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].pergunta))
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].alternativaA))
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].alternativaB))
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].alternativaC))
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].alternativaD))
                auxiliarPerguntas.writelines("{}\n".format(perguntas[ordemExibicao[i]].alternativaCorreta))

            auxiliarPerguntas.close()

            auxiliarPerguntas = open("aux.txt", "r")

            # Laço de execução da partida
            while jogador.jogando:
                # Lê pergunta do arquivo auxiliar
                pergunta = auxiliarPerguntas.readline()
                alternativaA = auxiliarPerguntas.readline()
                alternativaB = auxiliarPerguntas.readline()
                alternativaC = auxiliarPerguntas.readline()
                alternativaD = auxiliarPerguntas.readline()
                alternativaCorreta = auxiliarPerguntas.readline()

                # Cria objeto do tipo Pergunta e imprime a pergunta na tela
                perguntaAtual = Pergunta(pergunta, alternativaA, alternativaB,
                                         alternativaC, alternativaD, alternativaCorreta)
                perguntaAtual.imprimirPergunta(jogador)

                # Verifica se a alternativa escolhida pelo usuário está correta
                alternativaEscolhida = perguntaAtual.verificaEscolha()
                perguntaAtual.verificaAlternativa(alternativaEscolhida, jogador)

            # Adiciona nova pontuação ao ranking e reordena de acordo com o valor do prêmio
            if tamanhoArquivo > 4:
                ranking.append(Ranking(jogador.nome,jogador.pontuacaoFinal))
                rankingOrdenado = sorted(ranking, key = Ranking.getPontuacao, reverse = True)
                rankingOrdenado.remove(rankingOrdenado[5])
                ranking = rankingOrdenado
            else:
                ranking.append(Ranking(jogador.nome,jogador.pontuacaoFinal))
                rankingOrdenado = sorted(ranking, key = Ranking.getPontuacao, reverse = True)
                ranking = rankingOrdenado
                tamanhoArquivo = tamanhoArquivo + 1

        # Exibe ranking
        elif comando == "2":
            for i in range(tamanhoArquivo):
                print("\n{}º lugar: {}   {:,} reais" .format(i+1, ranking[i].nome,
                                                             int(ranking[i].pontuacao)).replace(",","."))

        # Fecha o programa
        elif comando == "3":
            break

        # Exibe menu secundário
        print("\n[1] Jogar novamente [2] Ver ranking [3] Fechar jogo\n")
        comando = input("Digite o número da opção: ")

        while comando not in opcoes:
            comando = input("Comando inválido. Tente novamente: ")

    # Salva participantes do ranking no arquivo
    arquivoRanking = open("ranking.txt", "w")
    for i in range(tamanhoArquivo):
        arquivoRanking.write("{}\n".format(ranking[i].nome))
        arquivoRanking.write("{:d}\n".format(int(ranking[i].pontuacao)))
    arquivoRanking.close()

if __name__ == '__main__':
    main()
