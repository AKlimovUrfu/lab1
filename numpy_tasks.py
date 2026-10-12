"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    return np.matmul(matrices, vectors).sum(axis=0)


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    return np.where(matrix > threshold, 1, 0)


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(row).tolist() for row in matrix]


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    return [np.unique(col).tolist() for col in matrix.T]


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    
    rng = np.random.default_rng(seed)
    matrix = rng.normal(loc=mean, scale=std, size=(rows, columns))
    
    mean_by_rows = matrix.mean(axis=1)
    mean_by_columns = matrix.mean(axis=0)
    var_by_rows = matrix.var(axis=1)
    var_by_columns = matrix.var(axis=0)
    
    return MatrixStatistics(
        matrix=matrix,
        mean_by_rows=mean_by_rows,
        mean_by_columns=mean_by_columns,
        variance_by_rows=var_by_rows,
        variance_by_columns=var_by_columns
    )


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    grid = np.indices((rows, columns)).sum(axis=0)
    return np.where(grid % 2 == 0, first, second)


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    
    image = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    y0, x0 = image_height // 2, image_width // 2
    
    y_start = y0 - height // 2
    y_end = y_start + height
    x_start = x0 - width // 2
    x_end = x_start + width
    
    image[y_start:y_end, x_start:x_end] = shape_color
    return image


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    
    image = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)
    y0, x0 = image_height // 2, image_width // 2
    
    y, x = np.ogrid[:image_height, :image_width]
    mask = ((x - x0) / semi_axis_x) ** 2 + ((y - y0) / semi_axis_y) ** 2 <= 1
    
    image[mask] = shape_color
    return image


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    
    mean = float(np.mean(values))
    variance = float(np.var(values))
    std = float(np.std(values))
    
    if len(values) > 2:
        is_max = (values[1:-1] > values[:-2]) & (values[1:-1] > values[2:])
        is_min = (values[1:-1] < values[:-2]) & (values[1:-1] < values[2:])
        max_indices = np.where(is_max) + 1
        min_indices = np.where(is_min) + 1
    else:
        max_indices = np.array(, dtype=int)
        min_indices = np.array(, dtype=int)
        
    cumsum = np.cumsum(np.insert(values, 0, 0))
    moving_average = (cumsum[window:] - cumsum[:-window]) / window
    
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        standard_deviation=std,
        local_maxima_indices=max_indices,
        local_minima_indices=min_indices,
        moving_average=moving_average
    )


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    
    if class_count is None:
        class_count = int(np.max(labels)) + 1
        
    return np.eye(class_count)[labels]
