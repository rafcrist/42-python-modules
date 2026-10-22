import os
import site
import sys


def in_virtual_environment() -> bool:
    return (sys.prefix != sys.base_prefix or "VIRTUAL_ENV" in os.environ)


def show_global_environment() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("Global package locations:")
    for path in site.getsitepackages():
        print(path)
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print(r"matrix_env\Scripts\activate # On Windows")
    print("Then run this program again.")


def show_virtual_environment() -> None:
    env_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    env_name = os.path.basename(env_path)

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {env_path}")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("Package installation path:")
    for path in site.getsitepackages():
        print(path)


def main() -> None:
    if in_virtual_environment():
        show_virtual_environment()
    else:
        show_global_environment()


if __name__ == "__main__":
    main()
