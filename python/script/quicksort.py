def quicksort(arr):
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]

    return quicksort(left) + [pivot] + quicksort(right)
