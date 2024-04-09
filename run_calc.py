from calc_test import calc_test


def run_calc():
    expression = input("Enter your expression: ")
    listed_expression = expression.split(' ')
    print(calc_test(listed_expression))


run_calc()
