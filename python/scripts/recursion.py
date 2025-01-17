def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


def sum_arr(arr):
    if not arr:
        return 0
    return arr[0] + sum_arr(arr[1:])


def count_list_items(arr):
    if not arr:
        return 0
    return 1 + count_list_items(arr[1:])


def get_max(arr):
    if len(arr) == 1:
        return arr[0]
    left = arr[0]
    right = get_max(arr[1:])
    return left if left > right else right
