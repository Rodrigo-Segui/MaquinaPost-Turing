class EscritasELeituras:
    origem = None
    simbolo = None
    destino = None
    tipo = None
    
    def __init__(self, origem, simbolo, destino, tipo):
        self.origem = origem
        self.destino = destino
        self.simbolo = simbolo
        self.tipo = tipo
        
    def __eq__(self, other):
        if(other == None):
            return False
        
        if((self.origem.id == other.origem.id)
            and (self.simbolo == other.simbolo)
            and (self.tipo ==  other.tipo)
            and (self.destino.id == other.destino.id)):
            return True
        
        return False