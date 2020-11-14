masiv=[[" ", "1", "2", "3"],
       ["1", "-", "-", "-"],
       ["2", "-", "-", "-"],
       ["3", "-", "-", "-"]]

def draw():
    for x in masiv:
        print(x[0], x[1], x[2], x[3])

def stepX():
    print("\nХодит X\n")
    row=int(input("Введите номер строки = "))
    column = int(input("Введите номер столбца = "))

    while row < 1 or row > 3 or column < 1 or column > 3 or masiv[row][column]=="X" or masiv[row][column]=="O":
        row = int(input("Введите номер строки заного = "))
        column = int(input("Введите номер столбца заного = "))

    masiv[row][column]="X"


def step0():
    print("\nХодит 0\n")
    row=int(input("Введите номер строки = "))
    column = int(input("Введите номер столбца = "))

    while row < 1 or row > 3 or column < 1 or column > 3 or masiv[row][column]=="X" or masiv[row][column]=="O":
        row = int(input("Введите номер строки заного = "))
        column = int(input("Введите номер столбца заного = "))

    masiv[row][column]="O"


def win():
    for x in masiv:
        if x[1] == x[2] == x[3] != "-":
            print("Победитель -", x[1])
            victory[0] = 1
            break
    for i in range(1, 3):
        if masiv[1][i] == masiv[2][i] == masiv[3][i] != "-":
            print("Победитель -", masiv[1][i])
            victory[0] = 1
            break
        if masiv[1][1] == masiv[2][2] == masiv[3][3] != "-":
            print("Победитель -", masiv[1][1])
            victory[0] = 1
        if masiv[1][3] == masiv[2][2] == masiv[3][1] != "-":
            print("Победитель -", masiv[1][3])
            victory[0] = 1


print("Крестики-нолики 3 х 3.\n")
draw()
k = 0
victory = [0]
while True:
    stepX()
    k += 1
    draw()
    win()
    if victory[0] == 1:
        break
    elif k == 9:
        print("Ничья")
        break
    step0()
    win()
    if victory[0] == 1:
        break
    k += 1
    draw()
