from enum import Enum


class Cell(Enum):
    FREE = 0
    BLOCKED = 1
    TARGET = 2
    OCCUPIED = 3

    def __str__(self):
        representation = {
            self.FREE: '_',
            self.BLOCKED: 'X',
            self.TARGET: '*',
            self.OCCUPIED: 'O'
        }
        return representation[self]