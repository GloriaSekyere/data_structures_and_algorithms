function factorial(x) {
    if (x === 1) {
        return 1
    } else {
        return x * factorial(x - 1)
    }
}

// console.log(factorial(5)) // 120
// console.log(factorial(1)) // 1
// console.log(factorial(3)) // 6


function sumArr(arr) {
    if (arr.length === 0) {
        return 0
    } else {
        return arr[0] + sumArr(arr.slice(1))
    }
    
}

// console.log(sumArr([2, 3, 5, 7, 11])) // 28
// console.log(sumArr([11])) // 11
// console.log(sumArr([])) // 0