# Day152 - LeetCode 1096. Brace Expansion II

def brace_expansion_ii(expression):
    n = len(expression)
    pos = 0

    def parse_expression():
        nonlocal pos
        result = parse_term()

        while pos < n and expression[pos] == ',':
            pos += 1
            result |= parse_term()

        return result

    def parse_term():
        nonlocal pos
        result = {""}

        while pos < n and expression[pos] not in "},":
            part = parse_factor()
            result = {a + b for a in result for b in part}

        return result

    def parse_factor():
        nonlocal pos

        if expression[pos] == '{':
            pos += 1
            result = parse_expression()
            pos += 1
            return result

        ch = expression[pos]
        pos += 1
        return {ch}

    return sorted(parse_expression())


expression = input("Enter the expression: ").strip()

print("Output:", brace_expansion_ii(expression))
