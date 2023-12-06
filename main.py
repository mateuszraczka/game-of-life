from config import WIDTH, HEIGHT, CELL_WIDTH, CELL_HEIGHT, N_CELLS_X, N_CELLS_Y
from game import Game
from renderer import GameRenderer
import pygame
from event_handler import GameEventHandler
from command import GameCommand, Commands
from ui import PAUSE_BUTTON, LOAD_BUTTON, SAVE_BUTTON

# Init pygame
pygame.init()
clock = pygame.time.Clock()

# Init game logic
game = Game(N_CELLS_X, N_CELLS_Y)

# Set buttons
BUTTONS = [PAUSE_BUTTON, LOAD_BUTTON, SAVE_BUTTON]

# Init renderer
game_renderer = GameRenderer(game, WIDTH, HEIGHT, CELL_WIDTH, CELL_HEIGHT, N_CELLS_X, N_CELLS_Y, BUTTONS)

# Init event handler
event_handler = GameEventHandler(BUTTONS, game)

# Init commands
pause_command = GameCommand(game, Commands.PAUSE)
load_command = GameCommand(game, Commands.LOAD)
save_command = GameCommand(game, Commands.SAVE)

# Attach commands to UI
PAUSE_BUTTON.set_command(pause_command)
LOAD_BUTTON.set_command(load_command)
SAVE_BUTTON.set_command(save_command)


while game.running:
    game_renderer.render()
    event_handler.handle_events()
    game.run()
    clock.tick(30)

pygame.quit()
