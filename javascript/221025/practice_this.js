const myPrice1 = {
  exchangeRate: 1432,
  prices: [10, 50, 100],

  printPrices: function() {
    this.prices.forEach(function(price){    // (1) this가 myPrice를 가리킴
      console.log(price*this.exchangeRate)  // (2) this는 콜백함수의 것으로 최상위 객체인 window를 가리킴
    }.bind(this)                            // (3) 2이 문제를 해결하기 위해 사용
    )
  }
}

const myPrice2 = {
  exchangeRate: 1432,
  prices: [10, 50, 100],

  printPrices: function() {
    this.prices.forEach((price) => {        // arrow function에 .bind(this)가 내포되어 있음
      console.log(price*this.exchangeRate)
    })
  }
}

myPrice1.printPrices()
/*
14320
71600
143200
*/
myPrice2.printPrices()
/*
14320
71600
143200
*/

const obj = {
  a: 1,
  test1: function(){
    console.log(this.a)   // 1
  },
  test2: () => {
    console.log(this.a)   // undefined
    console.log(this)     // window
  }
}

obj.test1()
obj.test2()