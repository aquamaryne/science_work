import React from 'react';
import { QozFormData } from './interface/qoz';
import Qoz from './components/qozForm';
import { QmzFormData } from './interface/qmz';
import Qmz from './components/qmzForm';

function App() {
  const [qozResult, setQozResult] = React.useState<number | null>(null);
  const [qmzResult, setQmzResult] = React.useState<number | null>(null);

  const handleQozSubmit = async(formData: QozFormData) => {
    const responce = await fetch('http://127.0.0.1:5000/api/calculate_qoz', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });

    const data = await responce.json();
    setQozResult(data.Qoz)
  }

  const handleQmzSubmit = async(formData: QmzFormData) => {
    const responce = await fetch('http://127.0.0.1:5000/api/calculate_qmz', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    });

    const data = await responce.json();
    setQozResult(data.QMZ)
  }

  return (
    <div>
      <h1>Calculate QOZ</h1>
      <Qoz onSubmit={handleQozSubmit} />
      { qozResult !== null && <p>Result: {qozResult}</p>}

      <h1>Calculate QMZ</h1>
      <Qmz onSubmit={handleQmzSubmit} />
      { qmzResult !== null && <p>Result: {qmzResult}</p>}
    </div>
  );
}

export default App;
