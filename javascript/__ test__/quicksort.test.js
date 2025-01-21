const quicksort = require('../script/quicksort')


test("Sort an array", () => {
    const arr = [10, 5, 2, 3]
    const expected = [...arr].sort((a, b) => a - b)
    expect(quicksort(arr)).toEqual(expected)
})

test("Sort an empty array", () => {
    const arr = []
    expect(quicksort(arr)).toEqual(arr)
})

test("Sort an array with one number", () => {
    const arr = [10]
    expect(quicksort(arr)).toEqual(arr)
})

test("Sort an array with negative numbers", () => {
    const arr = [-10, -5, -2, -3]
    const expected = [...arr].sort((a, b) => a - b)
    expect(quicksort(arr)).toEqual(expected)
})

test("Sort an array with positive and negative numbers", () => {
    const arr = [-10, -5, -2, -3, 10, 5, 2, 3]
    const expected = [...arr].sort((a, b) => a - b)
    expect(quicksort(arr)).toEqual(expected)
})

test("Sort an array with the same numbers", () => {
    const arr = [4, 4, 4]
    const expected = [...arr].sort((a, b) => a - b)
    expect(quicksort(arr)).toEqual(expected)
})