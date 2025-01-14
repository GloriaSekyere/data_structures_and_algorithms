def binary_search(arr: list[int], num: int) -> int | None:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return guess
        elif guess > num:
            high = mid - 1
        elif guess < num:
            low = mid + 1
    return None
