# Author
Maxwell Rovenger - mrovenger@chapman.edu - 002398501

# Methods
calculatory_cfg.py
    - number()
    - add()
    - sub()
    - mul()
    - pow()
    - neg()
    - log_base()
    - int()
    - main()
# Purpose & Internal Logic of Methods
    - number()/add()/sub()/mul()/pow()/neg()/log_base()/int()/
        - All of these methods serve the purpose of defining the operations names that are stated within the grammar lark file. More specificaly, they state the exact function of each of the operation. So now, when the grammar.lark file tells the program that what it is seeing is addition, the add() function adds the two numbers together.
    - main()
        - The main function's primary objective is to combine all of the elements by running applying both the grammar file and the operation definitions while parsing through the file.
# General Logic of Program Flow
    - The main file utilizes the grammar lark file to parse through the command line input. The grammar lark file understands the order of operation and additionally also understands which function to use for each operation. The functions within the CalculateTree object then help transform the tree and then lastly the results are printed.