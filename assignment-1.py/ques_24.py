def calculator(num1,num2,operator):
    if operator == '+':
        result=num1+num2
    elif operator == '-':
        result=num1-num2
    elif operator =="*":
        result=num1*num2
    elif operator =="/":
        result=num1/num2
    else:return "Error,the operator is invalid"

    return result 
def main():
    print('Simple Calculator')
    num1=float(input('Enter the first number:'))
    num2=float(input('Enter another number:'))
    operator=input('Enter an operator:')
    result = calculator(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()