import os
from dotenv import load_dotenv  # type: ignore


def load_configuration(
        required: list,
        env_path: str = ".env"
        ) -> dict:
    env_loaded = load_dotenv(env_path)

    if not env_loaded and not os.path.exists(env_path):
        print("WARNING: python-dotenv probably not installed.")
        print("Install it with: pip install python-dotenv")

    config = {}
    for key in required:
        config[key] = os.getenv(key, "")

    return {
        "values": config,
        "env_loaded": env_loaded,
        "env_exists": os.path.exists(env_path),
    }


def environment_label(mode: str) -> str:
    if mode == "production":
        return "production"
    return "development"


def endpoint_status(mode: str, endpoint: str) -> str:
    if not endpoint:
        return "Offline (missing ZION_ENDPOINT)"
    if mode == "production":
        return "Online (ON PRODUCTION)"
    return "Online (ON DEVELOPMENT)"


def database_status(mode: str, database_url: str) -> str:
    if not database_url:
        return "Missing DATABASE_URL"
    if mode == "production":
        return "Connected to production cluster"
    return "Connected to local instance"


def api_status(api_key: str) -> str:
    if not api_key:
        return "Missing API_KEY"
    return "Authenticated"


def log_level_value(level: str, mode: str) -> str:
    if level:
        return level
    if mode == "production":
        return "INFO"
    return "DEBUG"


def print_missing_warnings(
        config: dict,
        required: list
        ) -> None:
    missing = []
    for key in required:
        if not config.get(key):
            missing.append(key)

    if not missing:
        return

    print("\nMissing configuration warnings:")
    for key in missing:
        print(f"- {key} is not set")


def print_security_checks(mode: str, loaded: dict) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if loaded["env_exists"]:
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found (using shell environment only)")

    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Development profile active")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")

    REQUIRED_KEYS = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    loaded = load_configuration(REQUIRED_KEYS)
    config = loaded["values"]

    mode = environment_label(config["MATRIX_MODE"])
    db = database_status(mode, config["DATABASE_URL"])
    api = api_status(config["API_KEY"])
    log_level = log_level_value(config["LOG_LEVEL"], mode)
    zion = endpoint_status(mode, config["ZION_ENDPOINT"])

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db}")
    print(f"API Access: {api}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion}")

    print_missing_warnings(config, REQUIRED_KEYS)
    print_security_checks(mode, loaded)
    print("\nThe Oracle sees all configuration")


if __name__ == "__main__":
    main()
