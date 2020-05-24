import pygame
from time import sleep
from numpy import interp
from random import randint

numbers = [randint(10, 100) for i in range(60)]
sorted_list = numbers
comparator = sorted(numbers)

w, h = 800, 600
win = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()


def main():
    bar_w = w // len(numbers)
    max_bar_y = max(numbers)

    i = 0

    # Loop through the entire list and perform operations.
    while sorted_list != comparator:
        clock.tick(200)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        # Reset i if it is outside index
        if i >= len(sorted_list) - 1:
            i = 0

        # Get the numbers at the current and next index
        first = sorted_list[i]
        second = sorted_list[i + 1]

        # If the first number is greater, swap them
        if first > second:
            sorted_list[i], sorted_list[i + 1] = second, first

        # Render a bar for each number
        win.fill((0, 0, 0))

        for j in range(len(sorted_list)):
            bar_h = interp(sorted_list[j], (0, max_bar_y), (0, h))

            # Draw the bars being checked in green
            if j == i or j == i + 1:
                pygame.draw.rect(win, (0, 255, 0), (j * bar_w, h - bar_h, bar_w, bar_h))
            else:
                pygame.draw.rect(win, (255, 255, 255), (j * bar_w, h - bar_h, bar_w, bar_h))

        pygame.display.update()

        i += 1


if __name__ == "__main__":
    main()
    print("Unsorted: ", numbers)
    print("Sorted:", sorted_list)
    sleep(5)
