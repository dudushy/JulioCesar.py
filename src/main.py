# pip freeze > requirements.txt
#* -- Imports
import os

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

TITLE = """
/----------------------------------------------------------------------------------\\
|  Júlio César trocou cada letra do seu nome para as 3 seguintes do alfabeto.      |
|                                                                                  |
|  Transcreva as seguintes palavras:                                               |
|  - Marrocos                                                                      |
|  - Matemática                                                                    |
|  - Qualidade                                                                     |
|  - Copa do Mundo                                                                 |
|  - Inconstitucionalíssimo                                                        |
\\----------------------------------------------------------------------------------/
"""

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabeto3seguintes = "defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC"

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def julioCesar() -> None: #? Julio Cesar
    clearConsole()
    print(TITLE)
    print("Resposta: ")
    for palavra in input().split():
        for letra in palavra:
            if letra in alfabeto:
                print(alfabeto3seguintes[alfabeto.index(letra)], end="")
            else:
                print(letra, end="")
        print(" ", end="")
    print()

def main() -> None:
    julioCesar()
    print("\n")
    os.system("pause")

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
