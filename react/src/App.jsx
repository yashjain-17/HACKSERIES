app.jsx ;
import React, {useState} from 'react';

import Counter from './counter';
const App = () => {
  const [count, setCount] = useState(0);
  const addNumber = () => {
    setCounter(prevCounter => preCounter + 1);
    setCounter(prevCounter => prevCounter + 1);
    setCounter(prevcounter => prevCounter + 1);
    setCounter(prevCounter => prevCounter + 1);
  }
  const removeNumber = () => {
    setCounter(prev => prev - 1);
  }
  return (
    <>
      <Nav />
      <h1>Hackseries with React</h1>
      <Counter 
      counter={counter}
      addNumber={addNumber}
      removeNumber={removeNumber}
      />
    </>
  )
}
export default App;