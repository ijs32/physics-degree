import math as m
import numpy as np
import matplotlib as mplt

from numpy import typing as npt


def get_permutation_matrix(
    n: int,
    set: npt.NDArray[np.object_]
) -> npt.NDArray[np.object_]:

    if n == 1:
        return np.ndarray([1])

    new_set: npt.NDArray[np.object_] = np.array([], dtype=object)

    set = get_permutation_matrix(n - 1, set)
    for row in set:
        for i in range(0, (n-1)):
            copy: list[int] = row.copy()
            copy[i] = n

            np.append(new_set, copy)

    return new_set


def get_permutation_sign(row: list[int]) -> int:
    n_swaps: int = 0
    i: int = 0

    while i < len(row):
        if list[i] > list[i+1]:
            n_swaps += 1

        i += 1

    return (-1)**n_swaps


def leibniz_det(arr: np.ndarray) -> int:

    det: int = 0
    for row in get_permutation_matrix(arr.ndim, []):
        sgn_sigma = get_permutation_sign(row)

        product: int = sgn_sigma * np.prod(row)
        det += product

    return det


arr: np.ndarray = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
