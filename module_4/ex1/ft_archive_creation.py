import sys

if __name__ == "__main__":
    if (len(sys.argv) == 2):
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery & Preservation ===")
        print(f"Accessing file '{filename}'")
        try:
            file = open(filename, "r")
            content = file.read()
            print("---")
            print(content)
            print("---")
            file.close()
            print(f"File '{filename}' closed.")
        except (FileNotFoundError, PermissionError) as error:
            print(f"Error opening file '{filename}': {error}")
        else:
            new_content = ""
            for line in content.splitlines():
                new_content = new_content + line + "#\n"
            print("Transform data:")
            print("---")
            print(new_content, end="")
            print("---")
            new_filename = input("Enter new file name (or empty): ")
            if (new_filename):
                try:
                    print(f"Saving data to '{new_filename}'")
                    file = open(new_filename, "w")
                    file.write(new_content)
                    print(f"Data saved in file '{new_filename}'")
                    file.close()
                except (FileNotFoundError, PermissionError) as error:
                    print(f"Error opening file '{new_filename}': {error}")
            else:
                print("Not saving data.")
    else:
        print("Usage: ft_archive_creation.py <file>")
