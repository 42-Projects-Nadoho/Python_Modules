import sys


def recover_ancient_text(file_name: str) -> None:
    """Read and display file content with archival headers."""
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{file_name}'")
    try:
        file_handle = open(file_name, "r", encoding="utf-8")
        content: str = file_handle.read()
        print("---\n")
        print(content, end="")
        print("\n---")
        file_handle.close()
        print(f"File '{file_name}' closed.")
    except OSError as err:
        print(f"Error opening file '{file_name}': {err}")


def main() -> None:
    """Validate CLI arguments and trigger recovery."""
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
