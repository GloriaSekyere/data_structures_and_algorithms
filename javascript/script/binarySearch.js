function binarySearch (arr, num) {
    if (arr.length === 0) {
        return -1
    }
    
    let low = 0
    let high = arr.length - 1

    while (low <= high) {
        let mid = Math.floor((high + low) / 2)
        let guess = arr[mid]

        if (guess === num) {
            return mid
        } else if (guess < num) {
            low = mid + 1
        } else if (guess > num) {
            high =  mid - 1
        }
    }

    return -1
}

module.exports = binarySearch