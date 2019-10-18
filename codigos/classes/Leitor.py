import re

class Leitor:
    arquivo = None
    linhas = None
    partida = None
    leituras = None
    escritas = None
    desvios = None
    alfabeto = None
    
    
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, "r")
        #print(self.arquivo.read())
        self.leDados()
        self.arquivo.close()
    
    def leDados(self):
        self.linhas = self.arquivo.read().splitlines()
        while '' in self.linhas: #cria uma lista de linhas
            self.linhas.remove('')
        self.leAlfabeto()
        self.lePartida()
        self.leLeituras()
        self.leEscritas()
        self.leDesvios()

    def leAlfabeto(self):
        aux = re.compile(r"(\w+|#)")
        self.alfabeto = aux.findall(self.linhas[0])  #w retorna uma lista todos simbolos do alfabeto
        #print(self.alfabeto)
        #print(len(self.alfabeto))
    
    
    def lePartida(self):
        aux = re.compile(r"(\d+)")
        self.partida = aux.findall(self.linhas[1]) #lista com estado de partida =0 e destino = 1
        #print(self.partida)# lista com estados
    

    def leLeituras(self):
        aux = re.compile(r"(\d+)")
        self.leituras= aux.findall(self.linhas[2]) #lista com estado de leituras
    #    print(self.leituras)# lista com estados
    
    
    def leEscritas(self):
        self.escritas = []
        dados = 'jkj'
        #for i in range(4, len(self.linhas) - 2): #6 (a numero de linhas -2)
        for i in range(4,20):#problema -- tem que parar quando acabar escritas
            aux = re.compile(r"(\w+|#)")
            dados = aux.findall(self.linhas[i][:-1])
            #print(dados)
            self.escritas.append(dados)
        #self.escritas.append(re.compile(r"(\w+|#)").findall(self.linhas[-2]))
        #print(self.escritas) #pega a ultima transicao
        
    
    def leDesvios(self):
        self.desvios = []
        for i in range(22, len(self.linhas) - 2): #6 (a numero de linhas -2)
        #for i in range(4,20):#problema -- tem que comecar quando
            aux = re.compile(r"(\w+|#)")
            dados = aux.findall(self.linhas[i][:-1])
            #print(dados)
            self.desvios.append(dados)
        self.desvios.append(re.compile(r"(\w+|#)").findall(self.linhas[-2]))
        print(self.desvios) #pega a ultima transicao
    

