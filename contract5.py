"""This is contract #5 from the tinkering graphics assignment.

I have attempted to simulate colour-blindness onto a image, as with the
requirements of the contract.
"""
import pygame

__author__ = 'Luke Day'


# path to image file, which is located in the same folder as this project
image_path = "image.jpeg"

# pygame initialisation
pygame.init()
pygame.display.set_caption("Contract #5")
screen = pygame.display.set_mode((500, 750))

# open the image and load it as a pygame.Surface
image = pygame.image.load(image_path).convert()


def protanopia():
    """Simulate the protanopia colour-blindness.

    Protanopia is a type of colour-blindness, which means that the person is
    less sensitive to red light.
    In this function, I have attempted to alter the colour of each pixel within
    a given image to simulate protanopia. I have used 2 for loops to ensure
    that I iterate upon every pixel in the image.
    """
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_at((x, y))
            temp_pixel = pixel

            if pixel.r > pixel.g * 2:
                pixel.g = int(pixel.r / 2) - 10
                pixel.r = int(pixel.r / 2) + 10
            else:
                if pixel.r > pixel.g:
                    red_green_diff = max(min(10*(pixel.g/pixel.r), 10), 7)/10
                else:
                    red_green_diff = max(min(10*(pixel.r/pixel.g), 10), 7)/10

                if pixel.r > pixel.g:
                    original_r = pixel.r
                    temp_pixel.r = int(temp_pixel.r * red_green_diff)
                    red_diff = original_r - temp_pixel.r
                    red_diff = 20 if red_diff > 20 else red_diff
                    temp_pixel.g = max(min(int(temp_pixel.g+red_diff), 255), 0)

                elif pixel.g > pixel.r:
                    original_g = pixel.g
                    temp_pixel.g = int(temp_pixel.g * red_green_diff)
                    green_diff = original_g - temp_pixel.g
                    green_diff = 20 if green_diff > 20 else green_diff
                    temp_pixel.r = max(min(int(temp_pixel.r+green_diff), 255), 0)
            image.set_at((x, y), temp_pixel)


def main():
    """Main program loop.

    Main function holds the while loop that keeps the program displayed
    on the screen. It runs until the user closes the application window.
    It also calls the function 'protanopia' in order to simulate the
    respective colour-blindness.
    """
    protanopia()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(image, (0, 0))
        pygame.display.update()

    exit()


main()
