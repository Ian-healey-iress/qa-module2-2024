class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Custom Error: Inputs must be numeric")
        return a + b
    
    def multiply(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Custom Error: Inputs must be numeric")
        return a * b
    
    def divide(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Custom Error: Inputs must be numeric")
        elif a <= 0 or b <= 0:
            raise ZeroDivisionError
        return a / b