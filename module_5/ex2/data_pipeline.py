import abc
import typing


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.data: list[tuple[int, str]] = []
        self.rank: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not (self.data):
            raise IndexError("Twin what exactly are we removing here")
        else:
            removed = self.data.pop(0)
            return (removed)


class NumericProcessor(DataProcessor):

    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, (int, float))):
            return (True)
        elif (isinstance(data, list)):
            if (all(isinstance(item, (int, float)) for item in data)):
                return (True)
        return (False)

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not (self.validate(data)):
            raise ValueError("Improper numeric data")
        if (isinstance(data, (int, float))):
            str_data = str(data)
            self.data.append((self.rank, str_data))
            self.rank += 1
        elif (isinstance(data, list)):
            for item in data:
                str_data = str(item)
                self.data.append((self.rank, str_data))
                self.rank += 1


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, str)):
            return (True)
        elif (isinstance(data, list)):
            if (all(isinstance(item, str) for item in data)):
                return (True)
        return (False)

    def ingest(self, data: str | list[str]) -> None:
        if not (self.validate(data)):
            raise ValueError("Improper text data")
        if (isinstance(data, str)):
            self.data.append((self.rank, data))
            self.rank += 1
        elif (isinstance(data, list)):
            for item in data:
                self.data.append((self.rank, item))
                self.rank += 1


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if (isinstance(data, dict)):
            for key, value in data.items():
                if not (isinstance(key, str) and isinstance(value, str)):
                    return (False)
            return (True)
        elif (isinstance(data, list)):
            if (all(self.validate(item) for item in data)):
                return (True)
        return (False)

    def ingest(self, data: list[dict[str, str]] | dict[str, str]) -> None:
        if not (self.validate(data)):
            raise ValueError("Improper log data")
        if (isinstance(data, dict)):
            log_str = data["log_level"] + ": " + data["log_message"]
            self.data.append((self.rank, log_str))
            self.rank += 1
        elif (isinstance(data, list)):
            for item in data:
                log_str = item["log_level"] + ": " + item["log_message"]
                self.data.append((self.rank, log_str))
                self.rank += 1


class ExportPlugin(typing.Protocol):

    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        ...


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for item in stream:
            handled = False
            for proc in self.processors:
                if (proc.validate(item)):
                    proc.ingest(item)
                    handled = True
                    break
            if not (handled):
                print(
                    "DataStream error - "
                    f"Can't process element in stream: {item}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not (self.processors):
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.__class__.__name__.replace("Processor", " Processor")
            print(
                f"{name}: "
                f"total {proc.rank} items processed, "
                f"remaining {len(proc.data)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            empty_list: list[tuple[int, str]] = []
            for _ in range(nb):
                if not (proc.data):
                    break
                result = proc.output()
                empty_list.append(result)
            plugin.process_output(empty_list)


class CSVPlugin(ExportPlugin):
    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        values = [value for _, value in data]
        result = ",".join(values)
        print("CSV Output:")
        print(result)


class JSONPlugin(ExportPlugin):
    def process_output(
        self, data: list[tuple[int, str]]
    ) -> None:
        values = [f'"item_{rank}": "{value}"' for rank, value in data]
        result = ", ".join(values)
        print("JSON Output:")
        print("{" + result + "}")


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    print("Registering Processors")
    stream.register_processor(numeric)
    stream.register_processor(text)
    stream.register_processor(log)

    data: list[typing.Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected"
            }
        ],
        42,
        ["Hi", "five"]
    ]

    print(f"Send first batch of data on stream: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    csv = CSVPlugin()

    print("Send 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, csv)
    stream.print_processors_stats()

    data = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {
                "log_level": "ERROR",
                "log_message": "500 server crash"
            },
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days"
            }
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello"
    ]

    print(f"Send another batch of data: {data}")
    stream.process_stream(data)
    stream.print_processors_stats()

    json = JSONPlugin()

    print("Send 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, json)
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
