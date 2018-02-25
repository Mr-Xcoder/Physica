from Functions import *
from ParsingInfix import *

if __name__ == "__main__":
    program = open(__import__("sys").argv[1], "r", encoding='utf-8').read()
    code = Transpiler().transpile(program)
    exec(code)
