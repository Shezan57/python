
# Write a function that takes a string as input and returns the reversed version of that string. For example,
# if the input is "hello", the output should be "olleh".



def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:       # Step1:	Iterate through each character of the string using a for loop
        reversed_string = char + reversed_string    # Step2:	Append the characters to a new string, paying attention to the method of string concatenation.

    return reversed_string


input_str = "hello"
reversed_str = reverse_string(input_str)
print(reversed_str)     # Step3:	Call the function outside its definition and print the reversed string.


    
    