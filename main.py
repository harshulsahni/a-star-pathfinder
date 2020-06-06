from enum import Enum
import math

import pygame

CELL_WIDTH = 10


class Status(Enum):
    FREE = 0
    SELF = 1
    BLOCKED = 2
    GOAL = 3

    def to_color(self) -> tuple:
        if self is Status.FREE:
            return 0, 0, 0
        elif self is Status.SELF:
            return 52, 88, 235
        elif self is Status.BLOCKED:
            return 166, 10, 10
        elif self is Status.GOAL:
            return 0, 240, 100


class Cell:
    def __init__(self, x: int, y: int, status: Status = Status.FREE):
        self.x = x
        self.y = y
        self.status = status

    def change_status(self, new_status: Status):
        self.status = new_status


def init_board(height: int, width: int, cell_width: int) -> [[int]]:
    board = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(Cell(i * cell_width, j * cell_width, Status.FREE))

        board.append(row)

    board[0][0].change_status(Status.SELF)
    board[height - 1][width - 1].change_status(Status.GOAL)

    return board


def draw_board(b: [[Cell]], window: pygame.display) -> None:
    for row in b:
        for cell in row:
            pygame.draw.rect(window, cell.status.to_color(), (cell.x, cell.y, CELL_WIDTH, CELL_WIDTH))
    pygame.display.update()


def mouse_posn_to_board_posn(mouse_x: float, mouse_y: float) -> (int, int):
    float_board_posn_x = mouse_x / CELL_WIDTH
    float_board_posn_y = mouse_y / CELL_WIDTH

    return math.floor(float_board_posn_x), math.floor(float_board_posn_y)


def add_board_blocks(b: [[Cell]], mouse_pos: (float, float)) -> None:
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    board_x, board_y = mouse_posn_to_board_posn(mouse_x, mouse_y)

    b[board_x][board_y].change_status(Status.BLOCKED)


def run_game(height: int = 500, width: int = 500, caption: str = 'Game', background_color=(0, 0, 0)) -> None:
    pygame.init()
    window = pygame.display.set_mode((height, width))
    pygame.display.set_caption(caption)
    game_is_running = True
    window.fill(background_color)

    is_mouse_down = False

    board = init_board(math.floor(height / CELL_WIDTH), math.floor(width / CELL_WIDTH), CELL_WIDTH)

    while game_is_running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_down = True

            elif event.type == pygame.MOUSEBUTTONUP:
                is_mouse_down = False

            elif event.type == pygame.MOUSEMOTION and is_mouse_down:
                add_board_blocks(board, pygame.mouse.get_pos())

        draw_board(board, window)
        window.fill(background_color)
    pygame.quit()


if __name__ == '__main__':
    run_game()
