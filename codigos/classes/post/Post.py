
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
    
    def __init__(self, alfabeto,partida,leituras,escritas,desvios):
        #cria um dicionario com o alfabeto de entrada da MP
        self.alfabeto = {}
        for letra in alfabeto:
            self.alfabeto[letra] = letra
            
        