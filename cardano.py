import random

frase = "Teste da grade de Cardano"

def cardano (string):
    # Verificar se o que foi recebido por parâmetros é uma String, se não for faz o cast
    if type(string) != str:
        string = str(string)

    # Retira os espaços em braco da String e deixa tudo maiúsculo
    string = string.replace(" ", "")
    string = string.upper()

    # Listas que receberão a grade e as posições das letras que devem ser lidas
    nova_string = []
    lista_posicoes = [1, 2, 3]
    tamanho = len(string)
    preencher = 100 - tamanho
    dicionario = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
                  11: "K", 12: "L", 13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T",
                  21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z"}

    # As letras da String recebida são inseridas na lista
    for i in range(tamanho):
        nova_string.append(string[i: i + 1])

    # A lista é preenchida com caracteres aleatórios do dicionário
    for i in range(preencher):
        nova_string.append(dicionario[random.randint(1, 26)])

    # Atribuição da lista à grade que será devolvida pela função e remoção dos caracteres diferentes de letras
    grade = str(nova_string)
    grade = grade.replace("'", "")
    grade = grade.replace(" ", "")
    grade = grade.replace(",", "")
    grade = grade.replace("[", "")
    grade = grade.replace("]", "")

    # Tratamento da lista que será devolvida com as posições
    posicoes = str(lista_posicoes)
    posicoes = posicoes.replace("'", "")
    posicoes = posicoes.replace("[", "(")
    posicoes = posicoes.replace("]", ")")

    return grade, posicoes


def imprimir_cardano (grille, positions):
    for i in range(10):
        print(str(i + 1) + "\t", end="")

    for i in range(101):
        if i % 10 == 0:
            print(str(i-10)[0:1] + "\n")

        print(grille[i:i + 1] + "\t", end="")

    print(positions)


grade, posic = cardano(frase)

imprimir_cardano(grade, posic)
