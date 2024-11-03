import os   # Step 1: Import the necessary modules: import os.


def read_file(path):    # Step 2: Define a function named read_file that takes a file path as input.

    try:    # Step 3: Inside the function, use a try block to attempt to open the file in read mode and read its contents.
        f = open(path,"r")
        print(f.read()) # Step 5: If the file is successfully read, print its contents.
        
    except FileNotFoundError: # Step 4: If any exception occurs (e.g., file not found), catch it using an except block and print an appropriate error message.

        print("Something went wrong or file not found!")
    finally:
        f.close()
        

read_file("demofile.txt")    # Step 6: Call the read_file function with a valid file path.

    

