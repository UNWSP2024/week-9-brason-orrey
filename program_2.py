import random

def write_random_numbers_to_file(filename, count):
    try:
        with open(filename, 'w') as file: # Open the file
            for _ in range(count):
                number = random.randint(1, 500)  # Generate a random number between 1 and 500
                file.write(f"{number}\n")  # Write the number to the file
        print(f"{count} random numbers have been written to '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        try:
            user_input = int(input("How many random numbers do you want to generate (up to 1000)? "))
            if 1 <= user_input <= 1000:
                break  # Valid input
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    write_random_numbers_to_file('random_numbers.txt', user_input)

# Run the program
main()
