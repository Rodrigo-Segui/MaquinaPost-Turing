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
        #print(len(self.post.escritasEleituras))
        #if('escrita' == (str(self.post.escritasEleituras[0].tipo))):
        #    print("entrou")
        #===========================================
        for i in range(len(self.post.escritasEleituras)):
             #LEITURA
            if('leitura' == (str(self.post.escritasEleituras[i].tipo))):
                    print("-----------CODIFICACAO ESTADOS DE LEITURA----------------")
                    
                    estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                    #print("Orig   ", self.post.escritasEleituras[i].origem," : ", estado_atual)
                    proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                    #print("Dest   ", self.post.escritasEleituras[i].destino," : ",proximo_estado)
                    for simbolo in self.post.alfabeto:
                        if(simbolo == self.post.escritasEleituras[i].simbolo):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_lido = self.converte_simbolos(simbolo)
                            print(simbolo_lido,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador1 = contador1 + 1
                    for simbolo in self.post.alfabeto:
                        if(simbolo == "U"):
                           # print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_escrito = self.converte_simbolos(simbolo)
                           # print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador2 = contador2 + 1
                    
                    contador1 = 0
                    contador2 = 0
                    self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                         
            elif('inicio' == (str(self.post.escritasEleituras[i].tipo))):
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
           # print(i, ' : ', self.post.alfabeto)
            disc[i] = iteracao
            iteracao = iteracao + 1
        
        #for i in disc:// percorrer dicionario
            #if(simbolo == indice)
                #simbolo_para_codificar = conteudo_do 
        #print('**********************************')
        for e in disc:
           # print(e)
            if(e == simbolo):
               # print('igual : ',e, '= ', simbolo)
               # print('simbolo_para_codificar <===', disc[e])
                simbolo_para_codificar = disc[e]
       # print(simbolo_para_codificar)
       # print('***********************************')

        #print("alfabeto",self.post.alfabeto)
        #print('tamanho', tamanho_Alfabeto)
        qnt_SimbTuring = round(math.log(tamanho_Alfabeto, 2) + 0.5)
        #print("Número de símbolos da máquina de turing = ", qnt_SimbTuring)
        marcador_inicial = "a"
        simbolo_transformado = marcador_inicial + bin(simbolo_para_codificar)[2:].zfill(qnt_SimbTuring) 
        #print("simbolo",simbolo) 
        iteracao = 0
        print(disc)
        return simbolo_transformado

    def converte_estados(self,estado):
       # print(len(self.post.escritasEleituras))
       # for i in range(len(self.post.escritasEleituras)): 
         #   lista_estados = self.post.escritasEleituras[i].origem

       # print(lista_estados)
        #print('lista', set(lista_estados))
       # num_estado =( len(set(lista_estados))+1)
       
       # num_estado = 19 # colocar entrada 2
       # num_estado = 20              # colocar entrada 1
        num_estado = (int(self.post.numerosLED[1]) + 1 + int(self.post.numeroestados[0]))
        print('numero para dar : ',(int(self.post.numerosLED[1]) + 1 + int(self.post.numeroestados[0])))
        print('numero de leituras : ',self.post.numerosLED[0])
        print('numero de escritas : ',self.post.numerosLED[1])
        print('numero de decicoes : ',self.post.numerosLED[2])
        print
        #num_estado = int(self.post.numeroestados[1])
       # num_estado = 9 #entrada3
        #print("Número de estados1 =", num_estado)
        qnt_Simbestados = round(math.log(int(num_estado), 2) + 0.5)
        #print("Número de simbolos para os estados da máquina de turing = ",qnt_Simbestados)
        marcador_inicialEstados = "q"
        #Estou criando um estado de escrita no final da fita da máquina de turing
        estado_transformado = marcador_inicialEstados + bin(estado)[2:].zfill(qnt_Simbestados)
        return estado_transformado
