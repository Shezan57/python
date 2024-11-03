import os   # Step 1: Import the necessary modules: import os.


def modify_file(path,content):  # Step 2: Define a function named modify_file that takes a file path as input.

    
    try:    # Step 3: Inside the function, use a try block to attempt to open the file in read mode and read its contents.

        f = open(path,"r")
        print(f.read()) # Step 5: If the file is successfully read, modify its contents (e.g., by appending some text).

    except FileNotFoundError:   # Step 4: If any exception occurs during reading, catch it using an except block and print an appropriate error message.

        print("Something wrong while reading file!")
    finally:
        f.close()
    
    try:    # Step 6: Use another try block to attempt to open the file in write mode and write the modified content back to it.

        f = open(path,"a")
        f.write(content)
        # Step 8: If the modified content is successfully written to the file, print a confirmation message.
        print("file writting successfully done!")
        
    except PermissionError: # Step 7: If any exception occurs during writing, catch it using an except block and print an appropriate error message.

        print("Something went wrong while writing file")
    finally:
        f.close()
        
        
# Step 9: Call the modify_file function with a valid file path.
        
modify_file("modifyFile.txt","\n Good luck")