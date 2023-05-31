## Promise란?

---

> “A promise is an object that may produce a single value some time in the future”

프로미스는 자바스크립트 비동기 처리에 사용되는 객체

비동기 처리란 특정 코드의 실행이 완료될 때까지 기다리지 않고 다음 코드를 먼저 수행하는 자바스크립트의 특성을 의미

## Why Promise?

---

### Single Thread

자바스크립트는 Single Thread 언어로 비동기 처리를 위한 작업은 브라우저나 Node 런타임 환경에서 처리
- 런타임이란 특정 언어가 동작할 수 있는 환경
- 비동기 처리에서 순서를 보장받기 위해 콜백 함수를 사용할 수 있으나, 콜백 지옥에 빠질 수 있음
- 이러한 콜백 지옥을 해결할 수 있는 것이 프로미스 객체
- 프로미스 객체는 비동기 처리를 위한 객체로 비동기 작업의 완료 또는 실패를 나타내는 객체

### Promise의 장점

- 비동기 처리 시점을 명확하게 표현할 수 있다
- 연속된 비동기 처리 작업을 수정, 삭제, 추가하기 편하고 유연하다
- 비동기 작업 상태를 쉽게 확인할 수 있다
- 코드의 유지 보수성이 증가한다

## Promise의 상태 (states)

---

프로미스는 `new Promise()` 로 프로미스를 생성하고 종료될 때까지 3가지 상태를 가짐

- Pending(대기): 비동기 처리 로직이 아직 완료되지 않은 상태
- Fulfilled(이행): 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
- Rejected(실패): 비동기 처리가 실패하거나 오류가 발생한 상태

프로미스는 객체이기에 생성자 함수를 호출하여 인스턴스화할 수 있음
- 프로미스 생성자 함수는 `resolve` 와 `reject` 함수를 인자로 전달받는 콜백 함수를 인자로 전달받는다
- 프로미스는 인자로 전달받은 콜백 함수를 내부에서 비동기 처리함
- `new Promise()` 로 인스턴스화하면 pending
- `resolve` 함수가 호출된 경우 fulfilled
- `reject` 함수가 호출된 경우 rejected

```jsx
const promise = () => new Promise((resolve, reject) => {
	let a = 1 + 1
	
	if(a == 2) {
    resolve('success')
	} else {
    reject('failed')
	}
})

promise().then((message) => {
	console.log('This is in the then ' + message)
}).catch((message) => {
	console.log('This is in the catch' + message)
})
```

## 후속 처리 메서드

---

프로미스로 구현된 비동기 함수를 호출하는 측에서는 프로미스 객체의 후속 처리 메서드(`then` , `catch`)를 통해 비동기 처리 결과 또는 에러 메세지를 전달받아 처리

- `then`
    - then 메서드는 2개의 콜백 함수를 인자로 전달받음
        - 첫번째는 성공(fulfilled, resolve 함수가 호출된 경우)시에 실행
        - 두번째는 성공(rejected, reject 함수가 호출된 경우)시에 실행
        - then 메서드는 기본적으로 프로미스를 반환함
- `catch`
    - catch 메서드는 비동기 처리 혹은 then 메서드 실행 중 발생한 에러(예외)가 발생하면 호출됨
    - catch 메서드 역시 프로미스를 반환함

## 프로미스의 에러 처리 방법

---

프로미스를 이용한 에러 처리 방법은 2가지

1. then 메서드의 두번째 인자로 예외를 처리

```jsx
const promise = () => new Promise((resolve, reject) => {
	let a = 1 + 1
	
	if(a == 3) {
    resolve('success')
	} else {
    reject('failed')
	}
})

promise().then((message) => {
	console.log('This is in the then ' +  message)
}, (error) => {
	console.log('This is in the then ' +  error)
})

// This is in the then failed
```

2. catch 메서드를 이용하여 예외를 처리

```jsx
const promise = () => new Promise((resolve, reject) => {
	let a = 1 + 1
	
	if(a == 3) {
    resolve('success')
	} else {
    reject('failed')
	}
})

promise().then((message) => {
	console.log('This is in the then ' +  message)
}).catch((error) => {
	console.log('This is in the catch ' + error)
})

// This is in the then failed
```

프로미스에서는 가급적 catch 메서드를 활용하는 것이 좋다

then 메서드의 두번째 인자를 활용하는 것보다 catch 메서드를 활용할 경우 더 많은 상황의 에러를 처리할 수 있음

1. then 메서드의 두번째 인자를 활용하는 경우

```jsx
const promise = () => new Promise((resolve, reject) => {
	let a = 1 + 1
	
	if(a == 2) {
    resolve('success')
	} else {
    reject('failed')
	}
})

promise().then((message) => {
	console.log('This is in the then ' +  message)
	throw new Error('failed')
}, (error) => {
	console.log('This is in the then ' + error)
})

// This is in the then success
// (node:52580) UnhandledPromiseRejectionWarning: Error: failed
```

2. catch 메서드를 활용하는 경우

```jsx
const promise = () => new Promise((resolve, reject) => {
	let a = 1 + 1
	
	if(a == 2) {
    resolve('success')
	} else {
    reject('failed')
	}
})

promise().then((message) => {
	console.log('This is in the then ' +  message)
	throw new Error('failed')
}).catch((error) => {
	console.log('This is in the catch ' +  error)
})

// This is in the then success
// This is in the catch Error: failed
```

## 프로미스 체이닝

---

프로미스는 후속 처리 메소드를 체이닝하여 프로미스를 반환하는 여러개의 비동기 함수들을 연결하여 사용할 수 있음 (콜백 지옥을 해결할 수 있음)

```jsx
const promise = (result) => {
	return new Promise((resolve, reject) => {
    if(result == 'success')
      resolve('success')
    else
      reject('failed')
	})
}

promise('success')
	.then(promise) // .then(result => promise(result))
	.then(message => console.log('This is in the then ' + message))
	.catch(error => console.log('This is in the catch ' + error))

// This is in the then success
```

## 정적 메서드

---

프로미스는 5가지 정적 메서드를 제공

정적 메서드이기에 객체의 생성없이 사용 가능하다

### 1. `Promise.resolve`

인자값을 래핑하여 프로미스를 반환 (fulfilled)

```jsx
const promise = Promise.resolve('success') // new Promise(resolve => resolve('success'))
promise.then(message => console.log('This is in the then ' + message))

// This is in the then success
```

### 2. `Promise.reject`

인자값을 래핑하여 프로미스를 반환 (rejected)

```jsx
const promise = Promise.reject('failed') // new Promise((resolve, reject) => reject('failed'))
promise.catch(error => console.log('This is in the catch ' + error))

// This is in the catch failed
```

### 3. `Promise.all`

프로미스가 담겨있는 배열과 같은 이터러블 객체를 인자로 받는다

인자로 전달받은 모든 프로미스를 병렬로 처리하고 그 결과값을 배열에 담아 resolve로 반환함

여러 개의 프로미스를 순차적으로 처리한다면?

```jsx
const promise1 = () => new Promise(resolve => setTimeout(() => resolve(1), 1000))
const promise2 = () => new Promise(resolve => setTimeout(() => resolve(2), 2000))
const promise3 = () => new Promise(resolve => setTimeout(() => resolve(3), 3000))

promise1().then(result => {
  console.log(result) // 프로그램을 실행하고 1초뒤에 수행됨
  return promise2()
}).then(result => {
  console.log(result) // 프로그램을 실행하고 3초뒤에 수행됨 (1 + 2)
  return promise3()
}).then(result => {
  console.log(result) // 프로그램을 실행하고 6초뒤에 수행됨 (1 + 2 + 3)
})

// 1
// 2
// 3
```

- 프로미스가 다른 프로미스를 의존하는 경우에는 순차적으로 처리할 필요가 있으나 의존성이 없는 경우에는 순차적으로 처리할 필요가 없음
- 때문에 서로 의존관계에 있지 않은 여러 프로미스들을 이터러블 객체에 담아 `Promise.all` 메서드를 활용하여 한번에 병렬처리할 수 있음
- 가장 마지막으로 끝나는 프로미스를 기준으로 수행되고, 모든 프로미스가 fulfilled 상태가 되면 결과값을 배열에 담아 새로운 프로미스를 반환함
- 프로미스를 수행하던 중 하나라도 에러가 발생하면 rejected 상태가 되고 수행을 종료함

```jsx
Promise.all([
  new Promise(resolve => setTimeout(() => resolve(1), 1000)),
  new Promise(resolve => setTimeout(() => resolve(2), 2000)),
  new Promise(resolve => setTimeout(() => resolve(3), 3000))
]).then(console.log) // 프로그램을 실행하고 3초뒤에 실행됨
.catch(console.log)

// [1, 2, 3]
```

### 4. `Promise.race`

`Promise.race` 메서드는 `Promise.all` 메서드와 동일하게 프로미스가 담겨있는 이터러블 객체를 인자로 받지만, `Promise.all` 과 달리 병렬로 처리하지 않고 가장 먼저 끝나는 프로미스의 결곽밧을 resolve로 반환함

```jsx
Promise.race([
  new Promise(resolve => setTimeout(() => resolve(1), 1000)),
  new Promise(resolve => setTimeout(() => resolve(2), 2000)),
  new Promise(resolve => setTimeout(() => resolve(3), 3000))
]).then(console.log) 
.catch(console.log)

// 1
```

### 5. `Promise.allSettled`

`Promise.allSettled` 메서드 역시 `Promise.all` 메서드와 동일하게 프로미스가 담겨있는 이터러블 객체를 인자로 받고 병렬로 처리함

다만 `Promise.all` 의 경우 프로미스를 수행하던 도중 하나라도 에러가 발생하면 rejected 상태가 되고 수행을 종료하는 반면, `Promise.allSettled` 메서드의 경우 rejected 상태가 되어도 수행을 종료하지 않고, 프로미스가 수행된 상태와 결과값을 배열에 담아 resolve로 반환함

```jsx
Promise.allSettled([
  new Promise(resolve => setTimeout(() => resolve(1), 1000)),
  new Promise((resolve, reject) => setTimeout(() => reject(2), 2000))
]).then(console.log)

/*
[
	{ status: 'fulfilled', value: 1 },
	{ status: 'rejected', reason: 2 }
]
*/
```

`Promise.all` 메서드와 또 다른 차이점은 각각의 프로미스 처리 결과를 객체로 나타내고 status 프로퍼티를 가짐
- fulfilled 상태인 경우 value 프로퍼티를, rejected 상태인 경우 reason 프로퍼티를 가지게 됨
