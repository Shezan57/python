class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return "Woof!"

# Create an instance of the Dog class
my_dog = Dog("Buddy", "Labrador")

# Accessing inherited attributes and methods
print(my_dog.name)  # Output: Buddy

# Accessing specific attributes and methods of the Dog class
print(my_dog.breed)  # Output: Labrador
print(my_dog.speak())  # Output: Woof!
