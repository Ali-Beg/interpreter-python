# Development Diary: Building a Lox Interpreter

## Day 1: Project Setup and Basic Scanner Implementation

### Project Structure
We set up a modular project structure following good Python practices:
```
codecrafters-interpreter-python/
├── app/
│   ├── lexer/           # Handles tokenization
│   │   ├── __init__.py  # Exports module components
│   │   ├── token.py     # Token definitions
│   │   └── scanner.py   # Scanner implementation
│   ├── parser/          # Future parsing implementation
│   ├── interpreter/     # Future interpreter implementation
│   ├── error/           # Error handling
│   └── main.py          # Entry point
└── docs/                # Documentation
    └── development_diary.md  # This file
```

### Concepts Used Today

1. **Enum Implementation**
   - Used Python's `Enum` class for TokenType
   - Provides type safety and string representation
   ```python
   from enum import Enum
   class TokenType(Enum):
       LEFT_PAREN = "LEFT_PAREN"
   ```

2. **Object-Oriented Design**
   - Created classes for different responsibilities:
     - `Token`: Data structure for tokens
     - `Scanner`: Handles lexical analysis
   - Used encapsulation to hide implementation details

3. **Iterator Pattern**
   - Scanner implements character-by-character iteration
   - Tracks position using `start` and `current` indices

4. **Python Package Organization**
   - Used `__init__.py` for package initialization
   - Implemented proper module exports
   - Structured imports for clean code organization

5. **Error Handling**
   - Set up basic error infrastructure
   - Created custom `LoxError` class

### Implementation Progress

1. **Scanner Implementation**
   - Basic character processing
   - Token generation for:
     - Parentheses: `(` and `)`
     - Braces: `{` and `}`
     - EOF handling

2. **Output Formatting**
   - Implemented specific output format:
     ```
     TOKEN_TYPE lexeme null
     ```
   - Special handling for EOF token

### Best Practices Used

1. **Code Organization**
   - Separated concerns into modules
   - Clear class responsibilities
   - Minimal coupling between components

2. **Documentation**
   - Inline comments for complex logic
   - Module-level documentation
   - Development diary for progress tracking

3. **Testing**
   - Used provided test cases
   - Followed TDD approach
   - Fixed formatting issues based on test feedback

### Challenges Faced and Solutions

1. **Module Import Issues**
   - Problem: ModuleNotFoundError
   - Solution: Updated import paths and package structure

2. **Output Formatting**
   - Problem: Extra spaces in output
   - Solution: Carefully formatted f-strings

3. **Token Handling**
   - Problem: Missing EOF token
   - Solution: Added EOF to TokenType enum

### Next Steps

1. Implement remaining single-character tokens
2. Add support for:
   - String literals
   - Number literals
   - Keywords
   - Identifiers

### Learning Resources Used
1. Crafting Interpreters book - Chapter 4
2. Python documentation:
   - Enum class
   - Package structuring
   - String formatting

### Testing Commands
```bash
# Run specific test
./your_program.sh tokenize test.lox

# Example test input/output
Input: "{()}"
Output:
LEFT_BRACE { null
LEFT_PAREN ( null
RIGHT_PAREN ) null
RIGHT_BRACE } null
EOF  null
```

## End of Day 1 Summary

### Completed Tasks
1. ✅ Set up project structure
2. ✅ Implemented basic scanner
3. ✅ Handled parentheses and braces
4. ✅ Fixed output formatting
5. ✅ Passed initial test cases

### Current State
- Working scanner that recognizes:
  - Parentheses: ( )
  - Braces: { }
  - EOF token
- Proper module organization
- Clean test output format

## Tomorrow's Goals (Day 2)

### Priority Tasks
1. Implement remaining single-character tokens:
   - Comma: ,
   - Dot: .
   - Minus: -
   - Plus: +
   - Semicolon: ;
   - Slash: /
   - Star: *

### Secondary Goals
1. Add support for whitespace handling
2. Implement comments
3. Begin work on string literals

### Preparation
1. Review Chapter 4.5 - 4.7 of Crafting Interpreters
2. Study test cases for next stage
3. Consider error handling improvements

Remember to:
- Start with test cases first (TDD)
- Update documentation as we go
- Keep commit messages clear and focused


