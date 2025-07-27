from arithmetic_operations import perform_operation;

def main():
    print("Arithmetic OPerations")
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operations")

    result = perform_operation(num1,num2, operation)
    print(f"Result: {result}")
if __name__== "__main__":
    main()