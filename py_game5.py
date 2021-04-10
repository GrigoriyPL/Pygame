# круг двигается по клавишам, существует зона в которой круг двигается быстрее и меняет цвет, при отсутвии
# нажатия на кнопки, то круг возвращается в исхнодное положение

import pygame

x, y = 100, 100
W, H = 500, 500

pygame.init()
sc = pygame.display.set_mode((W,H))
color = (255,255,255)
fps = pygame.time.Clock()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    sc.fill((0,0,0))
    
    keys = pygame.key.get_pressed() # перемещение с клавиатуры
    if keys [pygame.K_DOWN]:
        y += 1
        if y > H:
            y = 0

    if keys [pygame.K_UP]:
        y -= 1
        if y > H:
            y = 0

    if keys [pygame.K_RIGHT]:
        x += 1
        if x > W:
            x = 0

    if keys[pygame.K_LEFT]:
        x -= 1
        if x > W:
            x = 0
    if x < 100 or x > 400 and y < 400 and y > 100:
        if keys [pygame.K_DOWN]:
            y += 3
            if y > H:
                y = 0

    if keys [pygame.K_UP]:
            y -= 3
            if y > H:
                y = 0

    if keys [pygame.K_RIGHT]:
            x += 3
            if x > W:
                x = 0

    if keys[pygame.K_LEFT]:
            x -= 3
            if x > W:
                x = 0
            

    if keys[pygame.K_ESCAPE]:
        exit()
    pygame.draw.circle(sc, color, (x, y), 25)

    fps.tick(200)
    pygame.display.update()