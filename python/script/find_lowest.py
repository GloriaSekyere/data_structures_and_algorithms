def find_lowest(arr):
    if not arr:
        return None
    lowest = arr[0]
    for num in arr:
        if num < lowest:
            lowest = num
    return lowest


print(find_lowest([345, 567, 234, 7, 857, 675, 1, -6412]))
print(find_lowest([4]))
print(find_lowest([]))
