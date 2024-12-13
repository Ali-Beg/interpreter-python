import sys
from lexer import Scanner, Token, TokenType

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    scanner = Scanner(file_contents)
    tokens = scanner.scan_tokens()
    
    for token in tokens:
        if token.type == TokenType.EOF:
            print(f"{token.type.value}  {token.lexeme}null")
        else:
            print(f"{token.type.value} {token.lexeme} null")

if __name__ == "__main__":
    main()
