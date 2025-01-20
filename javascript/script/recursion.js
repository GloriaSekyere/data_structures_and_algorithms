function factorial (n) {
    if (n === 0 || n === 1) return 1
    return n * factorial(n - 1)
}

function sumArr (arr) {
    if (arr.length === 0) return 0
    return arr[0] + sumArr(arr.slice(1)) 
}

function countListItems (arr) {
    if (arr.length === 0) return 0
    return 1 + countListItems(arr.slice(1))
}

function getMin (arr) {
    if (arr.length === 0) return null
    if (arr.length === 1) return arr[0]
    let left = arr[0]
    let right = getMin(arr.slice(1))
    return left < right ? left : right
}

function binarySearch (arr, num) {
    if (arr.length === 0) return null
    if (arr.length === 1) {
        if (arr[0] == num) return arr[0]
        return null
    }

    let mid = Math.floor(arr.length / 2)
    let guess = arr[mid]
    if (guess ===  num) {
        return guess
    } else if (guess < num) {
        return binarySearch(arr.slice(mid+1), num)
    } else if (guess > num) {
        return binarySearch(arr.slice(0, mid), num)
    }
}

module.exports = {
    factorial,
    sumArr,
    countListItems,
    getMin,
    binarySearch
}