const numbers = [1, 2, 3, 4, 5]

const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)

console.log(newArry)

// 2.
const newArry = numbers.map(function (number) {
  return number * 2
})

// 3.
const newArry = numbers.map((number) => {
  return number * 2
})

// 4.
const newArry = numbers.map((number) => number * 2)
