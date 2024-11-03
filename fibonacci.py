# Write a function that calculates the nth term of the Fibonacci sequence. The Fibonacci
# sequence is a series of numbers where each number (starting from the third number) is 
# the sum of the two preceding numbers. 
# For instance, the first few terms of the Fibonacci sequence are: 0, 1, 1, 2, 3, 5, 8, 13, ...




def fibonacci(n):
    if n < 0:
        return "Input should be a positive integer"
    elif n == 0:
        return 0            # Step3:	Use if conditionals to handle special cases, such as when n is 0 or 1.
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)     # Step1:	Implement the Fibonacci sequence 
                                                    #calculation using recursion or iteration.


value = int(input("Please Enter a Integer number: "))  
print(fibonacci(value))             # Step2:Call the function outside its definition, taking the
                                    #value of n as input from the user.

        
        