#classe converter MP EM MTfrom classes.post.Post import Post
from classes.post.Leitura import Leitura
from classes.post.EscritasELeituras import EscritasELeituras


class Conversor:
    contadorID = 0
    turing = None
    post = None
    
    def __init__(self, post):
        self.post = post
        #Lista com elementos de escrita ou leituras 
        print(self.post.alfabeto)
        print(self.post.escritasEleituras[0].origem)
        print(self.post.escritasEleituras[0].simbolo)
        print(self.post.escritasEleituras[0].destino)
        print(self.post.escritasEleituras[0].tipo)
        #print(turing.todosSimbolos)
       # self.post = Turing(post.todosSimbolos)
        #cria uma maquina de post com simbolos e cria desvios, leituras e escritas vazias
        #print(self.post.alfabeto)
        #print(self.post.desvios)
       # self.incrementarContador()
       # self.incrementarContador()
        #for estado in self.turing.estados:
         #   turing.estados[estado].equivalentePost = None
            #print(turing.estados[estado].equivalentePost) 
            #cria mesmo numero de estados equivalentes
       # for transicao in self.turing.transicoes:
         #   transicao.usada = False
            #print(transicao.usada)
            #cria numero de trancioes equivalentes
        #self.converter(self.turing.estadoInicial)
        # manda o estado inicial pra funcao converter
