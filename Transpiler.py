def transpile(code):
    result = ""
    pause = False
    for index, character in enumerate(code):
        if pause:
            pause = False
            continue
        if code[: index].count('"') % 2:
            result += character
        else:
            if character == "[":
                result += "("
            elif character == "]":
                result += ")"
            elif character == ";":
                result += ","
            elif character == ",":
                result += ";"
            elif character == "^":
                result += "**"
            elif character == "*" and index < len(code) - 1 and code[index + 1] == "*":
                pause = True
                result += "^"
            else:
                result += character
    return result
