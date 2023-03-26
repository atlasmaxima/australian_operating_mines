import './App.css';
import React, { useState, useEffect } from 'react';
import Map from './Map';

function App() {
  const [marks, setMarks] = useState([]);
  const [googleMapApi, setGoogleMapApi] = useState('');

  useEffect(() => { 
    fetch('http://127.0.0.1:5000/')
    .then(response => response.json())
    .then(data => { 
      setMarks(data.marks);
    })
  }, []);

  useEffect(() => { 
    fetch('http://127.0.0.1:5000/config')
    .then(response => response.json())
    .then(data => {
      console.log(data.googleMapApi)
      setGoogleMapApi(data.google_map_api);
    })
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <Map marks={marks} googleMapApi={googleMapApi}/>
      </header>
    </div>
  );
}

export default App;
