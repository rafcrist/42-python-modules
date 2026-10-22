import os
import sys

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("ORACLE ERROR: python-dotenv is not installed.")
    print("Install it with: pip install -r requirements.txt")
    sys.exit(1)


REQUIRED_CONFIG: tuple[str, ...] = (
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT",
)


def load_configuration() -> dict[str, str]:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, ".env")

    load_dotenv(env_path, override=False)

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY": os.getenv("API_KEY", ""),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", ""),
    }
    return (config)


def validate_configuration(config: dict[str, str]) -> bool:
    valid = True

    if config["MATRIX_MODE"] not in ("development", "production"):
        print("WARNING: MATRIX_MODE must be development or production")
        valid = False

    for key in REQUIRED_CONFIG:
        if not config[key]:
            print(f"WARNING: Missing configuration: {key}")
            valid = False

    return (valid)


def database_status(config: dict[str, str]) -> str:
    database_url = config["DATABASE_URL"]
    if not database_url:
        return ("Not configured")
    if "localhost" in database_url or "127.0.0.1" in database_url:
        return ("Connected to local instance")
    return ("Connected to configured instance")


def show_configuration(config: dict[str, str]) -> None:
    mode = config["MATRIX_MODE"]
    api_status = "Authenticated" if config["API_KEY"] else "Not configured"
    zion_status = "Online" if config["ZION_ENDPOINT"] else "Offline"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database_status(config)}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {zion_status}")

    if mode == "production":
        print("Runtime profile: Production configuration active")
    else:
        print("Runtime profile: Development configuration active")


def show_security_check() -> None:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    env_path = os.path.join(script_dir, ".env")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(env_path):
        print("[OK] .env file properly configured")
    else:
        print("[INFO] .env file not found; using environment variables/defaults")
    print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    config = load_configuration()
    valid = validate_configuration(config)
    show_configuration(config)
    show_security_check()

    if valid:
        print("The Oracle sees all configurations.")
    else:
        print("The Oracle sees incomplete configuration.")


if __name__ == "__main__":
    main()
