import random
from termcolor import colored
from enum import Enum

UNIT_SYM = "O"

class Unit(Enum):
    WHITE_ON_RED         = 1
    #WHITE_ON_GREEN       = 2
    WHITE_ON_YELLOW      = 3
    WHITE_ON_BLUE        = 4
    WHITE_ON_MAGENTA     = 5
    WHITE_ON_CYAN        = 6
    RED_ON_WHITE         = 7
    RED_ON_GREEN         = 8
    RED_ON_YELLOW        = 9
    #RED_ON_BLUE          = 10
    #RED_ON_MAGENTA       = 11
    #RED_ON_CYAN          = 12
    #GREEN_ON_WHITE       = 13
    GREEN_ON_RED         = 14
    #GREEN_ON_YELLOW      = 15
    #GREEN_ON_BLUE        = 16
    GREEN_ON_MAGENTA     = 17
    GREEN_ON_CYAN        = 18
    YELLOW_ON_WHITE      = 19
    #YELLOW_ON_RED        = 20
    #YELLOW_ON_GREEN      = 21
    #YELLOW_ON_BLUE       = 22
    #YELLOW_ON_MAGENTA    = 23
    YELLOW_ON_CYAN       = 24
    BLUE_ON_WHITE        = 25
    #BLUE_ON_RED          = 26
    #BLUE_ON_GREEN        = 27
    #BLUE_ON_YELLOW       = 28
    #BLUE_ON_MAGENTA      = 29
    #BLUE_ON_CYAN         = 30
    MAGENTA_ON_WHITE     = 31
    #MAGENTA_ON_RED       = 32
    MAGENTA_ON_GREEN     = 33
    #MAGENTA_ON_YELLOW    = 34
    #MAGENTA_ON_BLUE      = 35
    #MAGENTA_ON_CYAN      = 36
    CYAN_ON_WHITE        = 37
    #CYAN_ON_RED          = 38
    CYAN_ON_GREEN        = 39
    CYAN_ON_YELLOW       = 40
    #CYAN_ON_BLUE         = 41
    #CYAN_ON_MAGENTA      = 42


    def __repr__(self):
        color, highlight = map(lambda x: x.lower(), self.name.split("_ON_"))
        return colored(UNIT_SYM, color, "on_"+ highlight, ["bold"])
    def __str__(self):
        color, highlight = map(lambda x: x.lower(), self.name.split("_ON_"))
        return colored(UNIT_SYM, color, "on_"+ highlight, ["bold"])


def get_colors(n):
    clist = list(Unit)
    random.shuffle(clist)
    return clist[:n]


class Empty:
    def __repr__(self):
        return " "
    def __str__(self):
        return " "
    def __eq__(self, oth):
        return isinstance(oth, Empty)