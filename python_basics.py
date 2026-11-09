"""Заготовки задач на базовый Python."""

import math
from grader_contracts.python_basics import (
    PositiveIntegerInput, TextInput, VectorPairInput,
    PrimeFactorizationOutput, PyramidOutput
)


def count_vowels(data: TextInput) -> int:
    text = data.value
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    return len(set(text)) == len(text)


def count_one_bits(data: PositiveIntegerInput) -> int:
    number = data.value
    return bin(number).count('1')


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    steps = 0
    while number >= 10:
        product = 1
        for digit in str(number):
            product *= int(digit)
        number = product
        steps += 1
    return steps


def mse(data: VectorPairInput) -> float:
    x, y = data.x, data.y
    n = len(x)
    squared_errors_sum = sum((xi - yi) ** 2 for xi, yi in zip(x, y))
    return squared_errors_sum / n


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    n = number
    factors = []
    
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    if count > 0:
        factors.append((2, count))
        
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count > 0:
            factors.append((i, count))
            
    if n > 1:
        factors.append((n, 1))
        
    result = ""
    for factor, power in factors:
        if power == 1:
            result += f"({factor})"
        else:
            result += f"({factor}**{power})"
            
    return result


def pyramid(data: PositiveIntegerInput) -> int | str:
    n = data.value
    current_sum = 0
    k = 0
    while current_sum < n:
        k += 1
        current_sum += k ** 2
        
    if current_sum == n:
        return k
    return "It is impossible"


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    digits = [int(d) for d in str(number)]
    length = len(digits)
    mid = length // 2
    
    if length % 2 == 1:
        left_sum = sum(digits[:mid])
        right_sum = sum(digits[mid + 1:])
    else:
        left_sum = sum(digits[:mid - 1])
        right_sum = sum(digits[mid + 1:])
        
    return left_sum == right_sum
