import pygame

pygame.init()
# Код, описывающий окно программы
w = 600  # Ширина окна
h = 600  # Высота окна
screen = pygame.display.set_mode([w, h])


cellclose = pygame.image.load('minefield\\background\\paralax-background.png')
wc = w // 12
hc = h // 12
delta=w // 100
cellclose = pygame.transform.scale(cellclose, (wc-delta,hc-delta))


fon = pygame.image.load('minefield\\background\\bg7.png')
fon_x = 0
fon_y = 0


# Создаём контроль FPS
clock = pygame.time.Clock()  # Создаём таймер
FPS = 30  # Устанавливаем нужное значение FPS

# Игровой цикл и флаг выполнения программы
game_run = True
while game_run:
    # БЛОК ОБРАБОТКИ СОБЫТИЙ ИГРЫ
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  # Закрыли окно?
            game_run = False

    # БЛОК ИГРОВОЙ ЛОГИКИ
    # ... тут размещаем все вычисления ...

    # БЛОК ОТРИСОВКИ ОБЪЕКТОВ В ОКНЕ ПРОГРАММЫ
    # ... тут закрашиваем фон и рисуем все объекты программы ...
    screen.blit(fon, (fon_x, fon_y))

    for r in range(0,10):
        for c in range(0,10):
            x = wc + c * wc
            y = hc + r * hc
            screen.blit(cellclose, (x,y))

    # Отображение нарисованных объектов
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

pygame.quit()