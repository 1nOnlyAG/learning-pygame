import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
paddle = {
    "color": "red",
    "shape": (100, 24),
    "pos": (320, 0.9 * 480)
}
ball = {
    
}

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    paddle["pos"] = (mouse_x - 50, paddle["pos"][1])

    screen.fill("#001200") 
    pygame.draw.rect(screen, paddle["color"], paddle["pos"] + paddle["shape"])
    pygame.display.flip()
    clock.tick(60)
