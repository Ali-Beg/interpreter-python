from .token import Token, TokenType

class Scanner:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
    
    def scan_tokens(self) -> list[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, "", "null"))
        return self.tokens
    
    def scan_token(self):
        c = self.advance()
        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif c == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        # Skip all other characters silently
    
    def is_at_end(self) -> bool:
        return self.current >= len(self.source)
    
    def advance(self) -> str:
        self.current += 1
        return self.source[self.current - 1]
    
    def add_token(self, type: TokenType):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, "null"))
