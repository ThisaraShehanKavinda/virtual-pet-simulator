import React from 'react';
import '../styles/ActionButton.css';

const ActionButton = ({ label, onClick }) => {
  return (
    <button className="action-button" onClick={onClick}>
      {label}
    </button>
  );
};

export default ActionButton;
