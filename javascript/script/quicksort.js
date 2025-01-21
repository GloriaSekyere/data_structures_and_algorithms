function quicksort (arr) {
    if (arr.length < 2) return arr

    let pivot = arr[0]
    let left = arr.slice(1).filter(num => num <= pivot)
    let right = arr.slice(1).filter(num => num > pivot)

    return [...quicksort(left), pivot, ...quicksort(right)]
}

module.exports = quicksort