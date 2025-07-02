import { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('https://stockview-h0hghsfjf6b8gthr.canadacentral-01.azurewebsites.net') // Update this if hosted elsewhere
      .then(res => res.json())
      .then(data => {
        setMessage(data["Hello!"]);
      })
      .catch(err => console.error('Error fetching:', err));
  }, []);

  return (
    <div>
      <h1>Stock Predictor</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
