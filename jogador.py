from ranking import Ranking
class Jogador:
    def __init__(self, nome, pulos, pontuacaoInicial, pontuacaoFinal, checkpoint, jogando):
        self.nome = nome
        self.pulos = pulos
        self.pontuacaoInicial = pontuacaoInicial
        self.pontuacaoFinal = pontuacaoFinal
        self.checkpoint = checkpoint
        self.jogando = jogando
        self.contador = 1

    # Verifica se o limite de pulos já foi atingido
    def limitePulos(self, controleAlternativa, perguntaAtual):
        if controleAlternativa == "P":
            print("Todos os pulos já foram utilizados")
            alternativaEscolhida = perguntaAtual.verificaEscolha()
            perguntaAtual.verificaAlternativa(alternativaEscolhida, self)

    # Calcula o prêmio de acordo com a posição no jogo
    def calculoPremio(self, acertou):
        if acertou:
            if self.contador < 5:
                self.pontuacaoFinal = self.pontuacaoInicial
                self.pontuacaoInicial = self.pontuacaoInicial + (self.pontuacaoInicial / self.contador)
                self.contador = self.contador + 1
            else:
                self.pontuacaoFinal = self.pontuacaoInicial
                self.pontuacaoInicial = self.pontuacaoInicial * 2
                self.contador = 1
        elif not acertou and self.pontuacaoInicial == 1000000:
            self.pontuacaoFinal = 0
        else:
            self.pontuacaoFinal = self.pontuacaoFinal / 2

    # Finaliza a partida
    def finalizarJogo(self, acertou):
        self.jogando = False
        self.calculoPremio(acertou)
        print("Prêmio final: {:,} reais " .format(int(self.pontuacaoFinal)).replace(",","."))

