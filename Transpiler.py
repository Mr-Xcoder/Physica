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
            elif character == "≤":
                result += "<="
            elif character == "≥":
                result += ">="
            elif character == "√":
                result += "Root"
            elif character == "µ":
                result += "FrictionCoefficient"
            elif character == "∂":
                result += "Differentiate"
            elif character == "∫":
                result += "Integrate"
            elif character == "⟶":
                result += "lambda "
            else:
                result += character
    result = result.replace("Until", "while not ")
    return result
