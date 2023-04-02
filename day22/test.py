# check duplicates
lst = [1, 2, 2, 3, 4]

# 2
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j]:
            print(lst[i])
