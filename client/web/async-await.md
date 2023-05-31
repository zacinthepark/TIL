## async and await

---

- `async` 와 `await` 는 가장 최근에 나온 비동기 처리 패턴으로, 기존의 콜백함수와 프로미스의 단점을 보완한 문법
- 콜백함수 혹은 여러 개의 프로미스가 서로 의존하고 있는 경우에 비해 가독성있는 코드 작성 가능

## 사용법

---

- 함수 앞에 `async` 를 붙이면 해당 함수는 자동으로 프로미스를 반환함
- 비동기로 처리되는 부분에 `await` 를 붙이면 해당 프로미스가 끝날 때까지 기다림 (동기적 처리)
- `await` 은 `async` 가 붙은 함수 안에서만 사용 가능
- `async` 함수에서 `return` 은 `resolve()` 와 같은 역할을 함

```jsx
function promiseFunc() {
  return new Promise((resolve, reject) => {
    resolve('Promise is awesome')
  })
}

promiseFunc().then(console.log)

// Promise is awesome

async function asyncFunc() {
  return 'Async is awesome'
}

asyncFunc().then(console.log)

// Async is awesome
// 문자열을 반환하는 것처럼 보이지만 실제로는 프로미스를 반환
```

프로미스에서 동기적으로 처리하기 위해 후속 처리 메서드인 `then()` 메서드를 사용하여 동기적으로 처리했다면, 이제는 프로미스를 반환하는 함수 앞에 `await` 을 붙여 더 간편하게 동기적으로 처리할 수 있음

또한 프로미스를 사용하여 동기적으로 처리하는 경우 fulfilled 값을 `then()` 후속 처리 메서드를 통해 결과값을 인자로 넘겨 체인 내에서 처리해야 하지만, `await` 을 사용하면 fulfilled 값을 외부로 넘겨줄 수 있음

```jsx
const timeout = (value, timeout) => new Promise((resolve, reject) => {
  setTimeout(() => resolve(value), timeout)
})

timeout('Hello ', 1000)                           // 프로그램 실행후 1초뒤에 수행됨
	.then(result => {
		console.log('complete promise')
		return timeout(result + 'My Name is ', 2000)  // 프로그램 실행후 3초뒤에 수행됨(1 + 2)
	}).then(result => {
		console.log('complete promise')
		return timeout(result + 'manja ', 3000)       // 프로그램 실행후 6초뒤에 수행됨(1 + 2 + 3)
	}).then(result => {
		console.log('complete promise')
		console.log(result)
	})

// complete promise
// complete promise
// complete promise
// Hello My name is manja
```

```jsx
const timeout = (value, timeout) => new Promise((resolve, reject) => {
	setTimeout(() => resolve(value), timeout)
})

async function awaitFunc() {
	let str = ''
	
	str += await timeout('Hello ', 1000)       // 프로그램 실행후 1초뒤에 수행됨
	console.log('complete promise')
	str += await timeout('My name is ', 2000)  // 프로그램 실행후 3초뒤에 수행됨(1 + 2)
	console.log('complete promise')
	str += await timeout('manja ', 3000)       // 프로그램 실행후 6초뒤에 수행됨(1 + 2 + 3)
	console.log('complete promise')
	
	return str
}

awaitFunc().then(console.log)

// complete promise
// complete promise
// complete promise
// Hello My name is manja
```

## 예외 처리

---

- 프로미스에서 예외 처리를 할 때 후속 처리 메서드인 `catch()` 메서드를 사용하여 예외 처리를 했음
- async와 await을 사용하면 프로미스를 함수 내부에서 동기적으로 처리할 수 있기 때문에 `try-catch` 구문을 사용하여 예외 처리를 할 수 있음
- 모든 예외를 `try-catch` 구문으로 처리하는 것은 아님
    - await은 async가 붙은 함수 내에서만 사용 가능하기에 최정겨로가나 처리되지 못한 에러의 경우 `catch()` 메서드를 사용하여 처리해주곤 함

### `catch()` 메서드를 사용한 예외 처리 방법

프로미스에서 예외 처리하는 방법과 동일하게 `catch()` 메서드를 이용하여 예외를 처리할 수 있음

```jsx
async function promise() {
  throw 'error';
}

promise()
  .then(result => console.log('status : fulfilled,', result))
  .catch(error => console.log('status : rejected,', error))

// status : rejected, error
```

### `try-catch` 구문을 이용한 예외 처리 방법

함수 내부에서 예외가 발생한 경우 `try-catch` 구문을 이용하여 예외를 처리할 수 있음

```jsx
async function promise() {
  throw 'rejected';
}

async function exceptionFunc() {
  try {
      await promise()
  } catch (err) {
      console.log('catch error!', err)
  }
}

exceptionFunc()

// catch error! rejected
```

### `catch()` 메서드와 `try-catch` 메서드를 혼용한 예외 처리 방법

함수 내부에서 예외가 발생하였지만 예외를 내부가 아닌 외부로 넘겨 처리하고 싶은 경우 다음과 같이 혼용 가능

```jsx
async function promise() {
  throw 'rejected';
}

async function exceptionFunc() {
  try {
    return await promise()
	} catch (err) {
    console.log('catch error!', err
    throw err
  }
}

exceptionFunc()
  .then(result => console.log('status : fulfilled,', result))
  .catch(error => console.log('status : rejected,', error))

// catch error! rejected
// status : rejected, rejected
```
