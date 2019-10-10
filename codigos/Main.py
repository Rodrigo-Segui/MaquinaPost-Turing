##autores Rodrigo Segui, Marcelo Marchioro, Arthur Teixeira, Gabriel Velasco
import sys
from classes.Leitor import Leitor
def main():
    #try:
        if(len(sys.argv) != 3):
            print("Modo de execucao: ./Main.py <arquivo-de-entrada> <arquivo-de-saida>")
            print("Obs: O arquivo de entrada deve estar no diretorio: \"arquivos/estradas\" "
                   + "deste projeto")
            return

        entrada = "../arquivos/entradas/" + sys.argv[1]
        saida = "../arquivos/saidas/" + sys.argv[2]

        leituraMP = Leitor(entrada)

main()