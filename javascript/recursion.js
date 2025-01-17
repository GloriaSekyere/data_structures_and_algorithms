const factorial = (x) => x === 1 ? 1 : x * factorial(x - 1)

/* TESTS
console.log(factorial(5)) // 120
console.log(factorial(1)) // 1
console.log(factorial(3)) // 6
*/


const sumArr = (arr) => arr.length === 0 ? 0 : arr[0] + sumArr(arr.slice(1)) 

/* TESTS
console.log(sumArr([2, 3, 5, 7, 11])) // 28
console.log(sumArr([11])) // 11
console.log(sumArr([])) // 0
console.log(sumArr([-1, -2, -3, -4. -5])) // -15
*/


const countListItems = (arr) => arr.length === 0 ? 0 : 1 + countListItems(arr.slice(1))

/* TESTS
console.log(countListItems(['a', 'b', 'c', 'd', 'e'])) // 5
console.log(countListItems(['e'])) // 1
console.log(countListItems([])) // 0
 */

const getMin = (arr) => {
    if (arr.length < 2) return arr[0]
    
    let left = arr[0]
    let right = getMin(arr.slice(1))
    
    return left < right ? left : right
}

/* TESTS
console.log(getMin([8, 12, 3, 0, 19, 2])) // 0
console.log(getMin([4])) // 4
console.log(getMin([5, 5])) // 5
*/