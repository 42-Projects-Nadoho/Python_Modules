import sys
from typing import IO


def transform_content(content: str) -> str:
    """Append '#' to every line while preserving line structure."""
    return "".join(f"{line}#\n" for line in content.splitlines())


def create_archive(source_file: str) -> None:
    """Read, transform and optionally save archival content."""
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{source_file}'")
    try:
        source_handle: IO[str] = open(source_file, "r", encoding="utf-8")
    except OSError as err:
        print(f"Error opening file '{source_file}': {err}")
        return

    try:
        content: str = source_handle.read()
        text = f"""---\n\n{content}\n---"""
        print(text)
    finally:
        source_handle.close()
        print(f"File '{source_file}' closed.\n")

    transformed: str = transform_content(content)
    print("Transform data:")
    print("---\n")
    print(transformed, end="")
    print("\n---")

    destination: str = input("Enter new file name (or empty): ")
    if destination == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{destination}'")
    try:
        output_handle: IO[str] = open(destination, "w", encoding="utf-8")
    except OSError as err:
        print(f"Error opening file '{destination}': {err}")
        print("Data not saved.")
        return

    try:
        output_handle.write(transformed)
    except OSError as err:
        print(f"Error opening file '{destination}': {err}")
        print("Data not saved.")
        return
    finally:
        output_handle.close()

    print(f"Data saved in file '{destination}'.")


def main() -> None:
    """Validate CLI arguments and run archive creation."""
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    create_archive(sys.argv[1])


if __name__ == "__main__":
    main()
