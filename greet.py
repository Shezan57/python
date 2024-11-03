# Define a function called greet that takes a name as an argument and prints a greeting message.
def greet(s):
    print(f"Hello,{s} welcome to this programme.")
    
# Step1:	Call the greet function with different names and observe the output.
greet("shezan")
greet("jack")
greet("xiaoyu")

#Step2:	Modify the greet function to include an optional argument for a custom greeting.
def greet(s,custom_greeting=None):
    if custom_greeting:
        print(f"Hello,{s}. {custom_greeting}")
    else:
        print(f"Hello,{s} welcome to this programme.")

# Step3:	Call the greet function with and without the optional argument to see the different outputs.
greet("shezan","It's good to see you")
greet("shezan")