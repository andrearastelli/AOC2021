from dataclasses import dataclass, field


@dataclass
class Cell:
    number: int
    marked: bool = field(default=False)

    def __str__(self):
        return f"{self.number} [{self.marked}]"