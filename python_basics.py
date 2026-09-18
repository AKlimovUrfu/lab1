"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    raise NotImplementedError  # TODO


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    raise NotImplementedError  # TODO


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    raise NotImplementedError  # TODO


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    raise NotImplementedError  # TODO


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    raise NotImplementedError  # TODO


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    raise NotImplementedError  # TODO


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    raise NotImplementedError  # TODO


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    raise NotImplementedError  # TODO
