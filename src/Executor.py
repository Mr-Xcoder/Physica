from Functions import *

if __name__ == "__main__":
    code = open(sys.argv[1], "r", encoding='utf-8').read()
    exec(Parser().parse(code))
