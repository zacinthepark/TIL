import React from 'react'

interface GreeterProps {
  person: string
}

function Greeter(props: GreeterProps): JSX.Element {
  return <h1>Hello {props.person}!</h1>
}

// React Functional Component의 다른 선언법
// const Greeter: React.FC = () => {
//   return <h1>Hello!</h1>
// }

export default Greeter
