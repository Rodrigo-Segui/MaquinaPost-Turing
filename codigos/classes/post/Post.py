


from classes.post.numerosLED import numerosLED
from classes.post.EscritasELeituras import EscritasELeituras
class Post:
    numerosLED = None
    escritasEleituras = None
   # desvios = None      #conjunto de todos os desvios
    numeroestados = None   
    alfabeto = None #conjunto de todos simbolos do alfabeto + #
  
    
    def __init__(self,alfabeto,numerosLED,escritasEleituras,numeroestados):
        #cria um dicionario com o alfabeto de entrada da MP
        self.alfabeto = []
        for letra in alfabeto:
            self.alfabeto.append(letra)
          #  self.alfabeto[letra] = letra
        
        #cria partida
        self.numeroestados = numeroestados
        self.numerosLED = numerosLED


        #cria os desvios e as insere na lista de desvios
        #self.numerosLED = []
        #for n in self.numerosLED :
         #   self.numerosLED.append(Desvio(desvio[0], desvio[1], desvio[2]))

        #cria as escritas e leituras uma lista leituras
        self.escritasEleituras = []
        for escritaEleituras in escritasEleituras:
            self.escritasEleituras.append(EscritasELeituras(escritaEleituras[0],escritaEleituras[1],escritaEleituras[2],escritaEleituras[3]))

        
            
        
        