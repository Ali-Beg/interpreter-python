# Building a Lox Interpreter: Implementation Guide

## Project Structure
```
app/
├── lexer/
│   ├── __init__.py
│   ├── token.py
│   └── scanner.py
├── parser/
│   └── __init__.py
├── interpreter/
│   └── __init__.py
├── error/
│   └── __init__.py
└── main.py
```

## Implementation Stages

### Stage 1: Scanner - Parentheses
Initial implementation focused on scanning parentheses.

#### Key Components:
1. **TokenType Enum**
   ```python
   class TokenType(Enum):
       LEFT_PAREN = "LEFT_PAREN"
       RIGHT_PAREN = "RIGHT_PAREN"
       EOF = "EOF"
   ```

2. **Token Class**
   ```python
   class Token:
       def __init__(self, type: TokenType, lexeme: str, literal: object):
           self.type = type
           self.lexeme = lexeme
           self.literal = literal
   ```

3. **Scanner Class**
   - Tracks position with `start` and `current` indices
   - Processes character by character
   - Handles EOF token

#### Example Output (Stage 1):
Input: "(("
```
LEFT_PAREN ( null
LEFT_PAREN ( null
EOF  null
```

### Stage 2: Scanner - Braces
Extended scanner to handle curly braces.

#### Changes Made:
1. **Added Token Types**
   ```python
   class TokenType(Enum):
       # ...existing tokens...
       LEFT_BRACE = "LEFT_BRACE"
       RIGHT_BRACE = "RIGHT_BRACE"
   ```

2. **Extended Scanner**
   ```python
   def scan_token(self):
       c = self.advance()
       if c == '{': self.add_token(TokenType.LEFT_BRACE)
       elif c == '}': self.add_token(TokenType.RIGHT_BRACE)
       # ...existing cases...
   ```

#### Example Output (Stage 2):
Input: "{{}}"
```
LEFT_BRACE { null
LEFT_BRACE { null
RIGHT_BRACE } null
RIGHT_BRACE } null
EOF  null
```

### Future Stages
1. Single-character tokens (coming next)
2. Operators and comparison
3. String literals
4. Number literals
5. Keywords and identifiers
6. Expressions
7. Statements
8. Control flow
9. Functions

### Implementation Notes
- Each token includes type, lexeme, and literal value
- Scanner skips unrecognized characters
- Unbalanced brackets are valid at scanner level
- Error handling will be added in parsing stage

### Testing
To run tests:
```bash
./your_program.sh tokenize test.lox
```
