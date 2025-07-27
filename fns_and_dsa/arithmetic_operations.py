
def perform_operation(num1,num2,operation):
    if operation.lower() == 'add':
        return num1 + num2
    elif operation.lower() == 'subtract':
        return  num1 - num2
    elif operation.lower() == 'multiply':
        return num1 * num2
    elif operation.lower() == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else :
        print("Enter the operation (add, subtract, multiply, divide): ")
