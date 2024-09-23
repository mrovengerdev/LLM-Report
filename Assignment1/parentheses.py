import sys

class Parentheses():
    # Added stack functions
    def push(self, stack, item):
        stack.append(item)
    
    def pop(self, stack):
        if not self.is_empty(stack):
            return stack.pop()
    
    def is_empty(self, stack):
        return len(stack) == 0
    
    # Parses through equation string and checks if for each parentheses open symbol '(' there is a closing symbol ')'.
    def parenthesesScanner(self, equation):
        stack = []
        for i in range(0, len(equation)):
            if equation[i] == '(':
                self.push(stack, equation[i])
            elif equation[i] == ')':
                if self.is_empty(stack):
                    return False
                self.pop(stack)
        return self.is_empty(stack)
    
    def check(self, equation):
        result = self.parenthesesScanner(equation)
        if result == True:
            print("yes")
        else:
            print("no")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        equation = sys.argv[1]  # Get the first argument
    else:
        print("No argument passed")
    Parentheses().check(equation)

# Example run:
# python parentheses.py "(()()(()))"
# Example output:
# yes

# Example run:
# python parentheses.py "(()()(())"
# Example output:
# no