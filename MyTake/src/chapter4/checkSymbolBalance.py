from MyTake.src.chapter4.StackDynamicArray import Stack


def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced = False
    for symbol in input:
        if symbol in ["(", "{", "{"]:
            symbolstack.push(symbol)
        else:
            if symbolstack.isEmpty():
                balanced = False
            else:
                topSymbol = symbolstack.pop()
        if not (topSymbol == symbol):
            balanced = False
        else:
            balanced = True
    return balanced
