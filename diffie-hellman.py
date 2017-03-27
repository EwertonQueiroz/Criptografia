def gerar_chave_publica (chave_privada, primo, raiz_primitiva):
    raizes_primitivas = []

    if type(chave_privada) != int or type(primo) != int or type(raiz_primitiva) != int:
        return -1

    elif chave_privada > primo:
        chave_privada = chave_privada % primo

#    if verificar se raiz_primitiva é raiz primitiva modulo primo
#    elif raiz_primitiva not in raizes_primitivas:

    return (raiz_primitiva ** chave_privada) % primo


def gerar_chave_secreta (chave_privada, primo, chave_publica_recebida):
    if type(chave_privada) != int or type(primo) != int or type(chave_publica_recebida) != int:
        return -1

    if chave_privada > primo:
        chave_privada = chave_privada % primo

    return (chave_publica_recebida ** chave_privada) % primo


def calcular_chave_secreta (chave_privada_a, chave_privada_b, primo, raiz_primitiva):
    if type(chave_privada_a) != int or type(chave_privada_b) != int or type(primo) != int or type(raiz_primitiva) != int:
        return -1

    if chave_privada_a >= primo and chave_privada_b >= primo:
        chave_privada_a = chave_privada_a % primo
        chave_privada_b = chave_privada_b % primo

    # if verificar se raiz_primitiva é raiz primitiva modulo primo

    return (raiz_primitiva ** (chave_privada_a * chave_privada_b)) % primo


public_key_alice = gerar_chave_publica(6, 23, 5)
public_key_bob = gerar_chave_publica(15, 23, 5)

print ("Chave Pública Alice:", public_key_alice)
print ("Chave Pública Bob:", public_key_bob)
print ("Chave Secreta Alice:", gerar_chave_secreta (6, 23, public_key_bob))
print ("Chave Secreta Bob:", gerar_chave_secreta (15, 23, public_key_alice))
print ("Chave Secreta calculada:", calcular_chave_secreta (15, 6, 23, 5))