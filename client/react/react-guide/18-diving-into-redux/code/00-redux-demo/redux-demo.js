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
