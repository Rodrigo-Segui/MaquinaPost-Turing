import re

class Leitor:
    arquivo = None
    linhas = None
    numeroestados = None
    numerosLED = None
    escritasEleituras = None
    alfabeto = None
    
    
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, "r")
        self.leDados()
        self.arquivo.close()
    
    def leDados(self):
        self.linhas = self.arquivo.read().splitlines()
        while '' in self.linhas: 
            self.linhas.remove('')
        self.leAlfabeto()
        self.leNumeroEstados()
        self.leNumerosLED()
        self.leEscritasELeituras()

    def leAlfabeto(self):
        aux = re.compile(r"(\w+|#)")
        self.alfabeto = aux.findall(self.linhas[0])
    
    
    def leNumeroEstados(self):
         aux = re.compile(r"(\d+)")
         self.numeroestados = aux.findall(self.linhas[2]) #numero de estados
         print(self.numeroestados)
    

    def leNumerosLED(self):
        aux = re.compile(r"(\d+)")
        self.numerosLED= aux.findall(self.linhas[1]) #lista com estado de leituras
    
    
    def leEscritasELeituras(self):
        self.escritasEleituras = []
        dados = 'jkj'
        for i in range(4, len(self.linhas) - 2): 
            aux = re.compile(r"(\w+|#)")
            dados = aux.findall(self.linhas[i][:-1])
            self.escritasEleituras.append(dados)
        self.escritasEleituras.append(re.compile(r"(\w+|#)").findall(self.linhas[-2]))
    

