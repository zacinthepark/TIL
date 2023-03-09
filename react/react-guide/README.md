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
      - `selectorFn(state managed by redux => part of the state you want to extract)`
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

- Extra package which makes working with Redux more convenient and easier
- Potential problems with Redux when managing more and more states
  1. Clashing between action type identifiers
    - Solution: `const INCREMENT = 'increment'` and export
  2. Have to copy a lot of states, making the reducer function longer, and making redux file unmaintainably big
    - Solution: splitting reducer into multiple smaller reducers
  3. Easy to accidentally change the existing state
    - Solution: Third-party packages that allow you to automatically copy state
- Redux Toolkit provides more convenient ways for the potential problems