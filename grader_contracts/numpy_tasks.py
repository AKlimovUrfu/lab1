from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class MatrixVectorBatchInput:
    matrices: Any
    vectors: Any


@dataclass(frozen=True)
class BinarizeInput:
    matrix: Any
    threshold: float = 0.5


@dataclass(frozen=True)
class MatrixInput:
    matrix: Any


@dataclass(frozen=True)
class RandomMatrixInput:
    rows: int
    columns: int
    mean: float = 0.0
    std: float = 1.0
    seed: int = 42


@dataclass(frozen=True)
class MatrixStatistics:
    matrix: Any
    row_means: Any
    column_means: Any
    row_variances: Any
    column_variances: Any


@dataclass(frozen=True)
class ChessInput:
    rows: int
    columns: int
    first: float
    second: float


@dataclass(frozen=True)
class RectangleInput:
    width: int
    height: int
    image_height: int
    image_width: int
    shape_color: tuple[int, int, int]
    background_color: tuple[int, int, int]


@dataclass(frozen=True)
class EllipseInput:
    semi_axis_x: int
    semi_axis_y: int
    image_height: int
    image_width: int
    shape_color: tuple[int, int, int]
    background_color: tuple[int, int, int]


@dataclass(frozen=True)
class TimeSeriesInput:
    values: Any
    window: int


@dataclass(frozen=True)
class TimeSeriesStatistics:
    mean: float
    variance: float
    std: float
    local_maxima_indices: Any
    local_minima_indices: Any
    moving_average: Any


@dataclass(frozen=True)
class OneHotInput:
    labels: Any
    class_count: int | None = None
