import pygame 
pygame.init()
screen = pygame.display.set_mode((400, 300)) # parameters of the screen (width, length)
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip() # показывает изменения на экране
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(30, 30, 60, 60))
    #                        (RED, GREEN, BLUE) можно возпользоваться colorspire.com
# pressed= pygame.key.get_pressed() - список нажатых кнопок