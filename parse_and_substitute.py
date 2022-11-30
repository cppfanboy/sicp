from operator import add, mul

env = {
    '+': add,
    '*': mul,
}

def parse(expr):
    """Takes in an expression string and returns that represented as a nestesd
    list.

    >>> parse("(+ 1 2)")
    ['+', 1, 2]
    >>> parse("(+ 1 (* 2 3))")
    ['+', 1, ['*', 2, 3]]
    >>> parse("(+ (* 1 2) (* 3 4))")
    ['+', ['*', 1, 2], ['*', 3, 4]]
    """
    def tokenize():
        return expr.replace("(", "( ").replace(")", " )").split()

    def parse_tokens(tokens):
        token = tokens.pop(0)
        if token == "(":
            result = []
            while tokens[0] != ')':
                result.append(parse_tokens(tokens))
            tokens.pop(0) # to remove ")"
            return result
        elif token.isdigit():
            return int(token)
        else:
            return token

    return parse_tokens(tokenize())


def substitute(expr):
    """Takes in a parsed expression and evaluates it.

    >>> substitute(parse("(+ 1 2)"))
    3
    >>> substitute(parse("(+ 1 (* 2 3))"))
    7
    >>> substitute(parse("(+ (* 1 2) (* 3 4))"))
    14
    >>> substitute(parse("(+ (* 1 2) 3)"))
    5
    """
    if expr in ['+', '*']:
        return env[expr]
    elif isinstance(expr, int):
        return expr
    else:
        op = substitute(expr[0])
        args = [substitute(x) for x in expr[1:]]
        return op(*args)
