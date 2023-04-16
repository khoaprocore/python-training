""" def name_shuffler(full_name):
    first, last = full_name.split()
    return last + ' ' + first


print(name_shuffler("John Smith")) """


""" def goals(*a):
    print(a)
    print(type(a))
    return sum(a)


print(goals(1, 2, 3)) """


""" def stray(arr):
    # for x in set(arr):
    #     if arr.count(x) == 1:
    #         return x

    return min(arr, key=arr.count)


#            2  2  1
print(stray([1, 1, 2]))  # 2
print('c'.isupper()) """


# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
# def longest(a1, a2):
#     s = a1 + a2
#     new_set = set(s)
#     sorted_lst = sorted(new_set)
#     return ''.join(sorted_lst)


# print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq") == "abcdefklmopqwxy")

""" geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    not_geeses = []

    for bird in birds:
        if bird not in geese:
            not_geeses.append(bird)

    return not_geeses


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]) == ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]) """


""" def is_anagram(test, original):
    return sorted(test) == sorted(original)


print(is_anagram("foefet", "toffee") == True) """

print([[1, 2] * 2] * 3)



