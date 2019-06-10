# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"{cur_index}, current index, {i}")
        print(f"{smallest_index}, smallest index, {i}")
        print(f"{arr}, array out")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(0, len(arr) - 1):
            print(f"{cur_index}, current index start 2f, {j}")
            print(f"{smallest_index}, smallest index 2f, {j}")
            print(f"{arr}, array out 2f")
            if arr[smallest_index] > arr[j]:
                smallest_index = j
                print(f"{cur_index}, current index if, {j}")
                print(f"{smallest_index}, smallest index if, {j}")
                print(f"{arr}, array out if")
            print(f"{cur_index}, current index, end 2f {i}")
            print(f"{smallest_index}, smallest index, end 2f {i}")
            print(f"{arr}, array out end 2f")

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
