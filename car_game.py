import pygame
import time

WIDTH = 800
HEIGHT = 600
car_width = 250
car_height = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def car(carImg,gameDisplay, x, y):
    gameDisplay.blit(carImg,(x, y))

def message_display(message):
    text = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(message, text)
    TextRect.center = ((WIDTH/2), (HEIGHT/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    main()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def crash():
    message_display("You crashed!")

#def things(thing_x, thing_y, thing_w, thing_h, color):



def main():
    crashed = False
    end = False
    car_x = (WIDTH*0.35)
    car_y = (HEIGHT*0.8)
    x_change = 0
    y_change = 0


    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

        car_x += x_change
        car_y += y_change
        print(car_x,car_y)
        gameDisplay.fill(WHITE)
        car(carImg, gameDisplay, car_x, car_y)

        if car_x > WIDTH - car_width or car_y > HEIGHT - car_height or car_x < 0 or car_y < 0:
            crash()

        pygame.display.update() #if i put just one, it just updates ones
        clock.tick(60)  # FPS




if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))

    pygame.display.set_caption("Racee")
    clock = pygame.time.Clock()

    carImg = pygame.image.load("car_bmw.jpg")
    main()


    pygame.quit()