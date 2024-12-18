from enum import Enum

class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    LEFT_BRACE = "LEFT_BRACE"
    RIGHT_BRACE = "RIGHT_BRACE"
    COMMA = "COMMA"
    DOT = "DOT"
    MINUS = "MINUS"
    PLUS = "PLUS"
    SEMICOLON = "SEMICOLON"
    STAR = "STAR"
    EOF = "EOF"  # Add EOF token type

class Token:
    def __init__(self, type: TokenType, lexeme: str, literal: object):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
