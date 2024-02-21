import React from "react";
import Item from '../models/items'

interface ShoppingListProps {
  items: Item[]
}

function ShoppingList(props: ShoppingListProps): JSX.Element {
  return (
    <div>
      <h1>Shopping List</h1>
      {props.items && <ul>
        {props.items.map((item) => (
          <li key={item.id}>{item.product} - {item.quantity}</li>
        ))}
      </ul>}
    </div>
  )
}

export default ShoppingList
