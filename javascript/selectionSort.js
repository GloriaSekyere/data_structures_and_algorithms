function findBiggest(arr) {
    let biggest = 0
    let biggestIndex = 0

    for (let i = 0; i < arr.length; i++) {
        if (biggest < arr[i]) {
            biggest = arr[i]
            biggestIndex = i
        }
    }
    return biggestIndex
}


function selectionSort(arr) {
    const resultArr = []
    const copiedArr = [...arr]

    for (let i = 0; i < arr.length; i++) {
        let biggestIndex = findBiggest(copiedArr)
        let biggest = copiedArr.splice(biggestIndex, 1)
        resultArr.push(...biggest)
    }

    return resultArr
}

console.log(selectionSort([4, 9, 12, 2, 0, 8]))