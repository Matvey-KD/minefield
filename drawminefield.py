import pygame
import minefield

pygame.init()
# Код, описывающий окно программы
w = 600  # Ширина окна
h = 600  # Высота окна
screen = pygame.display.set_mode([w, h])

wc = w // (minefield.MINEFIELD_COLUMNS+2)
hc = h // (minefield.MINEFIELD_ROWS+2)
delta=w // 100

# Загружаем все картинки ячеек
cellclose = pygame.image.load("minefield\\background\\close-cell.png")
cellclose = pygame.transform.scale(cellclose, (wc-delta,hc-delta))
bomba = pygame.image.load("minefield\\background\\bomba.png")
bomba = pygame.transform.scale(bomba, (wc-delta,hc-delta))
opencell1 = pygame.image.load("minefield\\background\\open-cell-1.png")
opencell1 = pygame.transform.scale(opencell1, (wc-delta,hc-delta))
opencell2 = pygame.image.load("minefield\\background\\open-cell-2.png")
opencell2 = pygame.transform.scale(opencell2, (wc-delta,hc-delta))
opencell3 = pygame.image.load("minefield\\background\\open-cell-3.png")
opencell3 = pygame.transform.scale(opencell3, (wc-delta,hc-delta))
opencell4 = pygame.image.load("minefield\\background\\open-cell-4.png")
opencell4 = pygame.transform.scale(opencell4, (wc-delta,hc-delta))
opencell5 = pygame.image.load("minefield\\background\\open-cell-5.png")
opencell5 = pygame.transform.scale(opencell5, (wc-delta,hc-delta))
opencell6 = pygame.image.load("minefield\\background\\open-cell-6.png")
opencell6 = pygame.transform.scale(opencell6, (wc-delta,hc-delta))
opencell7 = pygame.image.load("minefield\\background\\open-cell-7.png")
opencell7 = pygame.transform.scale(opencell7, (wc-delta,hc-delta))
opencell = pygame.image.load("minefield\\background\\open-cell.png")
opencell = pygame.transform.scale(opencell, (wc-delta,hc-delta))

opencell1caper = pygame.image.load("minefield\\background\\open-cell-1-caper.png")
opencell1caper = pygame.transform.scale(opencell1caper, (wc-delta,hc-delta))
opencell2caper = pygame.image.load("minefield\\background\\open-cell-2-caper.png")
opencell2caper = pygame.transform.scale(opencell2caper, (wc-delta,hc-delta))
opencell3caper = pygame.image.load("minefield\\background\\open-cell-3-caper.png")
opencell3caper = pygame.transform.scale(opencell3caper, (wc-delta,hc-delta))
opencell4caper = pygame.image.load("minefield\\background\\open-cell-4-caper.png")
opencell4caper = pygame.transform.scale(opencell4caper, (wc-delta,hc-delta))
opencell5caper = pygame.image.load("minefield\\background\\open-cell-5-caper.png")
opencell5caper = pygame.transform.scale(opencell5caper, (wc-delta,hc-delta))
opencell6caper = pygame.image.load("minefield\\background\\open-cell-6-caper.png")
opencell6caper = pygame.transform.scale(opencell6caper, (wc-delta,hc-delta))
opencell7caper = pygame.image.load("minefield\\background\\open-cell-7-caper.png")
opencell7caper = pygame.transform.scale(opencell7caper, (wc-delta,hc-delta))
opencellcaper = pygame.image.load("minefield\\background\\open-cell-caper.png")
opencellcaper = pygame.transform.scale(opencellcaper, (wc-delta,hc-delta))

# Загружаем фон окна
fon = pygame.image.load("minefield\\background\\fon.jpg")
fon = pygame.transform.scale(fon, (w,h))
fon_x = 0
fon_y = 0

# Загружаем картинки финальных сообщений
wewin = pygame.image.load("minefield\\background\\fon.jpg")
wewin = pygame.transform.scale(wewin, (w // 2, h // 2))
wewin_x = w // 3
wewin_y = h // 3

welose = pygame.image.load("minefield\\background\\fon.jpg")
welose = pygame.transform.scale(welose, (w // 2, h // 2))
welose_x = w // 3
welose_y = h // 3

# Функция, которая рисует минное поле по информации из массива minefield.minefieldArray[][] 
def draw_Minefield(showMine:bool) -> bool:

    for r in range(1, minefield.MINEFIELD_ROWS+1):
        for c in range(1, minefield.MINEFIELD_COLUMNS+1):
            v = minefield.minefieldArray[r][c]
            x = wc + (c-1) * wc
            y = hc + (r-1) * hc

            if (v >= 110):
                if v==110: screen.blit(opencellcaper, (x,y))
                elif v==111: screen.blit(opencell1caper, (x,y))
                elif v==112: screen.blit(opencell2caper, (x,y))
                elif v==113: screen.blit(opencell3caper, (x,y))
                elif v==114: screen.blit(opencell4caper, (x,y))
                elif v==115: screen.blit(opencell5caper, (x,y))
                elif v==116: screen.blit(opencell6caper, (x,y))
                elif v==117: screen.blit(opencell7caper, (x,y))
            elif (v >= 10):
                if v==10: screen.blit(opencell, (x,y))
                elif v==11: screen.blit(opencell1, (x,y))
                elif v==12: screen.blit(opencell2, (x,y))
                elif v==13: screen.blit(opencell3, (x,y))
                elif v==14: screen.blit(opencell4, (x,y))
                elif v==15: screen.blit(opencell5, (x,y))
                elif v==16: screen.blit(opencell6, (x,y))
                elif v==17: screen.blit(opencell7, (x,y))
            elif ((v == -1) and showMine):
                screen.blit(bomba, (x,y))
            else:
                screen.blit(cellclose, (x,y))

# Создаём контроль FPS
clock = pygame.time.Clock()  # Создаём таймер
FPS = 30  # Устанавливаем нужное значение FPS

minefield.fill_Minefield(minefield.NUMBER_MINES)

# Игровой цикл и флаг выполнения программы
# устанавливаем признак что не взорвались
notBlow = True 

game_run = True
while game_run:

    pos = [0,0]
    mousewas = False

    # БЛОК ОБРАБОТКИ СОБЫТИЙ ИГРЫ
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  # Закрыли окно?
            game_run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mousewas = True

    # БЛОК ИГРОВОЙ ЛОГИКИ
    # делаем шаг если щелкнули мышкой и не взорвались на прошлом шаге
    if (mousewas and notBlow):
        x = pos[0]
        y = pos[1]
        c = x // wc
        r = y // hc
        notBlow = minefield.do_Step_Minefield(r,c)

    screen.blit(fon, (fon_x, fon_y))
    # отрисовываем минное поле без мин если не взорвались
    # отрисовываем мины если взорвались
    if notBlow:
        draw_Minefield(False) # не рисуем мины
    else:
        draw_Minefield(True) # рисуем мины  
        game_run = False
    
    # если мы находимся в правой нижней клетке, то заканчиваем игру
    if minefield.minefieldArray[minefield.MINEFIELD_ROWS][minefield.MINEFIELD_COLUMNS] >= 110: 
        draw_Minefield(True) # рисуем мины  
        game_run = False

    # Отображение нарисованных объектов
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

game_run = True
while game_run:
    # БЛОК ОБРАБОТКИ СОБЫТИЙ ФИНАЛЬНОГО СООБЩЕНИЯ
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  # Закрыли окно?
            game_run = False
        if i.type == pygame.MOUSEBUTTONDOWN:
            game_run = False

    # если notBlow = True то мы находимся в правой нижней клетке и мы победили
    # иначе мы проиграли, наступили на мину.
    if notBlow:
        screen.blit(wewin, (wewin_x, wewin_y))
    else:
        screen.blit(welose, (welose_x, welose_y))
        
    # Отображение нарисованных объектов
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

pygame.quit()