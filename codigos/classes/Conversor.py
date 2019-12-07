#classe converter MP EM MTfrom classes.post.Post import Post
from classes.post.Leitura import Leitura
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
        #print(len(self.post.escritasEleituras))
        #if('escrita' == (str(self.post.escritasEleituras[0].tipo))):
        #    print("entrou")
        #===========================================
        for i in range(len(self.post.escritasEleituras)):
             #LEITURA
            if('leitura' == (str(self.post.escritasEleituras[i].tipo))):
                   # print("-----------CODIFICACAO ESTADOS DE LEITURA----------------")
                    estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                    #print("Orig   ", self.post.escritasEleituras[i].origem," : ", estado_atual)
                    proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                    #print("Dest   ", self.post.escritasEleituras[i].destino," : ",proximo_estado)
                    for simbolo in self.post.alfabeto:
                        if(simbolo == self.post.escritasEleituras[i].simbolo):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_lido = self.converte_simbolos(contador1)
                            #print(simbolo_lido,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador1 = contador1 + 1
                    for simbolo in self.post.alfabeto:
                        if(simbolo == "U"):
                            print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_escrito = self.converte_simbolos(contador2)
                            print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador2 = contador2 + 1
                    
                    contador1 = 0
                    contador2 = 0
                    self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_escrito + ', ' +  'd')
                    

            elif('escrita' == (str(self.post.escritasEleituras[i].tipo))):
                estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                #--------------------------------------------------------------------------------
                for simbolo in self.post.alfabeto:
                        if(simbolo == self.post.escritasEleituras[i].simbolo):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_escrito = self.converte_simbolos(contador3)
                            #print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador3 = contador3 + 1
                contador3 = 0

                #proximo_estado2 = self.converte_estados(int(19)) #entrada 2
                proximo_estado2 = self.converte_estados(int(20)) #entrada 1

                for simbolo in self.post.alfabeto:
                    for s in self.post.alfabeto:
                        if(s == simbolo ):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_lido = self.converte_simbolos(contador4)
                            #print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador4 = contador4 + 1
                    contador4 = 0

                    if(simbolo ==  "U"):
                        self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado2 + ', ' + simbolo_escrito + ', ' +  'd')
                    else:
                        self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  estado_atual + ', ' +  simbolo_lido + ', ' +  'd')
                
                for simbolo in self.post.alfabeto:
                    for s in self.post.alfabeto:
                        if(s == simbolo ):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_lido = self.converte_simbolos(contador4)
                            #print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador4 = contador4 + 1
                    contador4 = 0

                    if(simbolo == 'U'):
                        self.turing.append(proximo_estado2 + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' + simbolo_lido + ', ' +  'd')
                    else:
                    # para rebobinar a esquerda
                        self.turing.append(proximo_estado2 + ', ' + simbolo_lido + ', ' +  proximo_estado2 + ', ' +  simbolo_lido + ', ' +  'e')


                #================================================================================

            else:
                estado_atual = self.converte_estados(int(self.post.escritasEleituras[i].origem))
                proximo_estado = self.converte_estados(int(self.post.escritasEleituras[i].destino))
                for simbolo in self.post.alfabeto:
                    for s in self.post.alfabeto:
                        if(s == simbolo ):
                            #print('teste', simbolo, '==',self.post.escritasEleituras[i].simbolo )
                            simbolo_lido = self.converte_simbolos(contador5)
                            #print(simbolo_escrito,' : ',self.post.escritasEleituras[i].simbolo)
                        else:
                            contador5 = contador5 + 1
                    contador5 = 0
                self.turing.append(estado_atual + ', ' + simbolo_lido + ', ' +  proximo_estado + ', ' +  simbolo_lido + ', ' +  'f')

                print('-')
                #print("desvio")
        
        for i in range(len(self.turing)):
            print(self.turing[i])
        

        #===========================================
        

        #sim = self.converte_simbolos(contador1)
        #print(sim)

        #estado = self.converte_estados(int(self.post.escritasEleituras[0].origem))
        #print(estado)

    
    def converte_simbolos(self, simbolo):
        tamanho_Alfabeto = len(self.post.alfabeto)
        #print("alfabeto",self.post.alfabeto)
        #print('tamanho', tamanho_Alfabeto)
        qnt_SimbTuring = round(math.log(tamanho_Alfabeto, 2) + 0.5)
        #print("Número de símbolos da máquina de turing = ", qnt_SimbTuring)
        marcador_inicial = "a"
        simbolo_transformado = marcador_inicial + bin(simbolo)[2:].zfill(qnt_SimbTuring) 
        #print("simbolo",simbolo) 
        return simbolo_transformado

    def converte_estados(self,estado):
       # print(len(self.post.escritasEleituras))
        #for i in range(len(self.post.escritasEleituras)): 
          #  lista_estados = self.post.escritasEleituras[i].origem

        #print(lista_estados)
        #print('lista', set(lista_estados))
        #num_estado =( len(set(lista_estados))+1)
       
       # num_estado = 19 # colocar entrada 2
        num_estado = 20              # colocar entrada 1
        #print("Número de estados =", num_estado)
        qnt_Simbestados = round(math.log(int(num_estado), 2) + 0.5)
        #print("Número de simbolos para os estados da máquina de turing = ",qnt_Simbestados)
        marcador_inicialEstados = "q"
        #Estou criando um estado de escrita no final da fita da máquina de turing
        estado_transformado = marcador_inicialEstados + bin(estado)[2:].zfill(qnt_Simbestados)
        return estado_transformado
