# Parent class
class Animal:
    def make_sound(self):
        return "This animal makes a sound."

# Subclass inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        return "The dog barks."

# Creating an object of the Dog class
dog1 = Dog()

# Invoking the method
print(dog1.make_sound())  # Output: The dog barks.
