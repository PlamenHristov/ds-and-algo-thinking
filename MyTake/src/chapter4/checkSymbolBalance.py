from MyTake.src.chapter4.StackDynamicArray import Stack

def matches(top, symbol):
    openingSymbols = "({["
    closingSymbols = ")}]"

    return openingSymbols.index(top) == closingSymbols.index(symbol)


def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced = False
    for symbol in input:
        if symbol in ["(", "{", "["]:
            symbolstack.push(symbol)
        else:
            if symbolstack.isEmpty():
                balanced = False
            else:
                topSymbol = symbolstack.pop()
                print("topSymbol: {0} ,symbol: {1}".format(topSymbol, symbol))
                if not matches(topSymbol, symbol):
                    balanced = False
                else:
                    balanced = True
    return balanced
