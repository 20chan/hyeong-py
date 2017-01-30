from enum import Enum


class State(Enum):
    Hangul = 1
    Dot = 2
    Heart = 3


def parse_hangul(code):
    pass


def parse_dot(code):
    pass


def parse_heart(code):
    pass


def parse(code):
    state = State.Hangul
    tok = -1
    for i in len(code):
        if state == State.Hangul:
            state, tok = parse_hangul(code[i:])
        elif state == State.Dot:
            state, tok = parse_dot(code[i:])
        elif state == State.Heart:
            state, tok = parse_heart(code[i:])
        yield tok
