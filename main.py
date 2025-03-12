import pygame
import math

pygame.init()

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()
paddle = {
    "color": "red",
    "shape": (100, 24),
    "pos": (320, 0.9 * 480)
}
ball = {
    "color": "white",
    "shape": (18, 18),
    "pos": (320, 0.5 * 480)
}

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
    paddle["pos"] = (mouse_x, paddle["pos"][1])
    ball["pos"] = (ball["pos"][0], ball["pos"][1])

    # Clear Screen
    screen.fill("#001200") 
    # Draw Paddle
    pygame.draw.rect(screen, paddle["color"], paddle["pos"] + paddle["shape"])
    # Draw Ball
    pygame.draw.rect(screen, ball["color"], ball["pos"] + ball["shape"])

    paddle_x, paddle_y = paddle["pos"]
    ball_x, ball_y = ball["pos"]
    paddle_w, paddle_h = paddle["shape"]
    ball_w, ball_h = ball["shape"]

    pygame.draw.line(screen, "black", (paddle_x, 0), (paddle_x, 480))
    pygame.draw.line(screen, "black", (paddle_x + paddle_w, 0), (paddle_x + paddle_w, 480))


    if ball_x > paddle_x and ball_x < paddle_x + paddle_w:
        pygame.draw.rect(screen, "green", (0, 0, 640, 20))


    pygame.display.flip()
    clock.tick(60)
