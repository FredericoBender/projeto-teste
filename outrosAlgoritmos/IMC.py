# isso é uma calculadora de IMC
# IMC = PESO / ALTURA ²

# TIPOS DE DADOS
# INT -> INTEIRO
# FLOAT -> NUMERO COM VIRGULA
# STR (STRING) -> TEXTO

def lerAlturaEmMetro():
    """Funcao que le a altura"""
    ALTURA = int(input("Digite aqui a sua altura em cm:"))/100
    return ALTURA


def lerPeso():
    """Função que le o peso"""
    return int(input("Digite aqui o seu peso em KG:"))


def calculaIMC(peso, altura):
    """Função que recebe peso e altura e retorna o IMC calculado"""
    return peso / (altura * altura)


def avaliaIMC(IMC):
    """Essa funcionalidade recebe um IMC e exibe na tela qual o grau de obesidade respectivo"""
    print("Seu grau de obesidade é de: ")
    if IMC < 18.5:
        print("Abaixo do peso normal")
    if IMC >= 18.5 and IMC < 25:
        print("Peso Ideal")
    elif IMC >= 25 and IMC < 30:
        print("Sobrepeso")
    elif IMC >= 30 and IMC < 35:
        print("Obesidade 1")
    elif IMC >= 35 and IMC < 40:
        print("Obesidade 2")
    elif IMC >= 40:
        print("Obesidade 3")


def exibirResultados(PESO, ALTURA, IMC):
    """Essa funcao exibe nossos resultados"""
    print("\n")
    print("Seu peso é de:", PESO, "kg")
    print("Sua altura é de:", ALTURA, "m")
    print("Seu IMC é de:{0:.2f} ".format(IMC))
    print("\n")


def main():
    while True:
        print("-------------------------")
        PESO = lerPeso()
        ALTURA = lerAlturaEmMetro()
        IMC = calculaIMC(PESO, ALTURA)
        exibirResultados(PESO, ALTURA, IMC)
        avaliaIMC(IMC)
        print("-------------------------")
        SAIR = input("vc quer sair? ").lower().replace(" ", "", -1)
        if SAIR[0] == "s":
            break


main()
