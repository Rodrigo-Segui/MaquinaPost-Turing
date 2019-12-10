#classe converter MP EM MTfrom classes.post.Post import Post
from classes.post.numerosLED import numerosLED
from classes.post.EscritasELeituras import EscritasELeituras
import math
 #Lista com elementos de escrita ou leituras 
        #print(self.post.alfabeto)
        #print(self.post.escritasEleituras[0].origem)
        #print(self.post.escritasEleituras[0].simbolo)
       # print(self.post.escritasEleituras[0].destino)
        #print(self.post.escritasEleituras[0].tipo)
class Conversor:
    linha = None
    post = None
    

    def __init__(self, post):
        self.post = post
        self.turing = []
        #print(self.post.escritasEleituras[0].tipo)
        #print(post.escritasEleituras[0].tipo)
        self.Resolve()


    def Resolve(self): 
        contador1 = 0
        contador2 = 0
        contador3 = 0
        contador4 = 0
        contador5 = 0
        contadorEscritas = int(self.post.numeroestados[0])
        #===========================================
        for i in range(len(self.post.escritasEleituras)):
             #LEITURA
            if('leitura' == (str(self.post.escritasEleituras[i].tipo))):
                    print("-----------CODIFICACAO ESTADOS DE LEITURA----------------")
                    
                    estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                    proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                    for simbolo in self.post.alfabeto:
                        if(simbolo == self.post.escritasEleituras[i].simbolo):
                            simbolo_lido = self.converte_simbolos(simbolo)
                            print(simbolo_lido,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador1 = contador1 + 1
                    for simbolo in self.post.alfabeto:
                        if(simbolo == "U"):
                            simbolo_escrito = self.converte_simbolos(simbolo)
                        else:
                            contador2 = contador2 + 1
                    
                    contador1 = 0
                    contador2 = 0
                    self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                         
            elif('inicio' == (str(self.post.escritasEleituras[i].tipo))):
                contadorEscritas = contadorEscritas + 1
                estado_atual = self.converte_estados(int(contadorEscritas))
                proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                simbolo_lido = self.converte_simbolos('U')
                simbolo_escrito = self.converte_simbolos('U')
                self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                for simbolo in self.post.alfabeto:
                        if(simbolo != '#' and simbolo != 'U'):
                            estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                        if(simbolo == 'U'):
                            estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            contadorEscritas = contadorEscritas + 1
                            proximo_estado = self.converte_estados(int(contadorEscritas))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos('#')
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'e')
                
                for simbolo in self.post.alfabeto:
                        if(simbolo != '#' and simbolo != 'U'):
                            estado_atual = self.converte_estados(int(contadorEscritas))
                            proximo_estado = self.converte_estados(int(contadorEscritas))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'e')
                        if(simbolo == 'U'):
                            estado_atual = self.converte_estados(int(contadorEscritas))
                            proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
            
            elif('escrita' == (str(self.post.escritasEleituras[i].tipo))):
                #print('esntrou')
                
                simboloEscrita = self.post.escritasEleituras[i].simbolo
                for simbolo in self.post.alfabeto:
                        if(simbolo != 'U'):
                            estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                        if(simbolo == 'U'):
                            estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                            contadorEscritas = contadorEscritas + 1
                            proximo_estado = self.converte_estados(int(contadorEscritas))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simboloEscrita)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'e')
                for simbolo in self.post.alfabeto:
                        if(simbolo != 'U'):
                            estado_atual = self.converte_estados(int(contadorEscritas))
                            proximo_estado = self.converte_estados(int(contadorEscritas))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'e')
                        if(simbolo == 'U'):
                            estado_atual = self.converte_estados(int(contadorEscritas))
                            proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                            simbolo_lido = self.converte_simbolos(simbolo)
                            simbolo_escrito = self.converte_simbolos(simbolo)
                            self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                
        
        for i in range(len(self.turing)):
            print(self.turing[i])
    
    def converte_simbolos(self, simbolo):
        tamanho_Alfabeto = len(self.post.alfabeto)
        print(self.post.alfabeto)
        disc = {}
        iteracao = 0
        simbolo_para_codificar = 0

        for i in self.post.alfabeto:
            disc[i] = iteracao
            iteracao = iteracao + 1
        
        for e in disc:
            if(e == simbolo):
                simbolo_para_codificar = disc[e]
        qnt_SimbTuring = round(math.log(tamanho_Alfabeto, 2) + 0.5)
        marcador_inicial = "a"
        simbolo_transformado = marcador_inicial + bin(simbolo_para_codificar)[2:].zfill(qnt_SimbTuring)
        iteracao = 0
        print(disc)
        return simbolo_transformado

    def converte_estados(self,estado):
        num_estado = (int(self.post.numerosLED[1]) + 2 + int(self.post.numeroestados[0]))
        qnt_Simbestados = round(math.log(int(num_estado), 2) + 0.5)
        marcador_inicialEstados = "q"
        estado_transformado = marcador_inicialEstados + bin(estado)[2:].zfill(qnt_Simbestados)
        return estado_transformado
