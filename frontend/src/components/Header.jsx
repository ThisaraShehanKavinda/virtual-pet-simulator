import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <h1>Virtual Pet Simulator</h1>
      <nav>
        <Link to="/">Pet</Link>
        <Link to="/store">Store</Link>
        <Link to="/mini-games">Mini-Games</Link>
      </nav>
    </header>
  );
};

export default Header;
