"""Шаблон сдаваемых функций Лабораторной №1.

Функции можно переносить в другие Python-модули. Их имена и тип входного
объекта должны сохраниться. Дополнительные параметры разрешены только с default.
"""

import numpy as np

from grader_contracts.numpy_tasks import (
    BinarizeInput,
    ChessInput,
    EllipseInput,
    MatrixInput,
    MatrixStatistics,
    MatrixVectorBatchInput,
    OneHotInput,
    RandomMatrixInput,
    RectangleInput,
    TimeSeriesInput,
    TimeSeriesStatistics,
)
from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    raise NotImplementedError


def has_unique_characters(data: TextInput) -> bool:
    raise NotImplementedError


def count_one_bits(data: PositiveIntegerInput) -> int:
    raise NotImplementedError


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    raise NotImplementedError


def mse(data: VectorPairInput) -> float:
    raise NotImplementedError


def prime_factorization(data: PositiveIntegerInput) -> str:
    raise NotImplementedError


def pyramid(data: PositiveIntegerInput) -> int | str:
    raise NotImplementedError


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    raise NotImplementedError


def sum_prod(data: MatrixVectorBatchInput) -> "np.ndarray":
    raise NotImplementedError


def binarize(data: BinarizeInput) -> "np.ndarray":
    raise NotImplementedError


def unique_rows(data: MatrixInput) -> list[list[float]]:
    raise NotImplementedError


def unique_columns(data: MatrixInput) -> list[list[float]]:
    raise NotImplementedError


def matrix_statistics(data: RandomMatrixInput) -> "MatrixStatistics":
    raise NotImplementedError


def chess(data: ChessInput) -> "np.ndarray":
    raise NotImplementedError


def draw_rectangle(data: RectangleInput) -> "np.ndarray":
    raise NotImplementedError


def draw_ellipse(data: EllipseInput) -> "np.ndarray":
    raise NotImplementedError


def analyze_time_series(data: TimeSeriesInput) -> "TimeSeriesStatistics":
    raise NotImplementedError


def one_hot(data: OneHotInput) -> "np.ndarray":
    raise NotImplementedError
