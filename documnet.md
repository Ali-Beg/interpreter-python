# Building a Lox Interpreter: Step-by-Step Documentation

## Stage 1: Implementing the Scanner (Tokenizer)

### 1. Basic Setup and Token Types
- Created `TokenType` enum with initial token types:
  - `LEFT_PAREN`: For opening parenthesis '('
  - `RIGHT_PAREN`: For closing parenthesis ')'
  - `EOF`: For end of file marker

```python
class TokenType(Enum):
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    EOF = "EOF"
```

### 2. Token Class Implementation
- Created `Token` class to represent individual tokens:
  - `type`: The token's type (from TokenType enum)
  - `lexeme`: The actual character(s) from source code
  - `literal`: The processed value (currently always "null")

### 3. Scanner Implementation
Created `Scanner` class with:
1. State tracking:
   - `source`: Input string to be scanned
   - `tokens`: List to store found tokens
   - `start`: Start position of current lexeme
   - `current`: Current position in source

2. Core methods:
   - `scan_tokens()`: Main loop to process all characters
   - `scan_token()`: Process single character
   - `is_at_end()`: Check if we reached end of source
   - `advance()`: Move to next character
   - `add_token()`: Create and store new token

### 4. Main Function Updates
- Modified main function to:
  1. Read input file
  2. Create Scanner instance
  3. Process tokens
  4. Print tokens in required format: "TYPE  lexeme literal"

### Current Capabilities
- Can recognize opening and closing parentheses
- Handles EOF token
- Outputs tokens in specified format: `TOKEN_TYPE  lexeme literal`

### Example Output
For input: "()"
```
LEFT_PAREN  ( null
RIGHT_PAREN  ) null
EOF   null
```

### Next Steps
1. Add support for more token types
2. Implement string literals
3. Add number literals
4. Handle whitespace and comments
5. Add keyword recognition