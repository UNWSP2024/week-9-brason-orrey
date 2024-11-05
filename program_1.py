def count_names_in_file():
    try:
        with open('names.txt', 'r') as file:
            names = file.readlines()  # Read all lines in the file
            name_count = len(names)   # Count the number of lines
        print(f"The number of names in the file is: {name_count}")
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the filename
count_names_in_file()
