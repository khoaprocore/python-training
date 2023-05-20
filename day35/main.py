# def sum_pairs(ints, s):
#     cache = set()
    
#     for e in ints:
#         if s - e in cache:
#             return [s - e, e]
        
#         cache.add(e)

# print(sum_pairs([4, 3, 2, 3, 4], 6))

def primeFactors(n):
    i = 2
    j = 0
    p = []
    while n > 1:
        while n % i == 0:
            n = n//i
            j += 1
        if j > 0:
            p.append((i, j))
        i += 1
        j = 0
    return p


from timeit import repeat

def run_sort_algorithm(algorithm, n):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != 'sorted' else ''

    stmt = f"{algorithm}({n})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}s")

if __name__ == "__main__":
    run_sort_algorithm("primeFactors", 600851475143)
