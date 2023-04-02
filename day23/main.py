from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm, arr):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != 'sorted' else ''
    stmt = f"{algorithm}({arr})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minium execution time: {min(times)}s")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        already_sorted = True

        for j in range(n-1-i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                already_sorted = False

        if already_sorted:
            break
    
    return arr

lst = [randint(0, 1000) for _ in range(100)]
run_sorting_algorithm('bubble_sort', lst)