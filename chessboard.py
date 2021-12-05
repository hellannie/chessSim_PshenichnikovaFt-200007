import msvcrt as m
import sys
#массив для координат полей и строковое значение для названия фигуры
main_fields = [[0,0],[0,0]]
figure = None
def readCoordinates(chess_xy):
    check = 0
    while check == 0:
        try:
            chess_xy[0][0],chess_xy[0][1] = map(int, input("Координаты первого поля: ").split())
        except Exception:
            print("Координаты не являются целыми числами")
            check = 0
        if (1<=chess_xy[0][0]<=8) and (1<=chess_xy[0][1]<=8):
            check = 1
        else:
            print("Значения координат должны находиться в диапазоне от 1 до 8")
    check = 0
    while check == 0:
        try:
            chess_xy[1][0],chess_xy[1][1] = map(int, input("Координаты второго поля: ").split())
        except Exception:
            print("Координаты не являются целыми числами")
            check = 0
        if (1<=chess_xy[1][0]<=8) and (1<=chess_xy[1][1]<=8):
            check = 1
        else:
            print("Значения координат должны находиться в диапазоне от 1 до 8")
    return chess_xy
def readFigure(fig):
    fig = input("Введите фигуру (Конь - К (недоступно для третьего задания), Слон - С, Ладья - Л, Ферзь - Ф):")
    if fig.upper() == "К":
        return "конь"
    elif fig.upper() == "С":
        return "слон"
    elif fig.upper() == "Л":
        return "ладья"
    elif fig.upper() == "Ф":
        return "ферзь"
    else:
        return None
def colorCheck(a):
    if (a[0][0] + a[0][1]) % 2 == (a[1][0] + a[1][1]) % 2:
        return "одного цвета"
    else:
        return "не одного цвета"
def diagonalCheck(a):
    return (abs(a[0][0] - a[1][0]) == abs(a[0][1] - a[1][1]))
"""Ответ на вопрос Б)"""
def KnightMove(a):
    q = "не"
    moves = [[1,2],[2,1],[1,-2],[2,-1],[-1,2],[-2,1],[-1,-2],[-2,-1]]
    for i in range(len(moves)):
        if a[0][0]+moves[i][0] == a[1][0] and a[0][1]+moves[i][1] == a[1][1]:
            q = ""
    print("Конь с поля ({0},{1}) {2} угрожает полю ({3},{4})".format(a[0][0],a[0][1],q, a[1][0],a[1][1]))
def BishopMove(a):
    q = "не"
    if diagonalCheck(a):
        q = ""
    print("Слон на поле ({0},{1}) {4} угрожает полю ({2},{3})".format(a[0][0],a[0][1],a[1][0],a[1][1],q))
def RookMove(a):
    q = "не"
    if (a[0][0] == a[1][0]) or (a[0][1] == a[1][1]):
        q = ""
    print("Ладья на поле ({0},{1}) {4} угрожает полю ({2},{3})".format(a[0][0],a[0][1],a[1][0],a[1][1],q))
def QueenMove(a):
    q = "не"
    if (diagonalCheck(a) or (a[0][1] == a[1][1]) or (a[0][0] == a[1][0])):
        q = ""
    print("Ферзь на поле ({0},{1}) {4} угрожает полю ({2},{3})".format(a[0][0],a[0][1],a[1][0],a[1][1],q))

def Rook2Move(a):
    q = ""
    f = ""
    if (a[1][0] == a[0][0] or a[1][1] == a[0][1]) == False:
        q = "не"
        f = "Ладья может совершить ход на поле ({0},{1}), оттуда на первое поле".format(a[0][0],a[1][1])
    print("Ладья со второго поля " + q + " может попасть на первое. "+f)
def Queen2Move(a):
    q = ""
    f = ""
    if (diagonalCheck(a) or a[1][0] == a[0][0] or a[1][1] == a[0][1]) == False:
        q = "не"
        f = "Ферзь может совершить ход на поле ({0},{1}), оттуда на первое поле".format(a[0][0],a[1][1])
    print("Ферзь со второго поля " + q + " может попасть на первое. " + f)
def Bishop2Move(a):
    q = ""
    if diagonalCheck(a) == False:
        if colorCheck(a) == "не одного цвета":
            q = "не сможет попасть никогда, так как они разного цвета"
        else:
            q = ""
            x,y = a[0][0], a[0][1]
            while x>0 and y>0:
                x -= 1
                y -= 1
                if diagonalCheck([[x,y],[a[1][0], a[1][1]]]):
                    q = "сможет попасть через промежуточное поле ({0},{1})".format(x,y)
                    break
            x,y = a[0][0], a[0][1]
            if q == "":
                while x<8 and y>0:
                    x += 1
                    y -= 1
                    if diagonalCheck([[x,y],[a[1][0], a[1][1]]]):
                        q = "сможет попасть через промежуточное поле ({0},{1})".format(x,y)
                        break
            x,y = a[0][0], a[0][1]
            if q == "":
                while x>0 and y<8:
                    x -= 1
                    y += 1
                    if diagonalCheck([[x,y],[a[1][0], a[1][1]]]):
                        q = "сможет попасть через промежуточное поле ({0},{1})".format(x,y)
                        break
            x,y = a[0][0], a[0][1]
            if q == "":
                while x<8 and y<8:
                    x += 1
                    y += 1
                    if diagonalCheck([[x,y],[a[1][0], a[1][1]]]):
                        q = "сможет попасть через промежуточное поле ({0},{1})".format(x,y)
                        break
    else:
        q = "может попасть за один ход"
    print("Слон с первого на второе поле "+q)


readCoordinates(main_fields)
print("Были введены поля с координатами ({0},{1}) и ({2},{3})".format(main_fields[0][0],main_fields[0][1],main_fields[1][0],main_fields[1][1]))
print("\n Ответ на первый вопрос")
print("Поля ({0},{1}) и ({2},{3}) – {4}".format(main_fields[0][0],main_fields[0][1],main_fields[1][0],main_fields[1][1],colorCheck(main_fields)))
while figure == None:
    figure = readFigure(figure)
print("На поле с координатами ({0},{1}) стоит {2}".format(main_fields[0][0],main_fields[0][1],figure))
print("\n Ответ на второй вопрос")
if figure == "конь":
    KnightMove(main_fields)
elif figure == "слон":
    BishopMove(main_fields)
elif figure == "ладья":
    RookMove(main_fields)
elif figure == "ферзь":
    QueenMove(main_fields)
figure = None
while figure == None:
    figure = readFigure(figure)
print("На поле с координатами ({0},{1}) стоит {2}".format(main_fields[0][0],main_fields[0][1],figure))
print("\n Ответ на третий вопрос")
if figure == "слон":
    Bishop2Move(main_fields)
elif figure == "ладья":
    Rook2Move(main_fields)
elif figure == "ферзь":
    Queen2Move(main_fields)
elif figure == "конь":
    print("Невозможно рассчитать траекторию движения для коня")
m.getch()
sys.exit()