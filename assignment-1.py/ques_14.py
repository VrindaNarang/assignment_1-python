def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish):\n")
        if line == "":
            break
        lines.append(line)
    return lines

# Read multiple lines of input
lines = read_multiple_lines()

# Print all the lines entered
print("\nYou entered the following lines:")
for line in lines:
    print(line)