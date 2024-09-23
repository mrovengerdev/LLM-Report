import sys
from lark import Lark, Transformer, v_args

# Load the grammar from the grammar.lark file
with open('/Users/mrovenger/Desktop/ChapmanCode/CPSC354/Assignment1/grammar.lark', 'r') as file:
    grammar = file.read()

# Create the parser
parser = Lark(grammar, parser='lalr', transformer=None)

# Define the transformer to evaluate the parse tree
@v_args(inline=True)
class CalculateTree(Transformer):
    def number(self, n):
        return int(n)

    def add(self, a, b):
        for _ in range(b):
            a += 1
        return a

    def mul(self, a, b):
        output = 0
        for _ in range(b):
            output += a
        return output
    
    def expo(self, a, b):
        output = 1
        for _ in range(b):
            output *= a
        return output

    def int(self, n):
        return int(n)

def main(equation):
    parse_tree = parser.parse(equation)
    result = CalculateTree().transform(parse_tree)
    print(result)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        equation = sys.argv[1]  # Get the first argument
    else:
        print("No argument passed")
    main(equation)