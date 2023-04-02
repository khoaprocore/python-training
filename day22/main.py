from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, arr):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != 'sorted' else ''

    stmt = f"{algorithm}({arr})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    ARR_LENGTH = 100000

    arr = [randint(0, 10000) for _ in range(ARR_LENGTH)]
    run_sorting_algorithm('sorted', arr)

