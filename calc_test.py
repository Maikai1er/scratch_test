def calc_test(expression):
    num1, operator, num2 = expression
    result = 0
    match operator:
        case '+':
            result = int(num1) + int(num2)
        case '*':
            result = int(num1) * int(num2)
        case '-':
            result = int(num1) - int(num2)
        case '/':
            result = int(num1) / int(num2)
    return result
