import React from 'react';
import '../styles/PetStats.css';

const PetStats = ({ stats }) => {
  return (
    <div className="pet-stats">
      <p>Health: {stats.health}</p>
      <p>Happiness: {stats.happiness}</p>
      <p>Energy: {stats.energy}</p>
    </div>
  );
};

export default PetStats;
