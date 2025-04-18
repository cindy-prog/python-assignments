def modify_file_contents(original_filename, new_filename):
    try:
        with open(original_filename, 'r') as infile:
            lines = infile.readlines()
        
        modified_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]

        with open(new_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content has been written to '{new_filename}' successfully!")
    
    except FileNotFoundError:
        print(f"Error: The File '{original_filename}' does not exist.")
    
    except IOError:
        print("An error occured while reading or writting this file.")
        

filename = input("Enter the file name to be read: ")
new_filename = input("Enter the name of the new file to write to: ")
modify_file_contents(filename, new_filename)