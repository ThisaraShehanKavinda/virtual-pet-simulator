import React from 'react';
import ReactDOM from 'react-dom/client'; // Import `createRoot` from `react-dom/client`
import App from './App';
import './styles/App.css';

// Create a root and render the app
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
