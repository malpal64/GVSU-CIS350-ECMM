import pygame
from controller import Controller

pygame.init()
pygame.display.set_caption("Shop 'n Dash")
clock = pygame.time.Clock()

run = True
controller = Controller()

while run:
    # check quit button push
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Display screen based on status
    status = controller.current_state
    if status == 0:
        action = controller.show_start()
        if action:
            controller.current_state = 1
    elif status == 1:
        controller.show_character_select()
    elif status == 2:
        controller.show_level()
    elif status == 3:
        controller.show_revive()
    elif status == 4:
        controller.show_upgrade_screen()
    elif status == 5:
        controller.show_death()

    pygame.display.update()
    clock.tick(60)  # Cap the frame rate at 60 frames per second

pygame.quit()
