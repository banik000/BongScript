from .token import TokenType, Token

class Node:
    pass

class Program(Node):
    def __init__(self, body):
        self.body = body
    def __repr__(self):
        statements_repr = "\n ".join(repr(stmt) for stmt in self.body)
        return f"Program(\n  {statements_repr}\n)"

class Print(Node):
    def __init__(self, expr):
        self.expr = expr
    def __repr__(self):
        return f"Print({self.expr})"

class Assign(Node):
    def __init__(self, name, expr, declare=False):
        self.name = name
        self.expr = expr
        self.declare = declare
    def __repr__(self):
        return f"Assign({self.name} {self.expr} {self.declare})"

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
    def __repr__(self):
        return f"BinOp({self.left} {self.op} {self.right})"

class Number(Node):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"Number({self.value})"

class String(Node):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"String({self.value})"

class Variable(Node):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Variable({self.name})"

class If(Node):
    def __init__(self, cond, body, else_branch=None):
        self.cond = cond
        self.body = body
        self.else_branch = else_branch
    def __repr__(self):
        body_repr = "\n    ".join(repr(stmt) for stmt in self.body)
        if self.else_branch:
            if isinstance(self.else_branch, If):
                else_repr = f"\n  Else {repr(self.else_branch)}"
            else:
                else_body = "\n    ".join(repr(stmt) for stmt in self.else_branch)
                else_repr = f"\n  Else {{\n    {else_body}\n  }}"
        else:
            else_repr = ""
        return f"If({self.cond}) {{\n    {body_repr}\n  }}{else_repr}"

class While(Node):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body
    def __repr__(self):
        body_repr = "\n    ".join(repr(stmt) for stmt in self.body)
        return f"While({self.cond}) {{\n    {body_repr}\n  }}"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, type_=None, value=None):
        tok = self.current()
        if type_ and tok.type != type_:
            raise Exception(f"Expected {type_}, got {tok.type}")
        if value and tok.value != value:
            raise Exception(f"Expected {value}, got {tok.value}")
        self.pos += 1
        return tok

    def parse(self):
        self.eat(TokenType.KEYWORD, "kaj")
        self.eat(TokenType.KEYWORD, "shuru")
        body = self.parse_program_statements()
        self.eat(TokenType.KEYWORD, "kaj")
        self.eat(TokenType.KEYWORD, "shesh")
        return Program(body)

    def parse_program_statements(self):
        statements = []
        while self.current().type != TokenType.KEYWORD or self.current().value != "kaj":
            if self.current().type == TokenType.EOF:
                break
            statements.append(self.parse_statement())
        return statements
    
    def parse_block_statements(self):
        statements = []
        while self.current().type != TokenType.RBRACE:
            if self.current().type == TokenType.EOF:
                raise Exception("Unexpected end of file in block")
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        tok = self.current()
        if tok.value == "lekho":
            return self.parse_print()
        elif tok.value == "eta":
            return self.parse_declaration()
        elif tok.value == "jodi":
            return self.parse_if()
        elif tok.value == "jotokhon":
            return self.parse_while()
        elif tok.type == TokenType.IDENTIFIER:
            return self.parse_assignment()
        else:
            raise Exception(f"Unexpected statement: {tok}")

    def parse_declaration(self):
        self.eat(TokenType.KEYWORD, "eta")
        self.eat(TokenType.KEYWORD, "holo")
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.ASSIGN)
        expr = self.parse_expression()
        self.eat(TokenType.SEMICOLON)
        return Assign(name, expr, declare=True)

    def parse_assignment(self):
        name = self.eat(TokenType.IDENTIFIER).value
        self.eat(TokenType.ASSIGN)
        expr = self.parse_expression()
        self.eat(TokenType.SEMICOLON)
        return Assign(name, expr)

    def parse_print(self):
        self.eat(TokenType.KEYWORD, "lekho")
        self.eat(TokenType.LPAREN)
        expr = self.parse_expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.SEMICOLON)
        return Print(expr)

    def parse_if(self):
        self.eat(TokenType.KEYWORD, "jodi")
        self.eat(TokenType.LPAREN)
        cond = self.parse_expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.LBRACE)
        body = self.parse_block_statements()
        self.eat(TokenType.RBRACE)

        else_branch = None
        if self.current().type == TokenType.KEYWORD and self.current().value == "nahole":
            else_branch = self.parse_else()

        return If(cond, body, else_branch)
        
    def parse_else(self):
        # self.eat(TokenType.KEYWORD, "nahole")
        # if self.current().value == "jodi":
        #     self.eat(TokenType.KEYWORD, "jodi")
        #     self.eat(TokenType.LPAREN)
        #     cond = self.parse_expression()
        #     self.eat(TokenType.RPAREN)
        #     self.eat(TokenType.LBRACE)
        #     body = self.parse_block_statements()
        #     self.eat(TokenType.RBRACE)
        #     return If(cond, body)
        # else:
        #     self.eat(TokenType.LBRACE)
        #     body = self.parse_block_statements()
        #     self.eat(TokenType.RBRACE)
        #     return body
        self.eat(TokenType.KEYWORD, "nahole")
        if self.current().type == TokenType.KEYWORD and self.current().value == "jodi":
            return self.parse_if()
        else:
            self.eat(TokenType.LBRACE)
            body = self.parse_block_statements()
            self.eat(TokenType.RBRACE)
            return body

    def parse_while(self):
        self.eat(TokenType.KEYWORD, "jotokhon")
        self.eat(TokenType.LPAREN)
        cond = self.parse_expression()
        self.eat(TokenType.RPAREN)
        self.eat(TokenType.LBRACE)
        body = self.parse_block_statements()
        self.eat(TokenType.RBRACE)
        return While(cond, body)

    def parse_expression(self):
        left = self.parse_term()
        while self.current().type == TokenType.OPERATOR:
            op = self.eat().value
            right = self.parse_term()
            left = BinOp(left, op, right)
        return left

    def parse_term(self):
        tok = self.eat()
        if tok.type == TokenType.NUMBER:
            return Number(tok.value)
        elif tok.type == TokenType.STRING:
            return String(tok.value)
        elif tok.type == TokenType.IDENTIFIER:
            return Variable(tok.value)
        elif tok.type == TokenType.LPAREN:
            # expr = self.parse_expression()
            # self.eat(TokenType.RPAREN)
            # return expr
            self.eat(TokenType.LPAREN)
            expr = self.parse_expression()
            self.eat(TokenType.RPAREN)
            return expr
        else:
            raise Exception(f"Unexpected token in expression: {tok}")
