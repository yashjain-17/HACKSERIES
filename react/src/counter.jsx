function Counter({ counter, addNumber, removeNumber }) {
  return (
    <section aria-label="Counter controls">
      <h2>Counter value: {counter}</h2>
      <button type="button" onClick={addNumber}>
        Add one
      </button>
      <button type="button" onClick={removeNumber}>
        Remove one
      </button>
      <p>Current value: {counter}</p>
    </section>
  );
}

export default Counter;
