import random

def cardano (string):
    # Verificar se o que foi recebido por parâmetros é uma String, se não for faz o cast
    if type(string) != str:
        string = str(string)

    string = string.upper()

    # Listas que receberão a grade e as posições das letras que devem ser lidas
    nova_string = []
    lista_posicoes = []

    alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
                "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Retira todos os caracteres que não estão no alfabeto, inclusive letras acentuadas
    for i in string:
        if i not in alfabeto:
            string = string.replace(i, "")

    # A lista é preenchida com caracteres aleatórios do alfabeto
    for i in range(100):
        nova_string.append(alfabeto[random.randint(0, 25)])

    # São gerados N número aleatório únicos que determinarão as posições das letras da mensagem na grade
    # Com N sendo o tamanho da String após o tratamento
    for i in range(len(string)):
        x = random.randint(0, 99)

        while (x in lista_posicoes):
            x = random.randint(0, 99)

        lista_posicoes.append(x)

    # A lista contendo as posições é ordenada para se iniciar a substituição
    lista_posicoes.sort()

    # Substituição das letras aleatórias da grade pelas letras da mensagem
    y = 0
    for i in lista_posicoes:
        nova_string[i] = string[y: y + 1]
        y += 1

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
    # Imprime os números das colunas
    for i in range(10):
        print(str(i) + "\t", end="")

    print()
    print("-" * 40, end="")

    # Impressão da grade
    for i in range(101):
        # A cada 10 letras impressas, adiciona um marcador,
        # imprime o número da linha e passa para a próxima
        if i % 10 == 0:
            print("| " + str(i - 10)[0:1] + "\n")

        print(grille[i:i + 1] + "\t", end="")

    # Impressão da lista
    print("\n" + positions)


frase = "Teste da grade de Cardano"

grade, posic = cardano(frase)

imprimir_cardano(grade, posic)