// 회문 판별 함수
function isPalindrome(str) {
  // split을 통해 str -> array // reverse를 통해 array 뒤집고, join을 통해 array -> str
  const words = str.split(' ')
  const str1 = words.join('')
  const str2 = str1.split('').reverse().join('')
  if (str1 === str2) {
    return true
  } else {
    return false
  }
}

// 출력
console.log(
  isPalindrome('a santa at nasa'),  // true
  isPalindrome('google')  // false
)