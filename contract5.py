import pygame
import numpy as np

# path to image file, which is located in the same folder as this project
path = "image.jpeg"

# pygame initialisation
pygame.init()
pygame.display.set_caption("Contract #5")
screen = pygame.display.set_mode((500, 750))

# open the image and load it as a pygame.Surface
image = pygame.image.load(path).convert()


def protanopia():                              # I have no clue on how to simulate colour-blindness, I just altered some
                                               # of the rgb values of the image in some ways - trial and erroring until
                                               # I was fairly happy.
                                               # I'm using 2 for loops to loop through every pixel in the image
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_at((x, y))
            temp = pixel

            if pixel.r > pixel.g * 2:
                pixel.g = int(pixel.r / 2) - 10
                pixel.r = int(pixel.r / 2) + 10
            else:
                if pixel.r > pixel.g:
                    red_green_diff = max(min(10 * (pixel.g / pixel.r), 10), 7) / 10
                else:
                    red_green_diff = max(min(10 * (pixel.r / pixel.g), 10), 7) / 10

                if pixel.r > pixel.g:
                    original_r = pixel.r
                    temp.r = int(temp.r * red_green_diff)
                    red_diff = original_r - temp.r
                    red_diff = 20 if red_diff > 20 else red_diff
                    temp.g = max(min(int(temp.g + red_diff), 255), 0)

                elif pixel.g > pixel.r:
                    original_g = pixel.g
                    temp.g = int(temp.g * red_green_diff)
                    green_diff = original_g - temp.g
                    green_diff = 20 if green_diff > 20 else green_diff
                    temp.r = max(min(int(temp.r + green_diff), 255), 0)
            image.set_at((x, y), temp)


# i only managed to do one of the main three colour-blindness

protanopia()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(image, (0, 0))

    pygame.display.update()