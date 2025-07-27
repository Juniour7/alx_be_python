def perform_operation(num1,num2,operation):
    if operation.lower() == 'add':
        result = num1 + num2
    elif operation.lower() == 'subtract':
        result =  num1 - num2
    elif operation.lower() == 'multiply':
        result = num1 * num2
    elif operation.lower() == 'divide':
        result = num1 /num2
    else :
        print("Enter the operation (add, subtract, multiply, divide): ")
    return result
