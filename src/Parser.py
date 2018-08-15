from functools import reduce
from string import ascii_letters as letters


class Parser:
    restrict_unicode = False

    def __init__(self, *, restrict_unicode: bool = False):
        self.restrict_unicode = restrict_unicode

    def parse(self, program: str) -> str:
        pause = 0
        string_mode = False
        string_toggle = ""
        transpilation_result = ""

        for index, character in enumerate(program):
            if pause > 0:
                pause -= 1
                continue

            def validate(*indices, restricted_set=letters) -> bool:
                characters = [program[ind] for ind in indices if 0 <= ind < len(program)]
                for char in characters:
                    if char in restricted_set:
                        return False
                return True

            if self.restrict_unicode and ord(character > 127):
                raise UnicodeError("The use of characters outside the ASCII range 0-127 is forbidden while the "
                                   "--nounicode flag is enabled.")

            else:
                is_quote = character == "\"" or character == "'"

                if index > 1:
                    is_escaped = program[index - 1] == "\\" and program[index - 2] != "\\"
                elif index == 1:
                    is_escaped = program[index - 1] == "\\"
                else:
                    is_escaped = False

                if not string_mode and is_quote:
                    string_mode = True
                    string_toggle = character
                    transpilation_result += character
                elif string_mode and not is_escaped:
                    if character == string_toggle:
                        string_mode = False
                        string_toggle = ""
                        transpilation_result += character
                    else:
                        transpilation_result += character

                else:
                    if program[index:index + 2] == "##":
                        pause = 1
                        transpilation_result += " |red| "
                    elif program[index:index + 2] == "??":
                        pause = 1
                        transpilation_result += " == None and "
                    elif program[index:index + 2] == "@@":
                        pause = 1
                        transpilation_result += " |each| "
                    elif program[index:index + 2] == "%%":
                        pause = 1
                        transpilation_result += " :: "
                    elif program[index:index + 2] == "$$":
                        pause = 1
                        transpilation_result += " |filt| "
                    elif character == "∘":
                        transpilation_result += " |comp| "
                    elif character == "@":
                        transpilation_result += " |apply| "
                    elif program[index:index + 2] == "|>":
                        pause = 1
                        transpilation_result += ";"
                    elif program[index:index + 2] == "::":
                        pause = 1
                        transpilation_result += "->"
                    elif program[index:index + 2] == "->":
                        pause = 1
                        transpilation_result += "lambda "
                    elif program[index:index + 2] == "=>":
                        pause = 1
                        transpilation_result += " = lambda "
                    elif character == "[":
                        transpilation_result += "("
                    elif character == "×":
                        transpilation_result += " |prod| "
                    elif character == "]":
                        transpilation_result += ")"
                    elif character == "≤":
                        transpilation_result += "<="
                    elif character == "≥":
                        transpilation_result += ">="
                    elif character == ";":
                        transpilation_result += ","
                    elif character == "^":
                        transpilation_result += "**"
                    elif character == ",":
                        transpilation_result += "."
                    elif character == "?":
                        transpilation_result += " None "
                    elif character == "÷":
                        transpilation_result += "//"
                    elif program[index:index + 2] == "//":
                        pause = 1
                        transpilation_result += "#"
                    elif character == "{":
                        transpilation_result += "["
                    elif character == "}":
                        transpilation_result += "]"
                    elif character == ":":
                        transpilation_result += ": "
                    elif character in "¬!":
                        transpilation_result += " not "
                    elif character == "…":
                        transpilation_result += "Range "
                    elif program[index: index + 5] == "Until":
                        pause = 4
                        transpilation_result += "while not "
                    elif character == "≠":
                        transpilation_result += "!="
                    elif character == "∈":
                        transpilation_result += " in "
                    elif program[index:index + 3] == "For" and validate(index - 1, index + 3):
                        pause = 2
                        transpilation_result += "for "
                    elif program[index:index + 2] == "||":
                        pause = 1
                        transpilation_result += " or "
                    elif program[index:index + 2] == "&&":
                        pause = 1
                        transpilation_result += " and "
                    elif program[index:index + 4] == "Func" and validate(index - 1, index + 4):
                        pause = 3
                        transpilation_result += "def "
                    elif program[index:index + 6] == "Return" and validate(index - 1, index + 6):
                        pause = 5
                        transpilation_result += "return "
                    elif program[index:index + 2] == "If" and validate(index - 1, index + 2):
                        pause = 1
                        transpilation_result += "if"
                    elif program[index:index + 7] == "Else If" and validate(index - 1, index + 7):
                        pause = 6
                        transpilation_result += "elif"
                    elif program[index:index + 4] == "Else" and validate(index - 1, index + 4):
                        pause = 3
                        transpilation_result += "else"
                    elif character == "√":
                        transpilation_result += "Root"
                    elif character == "$":
                        transpilation_result += "()"
                    elif character == "µ":
                        transpilation_result += "FrictionCoefficient"
                    elif character == "∂":
                        transpilation_result += "Differentiate"
                    elif character == "∫":
                        transpilation_result += "Integrate"
                    elif program[index:index + 2] == "In" and validate(index - 1, index + 2):
                        pause = 1
                        transpilation_result += " in "
                    else:
                        transpilation_result += character
        return transpilation_result

    @staticmethod
    def parse_list(item: list) -> str:
        string_mode = False
        parse_result = ""
        string_toggle = ""
        obj = str(item)

        for index, character in enumerate(obj):
            is_quote = character == "\"" or character == "'"

            if index > 1:
                is_escaped = obj[index - 1] == "\\" and obj[index - 2] != "\\"
            elif index == 1:
                is_escaped = obj[index - 1] == "\\"
            else:
                is_escaped = False

            if not string_mode and is_quote:
                string_mode = True
                string_toggle = character
                parse_result += character
            elif string_mode and not is_escaped:
                if character == string_toggle:
                    string_mode = False
                    string_toggle = ""
                    parse_result += character
                else:
                    parse_result += character
            else:
                if character == ",":
                    parse_result += ";"
                elif character == "[":
                    parse_result += "{"
                elif character == "]":
                    parse_result += "}"
                else:
                    parse_result += character
        return parse_result

    @staticmethod
    def unparse_list(item: str) -> list:
        string_mode = False
        parse_result = ""
        string_toggle = ""

        for index, character in enumerate(item):
            is_quote = character == "\"" or character == "'"

            if index > 1:
                is_escaped = item[index - 1] == "\\" and item[index - 2] != "\\"
            elif index == 1:
                is_escaped = item[index - 1] == "\\"
            else:
                is_escaped = False

            if not string_mode and is_quote:
                string_mode = True
                string_toggle = character
                parse_result += character
            elif string_mode and not is_escaped:
                if character == string_toggle:
                    string_mode = False
                    string_toggle = ""
                    parse_result += character
                else:
                    parse_result += character
            else:
                if character == ";":
                    parse_result += ","
                elif character == "{":
                    parse_result += "["
                elif character == "}":
                    parse_result += "]"
                else:
                    parse_result += character
        return eval(parse_result)


# Inspired by http://program.activestate.com/recipes/384122/

class Infix:
    def __init__(self, func):
        self.func = func

    # noinspection PyShadowingNames
    def __ror__(self, other):
        return Infix(lambda x, self=self, other=other: self.func(other, x))

    def __or__(self, other):
        return self.func(other)

    def __call__(self, value1, value2):
        return self.func(value1, value2)


apply = Infix(lambda func, item: func(item))
each = Infix(lambda func, item: list(map(func, item)))
comp = Infix(lambda func1, func2: (lambda x: func1(func2(x))))
filt = Infix(lambda func, item: list(filter(func, item)))
red = Infix(lambda func, item: reduce(func, item))
prod = Infix(lambda item1, item2: __import__('Functions').GenMul(item1, item2))
