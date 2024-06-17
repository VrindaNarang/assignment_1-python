def calculate_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    return total_sum

# Function to get list of numbers from user input
def get_number_list():
    # Prompt the user to enter numbers, comma-separated
    input_str = input("Enter numbers separated by commas: ")
    
    # Split the input string by commas and convert each part to integer
    number_list = [int(num) for num in input_str.split(',')]
    
    return number_list

# Example usage:
num_list = get_number_list()
result_sum = calculate_sum(num_list)

print(f"The sum of numbers in the list {num_list} is: {result_sum}")