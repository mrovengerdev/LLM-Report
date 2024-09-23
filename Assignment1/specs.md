# Author
Maxwell Rovenger - mrovenger@chapman.edu - 002398501

# Methods
calculator.py
    - number():
    - add():
    - mul():
    - expo():
    - int():
    - main():
parentheses.py
    - push():
    - pop():
    - is_empty():
    - parenthesesScanner(self, equation):
    - check(self, equation):

# Purpose
calculator.py
    - number/add/mul/expo/int
        - All of these functions serve as definitions of their respective mathematical components for the context-free grammar to understand. This allows me to avoid the use of eval() or existing python methods for calculating.
    - main
        - First off, the inputted equation is parsed through by transformer and its related functions that are imported from the Lark library. It's children are then parsed through and transformed by using the grammar.lark file.

parentheses.py
    - push/pop/is_empty
        - These functions serve as a CRUD basis for a stack without the need to import a library for a stack data type. 
    - parenthesesScanner
        - This function utilizes the recently created stack data structure to push open parentheses and pop when closed parentheses are found. This means that when the stack, when checked if it is empty with the function: is_empty. Will verify in a foolproof manner whether all open parentheses symbols have a closed parentheses symbol.

# Internal Logic of Methods
The internal logic of both programs follows the same nature of taking an inputted string. Parsing through the string via either stack or tree and returning an output that's calculated by their main methods.

# General Logic of Program Flow
calculator.py
    - Upon execution of the program, calculator.py takes in the command line argument and splits it.
parentheses.py
    - Upon execution of the program, parentheses.py takes in the command line argument and begins parsing through it, pushing when an open parentheses is found and then popping when a closed parenthesis is found. It then prints "yes" if the stack is empty, meaning that the parentheses are properly instated, or otherwise printing "no", Signaling that the parentheses are not incorporatred correctly.