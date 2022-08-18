from audioop import reverse
from graphics import *


def carregaJanela():
    janela = GraphWin("Goku pulando", 800, 800, autoflush=True)
    janela.setCoords(-400, -400, 400, 400)
    return janela


def carregaSprites(personagem):
    dicionario = {}          # 0         1         2
    nomeDasImagens = ["parado", "pulando", "caindo"]
    for i in (nomeDasImagens):
        dicionario[i] = Image(Point(0, 0), "sprites/" +
                              personagem+" "+i + ".png")
    print("sprites/" + personagem+" "+i + ".png")
    return dicionario


def pulou(janela):
    teclaPressionada = janela.checkKey()
    time.sleep(0.1)
    if teclaPressionada == "space":
        return True
    else:
        return False


def realizaPulo(janela, sprites, velocidadeNoTempo):
    velocidadeNoTempo = sorted(velocidadeNoTempo, reverse=True)
    sprites["parado"].undraw()
    sprites["pulando"].draw(janela)
    for i in range(20):  # PULANDO
        sprites["pulando"].move(0, velocidadeNoTempo[i])
        sprites["caindo"].move(0, velocidadeNoTempo[i])

        time.sleep(0.01)


def realizaQueda(janela, sprites, velocidadeNoTempo):
    sprites["pulando"].undraw()
    sprites["caindo"].draw(janela)
    for i in range(20):  # PULANDO
        sprites["pulando"].move(0, -velocidadeNoTempo[i])
        sprites["caindo"].move(0, -velocidadeNoTempo[i])
        time.sleep(0.01)


# personagem = input("Quem quer ver pulando?")
personagem = "vegeta"
velocidadeNoTempo = [2, 5.609, 8.849, 11.73, 14.29, 16.54, 18.50, 20.19, 21.63,
                     22.84, 23.84, 24.65, 25.29, 25.78, 26.14, 26.39, 26.55, 26.64, 26.68, 26.69]
janela = carregaJanela()
sprites = carregaSprites(personagem)
sprites["parado"].draw(janela)
while 1:
    while not pulou(janela):
        pass
    realizaPulo(janela, sprites, velocidadeNoTempo)
    realizaQueda(janela, sprites, velocidadeNoTempo)

    sprites["caindo"].undraw()
    sprites["parado"].draw(janela)


janela.getMouse()  # Pause to view result
janela.close()    # Close window when done
