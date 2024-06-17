def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of character in the dictionary
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency

# Example usage:
input_string = "hello world"
frequency = count_character_frequency(input_string)

# Print the character frequencies
print(f"Character frequencies in '{input_string}':")
for char, count in frequency.items():
    print(f"'{char}' : {count}")