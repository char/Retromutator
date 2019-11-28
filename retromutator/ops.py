from retromutator import Operation

chr = Operation(chr, ord)
ord = chr.invert()

def add(n):
    return Operation(lambda x: x + n, lambda x: x - n)

def subtract(n):
    return Operation(lambda x: x - n, lambda x: x + n)

def multiply(n):
    return Operation(lambda x: x * n, lambda x: x / n)

def divide(n):
    return Operation(lambda x: x / n, lambda x: x * n)
