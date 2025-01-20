const selectionSort = require('../script/selectionSort')

test("Sort array from biggest to lowest", () => {
    const arr = [4, 9, 12, 2, 0, 8]
    const sorted_arr = [12, 9, 8, 4, 2, 0]
    expect(selectionSort(arr)).toEqual(sorted_arr)
})

test("Sort array with one item", () => {
    const arr = [4]
    const sorted_arr = [4]
    expect(selectionSort(arr)).toEqual(sorted_arr)
})

test("Empty array is passed", () => {
    const arr = []
    const sorted_arr = []
    expect(selectionSort(arr)).toEqual(sorted_arr)
})