import React, {useState} from 'react';
// import Greeter from './components/Greeter';
import ShoppingList from './components/ShoppingList';
import ShoppingListForm from './components/ShoppingListForm';
import Item from './models/items';
import { v4 as getId } from 'uuid';
import './App.css';

function App() {
  const [items, setItems] = useState<Item[]>([])
  const addItem = (product: string, quantity: number) => {
    console.log('MADE IT TO THE APP COMPONENT!')
    setItems([...items, {id: getId(), product: product, quantity: quantity}])
  }
  // const items = [
  //   {id: 1, product: 'Lemon', quantity: 3},
  //   {id: 2, product: 'Chicken Breast', quantity: 2}
  // ]
  return (
    <div>
      <ShoppingList items={items} />
      <ShoppingListForm onAddItem={addItem} />
    </div>
  );
}

export default App;
