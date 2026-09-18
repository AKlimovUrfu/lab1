from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class TextInput:
    value: str


@dataclass(frozen=True)
class PositiveIntegerInput:
    value: int


@dataclass(frozen=True)
class VectorPairInput:
    predicted: Sequence[int]
    expected: Sequence[int]

