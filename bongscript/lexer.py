from .token import TokenType, Token

class Lexer:
    KEYWORDS = {
        "eta",
        "holo",
        "lekho",
        "jodi",
        "nahole",
        "jotokhon",
        "kaj",
        "shuru",
        "shesh",
        "montobbo",
        "theme",
        "egiye",
        "jao"
    }
    OPERATORS = {
        '+', '-', '*', '/', '>', '<', '==', '=', '!='
    }

    def __init__(self, code):
        self.code = code
        self.pos = 0

    def peek(self):
        if self.pos < len(self.code):
            return self.code[self.pos]
        else:
            return None
    
    def advance(self):
        char = self.peek()
        self.pos += 1
        return char
    
    def tokenize(self):
        tokens = []
        while self.peek() is not None:
            char = self.peek()

            if char.isspace():
                self.advance()
                continue

            if char.isalpha():
                identifier = self.consume_identifier()

                if identifier in self.KEYWORDS:
                    if identifier == "montobbo":
                        self.consume_comment()
                    else:
                        tokens.append(Token(TokenType.KEYWORD, identifier))
                else:
                    tokens.append(Token(TokenType.IDENTIFIER, identifier))
            
            elif char.isdigit():
                tokens.append(Token(TokenType.NUMBER, self.consume_number()))

            elif char == '"':
                tokens.append(Token(TokenType.STRING, self.consume_string()))

            elif char in '+-*/<>=!':
                tokens.append(self.consume_operator())

            elif char == ';':
                tokens.append(Token(TokenType.SEMICOLON, ';'))
                self.advance()

            elif char == '(':
                tokens.append(Token(TokenType.LPAREN, '('))
                self.advance()
            
            elif char == ')':
                tokens.append(Token(TokenType.RPAREN, ')'))
                self.advance()
            
            elif char == '{':
                tokens.append(Token(TokenType.LBRACE, '{'))
                self.advance()

            elif char == '}':
                tokens.append(Token(TokenType.RBRACE, '}'))
                self.advance()

            else:
                raise Exception(f"Unknown character: {char}")
            
        tokens.append(Token(TokenType.EOF, None))
        return tokens
        
    def consume_identifier(self):
        result = ""
        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            result += self.advance()
        return result

    def consume_comment(self):
        while self.peek() and self.peek() != ';':
            self.advance()
        if self.peek() == ';':
            self.advance()

    def consume_number(self):
        result = ""
        has_dot = False
        while self.peek() and (self.peek().isdigit() or (self.peek() == '.' and not has_dot)):
            if self.peek() == '.':
                has_dot = True
            result += self.advance()
        return float(result) if has_dot else int(result)

    def consume_string(self):
        self.advance()
        result = ""
        while self.peek() != '"':
            result += self.advance()
        self.advance()
        return result

    def consume_operator(self):
        op = self.advance()
        if self.peek() in {'=', '!'} and op in {'<', '>', '=', '!'}:
            op += self.advance()
        if op == '=':
            return Token(TokenType.ASSIGN, op)
        else:
            return Token(TokenType.OPERATOR, op)

