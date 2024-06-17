def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    
    return starts_with_prefix, ends_with_suffix

# Example usage:
input_str = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"

starts_with, ends_with = check_prefix_suffix(input_str, prefix_to_check, suffix_to_check)

if starts_with:
    print(f"The string '{input_str}' starts with the prefix '{prefix_to_check}'.")
else:
    print(f"The string '{input_str}' does not start with the prefix '{prefix_to_check}'.")

if ends_with:
    print(f"The string '{input_str}' ends with the suffix '{suffix_to_check}'.")
else:
    print(f"The string '{input_str}' does not end with the suffix '{suffix_to_check}'.")