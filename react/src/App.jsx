import { useState } from 'react';
import Counter from './counter';

function App() {
  const [counter, setCounter] = useState(0);

  const addNumber = () => {
    setCounter((current) => current + 1);
  };

  const removeNumber = () => {
    setCounter((current) => current - 1);
  };

  return (
    <main>
      <h1>HackSeries React Counter</h1>
      <p>A small state-management exercise using React hooks.</p>
      <Counter
        counter={counter}
        addNumber={addNumber}
        removeNumber={removeNumber}
      />
    </main>
  );
}

export default App;
