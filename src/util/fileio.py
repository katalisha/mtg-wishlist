""" open a csv and process it with a generic function"""

import csv
import sys
from typing import TypeVar, Callable

T = TypeVar("T")


class FileReport:
    skipped_lines = 0
    processed_lines = 0

    def __str__(self) -> str:
        return f"{self.skipped_lines} skipped, {self.processed_lines} processed"


def process_csv_file(
    filepath: str,
    processor: Callable[[dict[str, str]], T | None],
    skip_header_lines: int = 0,
) -> list[T]:
    result_list: list[T] = []
    result = FileReport()

    try:
        with open(filepath, encoding="utf-8") as handle:
            for _ in range(skip_header_lines):
                next(handle)
                result.skipped_lines += 1

            for row in csv.DictReader(handle):
                elem = processor(row)
                if elem is not None:
                    result.processed_lines += 1
                    result_list.append(elem)
                else:
                    result.skipped_lines += 1

    except (FileNotFoundError, OSError):
        sys.exit("File {filepath} could not be opened")

    print(f"File successfully imported - {result}")
    return result_list
