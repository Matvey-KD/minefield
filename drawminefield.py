import pygame

pygame.init()
# Код, описывающий окно программы
w = 300  # Ширина окна
h = 300  # Высота окна
screen = pygame.display.set_mode([w, h])
screen.fill([255,255,255])

wc = w // 12
hc = h // 12
delta=3

for r in range(0,10):
    for c in range(0,10):
        x = wc + c * wc
        y = hc + r * hc
        pygame.draw.rect(screen, [0,0,0],[x,y,wc-delta,hc-delta])
        pygame.display.flip()

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


    # Отображение нарисованных объектов
    pygame.display.flip()

    # Контроль FPS
    clock.tick(FPS)

pygame.quit()