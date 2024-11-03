class Calculator:
    def add(self, *args):
        return sum(args)

# Create an instance of the Calculator class
calculator = Calculator()

# Testing the different versions of the add method
print(calculator.add(2, 3))  # Output: 5
print(calculator.add(2, 3, 4))  # Output: 9
print(calculator.add(1, 2, 3, 4, 5))  # Output: 15
