from random import randint
from timeit import repeat


lst = [8, 2, 6, 9, 4]


def run_sort_algorithm(algorithm, arr):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != 'sorted' else ''

    stmt = f"{algorithm}({arr})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}s")


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


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key_item

    return arr


if __name__ == "__main__":
    lst = [randint(0, 1000) for _ in range(1000000)]
    run_sort_algorithm(algorithm='bubble_sort', arr=lst)
    run_sort_algorithm(algorithm='insertion_sort', arr=lst)
