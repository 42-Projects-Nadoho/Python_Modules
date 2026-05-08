import sys
import os


def in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def venv_name() -> str:
    if not in_venv():
        return "None detected"
    return os.path.basename(sys.prefix)


def package_location(prefix: str) -> str:
    major = str(sys.version_info.major)
    minor = str(sys.version_info.minor)
    if sys.platform.startswith("win"):
        return os.path.join(
            prefix,
            "Lib",
            "site-packages"
        )
    else:
        return os.path.join(
            prefix,
            "lib",
            f"python{major}.{minor}",
            "site-packages",
        )


def print_outside_matrix() -> None:
    print("\nMATRIX STATUS: You're still plugged in")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name()}")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows")
    print("\nThen run this program again.")


def print_inside_construct() -> None:
    print("M\nATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name()}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print("\nPackage installation path:")
    print(package_location(sys.prefix))


def main() -> None:
    if in_venv():
        print_inside_construct()
    else:
        print_outside_matrix()


if __name__ == "__main__":
    main()
