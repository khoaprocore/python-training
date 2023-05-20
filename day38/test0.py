def gen_from_1_to_10():
    x = 1

    while x < 11:
        yield x
        x += 1


gen_obj = gen_from_1_to_10()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj)) # Error ?

