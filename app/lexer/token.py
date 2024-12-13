from enum import Enum

class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    # ...future token types will go here...

class Token:
    def __init__(self, type: TokenType, lexeme: str, literal: object):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
