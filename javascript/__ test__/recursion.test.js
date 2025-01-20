const re = require('../script/recursion')


//factorial
test("Calculate 5 factorial", () => {
    expect(re.factorial(5)).toEqual(120)
})

test("Calculate 1 factorial", () => {
    expect(re.factorial(1)).toEqual(1)
})

test("Calculate 0 factorial", () => {
    expect(re.factorial(0)).toEqual(1)
})

// sumArr
test("Find sum of array items", () => {
    const arr = [2, 3, 5, 7, 11]
    const sum = 28
    expect(re.sumArr(arr)).toEqual(sum)
})

test("Find sum of array with one item", () => {
    const arr = [2]
    const sum = 2
    expect(re.sumArr(arr)).toEqual(sum)
})

test("Find sum of empty array", () => {
    const arr = []
    const sum = 0
    expect(re.sumArr(arr)).toEqual(sum)
})

test("Find sum of array with negative integers", () => {
    const arr = [-1, -2, -3, -4, -5]
    const sum = -15
    expect(re.sumArr(arr)).toEqual(sum)
})

test("Find sum of array with positive and negative integers", () => {
    const arr = [-33, -2, 0, 7, 13]
    const sum = -15
    expect(re.sumArr(arr)).toEqual(sum)
})

// countListItems
test("Count number of items in array", () => {
    const arr = ['a', 'b', 'c', 'd', 'e']
    const count = 5
    expect(re.countListItems(arr)).toEqual(count)
})

test("Count number of items in array with one item", () => {
    const arr = ['a']
    const count = 1
    expect(re.countListItems(arr)).toEqual(count)
})

test("Count number of items in empty array", () => {
    const arr = []
    const count = 0
    expect(re.countListItems(arr)).toEqual(count)
})

// getMin
test("Get min item in array", () => {
    const arr = [8, 12, 3, 0, 19, 2]
    const min = 0
    expect(re.getMin(arr)).toEqual(min)
})

test("Get min item in array with one item", () => {
    const arr = [8]
    const min = 8
    expect(re.getMin(arr)).toEqual(min)
})

test("Get min item in empty array", () => {
    const arr = []
    expect(re.getMin(arr)).toBeNull()
})

test("Get min item in array with equal items", () => {
    const arr = [5, 5]
    const min = 5
    expect(re.getMin(arr)).toEqual(min)
})

// binarySearch
test("Find num exists in array", () => {
    const arr = [1, 2, 3, 4, 5]
    const num = 5
    expect(re.binarySearch(arr, num)).toEqual(num)
})

test("Find num does not exist in array", () => {
    const arr = [1, 2, 3, 4, 5]
    const num = 0
    expect(re.binarySearch(arr, num)).toBeNull()
})

test("Find num in array with one item", () => {
    const arr = [7]
    const num = 7
    expect(re.binarySearch(arr, num)).toEqual(num)
})

test("Find num in empty array", () => {
    const arr = []
    const num = 17
    expect(re.binarySearch(arr, num)).toBeNull()
})
