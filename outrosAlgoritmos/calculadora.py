# CALCULADORA EM PYTHON

def soma(a, b):
    return a+b


def subtrair(a, b):
    return a-b


def multiplicar(a, b):
    return a*b


def dividir(a, b):
    return a/b


def A_e_X_porcento_de_B(a, b):
    return a/100*b


def A_elevado_a_B(a, b):
    return a**b


def operacao(FUNCAO, a, b):
    """Esta funcao analisa as operacoes possiveis da calculadora e as realiza"""
    if FUNCAO == 1:
        TOTAL = soma(a, b)
        print("Sua soma é de:", TOTAL)
    elif FUNCAO == 2:
        TOTAL = subtrair(a, b)
        print("Sua subtracao é de:", TOTAL)
    elif FUNCAO == 3:
        TOTAL = multiplicar(a, b)
        print("Sua multiplicacao é de:", TOTAL)
    elif FUNCAO == 4:
        TOTAL = dividir(a, b)
        print("Sua divisao é de: {0:.2f}".format(TOTAL))
    elif FUNCAO == 5:
        TOTAL = A_e_X_porcento_de_B(a, b)
        print("{1} é {2} % de {0}".format(a, b, TOTAL))
    elif FUNCAO == 6:
        TOTAL = A_elevado_a_B(a, b)
        print("{0} elevado a {1} é {2}".format(a, b, TOTAL))


def sair():
    sair = input("Deseja sair do programa? (s) ou (n)?").lower()
    if sair[0] == "s":
        return True
    return False


def calculadora():
    while True:
        FUNCAO = int(input("--------------------------------------------\n\
        O que voce deseja fazer?\n\
            1 - Somar\n\
            2 - Subtrair\n\
            3 - Multiplicar\n\
            4 - Divisao\n\
            5 - Porcentagem\n\
            6 - Potencia\n"))

        a = float(input("Digite A:"))
        b = float(input("Digite B:"))
        operacao(FUNCAO, a, b)

        if sair():
            break


calculadora()
