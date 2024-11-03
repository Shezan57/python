import os   # Step 1: Import the necessary modules: import os.


def write_to_file(path,content):    # Step 2: Define a function named write_to_file that takes a file path and some text as inputs.

    try:        # Step 3: Inside the function, use a try block to attempt to open the file in write mode and write the text to it.

        f = open(path,"w")
        f.write(content)
        print("File writting successfully done!")   # Step 5: If the text is successfully written to the file, print a confirmation message.
    except PermissionError:  # Step 4: If any exception occurs (e.g., permission denied), catch it using an except block and print an appropriate error message.
        print("Something went wrong or system denied permission")
    finally:
        f.close()
        
# Step 6: Call the write_to_file function with a valid file path and some text to write.

write_to_file("demowrite.txt","Hello! this file is for writing testing purpose \n Good luck")