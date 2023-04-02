def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]

        j = i - 1

        while j >= left and arr[j] > key_item:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key_item

    return arr


if __name__ == "__main__":
    sorted_arr = insertion_sort([8, 2, 6, 4, 5])
    print(sorted_arr)
