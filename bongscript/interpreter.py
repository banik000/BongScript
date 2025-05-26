from .parser import Program, Print, Assign, BinOp, Number, String, Variable, If, While, Break, Continue, Input

class Environment:
    def __init__(self):
        self.vars = {}

    def get(self, name):
        if name not in self.vars:
            raise Exception(f"Undefined variable: {name}")
        return self.vars[name]

    def set(self, name, value):
        self.vars[name] = value

class BreakException(Exception):
    pass

class ContinueException(Exception):
    pass

class Interpreter:
    def __init__(self):
        self.env = Environment()

    def eval(self, node):
        if isinstance(node, Program):
            for stmt in node.body:
                self.eval(stmt)

        elif isinstance(node, Assign):
            value = self.eval(node.expr)
            self.env.set(node.name, value)

        elif isinstance(node, Print):
            value = self.eval(node.expr)
            if node.newline:
                print(value)
            else:
                print(value, end="")

        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                return left / right
            elif node.op == '%':
                return left % right
            elif node.op == '>':
                return left > right
            elif node.op == '<':
                return left < right
            elif node.op == '==':
                return left == right
            elif node.op == '!=':
                return left != right
            elif node.op == '>=':
                return left >= right
            elif node.op == '<=':
                return left <= right
            else:
                raise Exception(f"Unknown operator: {node.op}")

        elif isinstance(node, Number):
            return node.value

        elif isinstance(node, String):
            return node.value

        elif isinstance(node, Variable):
            return self.env.get(node.name)

        elif isinstance(node, If):
            if self.eval(node.cond):
                for stmt in node.body:
                    self.eval(stmt)
            # elif node.else_branch:
            #     for stmt in node.else_branch:
            #         self.eval(stmt)
            elif node.else_branch:
                if isinstance(node.else_branch, list):
                    for stmt in node.else_branch:
                        self.eval(stmt)
                elif isinstance(node.else_branch, If):
                    self.eval(node.else_branch)
                else:
                    raise Exception(f"Invalid else_branch type: {type(node.else_branch)}")

        elif isinstance(node, While):
            while self.eval(node.cond):
                try:
                    for stmt in node.body:
                        self.eval(stmt)
                except BreakException:
                    break
                except ContinueException:
                    continue

        elif isinstance(node, Break):
            raise BreakException()
        
        elif isinstance(node, Continue):
            raise ContinueException()
        
        elif isinstance(node, Input):
            if node.input_type == "int":
                return int(input())
            elif node.input_type == "float":
                return float(input())
            elif node.input_type == "string":
                return input()
            else:
                raise Exception(f"Unknown Input type: {node.input_type}")

        else:
            raise Exception(f"Unknown node type: {node}")
        

