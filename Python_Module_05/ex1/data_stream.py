import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._queue: list[tuple[int, str]] = []
        self._next_rank: int = 0
        self._total_processed: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._queue:
            raise IndexError("No data available")
        return self._queue.pop(0)

    def _store(self, value: str) -> None:
        self._queue.append((self._next_rank, value))
        self._next_rank += 1
        self._total_processed += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(
                isinstance(item, (int, float)) and not isinstance(item, bool)
                for item in data
            )
        return isinstance(data, (int, float)) and not isinstance(data, bool)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._store(str(item))
            return
        self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return isinstance(data, str)

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._store(item)
            return
        self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in data.items()
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict)
                and all(
                    isinstance(key, str) and isinstance(value, str)
                    for key, value in item.items()
                )
                for item in data
            )
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                self._store(self._stringify_log(item))
            return
        self._store(self._stringify_log(data))

    def _stringify_log(self, entry: dict[str, str]) -> str:
        return ": ".join(entry.values())


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for processor in self.processors:
                if processor.validate(element):
                    processor.ingest(element)
                    break
            else:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for processor in self.processors:
            total = processor._total_processed
            remaining = len(processor._queue)
            name = processor.__class__.__name__.replace(
                "Processor",
                " Processor",
            )
            print(
                f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor"
            )


def main() -> None:
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    logs = LogProcessor()

    print("\nRegistering Numeric Processor")
    stream.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
        {"level": "INFO", "message": "User wil is connected"},
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    stream.register_processor(text)
    stream.register_processor(logs)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: Numeric 3, Text 2, "
        "Log 1"
    )
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
