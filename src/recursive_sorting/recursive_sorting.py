# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = [0] * (len(arrA) + len(arrB))
    i = 0
    j = 0
    k = 0
    # TO-DO
    while j < len(arrA) and k < len(arrB):
        if arrA[j] <= arrB[k]:
            merged_arr[i] = arrA[j]
            j = j + 1
        else:
            merged_arr[i] = arrB[k]
            k = k + 1
        i = i + 1
    while j < len(arrA):
        merged_arr[i] = arrA[j]
        j = j + 1
        i = i + 1
    while k < len(arrB):
        merged_arr[i] = arrB[k]
        k = k + 1
        i = i + 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left, right)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
