import sys

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: ft_ancient_text.py <file>")
    else:
        filename = sys.argv[1]
        print("=== Cyber Archives Recovery ===")
        print(f"Accessing file '{filename}'")
        try:
            file = open(filename, "r")
            content = file.read()
            print("---")
            print(content)
            print("---")
            file.close()
            print(f"File '{filename}' closed.")
        except (PermissionError, FileNotFoundError) as error:
            print(f"Error opening file '{filename}': {error}")
