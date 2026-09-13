def secure_archive(filename: str, action: str = "r",
                   info: str = "") -> tuple[bool, str]:
    if (action == 'r'):
        try:
            with open(filename, action) as file:
                content = file.read()
            return (True, content)
        except (FileNotFoundError, PermissionError) as error:
            return (False, str(error))
    elif (action == 'w'):
        try:
            with open(filename, action) as file:
                file.write(info)
            return (True, "Content successfully written to file")
        except (FileNotFoundError, PermissionError) as error:
            return (False, str(error))
    else:
        return (False, "Please, select 'r' or 'w'.")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    if result[0]:
        print(secure_archive("new_archive.txt", "w", result[1]))
