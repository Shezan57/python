class MyClass:
    def __init__(self):
        print("Object is being created.")

    def __del__(self):
        print("Object is being destroyed.")

# Creating an object
obj = MyClass()  # Output: Object is being created.

