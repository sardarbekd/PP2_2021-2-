import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

is_blue = True
color = (0, 0, 255)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pygame.display.flip()

    if not is_blue : 
        color = 