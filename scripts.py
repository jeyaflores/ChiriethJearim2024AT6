def convert_to_uppercase():
    filename = input("Please enter the name of the file: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
        new_content = content.upper()
        with open(filename, 'w') as file:
            file.write(new_content)
        print("File converted to uppercase successfully.")
    except FileNotFoundError:
        print(f"The file {filename} was not found.")

if __name__ == "__main__":
    convert_to_uppercase()
