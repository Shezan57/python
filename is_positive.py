#  Define a function called is_positive that takes a number as an argument.
def is_positive(num):
    
    # step-1: Inside the function, use an if statement to check if the number is positive.
    if num > 0:
        return True  #Step2: If the number is positive, return True; otherwise, return False.
    else:
        return False
    
# Step3: Call the is_positive function with different numbers and verify the returned values.
print(is_positive(10))
print(is_positive(-10))
print(is_positive(1))
print(is_positive(-20))

    