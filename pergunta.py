class Pergunta:
    def __init__(self, pergunta, alternativaA, alternativaB, alternativaC, alternativaD, alternativaCorreta):
        self.pergunta = pergunta
        self.alternativaA = alternativaA
        self.alternativaB = alternativaB
        self.alternativaC = alternativaC
        self.alternativaD = alternativaD
        self.alternativaCorreta = alternativaCorreta

    #Imprime a pergunta na tela
    def imprimirPergunta(self, jogador):
        print("\n")
        print("Valendo {:,} reais\n" .format(int(jogador.pontuacaoInicial)).replace(",", "."))
        print(self.pergunta)
        print("A) " + self.alternativaA + "B) " + self.alternativaB + "C) " + self.alternativaC + "D) " + self.alternativaD)
        if jogador.pulos > 1:
            print("[P] - Pular ({} disponíveis) [S] - Sair ({:,} reais)\n"
                  .format(jogador.pulos, int(jogador.pontuacaoFinal)).replace(",","."))
        else:
            print("[P] - Pular ({} disponível) [S] - Sair ({:,} reais)\n"
                  .format(jogador.pulos, int(jogador.pontuacaoFinal)).replace(",","."))

    # Valida se a entrada é uma das opções permitidas, caso contrário pede para o usuário
    # inserir uma nova
    def verificaEscolha(self):
        alternativasValidas = ("A", "B", "C", "D", "P", "S")

        alternativaEscolhida = input("Digite a letra da alternativa escolhida: ")

        while alternativaEscolhida.upper() not in alternativasValidas:
            alternativaEscolhida = input("Alternativa inválida. Tente novamente: ")

        return alternativaEscolhida

    # Verifica se a alternativa escolhida pelo usuário está correta ou errada
    def verificaAlternativa(self, alternativaEscolhida, jogador):
        if alternativaEscolhida.upper() == "A":
            if self.alternativaA == self.alternativaCorreta:
                self.respostaCorreta(jogador)
            else:
                self.respostaErrada(jogador)
        elif alternativaEscolhida.upper() == "B":
            if self.alternativaB == self.alternativaCorreta:
                self.respostaCorreta(jogador)
            else:
                self.respostaErrada(jogador)
        elif alternativaEscolhida.upper() == "C":
            if self.alternativaC == self.alternativaCorreta:
                self.respostaCorreta(jogador)
            else:
                self.respostaErrada(jogador)
        elif alternativaEscolhida.upper() == "D":
            if self.alternativaD == self.alternativaCorreta:
                self.respostaCorreta(jogador)
            else:
                self.respostaErrada(jogador)
        elif alternativaEscolhida.upper() == "P":
            if jogador.pulos > 0:
                print("Pergunta pulada")
                jogador.pulos = jogador.pulos - 1
            else:
                jogador.limitePulos(alternativaEscolhida.upper(),self)
        elif alternativaEscolhida.upper() == "S":
            jogador.jogando = False
            print("Prêmio final: {:,} reais " .format(int(jogador.pontuacaoFinal)).replace(",", "."))

    # Finaliza o jogo caso seja a última pergunta
    def respostaCorreta(self, jogador):
        print("\nResposta correta")
        if jogador.pontuacaoInicial == 1000000:
            print("Você venceu! Parabéns")
            jogador.finalizarJogo(True)
        else:
            jogador.calculoPremio(True)

    # Finaliza o jogo caso o usuário tenha errado
    def respostaErrada(self, jogador):
        print("\nResposta errada"
              "\nVocê perdeu")
        jogador.finalizarJogo(False)
