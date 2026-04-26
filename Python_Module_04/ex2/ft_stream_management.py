import sys
from typing import IO


def transform_content(content: str) -> str:
    """Append '#' to every line while preserving line structure."""
    return "".join(f"{line}#\n" for line in content.splitlines())


def print_stderr_error(file_name: str, err: OSError) -> None:
    """Print standardized error messages to stderr."""
    print(f"[STDERR] Error opening file '{file_name}': {err}", file=sys.stderr)


def manage_streams(source_file: str) -> None:
    """Read, transform, and optionally save archival content."""
    source_handle: IO[str]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{source_file}'")
    try:
        source_handle = open(source_file, "r", encoding="utf-8")
    except OSError as err:
        print_stderr_error(source_file, err)
        return

    try:
        content: str = source_handle.read()
        print("Transform data:")
        print("---\n")
        print(content, end="")
        print("\n---")
    finally:
        source_handle.close()
        print(f"File '{source_file}' closed.")

    transformed: str = transform_content(content)
    print("Transform data:")
    print("---\n")
    print(transformed, end="")
    print("\n---")

    print("Enter new file name (or empty): ", end="")
    sys.stdout.flush()
    destination: str = sys.stdin.readline().rstrip("\n")
    if destination == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{destination}'")
    try:
        output_handle: IO[str] = open(destination, "w", encoding="utf-8")
    except OSError as err:
        print_stderr_error(destination, err)
        print("Data not saved.")
        return

    try:
        output_handle.write(transformed)
    except OSError as err:
        print_stderr_error(destination, err)
        print("Data not saved.")
        return
    finally:
        output_handle.close()

    print(f"Data saved in file '{destination}'.")


def main() -> None:
    """Validate CLI arguments and run stream management."""
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return
    manage_streams(sys.argv[1])


if __name__ == "__main__":
    main()
