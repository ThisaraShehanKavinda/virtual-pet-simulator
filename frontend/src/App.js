import React from 'react';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import Header from './components/Header';
import MiniGames from './pages/MiniGames';
import Pet from './pages/Pet';
import Store from './pages/Store';
import './styles/App.css';

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path="/" element={<Pet />} />
        <Route path="/store" element={<Store />} />
        <Route path="/mini-games" element={<MiniGames />} />
      </Routes>
    </Router>
  );
}

export default App;
