# В этом файле собраны переменные и функции для работы с массивом (матрицей) минного поля

# загружаем модуль для работы со случайными числами
import random

# задаем размер минного поля в ячейках, и кол-во мин на минном поле
MINEFIELD_ROWS = 10
MINEFIELD_COLUMNS = 10
NUMBER_MINES = 13

# создаем двумерный массив (список списков) и заполняем его нулями 
# как это сделать нашли здесь: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array
# массив для минного поля создаем с запасом:
# не от 1 до MINEFIELD_ROWS, а от 0 до MINEFIELD_ROWS + 1
# не от 1 до MINEFIELD_COLUMNS, а от 0 до MINEFIELD_COLUMNS + 1
minefieldArray = [[0 for c in range(MINEFIELD_COLUMNS+2)] for r in range(MINEFIELD_ROWS+2)]

# в нашем массиве будут такие числа:
# (-1) - в этой ячейке массива есть мина
# (+10) - ячейка открыта
# (+100) - в этой ячейке находится сапер
# (0..8) - число в ячейке, которое означает сколько мин в соседних ячайках

# Эта функция стирает все в массиве и случайным образом расставляет в нем мины
# у функции один параметр - кол-во мин
def fill_Minefield(mineNumber: int) -> bool:

    # заполняем весь массив нулями
    for r in range(0, MINEFIELD_ROWS+2):
        for c in range(0, MINEFIELD_COLUMNS+2):
            minefieldArray[r][c] = 0

    # устанавливаем в массив мины. не более mineNumber мин
    m = 0
    while m <= mineNumber:
        r = random.randint(1, MINEFIELD_ROWS)
        c = random.randint(1, MINEFIELD_COLUMNS)
        # в ячейку с координатами (1,1) и с координатами (MINEFIELD_ROWS, MINEFIELD_COLUMNS) мину не ставим
        if (not ((r == 1 and c == 1) or (r == MINEFIELD_ROWS and c == MINEFIELD_COLUMNS))):
            minefieldArray[r][c] = -1
            m += 1

    # считаем кол-во мин вокруг ячейки
    for r in range(1, MINEFIELD_ROWS+1):
        for c in range(1, MINEFIELD_COLUMNS+1):
            n = 0
            if (minefieldArray[r][c] != -1):
                if (minefieldArray[r-1][c-1] == -1): n+=1
                if (minefieldArray[r-1][c] == -1): n+=1
                if (minefieldArray[r-1][c+1] == -1): n+=1
                if (minefieldArray[r][c+1] == -1): n+=1
                if (minefieldArray[r+1][c+1] == -1): n+=1
                if (minefieldArray[r+1][c] == -1): n+=1
                if (minefieldArray[r+1][c-1] == -1): n+=1
                if (minefieldArray[r][c-1] == -1): n+=1
                minefieldArray[r][c] = n

    # открываем первую ячейку (+10) и помещаем в неё сапера (+100) 
    minefieldArray[1][1] += 110
    # открываем правую нижнюю ячейку (последнюю) - прибавляем в неё +10
    minefieldArray[MINEFIELD_ROWS][MINEFIELD_COLUMNS] += 10

    return True

# делаем один шаг по минному полю.
# у функции два параметра: ряд и колонка куда нужно шагнуть.
# Сапер может шагнуть только в соседнюю клетку той, где стоит.
# шагнув в закрытую клетку сапер её открывает.
# Сапер взрывается если в закрытой клетке мина.
# Функция возращает True если шаг сделан и False если Сапер взорвался
def do_Step_Minefield(toRow: int, toColumn: int) -> bool:

    # Ряд и колонка куда мы шагнем
    r = toRow
    c = toColumn

    # если мы находились в соседней ячейке, то делаем шаг

    if (minefieldArray[r-1][c-1] >= 100):
        minefieldArray[r-1][c-1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r-1][c] >= 100):
        minefieldArray[r-1][c] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r-1][c+1] >= 100):
        minefieldArray[r-1][c+1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r][c+1] >= 100):
        minefieldArray[r][c+1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r+1][c+1] >= 100):
        minefieldArray[r+1][c+1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r+1][c] >= 100):
        minefieldArray[r+1][c] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r+1][c-1] >= 100):
        minefieldArray[r+1][c-1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    if (minefieldArray[r][c-1] >= 100):
        minefieldArray[r][c-1] -= 100   # покидаем предыдущую ячейку
        if (minefieldArray[r][c] >= 10):
            minefieldArray[r][c] += 100   # помещаем сапера в эту ячейку
        elif (minefieldArray[r][c] >= 0):
            minefieldArray[r][c] += 110   # помещаем сапера в эту ячейку и открываем ячейку
        elif (minefieldArray[r][c] == -1):
            return False                  # взорвались!!!

    return True
