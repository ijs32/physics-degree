import numpy as np
import copy


def get_permutation_matrix(
    n: int,
    prev_perm_matrix: list
) -> list:

    if n == 1:
        return [[1]]

    new_perm_matrix: list = []

    prev_perm_matrix = get_permutation_matrix(n - 1, prev_perm_matrix)
    for row in prev_perm_matrix:
        for i in range(0, n):
            temp: list[int] = copy.deepcopy(row)
            temp.insert(i, n)

            new_perm_matrix.append(temp)

    return new_perm_matrix


def get_permutation_sign(row: list[int]) -> int:
    n_swaps: int = 0
    i: int = 0

    while i < len(row):

        j = 0
        while j < len(row):
            if row[i] > row[j] and i < j:
                n_swaps += 1
            j += 1

        i += 1

    return 1 if n_swaps % 2 == 0 else -1


def get_product(arr, row, n):
    i = 0
    prod = 1

    while i < n:
        # because in code everything is zero indexed.
        prod *= arr[i][(row[i] - 1)]

        i += 1

    return prod


def leibniz_det(arr: np.ndarray) -> float:

    det: int = 0

    m, n = arr.shape
    if m != n:
        raise Exception("Non Square matrices have no determinant!")

    for row in get_permutation_matrix(m, []):
        sgn_sigma = get_permutation_sign(row)

        product: int = sgn_sigma * get_product(arr, row, m)
        det += product

    return det


arr: np.ndarray = np.array([
    [1, 0, 0],
    [0, 4, 1],
    [4, 3, 1]
])

try:
    print(0 % 2 == 0)
    determinant = leibniz_det(arr)
    print(f"The determinant of your matrix is: {determinant}")
except Exception as e:
    print(f"Something went wrong: {e}")
