class Transpiler:

    restrict_unicode = False

    def __init__(self, *, restrict_unicode: bool = False):
        self.restrict_unicode = restrict_unicode

    def transpile(self, code: str) -> str:
        result = ""
        pause = 0

        if self.restrict_unicode and any(ord(character) > 127 for character in code):
            raise UnicodeError("Use of characters outside the ASCII range 0 – 127 is forbidden.")

        for index, character in enumerate(code):
            if pause:
                pause -= 1
                continue
            if (code[: index].count("'") - code[: index].count("\\'")) % 2:
                result += character
            else:
                if character == "[":
                    result += "("
                elif character == "]":
                    result += ")"
                elif character == "@":
                    result += " |apply| "
                elif character == ";":
                    result += ","
                elif character == ",":
                    result += ";"
                elif character == "^":
                    result += "**"
                elif code[index:index + 2] == "**":
                    pause = 1
                    result += "^"
                elif character == "≤":
                    result += "<="
                elif character == "≥":
                    result += ">="
                elif code[index:index + 2] == "If":
                    pause = 1
                    result += "if"
                elif code[index:index + 7] == "Else If":
                    pause = 6
                    result += "elif"
                elif code[index:index + 4] == "Else":
                    pause = 3
                    result += "else"
                elif character == "√":
                    result += "Root"
                elif character == "$":
                    result += "()"
                elif character == "µ":
                    result += "FrictionCoefficient"
                elif character == "∂":
                    result += "Differentiate"
                elif character == "∫":
                    result += "Integrate"
                elif code[index:index + 2] == "In":
                    pause = 1
                    result += "in"
                elif code[index:index + 2] == "->":
                    pause = 1
                    result += "lambda "
                elif code[index:index + 2] == "=>":
                    pause = 1
                    result += " = lambda "
                elif character == "#":
                    result += "::"
                elif code[index:index + 2] == "//":
                    pause = 1
                    result += "#"
                elif character == "_":
                    result += " _ "
                elif character == "{":
                    result += "["
                elif character == "}":
                    result += "]"
                elif character == "…":
                    result += "Range"
                elif code[index: index + 5] == "Until":
                    pause = 4
                    result += "while not"
                elif character == "≠":
                    result += "!="
                elif character == "!":
                    result += " not "
                elif character == "∈":
                    result += " in "
                elif code[index:index + 3] == "For":
                    pause = 2
                    result += "for"
                elif code[index:index + 2] == "||":
                    pause = 1
                    result += " or "
                elif code[index:index + 2] == "&&":
                    pause = 1
                    result += " and "
                elif code[index:index + 4] == "Func":
                    pause = 3
                    result += "def"
                elif code[index:index + 6] == "Return":
                    pause = 5
                    result += "return"
                elif character == "–":
                    result += "->"
                elif code[index: index + 6] == "import":
                    raise ImportError("Python imports are specifically disallowed")
                else:
                    result += character
        return result

    @staticmethod
    def format_list(item: list) -> str:
        result = ""
        item = str(item)
        for index, character in enumerate(item):
            if (item[: index].count("'") - item[: index].count("\\'")) % 2:
                result += character
            else:
                if character == ",":
                    result += ";"
                elif character == "[":
                    result += "{"
                elif character == "]":
                    result += "}"
                else:
                    result += character
        return result

    @staticmethod
    def unformat_list(item: str) -> list:
        result = ""
        for index, character in enumerate(item):
            if (item[: index].count("'") - item[: index].count("\\'")) % 2:
                result += character
            else:
                if character == ";":
                    result += ","
                elif character == "{":
                    result += "["
                elif character == "}":
                    result += "]"
                else:
                    result += character
        return eval(result)
