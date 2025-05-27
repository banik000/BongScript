import sys
from bongscript.lexer import Lexer
from bongscript.parser import Parser
from bongscript.interpreter import Interpreter
from pprint import pprint

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.bong>")
        sys.exit(1)
    
    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as file:
        code = file.read()

    lexer = Lexer(code)
    tokens = lexer.tokenize()

    if "-t" in sys.argv:
        pprint(tokens)

    parser = Parser(tokens)
    ast = parser.parse()

    if "-a" in sys.argv:
        pprint(ast)

    interpreter = Interpreter()
    interpreter.eval(ast)


if __name__ == "__main__":
    main()