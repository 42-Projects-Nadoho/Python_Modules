def secure_archive(
    file_name: str,
    action: str = "read",
    content_to_write: str = "",
) -> tuple[bool, str]:
    """Safely read from or write to a file using context managers."""
    try:
        if action == "write":
            with open(file_name, "w", encoding="utf-8") as file_handle:
                file_handle.write(content_to_write)
            return (True, "Content successfully written to file")

        with open(file_name, "r", encoding="utf-8") as file_handle:
            return (True, file_handle.read())
    except OSError as err:
        return (False, str(err))


def main() -> None:
    """Demonstrate secure archive operations."""
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/.pwd.lock"))

    print("Using 'secure_archive' to read from a regular file:")
    read_result: tuple[bool, str] = secure_archive("ex3/ft_vault_security.py")
    print(read_result)

    print("Using 'secure_archive' to write previous content to a new file:")
    content: str = read_result[1] if read_result[0] else ""
    print(secure_archive("secure_archive_output.txt", "write", content))


if __name__ == "__main__":
    main()
