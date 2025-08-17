class Calculator:
    """
    A class that demonstrates the use of static and class methods for calculations.
    """
    # Class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float) -> float:
        """
        A static method to add two numbers. It does not have access to class
        or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a: float, b: float) -> float:
        """
        A class method to multiply two numbers. It has access to the class
        itself (via 'cls') and can access class attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b