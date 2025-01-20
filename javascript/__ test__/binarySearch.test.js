const binarySearch = require('../script/binarySearch')

test('Number exists in array', () => {
    const arr = [1, 2, 3, 4, 5]
    const num = 4
    expect(binarySearch(arr, num)).toBe(3)
})

test('Number does not exist in array', () => {
    const arr = [1, 2, 3, 4, 5]
    const num = 12
    expect(binarySearch(arr, num)).toBe(-1)
})

test('Number exists in array with one item', () => {
    const arr = [1]
    const num = 1
    expect(binarySearch(arr, num)).toBe(0)
})

test('Number does not exist in array with one item', () => {
    const arr = [1]
    const num = 4
    expect(binarySearch(arr, num)).toBe(-1)
})

test('Empty array is passed', () => {
    const arr = []
    const num = 7
    expect(binarySearch(arr, num)).toBe(-1)
})