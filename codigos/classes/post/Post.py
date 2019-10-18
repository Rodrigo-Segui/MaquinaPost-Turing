


from classes.post.AceitaRejeita import Rejeita
from classes.post.AceitaRejeita import Aceita
from classes.post.Desvio import Desvio
from classes.post.Leitura import Leitura
from classes.post.Escrita import Escrita
class Post:
    leituras = None
    escritas = None
    desvios = None      #conjunto de todos os desvios
    partida = None   
    alfabeto = None #conjunto de todos simbolos do alfabeto + #
    rejeicao = Rejeita()
    aceitacao = Aceita()
    
    def __init__(self, alfabeto,partida,leituras,escritas,desvios):
        #cria um dicionario com o alfabeto de entrada da MP
        self.alfabeto = {}
        for letra in alfabeto:
            self.alfabeto[letra] = letra
        
        #cria partida
        self.partida = (partida[0], partida[1])


        #cria os desvios e as insere na lista de desvios
        self.desvios = []
        for desvio in desvios:
            self.desvios.append(Desvio(desvio[0], desvio[1], desvio[2]))

        #cria as escritas e um dicionario de leituras
        self.escritas = {}
        for escrita in escritas:
            self.desvios.append(Escrita(escrita[0],escrita[1],escrita[2]))

        
            
        
        