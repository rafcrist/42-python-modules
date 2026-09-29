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


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    numeric = NumericProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {numeric.validate(42)}")
    print(f"Trying to validate input 'Hello': {numeric.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")

    print("Processing data: [1, 2, 3, 4, 5]")
    numeric.ingest([1, 2, 3, 4, 5])

    print("Extracting 3 values...")
    for _ in range(3):
        rank, value = numeric.output()
        print(f"Numeric value {rank}: {value}")

    text = TextProcessor()
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {text.validate(42)}")
    text.ingest(["Hello", "Nexus", "World"])

    print("Extracting 1 value...")
    rank, value = text.output()
    print(f"Text value {rank}: {value}")

    log = LogProcessor()
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {log.validate('Hello')}")

    log.ingest([
        {
            "log_level": "NOTICE",
            "log_message": "Connection to server"
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!"
        }
    ])

    print("Extracting 2 values...")
    for _ in range(2):
        rank, value = log.output()
        print(f"Log entry {rank}: {value}")


if __name__ == "__main__":
    main()
