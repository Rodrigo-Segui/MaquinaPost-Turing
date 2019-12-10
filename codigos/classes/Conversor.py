#classe converter MP EM MTfrom classes.post.Post import Post
from classes.post.numerosLED import numerosLED
from classes.post.EscritasELeituras import EscritasELeituras
import math

class Conversor:
    linha = None
    post = None
    

    def __init__(self, post):
        self.post = post
        self.turing = []
        self.Resolve()


    def Resolve(self):
        contadorEscritas = int(self.post.numeroestados[0]) - 1
        print('www',contadorEscritas)
        for i in range(len(self.post.escritasEleituras)):
            if('leitura' == (str(self.post.escritasEleituras[i].tipo))):                   
                    estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                    proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                    for simbolo in self.post.alfabeto:
                        if(simbolo == self.post.escritasEleituras[i].simbolo):
                            simbolo_lido = self.converte_simbolos(simbolo)
                            print(simbolo_lido,' : ',self.post.escritasEleituras[i].simbolo)
                    for simbolo in self.post.alfabeto:
                        if(simbolo == "U"):
                            simbolo_escrito = self.converte_simbolos(simbolo)
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
                #x<=xa || x<=xb
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
        #print(self.post.alfabeto)
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
        return simbolo_transformado

    def converte_estados(self,estado):
        num_estado = (int(self.post.numerosLED[1]) + 2 + int(self.post.numeroestados[0]))
        
        print('--------------',num_estado, '--------------------')
        qnt_Simbestados = round(math.log(int(num_estado), 2) + 0.5)
        marcador_inicialEstados = "q"
        estado_transformado = marcador_inicialEstados + bin(estado)[2:].zfill(qnt_Simbestados)
        return estado_transformado
