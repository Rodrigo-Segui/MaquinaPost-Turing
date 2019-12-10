##autores Rodrigo Segui, Marcelo Marchioro, Arthur Teixeira, Gabriel Velasco
import sys
from classes.Leitor import Leitor
from classes.post.Post import Post
from classes.Conversor import Conversor
def main():
        if(len(sys.argv) != 3):
            print("Modo de execucao: ./Main.py <arquivo-de-entrada> <arquivo-de-saida>")
            print("Obs: O arquivo de entrada deve estar no diretorio: \"arquivos/estradas\" "
                   + "deste projeto")
            return

        entrada = "../arquivos/entradas/" + sys.argv[1]

        leituraMP = Leitor(entrada)
        mp = Post(leituraMP.alfabeto,leituraMP.numerosLED,leituraMP.escritasEleituras,leituraMP.numeroestados)

        conversor = Conversor(mp)
       

main()