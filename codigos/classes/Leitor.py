import re

class Leitor:
    arquivo = None
    linhas = None
    estadoInicial = None
    estadosFinais = None
    estados = None
    transicoes = None
    alfabeto = None
    todosSimbolos = None
    
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, "r")
        print(self.arquivo.read())
       # self.leDados()
       #L
        self.arquivo.close()