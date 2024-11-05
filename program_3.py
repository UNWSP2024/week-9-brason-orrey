def calculate_total_from_file(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())  # Convert line to an integer
                    total += number  # Add to total
                except ValueError:
                    print(f"ValueError: Could not convert '{line.strip()}' to an integer. Skipping.")
        print(f"The total of the numbers in the file is: {total}")
    except IOError:
        print(f"IOError: The file '{filename}' could not be opened or read.")

# Call the function with the filename
calculate_total_from_file('numbers.txt')
