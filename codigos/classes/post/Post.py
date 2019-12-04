


from classes.post.Leitura import Leitura
from classes.post.EscritasELeituras import EscritasELeituras
class Post:
    leituras = None
    escritasEleituras = None
   # desvios = None      #conjunto de todos os desvios
    partida = None   
    alfabeto = None #conjunto de todos simbolos do alfabeto + #
  
    
    def __init__(self, alfabeto,partida,leituras,escritasEleituras):
        #cria um dicionario com o alfabeto de entrada da MP
        self.alfabeto = []
        for letra in alfabeto:
            self.alfabeto.append(letra)
          #  self.alfabeto[letra] = letra
        
        #cria partida
        self.partida = (partida[0], partida[1])


        #cria os desvios e as insere na lista de desvios
        #self.desvios = []
        #for desvio in desvios:
         #   self.desvios.append(Desvio(desvio[0], desvio[1], desvio[2]))

        #cria as escritas e leituras uma lista leituras
        self.escritasEleituras = []
        for escritaEleituras in escritasEleituras:
            self.escritasEleituras.append(EscritasELeituras(escritaEleituras[0],escritaEleituras[1],escritaEleituras[2],escritaEleituras[3]))

        
            
        
        