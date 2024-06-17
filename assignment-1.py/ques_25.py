def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
source_file = "C:\python and machine learning\demo.txt"  
destination_file = "C:\python and machine learning\assignment-1.py\destination_file"  

copy_file(source_file, destination_file)