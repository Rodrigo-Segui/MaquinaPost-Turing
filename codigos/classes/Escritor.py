class Escritor:
    arquivo = None
    def __init__(self, arquivo, turing):
        self.arquivo = open(arquivo, "w+")
        #print(turing)
        
        self.arquivo.write(self.escreveMaquina(turing))
        
    def escreveMaquina(self, turing):
        texto = ""
        for i in range(len(turing)):
            texto += turing[i] + "\n"
        return texto