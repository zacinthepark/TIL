# React Guide

## INDEX

---

- [Settings](#settings)
- [How Does React Work?](#how-does-react-work)
- [Guides](#guides)
- [React Lifecycle](#react-lifecycle)
- [Custom Hooks](#custom-hooks)
- [Working with Forms with Validation Logic](#working-with-forms-with-validation-logic)
- [Redux](#redux)
- [Redux Toolkit](#redux-toolkit)
- [Side Effects, Async Tasks with Redux](#side-effects-async-tasks-with-redux)
- [React Router](#react-router)
- [Fetching Data by React Router](#fetching-data-by-react-router)
- [Sending Data by React Router](#sending-data-by-react-router)
- [Other Features in React Router](#other-features-in-react-router)
- [Authentication](#authentication)
- [Optimization and Deployment](#optimization-and-deployment)

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
  - When a component re-renders, functions inside the component are also newly made. By using `useCallBack()`, you can store the function in the same memory
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

## React Lifecycle

---

<img width="1124" alt="react-lifecycle" src="https://user-images.githubusercontent.com/86648892/222975631-5461f80b-d3b7-4858-bdca-f7e3834c5d30.png">

<img width="1091" alt="react-hooks-lifecycle" src="https://user-images.githubusercontent.com/86648892/222977099-3e02de83-bc0a-4ba0-8891-d94123e966aa.png">

### React Lifecycle (Functional Component)
>1. Calls Functional Component
>2. Executes Functional Component
>3. Renders by `return()`
>4. `useEffect()` is executed


### Sample Code
#### UserFinder.js
```jsx
import { Fragment, useState, useEffect, Component } from 'react';
import Users from './Users';
import classes from './UserFinder.module.css';
import UsersContext from '../store/users-context';
import ErrorBoundary from './ErrorBoundary';

class UserFinder extends Component {
  static contextType = UsersContext;

  constructor() {
    super();
    this.state = {
      filteredUsers: [],
      searchTerm: '',
    };
  }

  componentDidMount() {
    // Send http request...
    this.setState({ filteredUsers: this.context.users });
  }

  componentDidUpdate(prevProps, prevState) {
    if (prevState.searchTerm !== this.state.searchTerm) {
      this.setState({
        filteredUsers: this.context.users.filter((user) =>
          user.name.includes(this.state.searchTerm)
        ),
      });
    }
  }

  searchChangeHandler(event) {
    this.setState({ searchTerm: event.target.value });
  }

  render() {
    return (
      <Fragment>
        <div className={classes.finder}>
          <input type='search' onChange={this.searchChangeHandler.bind(this)} />
        </div>
        <ErrorBoundary>
          <Users users={this.state.filteredUsers} />
        </ErrorBoundary>
      </Fragment>
    );
  }
}

// const UserFinder = () => {
//   const [filteredUsers, setFilteredUsers] = useState(DUMMY_USERS);
//   const [searchTerm, setSearchTerm] = useState('');

//   useEffect(() => {
//     setFilteredUsers(
//       DUMMY_USERS.filter((user) => user.name.includes(searchTerm))
//     );
//   }, [searchTerm]);

//   const searchChangeHandler = (event) => {
//     setSearchTerm(event.target.value);
//   };

//   return (
//     <Fragment>
//       <div className={classes.finder}>
//         <input type='search' onChange={searchChangeHandler} />
//       </div>
//       <Users users={filteredUsers} />
//     </Fragment>
//   );
// };

export default UserFinder;
```
#### Users.js
```jsx
import { Component } from 'react';
import User from './User';
import classes from './Users.module.css';

class Users extends Component {
  constructor() {
    super();
    this.state = {
      showUsers: true,
      more: 'Test',
    };
  }

  componentDidUpdate() {
    // try {
    //   someCodeWhichMightFail()
    // } catch (err) {
    //   // handle error
    // }
    if (this.props.users.length === 0) {
      throw new Error('No users provided!');
    }
  }

  toggleUsersHandler() {
    // this.state.showUsers = false; // NOT!
    this.setState((curState) => {
      return { showUsers: !curState.showUsers };
    });
  }

  render() {
    const usersList = (
      <ul>
        {this.props.users.map((user) => (
          <User key={user.id} name={user.name} />
        ))}
      </ul>
    );

    return (
      <div className={classes.users}>
        <button onClick={this.toggleUsersHandler.bind(this)}>
          {this.state.showUsers ? 'Hide' : 'Show'} Users
        </button>
        {this.state.showUsers && usersList}
      </div>
    );
  }
}

// const Users = () => {
//   const [showUsers, setShowUsers] = useState(true);

//   const toggleUsersHandler = () => {
//     setShowUsers((curState) => !curState);
//   };

//   const usersList = (
//     <ul>
//       {DUMMY_USERS.map((user) => (
//         <User key={user.id} name={user.name} />
//       ))}
//     </ul>
//   );

//   return (
//     <div className={classes.users}>
//       <button onClick={toggleUsersHandler}>
//         {showUsers ? 'Hide' : 'Show'} Users
//       </button>
//       {showUsers && usersList}
//     </div>
//   );
// };

export default Users;
```
#### ErrorBoundary.js
```jsx
import { Component } from 'react';

class ErrorBoundary extends Component {
  constructor() {
    super();
    this.state = { hasError: false };
  }

  componentDidCatch(error) {
    console.log(error);
    this.setState({ hasError: true });
  }

  render() {
    if (this.state.hasError) {
      return <p>Something went wrong!</p>;
    }
    return this.props.children;
  }
}

export default ErrorBoundary;
```

## Custom Hooks

---

<img width="988" alt="rules-of-hook" src="https://user-images.githubusercontent.com/86648892/223175159-8da359d7-658b-4d41-a53b-0b0a5e7cebbc.png">

> Outsource **stateful** logic into **re-usable functions**

> Unlike "regular functions", custom hooks can use other React hooks and React state

- Re-usable logic with built-in React hooks and state
- Custom hook function name should start with 'use'
  - This signals to React that this function is a custom hook
- Components using the custom hook only shares the logic, not the state
- For more re-usability, work with parameters
- Return things to be used by other components

### Before Using Custom Hook for Http Request

```jsx
// App.js

import React, { useEffect, useState } from 'react';
import Tasks from './components/Tasks/Tasks';
import NewTask from './components/NewTask/NewTask';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);
  const [tasks, setTasks] = useState([]);

  const fetchTasks = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(
        'https://react-http-aa6ec-default-rtdb.firebaseio.com/tasks.json'
      );

      if (!response.ok) {
        throw new Error('Request failed!');
      }

      const data = await response.json();

      const loadedTasks = [];

      for (const taskKey in data) {
        loadedTasks.push({ id: taskKey, text: data[taskKey].text });
      }

      setTasks(loadedTasks);
    } catch (err) {
      setError(err.message || 'Something went wrong!');
    }
    setIsLoading(false);
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const taskAddHandler = (task) => {
    setTasks((prevTasks) => prevTasks.concat(task));
  };

  return (
    <React.Fragment>
      <NewTask onAddTask={taskAddHandler} />
      <Tasks
        items={tasks}
        loading={isLoading}
        error={error}
        onFetch={fetchTasks}
      />
    </React.Fragment>
  );
}

export default App;

```

```jsx
// NewTask.js

import { useState } from 'react';
import Section from '../UI/Section';
import TaskForm from './TaskForm';

const NewTask = (props) => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const enterTaskHandler = async (taskText) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(
        'https://react-http-aa6ec-default-rtdb.firebaseio.com/tasks.json',
        {
          method: 'POST',
          body: JSON.stringify({ text: taskText }),
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );

      if (!response.ok) {
        throw new Error('Request failed!');
      }

      const data = await response.json();

      const generatedId = data.name; // firebase-specific => "name" contains generated id
      const createdTask = { id: generatedId, text: taskText };

      props.onAddTask(createdTask);
    } catch (err) {
      setError(err.message || 'Something went wrong!');
    }
    setIsLoading(false);
  };

  return (
    <Section>
      <TaskForm onEnterTask={enterTaskHandler} loading={isLoading} />
      {error && <p>{error}</p>}
    </Section>
  );
};

export default NewTask;

```

### After Using Custom Hook for Http Request

```jsx
// use-http.js

import { useState, useCallback } from 'react';

const useHttp = () => {
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendRequest = useCallback(async (requestConfig, applyData) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await fetch(requestConfig.url, {
        method: requestConfig.method ? requestConfig.method : 'GET',
        headers: requestConfig.headers ? requestConfig.headers : {},
        body: requestConfig.body ? JSON.stringify(requestConfig.body) : null,
      });

      if (!response.ok) {
        throw new Error('Request failed!');
      }

      const data = await response.json();
      applyData(data);
    } catch (err) {
      setError(err.message || 'Something went wrong!');
    }
    setIsLoading(false);
  }, []);

  return {
    isLoading,
    error,
    sendRequest,
  };
};

export default useHttp;

```

```jsx
// App.js

import React, { useEffect, useState } from 'react';
import Tasks from './components/Tasks/Tasks';
import NewTask from './components/NewTask/NewTask';
import useHttp from './hooks/use-http';

function App() {
  const [tasks, setTasks] = useState([]);

  const { isLoading, error, sendRequest: fetchTasks } = useHttp();

  useEffect(() => {
    const transformTasks = (tasksObj) => {
      const loadedTasks = [];

      for (const taskKey in tasksObj) {
        loadedTasks.push({ id: taskKey, text: tasksObj[taskKey].text });
      }

      setTasks(loadedTasks);
    };

    fetchTasks(
      { url: 'https://react-http-aa6ec-default-rtdb.firebaseio.com/tasks.json' },
      transformTasks
    );
  }, [fetchTasks]);

  const taskAddHandler = (task) => {
    setTasks((prevTasks) => prevTasks.concat(task));
  };

  return (
    <React.Fragment>
      <NewTask onAddTask={taskAddHandler} />
      <Tasks
        items={tasks}
        loading={isLoading}
        error={error}
        onFetch={fetchTasks}
      />
    </React.Fragment>
  );
}

export default App;

```

```jsx
// NewTask.js

import Section from '../UI/Section';
import TaskForm from './TaskForm';
import useHttp from '../../hooks/use-http';

const NewTask = (props) => {
  const { isLoading, error, sendRequest: sendTaskRequest } = useHttp();

  const createTask = (taskText, taskData) => {
    const generatedId = taskData.name; // firebase-specific => "name" contains generated id
    const createdTask = { id: generatedId, text: taskText };

    props.onAddTask(createdTask);
  };

  const enterTaskHandler = async (taskText) => {
    sendTaskRequest(
      {
        url: 'https://react-http-aa6ec-default-rtdb.firebaseio.com/tasks.json',
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: { text: taskText },
      },
      createTask.bind(null, taskText)
    );
  };

  return (
    <Section>
      <TaskForm onEnterTask={enterTaskHandler} loading={isLoading} />
      {error && <p>{error}</p>}
    </Section>
  );
};

export default NewTask;

```

```jsx
// TaskForm.js

import { useRef } from 'react';
import classes from './TaskForm.module.css';

const TaskForm = (props) => {
  const taskInputRef = useRef();

  const submitHandler = (event) => {
    event.preventDefault();

    const enteredValue = taskInputRef.current.value;

    if (enteredValue.trim().length > 0) {
      props.onEnterTask(enteredValue);
    }
  };

  return (
    <form className={classes.form} onSubmit={submitHandler}>
      <input type='text' ref={taskInputRef} />
      <button>{props.loading ? 'Sending...' : 'Add Task'}</button>
    </form>
  );
};

export default TaskForm;

```

## Working with Forms with Validation Logic

---

### When To Validate?

- When form is **submitted**
  - Allows the user to enter a valid value before warning him or her
  - Avoid unnecessary warnings but maybe present feedback "too late"
- When a input is **losing focus**
  - Allows the user to enter a valid value before warning him or her
  - Very useful for untouched forms
- On **every keystroke**
  - Warns user before he or she had a chance of entering valid values
  - If applied only on invalid inputs, has the potential of providing more direct feedback

### Creating a Custom useInput Hook

```jsx
// use-input.js

import { useReducer } from 'react';

const initialInputState = {
  value: '',
  isTouched: false,
};

const inputStateReducer = (state, action) => {
  if (action.type === 'INPUT') {
    return { value: action.value, isTouched: state.isTouched };
  }
  if (action.type === 'BLUR') {
    return { isTouched: true, value: state.value };
  }
  if (action.type === 'RESET') {
    return { isTouched: false, value: '' };
  }
  return initialInputState;
};

const useInput = (validateValue) => {
  const [inputState, dispatch] = useReducer(
    inputStateReducer,
    initialInputState
  );

  const valueIsValid = validateValue(inputState.value);
  const hasError = !valueIsValid && inputState.isTouched;

  const valueChangeHandler = (event) => {
    dispatch({ type: 'INPUT', value: event.target.value });
  };

  const inputBlurHandler = (event) => {
    dispatch({ type: 'BLUR' });
  };

  const reset = () => {
    dispatch({ type: 'RESET' });
  };

  return {
    value: inputState.value,
    isValid: valueIsValid,
    hasError,
    valueChangeHandler,
    inputBlurHandler,
    reset,
  };
};

export default useInput;

```

```jsx
// BasicForm.js

import useInput from '../hooks/use-input';

const isNotEmpty = (value) => value.trim() !== '';
const isEmail = (value) => value.includes('@');

const BasicForm = (props) => {
  const {
    value: firstNameValue,
    isValid: firstNameIsValid,
    hasError: firstNameHasError,
    valueChangeHandler: firstNameChangeHandler,
    inputBlurHandler: firstNameBlurHandler,
    reset: resetFirstName,
  } = useInput(isNotEmpty);
  const {
    value: lastNameValue,
    isValid: lastNameIsValid,
    hasError: lastNameHasError,
    valueChangeHandler: lastNameChangeHandler,
    inputBlurHandler: lastNameBlurHandler,
    reset: resetLastName,
  } = useInput(isNotEmpty);
  const {
    value: emailValue,
    isValid: emailIsValid,
    hasError: emailHasError,
    valueChangeHandler: emailChangeHandler,
    inputBlurHandler: emailBlurHandler,
    reset: resetEmail,
  } = useInput(isEmail);

  let formIsValid = false;

  if (firstNameIsValid && lastNameIsValid && emailIsValid) {
    formIsValid = true;
  }

  const submitHandler = event => {
    event.preventDefault();

    if (!formIsValid) {
      return;
    }

    console.log('Submitted!');
    console.log(firstNameValue, lastNameValue, emailValue);

    resetFirstName();
    resetLastName();
    resetEmail();
  };

  const firstNameClasses = firstNameHasError ? 'form-control invalid' : 'form-control';
  const lastNameClasses = lastNameHasError ? 'form-control invalid' : 'form-control';
  const emailClasses = emailHasError ? 'form-control invalid' : 'form-control';

  return (
    <form onSubmit={submitHandler}>
      <div className='control-group'>
        <div className={firstNameClasses}>
          <label htmlFor='name'>First Name</label>
          <input
            type='text'
            id='name'
            value={firstNameValue}
            onChange={firstNameChangeHandler}
            onBlur={firstNameBlurHandler}
          />
          {firstNameHasError && <p className="error-text">Please enter a first name.</p>}
        </div>
        <div className={lastNameClasses}>
          <label htmlFor='name'>Last Name</label>
          <input
            type='text'
            id='name'
            value={lastNameValue}
            onChange={lastNameChangeHandler}
            onBlur={lastNameBlurHandler}
          />
          {lastNameHasError && <p className="error-text">Please enter a last name.</p>}
        </div>
      </div>
      <div className={emailClasses}>
        <label htmlFor='name'>E-Mail Address</label>
        <input
          type='text'
          id='name'
          value={emailValue}
          onChange={emailChangeHandler}
          onBlur={emailBlurHandler}
        />
        {emailHasError && <p className="error-text">Please enter a valid email address.</p>}
      </div>
      <div className='form-actions'>
        <button disabled={!formIsValid}>Submit</button>
      </div>
    </form>
  );
};

export default BasicForm;

```

### Creating a Custom useForm Hook

- [Creating a Custom useForm Hook](https://academind.com/tutorials/reactjs-a-custom-useform-hook)
- Creating a custom hook to manage forms in React without relying on any library
- Refer to sample codes in *16-working-with-forms-advanced*

### Formik

- [Formik Docs](https://formik.org/docs/overview)
- Third-party Library for working with forms
  - More complex forms and validations
- More using components than hooks
- Core idea is that you don't have to write much state management logic, but instead you write your validation logic, you define your fields, and then let Formik do the rest

## Redux

---

### What is Redux?

- Third-party Library for React
- A **state management system** for **cross-component or app-wide state**
  - Local State
    - State that belongs to a single component
    - e.g. listening to user input in a input field; toggling a "show more" details field
    - Should be managed component-internal with `useState()` or `useReducer()`
  - Cross-Component State
    - State that affects multiple components
    - e.g. open, closed state of a modal overlay
    - Requires "prop chains" or "prop drilling"
  - App-Wide State
    - State that affects the entire app (most or all components)
    - e.g. user authentication status
    - Requires "prop chains" or "prop drilling"
- Alternatives for prop chains
  - Context Api
  - **Redux**

### Redux vs Context Api

- Can mix both ways in one app
- Potential Disadvantages of React Context
  - Complex Setup and Management
    > In more complex apps, managing React Context can lead to deeply nested JSX code or huge 'Context Provider' components
    ```jsx
    return (
      <AuthContextProvider>
        <ThemeContextProvider>
          <UIInteractionContextProvider>
            <MultiStepFormContextProvider>
              <UserRegistration />
            </MultiStepFormContextProvider>
          </UIInteractionContextProvider>
        </ThemeContextProvider>
      </AuthContextProvider>
    )
    ```
    ![contextprovider](https://user-images.githubusercontent.com/86648892/223889201-8fe90150-b44f-4942-a5af-8092bc800ace.png)
  - Performance
  > React Context is not optimized for high-frequency state changes

### Core Redux Concepts

![core-redux-concepts](https://user-images.githubusercontent.com/86648892/223892078-e43fd5a1-d169-4529-9701-a53c8e40e367.png)

- `npm install redux`
- `npm install react-redux`
  - `createStore()` deprecated
    - `npm install redux@4.1.2 react-redux`
- The Reducer Function
  > Inputs: Old State + Dispatched Action => Output: New State Object
  - Should be a pure function
    - Same input leads to same output
    - There should be no side effects inside of this function
      - e.g. http requests, writing, fetching to or from local storage
```jsx
// redux-demo.js

// import redux
const redux = require('redux')

// define reducer
// both reducer and subscriber function will be executed by redux
// we don't execute, just point at it
const counterReducer = (state = { counter: 0 }, action) => {
  // Do actions based on type
  if (action.type === 'increment') {
    return {
      counter: state.counter + 1
    };
  }
  if (action.type === 'decrement') {
    return {
      counter: state.counter -1
    };
  }
  // return new state object
  return state;
};

// create central store
const store = redux.createStore(counterReducer);
// console.log(store.getState());

// set subscription
const counterSubscriber = () => {
  const latestState = store.getState(); // gives us latest state snapshot after it was updated
  console.log(latestState);
};
store.subscribe(counterSubscriber);

// dispatch action with type and payload
store.dispatch( { type: 'increment' } );
store.dispatch( { type: 'decrement' } );
```

### Working with Redux in React

- redux manages things about store
- react-redux manages things between react components and store
- create store file from redux `createStore()`
- wrap with `<Provider></Provider>` from react-redux
- notice which store to be provided
- react-redux hooks
  - `useSelector()`
    - access to store and select parts of overall state object
    - react-redux **automatically setup a subscription** to the redux store for the component
      - your component will be updated and will receive the latest data automatically whenever the data changes
    - `const result : any = useSelector(selector : Function, equalityFn? : Function)`
      - `selectorFn((state managed by redux) => part of the state you want to extract)`
  - `useStore()`
    - access to store
  - `useDispatch()`
    - `const dispatch = useDispatch();`
    - `dispatch(payload)`
    - dispatch an action to the store
- New state object returned by redux reducer will NOT be merged with the existing state, BUT override the existing state
  - Because Objects and Arrays are **REFERENCE VALUES** in Javascript, it's easy to accidentally override and change the existing state
  - **YOU SHOULD NEVER MUTATE THE EXISTING STATE**
    - Can lead to bugs, unpredictable behavior, and make debugging your app harder
  - **INSTEAD ALWAYS OVERRIDE IT BY RETURNING A BRAND NEW STATE**

#### Sample Codes

```jsx
// store/index.js
import { createStore } from 'redux';

const initialState = { counter: 0, showCounter: true };

const counterReducer = (state = initialState, action) => {
  if (action.type === 'increment') {
    return {
      counter: state.counter + 1,
      showCounter: state.showCounter,
    };
  }

  if (action.type === 'increase') {
    return {
      counter: state.counter + action.amount,
      showCounter: state.showCounter,
    };
  }

  if (action.type === 'decrement') {
    return {
      counter: state.counter - 1,
      showCounter: state.showCounter,
    };
  }

  if (action.type === 'toggle') {
    return {
      showCounter: !state.showCounter,
      counter: state.counter,
    };
  }

  return state;
};

const store = createStore(counterReducer);

export default store;
```
```jsx
// index.js
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import App from './App';
import store from './store/index';
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
```
```jsx
// Counter.js
import { useSelector, useDispatch } from 'react-redux';
import classes from './Counter.module.css';

const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector((state) => state.counter);
  const show = useSelector((state) => state.showCounter);

  const incrementHandler = () => {
    dispatch({ type: 'increment' });
  };

  const increaseHandler = () => {
    dispatch({ type: 'increase', amount: 10 });
  };

  const decrementHandler = () => {
    dispatch({ type: 'decrement' });
  };

  const toggleCounterHandler = () => {
    dispatch({ type: 'toggle' });
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {show && <div className={classes.value}>{counter}</div>}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={increaseHandler}>Increase by 10</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;
```

### Redux in Class-Based Components

```jsx
import { Component } from 'react';
import { connect } from 'react-redux';

class Counter extends Component {
  incrementHandler() {
    this.props.increment();
  }

  decrementHandler() {
    this.props.decrement();
  }

  toggleCounterHandler() {}

  render() {
    return (
      <main className={classes.counter}>
        <h1>Redux Counter</h1>
        <div className={classes.value}>{this.props.counter}</div>
        <div>
          <button onClick={this.incrementHandler.bind(this)}>Increment</button>
          <button onClick={this.decrementHandler.bind(this)}>Decrement</button>
        </div>
        <button onClick={this.toggleCounterHandler}>Toggle Counter</button>
      </main>
    );
  }
}

// store states in props
const mapStateToProps = state => {
  return {
    counter: state.counter
  };
}

// store dispatch functions in props
const mapDispatchToProps = dispatch => {
  return {
    increment: () => dispatch({ type: 'increment' }),
    decrement: () => dispatch({ type: 'decrement' }),
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(Counter);

// Using Functional Component
// import { useSelector, useDispatch } from 'react-redux';
// import classes from './Counter.module.css';

// const Counter = () => {
//   const dispatch = useDispatch();
//   const counter = useSelector(state => state.counter);

//   const incrementHandler = () => {
//     dispatch({ type: 'increment' });
//   };

//   const decrementHandler = () => {
//     dispatch({ type: 'decrement' });
//   };

//   const toggleCounterHandler = () => {};

//   return (
//     <main className={classes.counter}>
//       <h1>Redux Counter</h1>
//       <div className={classes.value}>{counter}</div>
//       <div>
//         <button onClick={incrementHandler}>Increment</button>
//         <button onClick={decrementHandler}>Decrement</button>
//       </div>
//       <button onClick={toggleCounterHandler}>Toggle Counter</button>
//     </main>
//   );
// };

// export default Counter;
```
- `connect(fn1, fn2)(Component)`
  - `connect()` returns new function
    - fn1 maps redux state to props of the component
    - fn2 stores dispatchFns in props
  - To the returned function, pass the component

## Redux Toolkit

---

### Install
- `npm install @reduxjs/toolkit`
  - uninstall the existing redux package

### What and Why React Toolkit?
- Extra package which makes working with Redux more convenient and easier
- Potential problems with Redux when managing more and more states
  1. Clashing between action type identifiers
    - Solution: `const INCREMENT = 'increment'` and export
  2. Have to copy a lot of states, making the reducer function longer, and making redux file unmaintainably big
    - Solution: splitting reducer into multiple smaller reducers
  3. Easy to accidentally change the existing state
    - Solution: Third-party packages that allow you to automatically copy state
- Redux Toolkit provides more convenient ways for the potential problems

### Features

![react-toolkit](https://user-images.githubusercontent.com/86648892/224208182-6d767a6b-1a04-4007-b0df-c7d1bc95656d.png)
  x
- `createSlice({ name, initialState, reducers })`
  - create different slices of state
    > reducer 함수와 action creator를 포함한 객체
  - `name: 'identifier'`
    > 해당 모듈의 이름 작성
  - `initialState: { ... }`
    > 해당 모듈의 초기값 세팅
  - `reducers: { method1(state, action?){}, method2(state, action?){}, ... }`
    > 리듀서 작성, 이때 **해당 리듀서의 키값으로 액션함수가 자동으로 생성**
    >> createSlice의 actions 속성, 즉 `.actions`를 통해 action creator를 호출하면 같은 이름의 리듀서 함수에게 action을 dispatch함
    ```jsx
    // Sample Code

    // src/store/index.js
    export const counterActions = counterSlice.actions;

    // src/components/Counter.js
    import { useDispatch } from 'react-redux';
    import { counterActions } from '../store/index';

    const Counter = () => {
      const dispatch = useDispatch();
      const incrementHandler = () => {
        dispatch(counterActions.increment());
      }
      const increaseHandler = () => {
        // 10 is a payload
        // { type: SOME_UNIQUE_IDENTIFIER, payload: 10 }
        dispatch(counterActions.increase(10))
      }
    }
    ```
    - No more if checks for action type
      - Methods will automatically be called depending on which action was triggered
    - In the reducers method, we are **allowed to mutate** the state
      - Actually, we are not really mutating the existing state
      - Redux Toolkit internally uses package called **'immer'**, and detects codes that try to change existing state, and automatically clones the existing state, creates a new state object, keeps all the state which we are not editing, and **overrides the state which we are editing in a IMMUTABLE WAY**
  - extraReducers
    > 액션함수가 자동으로 생성되지 않는 별도의 액션함수가 존재하는 리듀서를 정의

- `combineReducers()`
  > - 각 reducer를 호출하여 초기 상태를 검색
  > - 초기 상태를 정리하여 초기 상태 트리르 만
  > - reducer의 처리를 정리한 combination 함수를 돌려줌
  ```jsx
  const rootReducer = combineReducers({
    a: aSlice.reducer,
    b: bSlice.reducer,
    ...
  });
  ```

- `configureStore({ reducer: })`
  > - Reducer에서 반환한 새로운 state을 Store라는 객체로 정리해 관리하는 곳
  > - Store는 Redux Toolkit configureStore에 객체 형식으로 reducer를 전달하여 만들 수 있음
  ```jsx
  const store = configureStore({
    reducer: rootReducer,
  });
  ```

## Side Effects, Async Tasks with Redux

---

<img width="1069" alt="redux-async" src="https://user-images.githubusercontent.com/86648892/224492065-854598bb-593d-49f3-8d0f-b3feda623fbb.png">

<img width="1084" alt="where-should-the-logic-go" src="https://user-images.githubusercontent.com/86648892/224506037-1959939e-a3ce-4bde-8abb-501bb4f44238.png">

### Thunk Action Creators

- **A function that delays an action until later**
- An **action creator function** that **does NOT return the action itself** but **another function which eventually returns the action**

### Sample Codes

#### `store/cart-actions.js`
- **custom action creator**
- work as a middleware
- instead of returning action object, this returns another function that finally returns action object
- dispatch argument is automatically given
```jsx
import { uiActions } from './ui-slice';
import { cartActions } from './cart-slice';

export const fetchCartData = () => {
  return async (dispatch) => {
    const fetchData = async () => {
      const response = await fetch(
        'https://react-http-aa6ec-default-rtdb.firebaseio.com/cart.json'
      );

      if (!response.ok) {
        throw new Error('Could not fetch cart data!');
      }

      const data = await response.json();

      return data;
    };

    try {
      const cartData = await fetchData();
      dispatch(
        cartActions.replaceCart({
          items: cartData.items || [],
          totalQuantity: cartData.totalQuantity,
        })
      );
    } catch (error) {
      dispatch(
        uiActions.showNotification({
          status: 'error',
          title: 'Error!',
          message: 'Fetching cart data failed!',
        })
      );
    }
  };
};

export const sendCartData = (cart) => {
  return async (dispatch) => {
    dispatch(
      uiActions.showNotification({
        status: 'pending',
        title: 'Sending...',
        message: 'Sending cart data!',
      })
    );

    const sendRequest = async () => {
      const response = await fetch(
        'https://react-http-aa6ec-default-rtdb.firebaseio.com/cart.json',
        {
          method: 'PUT',
          body: JSON.stringify({
            items: cart.items,
            totalQuantity: cart.totalQuantity,
          }),
        }
      );

      if (!response.ok) {
        throw new Error('Sending cart data failed.');
      }
    };

    try {
      await sendRequest();

      dispatch(
        uiActions.showNotification({
          status: 'success',
          title: 'Success!',
          message: 'Sent cart data successfully!',
        })
      );
    } catch (error) {
      dispatch(
        uiActions.showNotification({
          status: 'error',
          title: 'Error!',
          message: 'Sending cart data failed!',
        })
      );
    }
  };
};

```

#### `store/cart-slice.js`
```jsx
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: {
    items: [],
    totalQuantity: 0,
    changed: false,
  },
  reducers: {
    replaceCart(state, action) {
      state.totalQuantity = action.payload.totalQuantity;
      state.items = action.payload.items;
    },
    addItemToCart(state, action) {
      const newItem = action.payload;
      const existingItem = state.items.find((item) => item.id === newItem.id);
      state.totalQuantity++;
      state.changed = true;
      if (!existingItem) {
        state.items.push({
          id: newItem.id,
          price: newItem.price,
          quantity: 1,
          totalPrice: newItem.price,
          name: newItem.title,
        });
      } else {
        existingItem.quantity++;
        existingItem.totalPrice = existingItem.totalPrice + newItem.price;
      }
    },
    removeItemFromCart(state, action) {
      const id = action.payload;
      const existingItem = state.items.find((item) => item.id === id);
      state.totalQuantity--;
      state.changed = true;
      if (existingItem.quantity === 1) {
        state.items = state.items.filter((item) => item.id !== id);
      } else {
        existingItem.quantity--;
        existingItem.totalPrice = existingItem.totalPrice - existingItem.price;
      }
    },
  },
});

// return action object { type: '', payload: ... };
export const cartActions = cartSlice.actions;

export default cartSlice;

```

#### `store/ui-slice.js`
```jsx
import { createSlice } from '@reduxjs/toolkit';

const uiSlice = createSlice({
  name: 'ui',
  initialState: { cartIsVisible: false, notification: null },
  reducers: {
    toggle(state) {
      state.cartIsVisible = !state.cartIsVisible;
    },
    showNotification(state, action) {
      state.notification = {
        status: action.payload.status,
        title: action.payload.title,
        message: action.payload.message,
      };
    },
  },
});

export const uiActions = uiSlice.actions;

export default uiSlice;

```

#### `store/index.js`
```jsx
import { configureStore } from '@reduxjs/toolkit';

import uiSlice from './ui-slice';
import cartSlice from './cart-slice';

const store = configureStore({
  reducer: { ui: uiSlice.reducer, cart: cartSlice.reducer },
});

export default store;

```

#### `src/index.js`
```jsx
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';

import store from './store/index';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);

```

#### `src/App.js`
```jsx
import { Fragment, useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import Cart from './components/Cart/Cart';
import Layout from './components/Layout/Layout';
import Products from './components/Shop/Products';
import Notification from './components/UI/Notification';
import { sendCartData, fetchCartData } from './store/cart-actions';

let isInitial = true;

function App() {
  const dispatch = useDispatch();
  const showCart = useSelector((state) => state.ui.cartIsVisible);
  const cart = useSelector((state) => state.cart);
  const notification = useSelector((state) => state.ui.notification);

  useEffect(() => {
    dispatch(fetchCartData());
  }, [dispatch]);

  useEffect(() => {
    if (isInitial) {
      isInitial = false;
      return;
    }

    if (cart.changed) {
      dispatch(sendCartData(cart));
    }
  }, [cart, dispatch]);

  return (
    <Fragment>
      {notification && (
        <Notification
          status={notification.status}
          title={notification.title}
          message={notification.message}
        />
      )}
      <Layout>
        {showCart && <Cart />}
        <Products />
      </Layout>
    </Fragment>
  );
}

export default App;

```

## React Router

---

> [React Router Docs](https://reactrouter.com/en/main)

### Defining Routes
- `npm install react-router-dom`
```jsx
import {
  createBrowserRouter,
  // createRoutesFromElements,
  RouterProvider,
  // Route,
} from 'react-router-dom';

import ErrorPage from './pages/Error';
import HomePage from './pages/Home';
import ProductDetailPage from './pages/ProductDetail';
import ProductsPage from './pages/Products';
import RootLayout from './pages/Root';

// React Router < 6.4
// const routeDefinitions = createRoutesFromElements(
//   <Route>
//     <Route path="/" element={<HomePage />} />
//     <Route path="/products" element={<ProductsPage />} />
//   </Route>
// );

const router = createBrowserRouter([
  {
    // absolute path (starts with slash, added after the domain)
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    // child routes are rendered in <Outlet />
    children: [
      // { path: '', element: <HomePage /> },
      { index: true, element: <HomePage /> },
      // relative path (added after the current path)
      { path: 'products', element: <ProductsPage /> },
      { path: 'products/:productId', element: <ProductDetailPage /> }
    ],
  }
]);

// const router = createBrowserRouter(routeDefinitions);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

### Routing through Links
- `<Link to='/...'></Link>`
  - renders anchor element at DOM by React
  - unlike `<a/>` tag, this does not re-render the whole single page
  - `<Link to='..' relative='route'>Back</Link>`
    - go to parent route in the definition
  - `<Link to='..' relative='path'>Back</Link>`
    - simply remove one segment of the currently active path
- `<NavLink to '...'></NavLink>`
  - support convenience to the links
  - className prop is a function which returns the class property to be used, and the parameter is what provided by react-router-dom
    - e.g. get isActive by object destructuring `{ isActive }`
  ```jsx
  <NavLink
    to="/"
    className={({ isActive }) =>
      isActive ? classes.active : undefined
    }
    // style={({ isActive }) => ({
    //   textAlign: isActive ? 'center' : 'left',
    // })}
    end={ true }
  >
  ```

### Navigating Programatically
- `useNavigate()`
  ```jsx
  const navigate = useNavigate();
  function navigateHandler() {
    navigate('/...')
  };
  ```

### Dynamic Routing
- `const params = useParams()`
- access to the identifier after colon(`:`) in the route definition

## Fetching Data by React Router

---

### Loader

- loader is a property that wants a function as a value
  - this function will be executed by react router whenever you are about to visit the route (before rendering the page)
  - return data to be used
    - browser response example
      ```jsx
      const res = new Response('any data', { status: 201 });
      return res;
      ```
    - react-router package extracts the data(in here, 'any data') from your response when using `useLoaderData()`
      - this **automatic data extraction** is useful for fetch API
      - fetch API returns Promise that resolves to Response
      ```jsx
      import { useLoaderData } from 'react-router-dom';
      import EventsList from '../components/EventsList';

      function EventsPage() {
        // const events = useLoaderData();
        const data = useLoaderData();
        // if (data.isError) {
          // return <p>{ data.message }</p>;
        // }
        const events = data.events;

        return <EventsList events={events} />;
      }

      export default EventsPage;

      export async function loader() {
        const response = await fetch('http://localhost:8080/events');

        if (!response.ok) {
          // error handling
          // 1) return custom error object (cannot use status)
          // return { isError: true, message: 'Could not fetch events.' };

          // 2) throw an error (can use status property)
          // first argument can be accessed by error.data, second argument is about configuration, and error.status is possible
          // when an error gets thrown in a loader, react-router will simply render the closest error element
          throw new Response(JSON.stringify({ message: 'Could not fetch events.' }), { 
            status: 500 
          });
        } else {

          // instead of manually extracting data from response
          const resData = await response.json()
          return resData;

          // you can just return response (react)
          return response;
        }
      }
      ```
- `useLoaderData()`
  - get access to the **closest loader data**
    - highest level at which it looks for data is the route defintion of the route for which the component is loaded
  - can use `useLoaderData()` in the element that's assigned to a route AND in all components that might be used inside that element
- put your loader logic in the page component and import it in the routing definition (RECOMMENDED)
- `useNavigation()`
  - check current route transition state
  ```jsx
  const navigation = useNavigation();
  // navigation.state: idle, loading, submitting
  ```

### Error Handling

- `useRouteError()`
  - get data from thrown error inside of the component that is being rendered as an `errorElement`
  ```jsx
  // Error.js

  import { useRouteError } from 'react-router-dom';
  import MainNavigation from '../components/MainNavigation';
  import PageContent from '../components/PageContent';

  function ErrorPage() {
    const error = useRouteError();

    let title = 'An error occurred!';
    let message = 'Something went wrong!';

    if (error.status === 500) {
      message = JSON.parse(error.data).message;
    }

    // default status set by react-router if you enter path that is not supported
    if (error.status === 404) {
      title = 'Not found!';
      message = 'Could not find resource or page.';
    }

    return (
      <>
        <MainNavigation />
        <PageContent title={title}>
          <p>{message}</p>
        </PageContent>
      </>
    );
  }

  export default ErrorPage;

  ```
  ```jsx
  // Events.js
  import { useLoaderData } from 'react-router-dom';
  import EventsList from '../components/EventsList';

  function EventsPage() {
    const data = useLoaderData();

    // if (data.isError) {
    //   return <p>{data.message}</p>;
    // }
    const events = data.events;

    return <EventsList events={events} />;
  }

  export default EventsPage;

  export async function loader() {
    const response = await fetch('http://localhost:8080/events');

    if (!response.ok) {
      // return { isError: true, message: 'Could not fetch events.' };
      throw new Response(JSON.stringify({ message: 'Could not fetch events.' }), {
        status: 500,
      });
    } else {
      return response;
    }
  }

  ```
  ```jsx
  // App.js

  import { RouterProvider, createBrowserRouter } from 'react-router-dom';
  import EditEventPage from './pages/EditEvent';
  import ErrorPage from './pages/Error';
  import EventDetailPage from './pages/EventDetail';
  import EventsPage, { loader as eventsLoader } from './pages/Events';
  import EventsRootLayout from './pages/EventsRoot';
  import HomePage from './pages/Home';
  import NewEventPage from './pages/NewEvent';
  import RootLayout from './pages/Root';

  const router = createBrowserRouter([
    {
      path: '/',
      element: <RootLayout />,
      errorElement: <ErrorPage />,
      children: [
        { index: true, element: <HomePage /> },
        {
          path: 'events',
          element: <EventsRootLayout />,
          children: [
            {
              index: true,
              element: <EventsPage />,
              loader: eventsLoader,
            },
            { path: ':eventId', element: <EventDetailPage /> },
            { path: 'new', element: <NewEventPage /> },
            { path: ':eventId/edit', element: <EditEventPage /> },
          ],
        },
      ],
    },
  ]);

  function App() {
    return <RouterProvider router={router} />;
  }

  export default App;

  ```

### Json Helper Function
- `json()`
  - `import { json } from 'react-router-dom'`
  - a helper function that simplifies creating a Response object that includes data in json format
  - In the first argument, simply pass the data that should be included in the Response
  - In the second argument, you can set extra response meta data (e.g. status)
  ```jsx
  export async function loader() {
    const response = await fetch('http://localhost:8080/events');

    if (!response.ok) {
      // return { isError: true, message: 'Could not fetch events.' };
      // throw new Response(JSON.stringify({ message: 'Could not fetch events.' }), {
      //   status: 500,
      // });
      throw json(
        { message: 'Could not fetch events.' },
        {
          status: 500,
        }
      );
    } else {
      return response;
    }
  }
  ```

### Loader in Dynamic Routes

```jsx
// EventDetail.js

import { useLoaderData, json } from 'react-router-dom';
import EventItem from '../components/EventItem';

function EventDetailPage() {
  const data = useLoaderData();

  return (
    <EventItem event={data.event} />
  );
}

export default EventDetailPage;

export async function loader({request, params}) {
  const id = params.eventId;

  const response = await fetch('http://localhost:8080/events/' + id);

  if (!response.ok) {
    throw json({message: 'Could not fetch details for selected event.'}, {
      status: 500
    })
  } else {
    return response;
  }
}

```

### `useRouteLoaderData()`

- `useRouteLoaderData('routeId')`
  - this hook makes the data at any currently rendered route available anywhere in the tree
  - useful for components deep in the tree needing data from routes much farther up, as well as parent routes needing the data of child routes deeper in the tree
```jsx
// App.js

import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage from './pages/NewEvent';
import RootLayout from './pages/Root';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
              },
              { path: 'edit', element: <EditEventPage /> },
            ],
          },
          { path: 'new', element: <NewEventPage /> },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

```jsx
// EditEvent.js

import { useRouteLoaderData } from 'react-router-dom';
import EventForm from '../components/EventForm';

function EditEventPage() {
  const data = useRouteLoaderData('event-detail');

  return <EventForm event={data.event} />;
}

export default EditEventPage;

```

```jsx
// EventForm.js
// defaultValue
// fills the form with default values

import { useNavigate } from 'react-router-dom';
import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  const navigate = useNavigate();
  function cancelHandler() {
    navigate('..');
  }

  return (
    <form className={classes.form}>
      <p>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          type="text"
          name="title"
          required
          defaultValue={event ? event.title : ''}
        />
      </p>
      <p>
        <label htmlFor="image">Image</label>
        <input
          id="image"
          type="url"
          name="image"
          required
          defaultValue={event ? event.image : ''}
        />
      </p>
      <p>
        <label htmlFor="date">Date</label>
        <input
          id="date"
          type="date"
          name="date"
          required
          defaultValue={event ? event.date : ''}
        />
      </p>
      <p>
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          rows="5"
          required
          defaultValue={event ? event.description : ''}
        />
      </p>
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler}>
          Cancel
        </button>
        <button>Save</button>
      </div>
    </form>
  );
}

export default EventForm;

```

## Sending Data by React Router

---

### Action

> This feature only works if using a data router like `createBrowserRouter`
```jsx
<Route
  path="/song/:songId/edit"
  element={<EditSong />}
  action={async ({ params, request }) => {
    let formData = await request.formData();
    return fakeUpdateSong(params.songId, formData);
  }}
  loader={({ params }) => {
    return fakeGetSong(params.songId);
  }}
/>
```
> Actions are called whenever the app sends a non-get submission ("post", "put", "patch", "delete") to your route. This can happen in a few ways:
```jsx
// forms
<Form method="post" action="/songs" />;
<fetcher.Form method="put" action="/songs/123/edit" />;

// imperative submissions
let submit = useSubmit();
submit(data, {
  method: "delete",
  action: "/songs/123",
});
fetcher.submit(data, {
  method: "patch",
  action: "/songs/123/edit",
});
```

#### `params`
> Route params are parsed from **dynamic segments** and passed to your action. This is useful for figuring out which resource to mutate:
```jsx
<Route
  path="/projects/:projectId/delete"
  action={({ params }) => {
    return fakeDeleteProject(params.projectId);
  }}
/>
```

#### `request`
> This is a Fetch Request instance being sent to your route. The most common use case is to parse the FormData from the request
```jsx
<Route
  action={async ({ request }) => {
    let formData = await request.formData();
    // ...
  }}
/>
```
> It might seem odd at first that actions receive a "request". Have you ever written this line of code?
```jsx
<form
  onSubmit={(event) => {
    event.preventDefault();
    // ...
  }}
/>
```
> What exactly are you preventing?

> Without JavaScript, just plain HTML and an HTTP web server, that default event that was prevented is actually pretty great. Browsers will serialize all the data in the form into `FormData` and send it as the body of a new request to your server. Like the code above, **React Router `<Form>` prevents the browser from sending that request and instead sends the request to your route action!** This enables highly dynamic web apps with the simple model of HTML and HTTP.

> Remember that the values in the `formData` are automatically serialized from the form submission, so your inputs need a `name`.
```jsx
<Form method="post">
  <input name="songTitle" />
  <textarea name="lyrics" />
  <button type="submit">Save</button>
</Form>;

// accessed by the same names
formData.get("songTitle");
formData.get("lyrics");
```

#### Returning Responses
> While you can return anything you want from an action and get access to it from `useActionData`, you can also return a web `Response`.

#### Throwing in Actions
> You can `throw` in your action to break out of the current call stack (stop running the current code) and React Router will start over down the "error path".
```jsx
<Route
  action={async ({ params, request }) => {
    const res = await fetch(
      `/api/properties/${params.id}`,
      {
        method: "put",
        body: await request.formData(),
      }
    );
    if (!res.ok) throw res;
    return { ok: true };
  }}
/>
```

### React `<Form>` tag and `action`

- For data submission, you can create a function that handles http request inside the component, but there is a better way
  - You can use `action` property to the route
  - This gives you the simple mental model of **HTML + HTTP** (where the browser handles the asynchrony and revalidation)

- `action({ request, params })`
  - Route actions are the "writes" to route loader "reads"
  - Actions are **called whenever the app sends a non-get submission ("post", "put", "delete") to your route**
  - `request.formData()` to access the submitted data
  - `data.get('input-name-property')` to access the the input data

- `<Form>` component provided by React
  - This form tag will make sure the browser default of sending a request to backend will be omitted
  - Instead, it will take that request that would have sent, and give it to your action
  - Useful because that request will contain all the data that was submitted as part of the form
  - If you want to trigger action defined in another route, not the current route, you can add action property to the Form
    - `<Form method='post' action='/any-other-path' className={classes.form}>`

```jsx
// App.js

import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage, { action as newEventAction } from './pages/NewEvent';
import RootLayout from './pages/Root';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
              },
              { path: 'edit', element: <EditEventPage /> },
            ],
          },
          { path: 'new', element: <NewEventPage />, action: newEventAction },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

```jsx
// NewEvent.js

import { json, redirect } from 'react-router-dom';
import EventForm from '../components/EventForm';

function NewEventPage() {
  return <EventForm />;
}

export default NewEventPage;

export async function action({ request, params }) {
  const data = await request.formData();

  const eventData = {
    title: data.get('title'),
    image: data.get('image'),
    date: data.get('date'),
    description: data.get('description'),
  };

  const response = await fetch('http://localhost:8080/events', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(eventData),
  });

  if (!response.ok) {
    throw json({ message: 'Could not save event.' }, { status: 500 });
  }

  return redirect('/events');
}

```

```jsx
// EventForm.js

import { useNavigate } from 'react-router-dom';
import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  const navigate = useNavigate();
  function cancelHandler() {
    navigate('..');
  }

  return (
    <Form method='post' className={classes.form}>
      <p>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          type="text"
          name="title"
          required
          defaultValue={event ? event.title : ''}
        />
      </p>
      <p>
        <label htmlFor="image">Image</label>
        <input
          id="image"
          type="url"
          name="image"
          required
          defaultValue={event ? event.image : ''}
        />
      </p>
      <p>
        <label htmlFor="date">Date</label>
        <input
          id="date"
          type="date"
          name="date"
          required
          defaultValue={event ? event.date : ''}
        />
      </p>
      <p>
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          rows="5"
          required
          defaultValue={event ? event.description : ''}
        />
      </p>
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler}>
          Cancel
        </button>
        <button>Save</button>
      </div>
    </Form>
  );
}

export default EventForm;

```

### `useSubmit()` and action

- Besides Form tag, you can also trigger route action programmatically by `useSubmit()`
- First argument is the data you want to submit
  - Can extract with `request.formData()` method
- Second argument is other configurations
  - same values we could set on the form
  - action key to different path if you want to
```jsx
// ...
const submit = useSubmit();

function startDeleteHandler() {
  const proceed = window.confirm('Are you sure?');
  if (proceed) {
    submit(null, { method: 'delete', actions: '/a-different-path' })
  }
}
// ...
```

```jsx
// App.js

import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
  action as deleteEventAction,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage, { action as newEventAction } from './pages/NewEvent';
import RootLayout from './pages/Root';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
                action: deleteEventAction,
              },
              { path: 'edit', element: <EditEventPage /> },
            ],
          },
          { path: 'new', element: <NewEventPage />, action: newEventAction },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

```jsx
// EventDetail.js

import { useRouteLoaderData, json, redirect } from 'react-router-dom';
import EventItem from '../components/EventItem';

function EventDetailPage() {
  const data = useRouteLoaderData('event-detail');

  return <EventItem event={data.event} />;
}

export default EventDetailPage;

export async function loader({ request, params }) {
  const id = params.eventId;

  const response = await fetch('http://localhost:8080/events/' + id);

  if (!response.ok) {
    throw json(
      { message: 'Could not fetch details for selected event.' },
      {
        status: 500,
      }
    );
  } else {
    return response;
  }
}

export async function action({ params, request }) {
  const eventId = params.eventId;
  const response = await fetch('http://localhost:8080/events/' + eventId, {
    method: request.method,
  });

  if (!response.ok) {
    throw json(
      { message: 'Could not delete event.' },
      {
        status: 500,
      }
    );
  }
  return redirect('/events');
}

```

```jsx
// EventItem.js

import { Link, useSubmit } from 'react-router-dom';
import classes from './EventItem.module.css';

function EventItem({ event }) {
  const submit = useSubmit();

  function startDeleteHandler() {
    const proceed = window.confirm('Are you sure?');

    if (proceed) {
      submit(null, { method: 'delete' });
    }
  }

  return (
    <article className={classes.event}>
      <img src={event.image} alt={event.title} />
      <h1>{event.title}</h1>
      <time>{event.date}</time>
      <p>{event.description}</p>
      <menu className={classes.actions}>
        <Link to="edit">Edit</Link>
        <button onClick={startDeleteHandler}>Delete</button>
      </menu>
    </article>
  );
}

export default EventItem;

```

### `useNavigation()` and form submission state

- `const navigation = useNavigation()`
  - This hook tells you everything you need to know about a page navigation to build pending navigation indicators and optimistic UI on data mutations
  - `navigation.state`
    - **idle**: There is no navigation pending
    - **submitting**: A route action is being called due to a form submission using POST, PUT, PATCH, or DELETE
    - **loading**: The loaders for the next routes are being called to render the next page
    > Normal navigations and GET form submissions transition
    >> idle -> loading -> idle

    > Form submissions with POST, PUT, PATCH, or DELETE transition
    >> idle -> submitting -> loading -> idle

  - `navigation.formData`
  > Any POST, PUT, PATCH, or DELETE navigation that started from a `<Form>` or `useSubmit` will have your form's submission data attached to it. This is primarily useful to build "Optimistic UI" with the submission.formData FormData object.

  >In the case of a GET form submission, formData will be empty and the data will be reflected in navigation.location.search.

  - `navigation.location`
  > This tells you what the next location is going to be.

  > Note that this link will not appear "pending" if a form is being submitted to the URL the link points to, because we only do this for "loading" states. The form will contain the pending UI for when the state is "submitting", once the action is complete, then the link will go pending.

- Sample Codes
```jsx
import { useNavigation } from "react-router-dom";

function SomeComponent() {
  const navigation = useNavigation();
  navigation.state;
  navigation.location;
  navigation.formData;
  navigation.formAction;
  navigation.formMethod;
}
```
```jsx
function SubmitButton() {
  const navigation = useNavigation();

  const text =
    navigation.state === "submitting"
      ? "Saving..."
      : navigation.state === "loading"
      ? "Saved!"
      : "Go";

  return <button type="submit">{text}</button>;
}
```
```jsx
// Is this just a normal load?
let isNormalLoad =
  navigation.state === "loading" &&
  navigation.formData == null;

// Are we reloading after an action?
let isReloading =
  navigation.state === "loading" &&
  navigation.formData != null &&
  navigation.formAction === navigation.location.pathname;

// Are we redirecting after an action?
let isRedirecting =
  navigation.state === "loading" &&
  navigation.formData != null &&
  navigation.formAction !== navigation.location.pathname;
```

```jsx
// EventForm.js

import { Form, useNavigate, useNavigation } from 'react-router-dom';
import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  const navigate = useNavigate();
  const navigation = useNavigation();

  const isSubmitting = navigation.state === 'submitting';

  function cancelHandler() {
    navigate('..');
  }

  return (
    <Form method="post" className={classes.form}>
      <p>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          type="text"
          name="title"
          required
          defaultValue={event ? event.title : ''}
        />
      </p>
      ...
      ...
      ...
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler} disabled={isSubmitting}>
          Cancel
        </button>
        <button disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Save'}
        </button>
      </div>
    </Form>
  );
}

export default EventForm;

```

### Returning Data from Route Action

- `useActionData()`
- Just as we can return responses in loaders and use the data in our pages and components, we can also **returned action data** in our pages and components
- Useful for **validation error responses where you don't want show on a separate error page**
```jsx
// NewEvent.js

import { json, redirect } from 'react-router-dom';
import EventForm from '../components/EventForm';

function NewEventPage() {
  return <EventForm />;
}

export default NewEventPage;

export async function action({ request, params }) {
  const data = await request.formData();

  const eventData = {
    title: data.get('title'),
    image: data.get('image'),
    date: data.get('date'),
    description: data.get('description'),
  };

  const response = await fetch('http://localhost:8080/events', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(eventData),
  });

  if (response.status === 422) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not save event.' }, { status: 500 });
  }

  return redirect('/events');
}

```

```jsx
// EventForm.js

import {
  Form,
  useNavigate,
  useNavigation,
  useActionData,
} from 'react-router-dom';
import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  const data = useActionData();
  const navigate = useNavigate();
  const navigation = useNavigation();

  const isSubmitting = navigation.state === 'submitting';

  function cancelHandler() {
    navigate('..');
  }

  return (
    <Form method="post" className={classes.form}>
      {data && data.errors && (
        <ul>
          {Object.values(data.errors).map((err) => (
            <li key={err}>{err}</li>
          ))}
        </ul>
      )}
      <p>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          type="text"
          name="title"
          required
          defaultValue={event ? event.title : ''}
        />
      </p>
      <p>
        <label htmlFor="image">Image</label>
        <input
          id="image"
          type="url"
          name="image"
          required
          defaultValue={event ? event.image : ''}
        />
      </p>
      <p>
        <label htmlFor="date">Date</label>
        <input
          id="date"
          type="date"
          name="date"
          required
          defaultValue={event ? event.date : ''}
        />
      </p>
      <p>
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          rows="5"
          required
          defaultValue={event ? event.description : ''}
        />
      </p>
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler} disabled={isSubmitting}>
          Cancel
        </button>
        <button disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Save'}
        </button>
      </div>
    </Form>
  );
}

export default EventForm;

```

### Reusing Action (CREATE and EDIT)

#### `EventForm.js`
```jsx
import {
  Form,
  useNavigate,
  useNavigation,
  useActionData,
  json,
  redirect
} from 'react-router-dom';

import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  const data = useActionData();
  const navigate = useNavigate();
  const navigation = useNavigation();

  const isSubmitting = navigation.state === 'submitting';

  function cancelHandler() {
    navigate('..');
  }

  return (
    <Form method={method} className={classes.form}>
      {data && data.errors && (
        <ul>
          {Object.values(data.errors).map((err) => (
            <li key={err}>{err}</li>
          ))}
        </ul>
      )}
      <p>
        <label htmlFor="title">Title</label>
        <input
          id="title"
          type="text"
          name="title"
          required
          defaultValue={event ? event.title : ''}
        />
      </p>
      <p>
        <label htmlFor="image">Image</label>
        <input
          id="image"
          type="url"
          name="image"
          required
          defaultValue={event ? event.image : ''}
        />
      </p>
      <p>
        <label htmlFor="date">Date</label>
        <input
          id="date"
          type="date"
          name="date"
          required
          defaultValue={event ? event.date : ''}
        />
      </p>
      <p>
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          rows="5"
          required
          defaultValue={event ? event.description : ''}
        />
      </p>
      <div className={classes.actions}>
        <button type="button" onClick={cancelHandler} disabled={isSubmitting}>
          Cancel
        </button>
        <button disabled={isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Save'}
        </button>
      </div>
    </Form>
  );
}

export default EventForm;

export async function action({ request, params }) {
  const method = request.method;
  const data = await request.formData();

  const eventData = {
    title: data.get('title'),
    image: data.get('image'),
    date: data.get('date'),
    description: data.get('description'),
  };

  let url = 'http://localhost:8080/events';

  if (method === 'PATCH') {
    const eventId = params.eventId;
    url = 'http://localhost:8080/events/' + eventId;
  }

  const response = await fetch(url, {
    method: method,
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(eventData),
  });

  if (response.status === 422) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not save event.' }, { status: 500 });
  }

  return redirect('/events');
}

```

#### `App.js`
```jsx
import { RouterProvider, createBrowserRouter } from 'react-router-dom';

import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
  action as deleteEventAction,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage from './pages/NewEvent';
import RootLayout from './pages/Root';
import { action as manipulateEventAction } from './components/EventForm';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
                action: deleteEventAction,
              },
              {
                path: 'edit',
                element: <EditEventPage />,
                action: manipulateEventAction,
              },
            ],
          },
          {
            path: 'new',
            element: <NewEventPage />,
            action: manipulateEventAction,
          },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

#### `NewEvent.js`
```jsx
import EventForm from '../components/EventForm';

function NewEventPage() {
  return <EventForm method="post" />;
}

export default NewEventPage;

```

#### `EditEvent.js`
```jsx
import { useRouteLoaderData } from 'react-router-dom';
import EventForm from '../components/EventForm';

function EditEventPage() {
  const data = useRouteLoaderData('event-detail');

  return <EventForm method="patch" event={data.event} />;
}

export default EditEventPage;

```

## Other Features in React Router

---

- **[useFetcher](#usefetcher)**
- **[defer](#defer)**
- **[Await](#await)**
- **[defer and Await](#defer-and-await)**

### `useFetcher`

- `useFetcher()` hook is a tool you should use if you want to interact with action or loader without transitioning
- Triggers loader or action **without navigating to the page to which the loader or action belongs**
- Sending your request behind-the-scenes without triggering any route changes

#### Sample Code

- NewsletterSignup component is included in navbar, so every page has this component
- Should we add the action to all routes?
  - Too much code duplication
  - Clash between actions
- Target a single route by setting the "action" attribute?
  - You would initialize a transition to Newsletter route and leave the current route
- `useFetcher()` can be a good solution

```jsx
// App.js

import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
  action as deleteEventAction,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage from './pages/NewEvent';
import RootLayout from './pages/Root';
import { action as manipulateEventAction } from './components/EventForm';
import NewsletterPage, { action as newsletterAction } from './pages/Newsletter';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
                action: deleteEventAction,
              },
              {
                path: 'edit',
                element: <EditEventPage />,
                action: manipulateEventAction,
              },
            ],
          },
          {
            path: 'new',
            element: <NewEventPage />,
            action: manipulateEventAction,
          },
        ],
      },
      {
        path: 'newsletter',
        element: <NewsletterPage />,
        action: newsletterAction,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

```jsx
// Newsletter.js

import NewsletterSignup from '../components/NewsletterSignup';
import PageContent from '../components/PageContent';

function NewsletterPage() {
  return (
    <PageContent title="Join our awesome newsletter!">
      <NewsletterSignup />
    </PageContent>
  );
}

export default NewsletterPage;

export async function action({ request }) {
  const data = await request.formData();
  const email = data.get('email');

  // send to backend newsletter server ...
  console.log(email);
  return { message: 'Signup successful!' };
}

```

```jsx
// NewsletterSignup.js

import { useEffect } from 'react';
import { useFetcher } from 'react-router-dom';
import classes from './NewsletterSignup.module.css';

function NewsletterSignup() {
  const fetcher = useFetcher();
  const { data, state } = fetcher;

  useEffect(() => {
    if (state === 'idle' && data && data.message) {
      window.alert(data.message);
    }
  }, [data, state]);

  return (
    <fetcher.Form
      method="post"
      action="/newsletter"
      className={classes.newsletter}
    >
      <input
        type="email"
        placeholder="Sign up for newsletter..."
        aria-label="Sign up for newsletter"
      />
      <button>Sign up</button>
    </fetcher.Form>
  );
}

export default NewsletterSignup;

```

> In HTML/HTTP, data mutations and loads are modeled with navigation: `<a href>` and `<form action>`. Both cause a navigation in the browser. The React Router equivalents are `<Link>` and `<Form>`.

> But sometimes you want to call a `loader` outside of navigation, or call an `action` (and get the data on the page to revalidate) without changing the URL. Or you need to have multiple mutations in-flight at the same time.

> Many interactions with the server aren't navigation events. This hook lets you plug your UI into your actions and loaders without navigating.

> This is useful when you need to:
> - fetch data not associated with UI routes (popovers, dynamic forms, etc.)
> - submit data to actions without navigating (shared components like a newsletter sign ups)
> - handle multiple concurrent submissions in a list (typical "todo app" list where you can click multiple buttons and all should be pending at the same time)
> - infinite scroll containers
> - and more!

> If you're building a highly interactive, "app like" user interface, you will `useFetcher` often.

```jsx
import { useFetcher } from "react-router-dom";

function SomeComponent() {
  const fetcher = useFetcher();

  // call submit or load in a useEffect
  React.useEffect(() => {
    fetcher.submit(data, options);
    fetcher.load(href);
  }, [fetcher]);

  // build your UI with these properties
  fetcher.state;
  fetcher.formData;
  fetcher.formMethod;
  fetcher.formAction;
  fetcher.data;

  // render a form that doesn't cause navigation
  return <fetcher.Form />;
}
```

> Fetchers have a lot of built-in behavior:
> - Automatically handles cancellation on interruptions of the fetch
> - When submitting with POST, PUT, PATCH, DELETE, the action is called first
>> - After the action completes, the data on the page is revalidated to capture any mutations that may have happened, automatically keeping your UI in sync with your server state
> - When multiple fetchers are inflight at once, it will
>> - commit the freshest available data as they each land
>> - ensure no stale loads override fresher data, no matter which order the responses return
> - Handles uncaught errors by rendering the nearest `errorElement` (just like a normal navigation from `<Link>` or `<Form>`)
> - Will redirect the app if your action/loader being called returns a redirect (just like a normal navigation from `<Link>` or `<Form>`)

#### `fetcher.state`

> You can know the state of the fetcher with `fetcher.state`. It will be one of:
> - **idle** - nothing is being fetched.
> - **submitting** - A route action is being called due to a fetcher submission using POST, PUT, PATCH, or DELETE
> - **loading** - The fetcher is calling a loader (from a `fetcher.load`) or is being revalidated after a separate submission or `useRevalidator` call

#### `fetcher.Form`

> Just like `<Form>` except it doesn't cause a navigation. (You'll get over the dot in JSX ... we hope!)
```jsx
function SomeComponent() {
  const fetcher = useFetcher();
  return (
    <fetcher.Form method="post" action="/some/route">
      <input type="text" />
    </fetcher.Form>
  );
}
```

#### `fetcher.load()`

> Load data from a route loader.
```jsx
import { useFetcher } from "react-router-dom";

function SomeComponent() {
  const fetcher = useFetcher();

  useEffect(() => {
    if (fetcher.state === "idle" && !fetcher.data) {
      fetcher.load("/some/route");
    }
  }, [fetcher]);

  return <div>{fetcher.data || "Loading..."}</div>;
}
```
> Although a URL might match multiple nested routes, a `fetcher.load()` call will only call the loader on the leaf match (or parent of index routes).

> If you find yourself calling this function inside of click handlers, you can probably simplify your code by using `<fetcher.Form>` instead.

> Note
>> Any `fetcher.load` calls that are active on the page will be re-executed as part of revalidation (either after a navigation submission, another fetcher submission, or a `useRevalidator()` call)

#### `fetcher.submit()`

> The imperative version of `<fetcher.Form>`. **If a user interaction should initiate the fetch**, you should use `<fetcher.Form>`. But **if you, the programmer are initiating the fetch** (not in response to a user clicking a button, etc.), then use this function.

> For example, you may want to log the user out after a certain amount of idle time:
```jsx
import { useFetcher } from "react-router-dom";
import { useFakeUserIsIdle } from "./fake/hooks";

export function useIdleLogout() {
  const fetcher = useFetcher();
  const userIsIdle = useFakeUserIsIdle();

  useEffect(() => {
    if (userIsIdle) {
      fetcher.submit(
        { idle: true },
        { method: "post", action: "/logout" }
      );
    }
  }, [userIsIdle]);
}
```
> If you want to submit to an index route, use the `?index` param.

> If you find yourself calling this function inside of click handlers, you can probably simplify your code by using `<fetcher.Form>` instead.

#### `fetcher.data`

> The returned data from the loader or action is stored here. Once the data is set, it persists on the fetcher even through reloads and resubmissions.
```jsx
function ProductDetails({ product }) {
  const fetcher = useFetcher();

  return (
    <details
      onToggle={(event) => {
        if (
          event.currentTarget.open &&
          fetcher.state === "idle" &&
          !fetcher.data
        ) {
          fetcher.load(`/product/${product.id}/details`);
        }
      }}
    >
      <summary>{product.name}</summary>
      {fetcher.data ? (
        <div>{fetcher.data}</div>
      ) : (
        <div>Loading product details...</div>
      )}
    </details>
  );
}
```

#### `fetcher.formData`

> When using `<fetcher.Form>` or `fetcher.submit()`, the form data is available to build optimistic UI.
```jsx
function TaskCheckbox({ task }) {
  let fetcher = useFetcher();

  // while data is in flight, use that to immediately render
  // the state you expect the task to be in when the form
  // submission completes, instead of waiting for the
  // network to respond. When the network responds, the
  // formData will no longer be available and the UI will
  // use the value in `task.status` from the revalidation
  let status =
    fetcher.formData?.get("status") || task.status;

  let isComplete = status === "complete";

  return (
    <fetcher.Form method="post">
      <button
        type="submit"
        name="status"
        value={isComplete ? "incomplete" : "complete"}
      >
        {isComplete ? "Mark Incomplete" : "Mark Complete"}
      </button>
    </fetcher.Form>
  );
}
```

#### `fetcher.formAction`

> Tells you the action url the form is being submitted to.
```jsx
<fetcher.Form action="/mark-as-read" />;

// when the form is submitting
fetcher.formAction; // "mark-as-read"
```

#### `fetcher.formMethod`

> Tells you the method of the form being submitted: get, post, put, patch, or delete.
```jsx
<fetcher.Form method="post" />;

// when the form is submitting
fetcher.formMethod; // "post"
```

### `defer`

- defer when data is loaded
- defer loading and tell react-router that we want to render a component even though the data is not fully there yet

> This utility allows you to defer values returned from loaders by passing promises instead of resolved values.
```jsx
async function loader() {
  let product = await getProduct();
  let reviews = getProductReviews();
  return defer({ product, reviews });
}
```

### `<Await>`

> Used to render **deferred** values with automatic error handling.
>> Note: `<Await>` expects to be rendered inside of a `<React.Suspense>` or `<React.SuspenseList>` parent to enable the fallback UI.

```jsx
import { Await, useLoaderData } from "react-router-dom";

function Book() {
  const { book, reviews } = useLoaderData();
  return (
    <div>
      <h1>{book.title}</h1>
      <p>{book.description}</p>
      <React.Suspense fallback={<ReviewsSkeleton />}>
        <Await
          resolve={reviews}
          errorElement={
            <div>Could not load reviews 😬</div>
          }
          children={(resolvedReviews) => (
            <Reviews items={resolvedReviews} />
          )}
        />
      </React.Suspense>
    </div>
  );
}
```

#### `children`

> Can either be React elements or a function.

> When using a function, the value is provided as the only parameter.

```jsx
<Await resolve={reviewsPromise}>
  {(resolvedReviews) => <Reviews items={resolvedReviews} />}
</Await>
```

> When using React elements, `useAsyncValue` will provide the data:
```jsx
<Await resolve={reviewsPromise}>
  <Reviews />
</Await>;

function Reviews() {
  const resolvedReviews = useAsyncValue();
  return <div>{/* ... */}</div>;
}
```

#### `errorElement`

> The error element renders instead of the children when the promise rejects. You can access the error with `useAsyncError`.

> If the promise rejects, you can provide an optional `errorElement` to handle that error in a contextual UI via the `useAsyncError` hook.

```jsx
<Await
  resolve={reviewsPromise}
  errorElement={<ReviewsError />}
>
  <Reviews />
</Await>;

function ReviewsError() {
  const error = useAsyncError();
  return <div>{error.message}</div>;
}
```

> If you do not provide an errorElement, the rejected value will bubble up to the nearest route-level `errorElement` and be accessible via the `useRouteError` hook.

#### `resolve`

> Takes a promise returned from a deferred loader value to be resolved and rendered.

```jsx
import {
  defer,
  Route,
  useLoaderData,
  Await,
} from "react-router-dom";

// given this route
<Route
  loader={async () => {
    let book = await getBook();
    let reviews = getReviews(); // not awaited
    return defer({
      book,
      reviews, // this is a promise
    });
  }}
  element={<Book />}
/>;

function Book() {
  const {
    book,
    reviews, // this is the same promise
  } = useLoaderData();
  return (
    <div>
      <h1>{book.title}</h1>
      <p>{book.description}</p>
      <React.Suspense fallback={<ReviewsSkeleton />}>
        <Await
          // and is the promise we pass to Await
          resolve={reviews}
        >
          <Reviews />
        </Await>
      </React.Suspense>
    </div>
  );
}
```

### `defer` and `<Await>`

#### Sample Code

```jsx
// EventDetail.js

import { Suspense } from 'react';
import {
  useRouteLoaderData,
  json,
  redirect,
  defer,
  Await,
} from 'react-router-dom';
import EventItem from '../components/EventItem';
import EventsList from '../components/EventsList';

function EventDetailPage() {
  const { event, events } = useRouteLoaderData('event-detail');

  return (
    <>
      <Suspense fallback={<p style={{ textAlign: 'center' }}>Loading...</p>}>
        <Await resolve={event}>
          {(loadedEvent) => <EventItem event={loadedEvent} />}
        </Await>
      </Suspense>
      <Suspense fallback={<p style={{ textAlign: 'center' }}>Loading...</p>}>
        <Await resolve={events}>
          {(loadedEvents) => <EventsList events={loadedEvents} />}
        </Await>
      </Suspense>
    </>
  );
}

export default EventDetailPage;

async function loadEvent(id) {
  const response = await fetch('http://localhost:8080/events/' + id);

  if (!response.ok) {
    throw json(
      { message: 'Could not fetch details for selected event.' },
      {
        status: 500,
      }
    );
  } else {
    const resData = await response.json();
    return resData.event;
  }
}

async function loadEvents() {
  const response = await fetch('http://localhost:8080/events');

  if (!response.ok) {
    // return { isError: true, message: 'Could not fetch events.' };
    // throw new Response(JSON.stringify({ message: 'Could not fetch events.' }), {
    //   status: 500,
    // });
    throw json(
      { message: 'Could not fetch events.' },
      {
        status: 500,
      }
    );
  } else {
    const resData = await response.json();
    return resData.events;
  }
}

export async function loader({ request, params }) {
  const id = params.eventId;

  return defer({
    event: await loadEvent(id),
    events: loadEvents(),
  });
}

export async function action({ params, request }) {
  const eventId = params.eventId;
  const response = await fetch('http://localhost:8080/events/' + eventId, {
    method: request.method,
  });

  if (!response.ok) {
    throw json(
      { message: 'Could not delete event.' },
      {
        status: 500,
      }
    );
  }
  return redirect('/events');
}

```

## Authentication

---

<img width="950" alt="getting-permission" src="https://user-images.githubusercontent.com/86648892/224759209-35405cf8-cb7a-4951-9b12-9d0d58a44db7.png">

### Query Parameters

- `const [searchParams, setSearchParams] = useSearchParams()`
  - object that gives us access to the currently set query parameters
  - function that allows to update the currently set query parameters
- Query Parameters are officially called search parameters

```jsx
import { Form, Link, useSearchParams } from 'react-router-dom';
import classes from './AuthForm.module.css';

function AuthForm() {
  const [searchParams] = useSearchParams();
  const isLogin = searchParams.get('mode') === 'login';

  // localhost:3000/auth/?mode=signup
  // localhost:3000/auth/?mode=login
  return (
    <>
      <Form method="post" className={classes.form}>
        <h1>{isLogin ? 'Log in' : 'Create a new user'}</h1>
        <p>
          <label htmlFor="email">Email</label>
          <input id="email" type="email" name="email" required />
        </p>
        <p>
          <label htmlFor="image">Password</label>
          <input id="password" type="password" name="password" required />
        </p>
        <div className={classes.actions}>
          <Link to={`?mode=${isLogin ? 'signup' : 'login'}`}>
            {isLogin ? 'Create new user' : 'Login'}
          </Link>
          <button>Save</button>
        </div>
      </Form>
    </>
  );
}

export default AuthForm;

```

### Signup and Login

- Pass form data for signup and login
- Update UI with validation and submitting state
- Store token in the localStorage
- Attach token to other http requests

```jsx
// Authentication.js

import { json, redirect } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

function AuthenticationPage() {
  return <AuthForm />;
}

export default AuthenticationPage;

export async function action({ request }) {
  const searchParams = new URL(request.url).searchParams;
  const mode = searchParams.get('mode') || 'login';

  if (mode !== 'login' && mode !== 'signup') {
    throw json({ message: 'Unsupported mode.' }, { status: 422 });
  }

  const data = await request.formData();
  const authData = {
    email: data.get('email'),
    password: data.get('password'),
  };

  const response = await fetch('http://localhost:8080/' + mode, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(authData),
  });

  if (response.status === 422 || response.status === 401) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not authenticate user.' }, { status: 500 });
  }

  // store the token
  const resData = await response.json();
  const token = resData.token;

  localStorage.setItem('token', token);

  return redirect('/');
}

```

```jsx
// AuthForm.js

import {
  Form,
  Link,
  useSearchParams,
  useActionData,
  useNavigation,
} from 'react-router-dom';
import classes from './AuthForm.module.css';

function AuthForm() {
  const data = useActionData(); // for user input validation
  const navigation = useNavigation();

  const [searchParams] = useSearchParams();
  const isLogin = searchParams.get('mode') === 'login';
  const isSubmitting = navigation.state === 'submitting'; // for submitting state

  return (
    <>
      <Form method="post" className={classes.form}>
        <h1>{isLogin ? 'Log in' : 'Create a new user'}</h1>
        {data && data.errors && (
          <ul>
            {Object.values(data.errors).map((err) => (
              <li key={err}>{err}</li>
            ))}
          </ul>
        )}
        {data && data.message && <p>{data.message}</p>}
        <p>
          <label htmlFor="email">Email</label>
          <input id="email" type="email" name="email" required />
        </p>
        <p>
          <label htmlFor="image">Password</label>
          <input id="password" type="password" name="password" required />
        </p>
        <div className={classes.actions}>
          <Link to={`?mode=${isLogin ? 'signup' : 'login'}`}>
            {isLogin ? 'Create new user' : 'Login'}
          </Link>
          <button disabled={isSubmitting}>
            {isSubmitting ? 'Submitting...' : 'Save'}
          </button>
        </div>
      </Form>
    </>
  );
}

export default AuthForm;

```

```jsx
// auth.js

export function getAuthToken() {
  const token = localStorage.getItem('token');
  return token;
}

```

```jsx
// EventForm.js

import {
  Form,
  useNavigate,
  useNavigation,
  useActionData,
  json,
  redirect
} from 'react-router-dom';
import { getAuthToken } from '../util/auth';
import classes from './EventForm.module.css';

function EventForm({ method, event }) {
  // ...
}

export default EventForm;

export async function action({ request, params }) {
  const method = request.method;
  const data = await request.formData();

  const eventData = {
    title: data.get('title'),
    image: data.get('image'),
    date: data.get('date'),
    description: data.get('description'),
  };

  let url = 'http://localhost:8080/events';

  if (method === 'PATCH') {
    const eventId = params.eventId;
    url = 'http://localhost:8080/events/' + eventId;
  }

  const token = getAuthToken();
  const response = await fetch(url, {
    method: method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + token
    },
    body: JSON.stringify(eventData),
  });

  if (response.status === 422) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not save event.' }, { status: 500 });
  }

  return redirect('/events');
}

```

### Logout

- Make an empty component, and export an action function that removes token
- Add new route with the action defined
- Wrap a logout button with React `<Form>`

```jsx
// Logout.js
import { redirect } from 'react-router-dom';

export function action() {
  localStorage.removeItem('token');
  return redirect('/');
}

```

```jsx
// MainNavigation.js

// ...

<li>
  <Form action="/logout" method="post">
    <button>Logout</button>
  </Form>
</li>

// ...
```

```jsx
// App.js
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
// ...
import { action as logoutAction } from './pages/Logout';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          // ...
        ],
      },
      {
        path: 'auth',
        element: <AuthenticationPage />,
        action: authAction,
      },
      {
        path: 'newsletter',
        element: <NewsletterPage />,
        action: newsletterAction,
      },
      {
        path: 'logout',
        action: logoutAction,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

### Updating UI based on Token

- Update token for every navigation by setting loader in the root route
- Use `useRouteLoaderData()` to check the token

```jsx
// auth.js

export function getAuthToken() {
  const token = localStorage.getItem('token');
  return token;
}

export function tokenLoader() {
  return getAuthToken();
}

```

```jsx
import { RouterProvider, createBrowserRouter } from 'react-router-dom';
// ...
import { tokenLoader } from './util/auth';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    id: 'root',
    loader: tokenLoader,
    children: [
      { index: true, element: <HomePage /> },
      // ...
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

```jsx
// MainNavigation.js

import { Form, NavLink, useRouteLoaderData } from 'react-router-dom';

import classes from './MainNavigation.module.css';
import NewsletterSignup from './NewsletterSignup';

function MainNavigation() {
  const token = useRouteLoaderData('root');

  return (
    <header className={classes.header}>
      <nav>
        <ul className={classes.list}>
          <li>
            <NavLink
              to="/"
              className={({ isActive }) =>
                isActive ? classes.active : undefined
              }
              end
            >
              Home
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/events"
              className={({ isActive }) =>
                isActive ? classes.active : undefined
              }
            >
              Events
            </NavLink>
          </li>
          <li>
            <NavLink
              to="/newsletter"
              className={({ isActive }) =>
                isActive ? classes.active : undefined
              }
            >
              Newsletter
            </NavLink>
          </li>
          {!token && (
            <li>
              <NavLink
                to="/auth?mode=login"
                className={({ isActive }) =>
                  isActive ? classes.active : undefined
                }
              >
                Authentication
              </NavLink>
            </li>
          )}
          {token && (
            <li>
              <Form action="/logout" method="post">
                <button>Logout</button>
              </Form>
            </li>
          )}
        </ul>
      </nav>
      <NewsletterSignup />
    </header>
  );
}

export default MainNavigation;

```

### Route Protection

- Utilize a loader that simply checks if we have a token
- If we don't have a token, redirect to another page(typically, login page)

```jsx
// auth.js

import { redirect } from 'react-router-dom';

export function getAuthToken() {
  const token = localStorage.getItem('token');
  return token;
}

export function tokenLoader() {
  return getAuthToken();
}

export function checkAuthLoader() {
  const token = getAuthToken();

  if (!token) {
    return redirect('/auth');
  }

  return null;
}

```

```jsx
// App.js

import { RouterProvider, createBrowserRouter } from 'react-router-dom';
import EditEventPage from './pages/EditEvent';
import ErrorPage from './pages/Error';
import EventDetailPage, {
  loader as eventDetailLoader,
  action as deleteEventAction,
} from './pages/EventDetail';
import EventsPage, { loader as eventsLoader } from './pages/Events';
import EventsRootLayout from './pages/EventsRoot';
import HomePage from './pages/Home';
import NewEventPage from './pages/NewEvent';
import RootLayout from './pages/Root';
import { action as manipulateEventAction } from './components/EventForm';
import NewsletterPage, { action as newsletterAction } from './pages/Newsletter';
import AuthenticationPage, {
  action as authAction,
} from './pages/Authentication';
import { action as logoutAction } from './pages/Logout';
import { checkAuthLoader, tokenLoader } from './util/auth';

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    errorElement: <ErrorPage />,
    id: 'root',
    loader: tokenLoader,
    children: [
      { index: true, element: <HomePage /> },
      {
        path: 'events',
        element: <EventsRootLayout />,
        children: [
          {
            index: true,
            element: <EventsPage />,
            loader: eventsLoader,
          },
          {
            path: ':eventId',
            id: 'event-detail',
            loader: eventDetailLoader,
            children: [
              {
                index: true,
                element: <EventDetailPage />,
                action: deleteEventAction,
              },
              {
                path: 'edit',
                element: <EditEventPage />,
                action: manipulateEventAction,
                loader: checkAuthLoader,
              },
            ],
          },
          {
            path: 'new',
            element: <NewEventPage />,
            action: manipulateEventAction,
            loader: checkAuthLoader,
          },
        ],
      },
      {
        path: 'auth',
        element: <AuthenticationPage />,
        action: authAction,
      },
      {
        path: 'newsletter',
        element: <NewsletterPage />,
        action: newsletterAction,
      },
      {
        path: 'logout',
        action: logoutAction,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```

### Token Expiration

- store the expiration time in the localStorage when we first get a token

```jsx
// Authentication.js

import { json, redirect } from 'react-router-dom';
import AuthForm from '../components/AuthForm';

function AuthenticationPage() {
  return <AuthForm />;
}

export default AuthenticationPage;

export async function action({ request }) {
  const searchParams = new URL(request.url).searchParams;
  const mode = searchParams.get('mode') || 'login';

  if (mode !== 'login' && mode !== 'signup') {
    throw json({ message: 'Unsupported mode.' }, { status: 422 });
  }

  const data = await request.formData();
  const authData = {
    email: data.get('email'),
    password: data.get('password'),
  };

  const response = await fetch('http://localhost:8080/' + mode, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(authData),
  });

  if (response.status === 422 || response.status === 401) {
    return response;
  }

  if (!response.ok) {
    throw json({ message: 'Could not authenticate user.' }, { status: 500 });
  }

  const resData = await response.json();
  const token = resData.token;

  localStorage.setItem('token', token);
  // 토큰 유효 기간이 1시간이므로, 나중에 비교를 위해 토큰 생성 시간 기준 1시간 뒤의 날짜 객체를 생성 및 localStorage에 저장
  const expiration = new Date();
  expiration.setHours(expiration.getHours() + 1);
  localStorage.setItem('expiration', expiration.toISOString());

  return redirect('/');
}

```

- get token duration by comparing expiration date and now
- set the token duration as a logout time out
- also check if token is expired, and if it is, logout
- remove expiration date stored in the localStorage when logging out

```jsx
// auth.js

import { redirect } from 'react-router-dom';

export function getTokenDuration() {
  const storedExpirationDate = localStorage.getItem('expiration');
  const expirationDate = new Date(storedExpirationDate);
  const now = new Date();
  // getTime() gives time value in milliseconds
  const duration = expirationDate.getTime() - now.getTime();
  return duration;
}

export function getAuthToken() {
  const token = localStorage.getItem('token');

  if (!token) {
    return null;
  }

  const tokenDuration = getTokenDuration();

  if (tokenDuration < 0) {
    return 'EXPIRED';
  }

  return token;
}

export function tokenLoader() {
  const token = getAuthToken();
  return token;
}

export function checkAuthLoader() {
  const token = getAuthToken();

  if (!token) {
    return redirect('/auth');
  }
}

```

```jsx
// Root.js

import { useEffect } from 'react';
import { Outlet, useLoaderData, useSubmit } from 'react-router-dom';
import MainNavigation from '../components/MainNavigation';
import { getTokenDuration } from '../util/auth';

function RootLayout() {
  const token = useLoaderData();
  const submit = useSubmit();
  // const navigation = useNavigation();
  useEffect(() => {
    if (!token) {
      return;
    }

    if (token === 'EXPIRED') {
      submit(null, { action: '/logout', method: 'post' });
      return;
    }

    const tokenDuration = getTokenDuration();
    console.log(tokenDuration);

    setTimeout(() => {
      submit(null, { action: '/logout', method: 'post' });
    }, tokenDuration);
  }, [token, submit]);

  return (
    <>
      <MainNavigation />
      <main>
        {/* {navigation.state === 'loading' && <p>Loading...</p>} */}
        <Outlet />
      </main>
    </>
  );
}

export default RootLayout;

```

```jsx
// Logout.js

import { redirect } from 'react-router-dom';

export function action() {
  localStorage.removeItem('token');
  localStorage.removeItem('expiration');
  return redirect('/');
}

```

## Optimization and Deployment

---

### Lazy Loading

- Load code only when it's needed
- `import` returns `Promise`
- A function is only a valid component if it returns jsx code
  - Because `import` returns `Promise`, wrap it with `lazy()`
- Wrap the element with `<Suspense>` component
  - Show `fallback` property until the element is loaded
- Change `loader` to be executed after `import`

```jsx
import { lazy, Suspense } from 'react';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

// import BlogPage, { loader as postsLoader } from './pages/Blog';
import HomePage from './pages/Home';
// import PostPage, { loader as postLoader } from './pages/Post';
import RootLayout from './pages/Root';

const BlogPage = lazy(() => import('./pages/Blog'));
const PostPage = lazy(() => import('./pages/Post'));

const router = createBrowserRouter([
  {
    path: '/',
    element: <RootLayout />,
    children: [
      {
        index: true,
        element: <HomePage />,
      },
      {
        path: 'posts',
        children: [
          {
            index: true,
            element: (
              <Suspense fallback={<p>Loading...</p>}>
                <BlogPage />
              </Suspense>
            ),
            loader: () =>
              import('./pages/Blog').then((module) => module.loader()),
          },
          {
            path: ':id',
            element: (
              <Suspense fallback={<p>Loading...</p>}>
                <PostPage />
              </Suspense>
            ),
            loader: (meta) =>
              import('./pages/Post').then((module) => module.loader(meta)),
          },
        ],
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;

```
