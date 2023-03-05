# React Guide

## Settings

---

### Create React App
- `npx create-react-app project-name`
  - `npx create-react-app .`
  - `npx create-react-app --template typescript`
- `npm install`
- `npm start`

### ESLint
- `npx eslint --init`
- `.eslintrc.json`
  - > env: javascript 코드가 동작하는 환경을 설정
  - > extends: 미리 만들어진 설정파일을 불러와서 사용할 수 있도록 해주는 옵션. package.json의 devDependencies에 설치된 모듈들을 extends 옵션에 추가하여 미리 만들어져 있는 설정값 사용 가능
  - > parserOptions: 사용하고자 하는 javascript 버전을 지정하는 옵션
  - > plugins: 미리 만들어진 rules를 불러와서 사용할 수 있도록 해주는 옵션. extends 옵션과 비슷하지만, plugins 옵션은 설정 파일의 rules만 불러온다는 점에서 다름
  - > rules: ESLint가 검사할 규칙들
```json
{
    "env": {
        "browser": true,
        "es2021": true,
        "node": true
    },
    "extends": [
        "plugin:react/recommended",
        "airbnb"
    ],
    "overrides": [
    ],
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": "latest",
        "sourceType": "module"
    },
    "plugins": [
        "react"
    ],
    "rules": {
        "react/jsx-filename-extension": [1, {"extensions": [".js", ".jsx"]}],
        "react/no-unescaped-entities": 0
    }
}
```
- **ESLint VSCode Extension** 설치하여 vscode editor 상에 에러 보이도록 설정

### Prettier
- > `npm install --save-dev --save-exact prettier`
- > `.prettierrcjson`
```json
{
    "tabWidth": 2,
    "semi": true,
    "singleQuote": true,
    "trailingComma": "all",
    "printWidth": 80
}
```

### VSCode

- `settings.json`
```json
{
  "eslint.workingDirectories": [
    {"mode": "auto"}
    ],
  "eslint.validate": [
    "javascript",
    "javascriptreact",
    "typescript",
    "typescriptreact",
    "vue",
    "markdown"
  ],
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "eslint.codeActionsOnSave.rules": null,
}
```

## How Does React Work?

---

### JSX and React Virtual DOM

> JSX Code => Babel => `React.createElement()`
>> `React.createElement(type, properties, children)`

> `React.createElement()` => Virtual DOM

> Virutal DOM => `React.render()` => DOM
```jsx
// JSX code
<div id="jsx">
  <h1>What is JSX</h1>
  <p>JSX is ...</p>
</div>

// React.createElement()
React.createElement(
  "div",
  { id: "jsx" },
  React.createElement("h1", null, "What is JSX"), 
  React.createElement("p", null, "JSX is ...")
);

// Render
ReactDOM.render(
  React.createElement(
    "div",
    { id: "jsx" },
    React.createElement("h1", null, "What is JSX"),
    React.createElement("p", null, "JSX is ...")
  ),
  document.getElementById("root")
);
```

![granular-dom-updates](https://user-images.githubusercontent.com/86648892/222876246-90958f29-352b-492a-83cb-bef42fe6c316.gif)
```jsx
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}

setInterval(tick, 1000);
```
> 분명 tick 함수가 1초에 한 번씩 호출되면서 element 전체가 새로 생성되는데 실제 DOM에서는 이전 화면과 달라지는 `{new Date().toLocaleTimeString()}` 부분만 새로 렌더링 되고 있습니다. 이것이 바로 Virtual DOM의 존재 이유입니다.

>`ReactDOM.render()` 함수가 실행이 될 때마다 React는 Virtual DOM을 새로 만듭니다. 그리고 `ReactDOM.render()` 함수가 실행되면서 새로 만들어진 VIrtual DOM과 실제 DOM의 내용을 비교해 달라진 부분을 찾아냅니다. 그리고 새로운 VIrtual DOM 전체가 아닌 찾아낸 달라진 부분만 실제 DOM에 반영해줍니다.

>Virtual DOM은 브라우저 화면에 표시되는 것이 아니라 내용이 메모리에 저장만 되고 있기 때문에 Virtual DOM을 새로 만드는 것은 비용이 큰 연산이 아닙니다. 하지만 Virtual DOM을 새로 만들고 실제 DOM과 달라진 부분을 찾아냄으로써 비용이 큰 실제 DOM 조작을 줄일 수 있습니다.

>React를 사용하지 않고 javascript로 실제 DOM을 바꾸려면 document 객체의 `createElement()`, `appendChild()` 등의 함수들을 통해서 일일이 코드 작성을 해줘야 했지만 React를 사용하면 DOM 조작은 Virtual DOM, `ReactDOM.render()` 함수에게 맡기고 어떤 데이터를 어떤 형태로 화면에 보여줄 것인지만 신경 쓰면 됩니다.

### React and ReactDOM
<img width="1038" alt="react1" src="https://user-images.githubusercontent.com/86648892/222943013-4b6c5947-1a58-4990-b873-f9811eaca2b3.png">

<img width="930" alt="react2" src="https://user-images.githubusercontent.com/86648892/222943014-f766b642-c75a-498c-a3c3-b54f5adf81ea.png">

### Re-Evaluating Components !== Re-Rendering the DOM
<img width="1055" alt="react3" src="https://user-images.githubusercontent.com/86648892/222943017-12237149-57ec-4c16-bac7-e927bd7da2c5.png">

### Virtual DOM Diffing
<img width="1060" alt="react4" src="https://user-images.githubusercontent.com/86648892/222943018-5884f8ae-34f4-4f7f-8226-36f3e11833c8.png">

### State Management with Scheduling Updates
<img width="1119" alt="behind-the-scene1" src="https://user-images.githubusercontent.com/86648892/222958112-5d900db1-9925-4e1f-8d5d-fc9194584c2f.png">

<img width="989" alt="behind-the-scene2" src="https://user-images.githubusercontent.com/86648892/222958102-6ab257f9-4b46-461a-a41d-2cc1e7105b4d.png">

## Guides

---

### Render UI & React to User Input

- Tasks
  - Pursues Declarative Programming(WHAT) (<=> Imperative Programming(HOW))
  - Evaluate & Render JSX
  - Manage State & Props
  - React to (User) Events & Input
  - Re-evaluate Component upon State & Prop changes
- `useState()`
  - The main state management "tool"
  - Great for independent pieces of state and data
  - Great if state updates are easy and limited to a few kinds of updates
- `useReducer()`
  - `const [state, dispatchFn] = useReducer(reducerFn, initialState, initFn)`
    - `dispatchFn(info)`
      - triggers the reducer function
      - info can be a string or number, but typically an object that identifies the action inside of your reducer function
      - `dispatchFn({type: '', val: null})`
    - `reducerFn()`
      - `reducerFn(state, action) => { return newStateSnapshot }`
  - Great if you need "more power"
    - More complex state update logic where you are always guaranteed to work with the latest state snapshot
    - Can also move more complex logic out of your component function body into a separate reducer function
  - Should be considered if you have related pieces of state and data
  - Can be helpful if you have more complex state updates
- Fragment
  - Solve div soup
- Portal
  - `ReactDOM.createPortal()`
  - Porting to different place in DOM
- Refs
  - `useRef()`
    - Refer to DOM element
  - `useImperativeHandle()`
    - Allows to interact with component imperatively
      - Not by passing some states(WHAT), then change something in the component
      - But by calling a function inside of the component(HOW)
    - Not a Typical React Pattern
  - `forwardRef()`
    - Allows to use ref for functional component
    - Forwarding the ref to DOM elements inside custom components
  - `useImperativeHandle()` and `forwardRef()`
    - Can expose functionalities or values from a react component to its parent component -> use the component in the parent component through refs -> and trigger certain functionalities or get values from the child
    - focusing, scrolling, ...
- Context Api
  - Solve props drilling
    - `React.createContext()`
    - `.Provider` with `value`
      - Manages the specific context and provide the value to other components
    - `.Consumer` or `useContext(contextName)`
      - The component will be re-evaluated by React whenever the context changes
  - React Context is NOT optimized for high frequency changes
    - Redux
  - React Context also shouldn't be used to replace ALL component communications and props
    - Component should still be configurable via props and short "prop chains" might not need any replacement

### Side Effects: Anything Else
- Tasks
  - Store Data in Browser Storage
  - Send Http Requests to Backend Servers
  - Set & Manage Timers
  - …
- These tasks must happen outside of the normal component evaluation and render cycle
  - especially since they might block or delay rendering (e.g. Http requests)
- `useEffect()`
  - Without dependencies
    - When you want to run the code once at the first rendering
  - With dependencies
    - When you want to deal with code that should be executed in response to something

### Rendering Optimization

- `useState()` makes a tie between component and state
  - React remembers this tie, and after initialization of the state(when the component is first rendered, or re-rendered after the component was unmounted from DOM), React does not re-initialize the state, but only manages the state updates
  - State Update Scheduling
    - State Update Detected -> Schedule State Update (Does not immediately change the state value) -> Re-render the component with the updated state
      - Multiple state update scheduled?
        - For state updates in the same code block, React badges the state updates with One update schedule
        - If not, we should guarantee the latest state snapshot
          - When working with same state, use function form `setState((prevState) => newState)`
          - When working with different state, use `useEffect()` with dependency
- `React.memo()`
  - Re-render component when there is props change
    - When parent component re-renders, but there is no change in children component, `export default React.memo(children-component)` can save unnecessary child components rendering
      - Since this process needs saving previous props info and comparing with current props info, you should decide which costs more
- `useCallback(()=>{}, [dependencies])`
  - When a component re-renders, functions inside the component are also newly made. By using `useCallBack()`, you can store the funciton in the same memory
  - Due to the characteristics of closures in javascript, you should declare dependencies for changes
  - Sample code
    ```jsx
    import React, { useState, useCallback } from 'react';
    import Button from './components/UI/Button/Button';
    import DemoOutput from './components/Demo/DemoOutput';
    import './App.css';

    function App() {
      const [showParagraph, setShowParagraph] = useState(false);
      const [allowToggle, setAllowToggle] = useState(false);

      console.log('APP RUNNING');

      const toggleParagraphHandler = useCallback(() => {
        if (allowToggle) {
          setShowParagraph((prevShowParagraph) => !prevShowParagraph);
        }
      }, [allowToggle]);

      const allowToggleHandler = () => {
        setAllowToggle(true);
      };

      return (
        <div className="app">
          <h1>Hi there!</h1>
          <DemoOutput show={showParagraph} />
          <Button onClick={allowToggleHandler}>Allow Toggling</Button>
          <Button onClick={toggleParagraphHandler}>Toggle Paragraph!</Button>
        </div>
      );
    }

    export default App;
    ```
- `useMemo(()=>{return storedData}, [dependencies])`
  - Like `useCallback()`, you can store data, especially referece type such as an array, by using `useMemo()`
  - Sample Code
    ```jsx
    // App.js
    import React, { useState, useCallback, useMemo } from 'react';
    import './App.css';
    import DemoList from './components/Demo/DemoList';
    import Button from './components/UI/Button/Button';

    function App() {
      const [listTitle, setListTitle] = useState('My List');

      const changeTitleHandler = useCallback(() => {
        setListTitle('New Title');
      }, []);

      const listItems = useMemo(() => [5, 3, 1, 10, 9], []);

      return (
        <div className="app">
          <DemoList title={listTitle} items={listItems} />
          <Button onClick={changeTitleHandler}>Change List Title</Button>
        </div>
      );
    }

    export default App;

    // DemoList.js
    import React, { useMemo } from 'react';
    import classes from './DemoList.module.css';

    const DemoList = (props) => {
      const { items } = props;

      const sortedList = useMemo(() => {
        console.log('Items sorted');
        return items.sort((a, b) => a - b);
      }, [items]); 
      console.log('DemoList RUNNING');

      return (
        <div className={classes.list}>
          <h2>{props.title}</h2>
          <ul>
            {sortedList.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        </div>
      );
    };

    export default React.memo(DemoList);
    ```
