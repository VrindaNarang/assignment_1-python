import csv

def read_csv_file(filename):
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))  # Print each row as comma-separated values

# Example usage:
filename = 'C:\python and machine learning\demo.txt' 
read_csv_file(filename)