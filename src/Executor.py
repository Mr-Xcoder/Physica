import Parser

if __name__ == "__main__":
    code = open(__import__("sys").argv[1], "r", encoding='utf-8').read()
    parsed_code = Parser.Parser().parse(code)
    exec("from Functions import *\n\n" + parsed_code)
