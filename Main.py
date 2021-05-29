import matplotlib.pylab as ptl
import matplotlib.animation as animacao
import random
from matplotlib.widgets import Button
import BubbleSort as Bubble
import SelectionSort as Selection
import InsertionSort as Insertion

time = 0

anim = animacao

passo = False

iteration = [0]

def update_fig(A, barras, iteration):
    global time
    global anim
    global passo
    if passo == True:
        anim.event_source.stop()
    else:
        time += 0.05
        text1.set_text("Tempo de Execução (Animação): {:.0f} segundos".format(time))
    for barra, val in zip(barras, A):
        barra.set_height(val)
    iteration[0] += 1
    text.set_text("Número de comparações: {}".format(iteration[0]))

def Button_Next():
    layout = ptl.axes([0.12, 0.91, 0.13, 0.075])
    botao = Button(layout, "Próximo")
    return botao


def Roda_Animacao(event):
    global anim
    anim.event_source.start()

#-------MENU--------
print("Selecione a ordem inicial do arrajo: \n [0] Aleatório\n [1] Invertido\n [2] Cresce e Diminui")
Arranjo = input()
print("Selecione o algoritmo para visualizar: \n [0] Bubble-Sort\n [1] Insertion-Sort\n [2] Selection-Sort")
algoritmo = input()
print("Selecione o tipo de visualização: \n [0] Automática\n [1] Passo a Passo")
aux = input()

#-----Seleção Arranjo------
if int(Arranjo) == 0:
    A = [x + 1 for x in range(16)]
    random.shuffle(A)
elif int(Arranjo) == 1:
    A = [x + 1 for x in range(16)]
    A.sort(reverse= True)
elif int(Arranjo) == 2:
    x = 1
    y = 1
    A = []
    B = []
    for x in range(16):
        if x%2 == 0:
            A.append(x + 1)
    for y in range(16):
        if y%2 == 1:
            B.append(y + 1)
    B.sort(reverse=True)

    A.extend(B)
else:
    print("Opcao invalida")

#---------Criando Grafico------------
fig, ax = ptl.subplots()
bar_rects = ax.bar(range(len(A)), A, color = "black", align = "edge")
ax.set_xlim(0, len(A))
ax.set_ylim(0, int(1.07 * max(A)))
text = ax.text(0.04, 0.95, "", transform = ax.transAxes)
text1 = ax.text(0.04, 0.90, "", transform = ax.transAxes, color="red")

#--------Selecao Tipo-------------
if int(aux) == 0:
    passo = False
elif int(aux) == 1:
    passo = True
else:
    "Opção inválida"

if passo == True:
    botao = Button_Next()
    botao.on_clicked(Roda_Animacao)

#--------Seleçao Algoritmo------
Frames = None

if int(algoritmo) == 0: Frames = Bubble.Bubble_Sort(A)

elif int(algoritmo) == 1: Frames = Insertion.Insertion_Sort(A)

elif int(algoritmo) == 2: Frames = Selection.Selection_Sort(A)


anim = animacao.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration), blit=False,
                                  frames = Frames, interval = 1, repeat=False)
ax.set_title(Frames.__name__)

ptl.show()