from random import randint
import numpy as np

print(randint(0,9))

class sala:
    def __init__(self, situacao, linhas, colunas):
        self.situacao = situacao
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = []
    
    def iniciarSalaLimpa(self): #0: limpo
        for i in range(self.linhas):
            mLinha = []
            for j in range(self.colunas):
                mLinha.append(0)
            matriz.append(mLinha)


class Ambiente:

    def __init__(self, linhasSala, colunasSala):
        self.linhasSala = linhasSala #dimensão das salas
        self.colunasSala = colunasSala #dimensão das salas
        self.salas = [None,None] #[0]:sala A; [1]:sala B

    def criarSalas(self):
        salas[0] = sala(self.linhasSala, self.colunasSala)
        salas[1] = sala(self.linhasSala, self.colunasSala)
    

    def sujarSala(self, sala):

        while self.salas[sala].estado == "Limpo":

            for i in range(self.linhasSala):
                for j in range(self.colunasSala):
                    num = randint(0,1)
                    self.salas[sala].matriz[i][j] = num
                    if num != 0:
                        self.salas[sala].situacao = "Sujo"
                        

    def atualizarAmbiente(self):
        
        sujar = randint(0,1) #0: manter limpo, 1: sujar
    
        if sujar == 1:

            if (self.salas[0].situacao == "Limpo" && self.salas[1].situacao == "Limpo"):
                sala = randint(0,1)
            elif (self.salas[0].situacao == "Limpo" && self.salas[1].situacao == "Sujo"):
                sala = 1
            elif (self.salas[0].situacao == "Sujo" && self.salas[1].situacao == "Limpo"):
                sala = 0
