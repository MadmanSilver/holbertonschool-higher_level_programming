#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    from sys import argv, exit
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == '+':
        func = calculator_1.add
    elif argv[2] == '-':
        func = calculator_1.sub
    elif argv[2] == '*':
        func = calculator_1.mul
    else:
        func = calculator_1.div
    print("{} {} {} = {}\
".format(argv[1], argv[2], argv[3], func(int(argv[1]), int(argv[3]))))
