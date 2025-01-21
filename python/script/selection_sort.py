def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    result_arr = []
    copied_arr = arr.copy()

    for _ in range(len(copied_arr)):
        smallest_index = find_smallest(copied_arr)
        smallest = copied_arr.pop(smallest_index)
        result_arr.append(smallest)

    return result_arr
