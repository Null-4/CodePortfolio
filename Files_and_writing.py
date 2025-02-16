

def sum_odd_lines(filename):
    try:
        with open(filename, 'r') as file:
            total = 0
            for line_number, line in enumerate(file, start=1):
                try:
                    if line_number % 2 != 0:  # Odd lines
                        total += int(line.strip())  # Strip any whitespace/newlines and convert to integer
                except ValueError:
                    print(f"Warning: Could not convert line {line_number} to an integer. Skipping.")
        
        print(f"The sum of numbers on odd lines is: {total}")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Call the function with the filename
sum_odd_lines('Numbers.txt')