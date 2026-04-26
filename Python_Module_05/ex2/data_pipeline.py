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


class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class CsvExportPlugin():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        values = [value for _, value in data]
        print("CSV Output:")
        print(",".join(values))


class JsonExportPlugin(ExportPlugin):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        parts: list[str] = []
        for rank, value in data:
            escaped = value.replace("\\", "\\\\").replace('"', '\\"')
            parts.append(f'"item_{rank}": "{escaped}"')
        json_payload = "{" + ", ".join(parts) + "}"
        print("JSON Output:")
        print(json_payload)


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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for processor in self.processors:
            exported_data: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    exported_data.append(processor.output())
                except IndexError:
                    break
            plugin.process_output(exported_data)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==")
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
    print("=== Code Nexus - Data Pipeline ===")

    stream = DataStream()
    print("\nInitialize Data Stream...")

    stream.print_processors_stats()

    print("\nRegistering Processors")
    stream.register_processor(NumericProcessor())
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())

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
    ]

    print(f"\nSend first batch of data on stream : {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CsvExportPlugin())
    stream.print_processors_stats()

    second_batch = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]
    print(f"\nSend another batch of data: {second_batch}")
    stream.process_stream(second_batch)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JsonExportPlugin())
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
