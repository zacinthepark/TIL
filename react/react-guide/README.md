## React Guide

---

### Render UI & React to User Input
- Tasks
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
- Context Api
  - Solve props drilling
    - `React.createContext()`
    - `.Provider`, `value`
    - `.Consumer`, `useContext()`
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
