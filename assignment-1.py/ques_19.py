import string

def remove_punctuation(input_string):
    # Create translation table for punctuation removal
    translator = str.maketrans('', '', string.punctuation)
    # Translate the input string using the translation table
    return input_string.translate(translator)

# Example usage:
input_string = "Hello, World! This is a test string with punctuation."
cleaned_string = remove_punctuation(input_string)

print(f"Original string: '{input_string}'")
print(f"String without punctuation: '{cleaned_string}'")