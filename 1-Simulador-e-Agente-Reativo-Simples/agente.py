import ambiente.py

class Agente:

    def __init__(self, sala):

        self.sala = sala
        self.desempenho = 0

    def percepcao(self):
        if self.sala.situacao == "Sujo":
            return "Sujo"
        return "Limpo"

    def limparSala(self):

        for i in range(self.sala.linhas):
            for j in range(self.sala.colunas):
                self.sala.matriz[i][j] = 0
        sala.situacao = "Limpo"
    
    def funcaoAgente(self, posicao, situacao):

        if(situacao=="Sujo"):
            print("Limpar")

        elif(posicao=="A"):
            print("Direita")
        elif(posicao=="B"):
            print("Esquerda")

