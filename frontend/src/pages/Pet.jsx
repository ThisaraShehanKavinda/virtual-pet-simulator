import React, { useEffect, useState } from 'react';
import petImage from '../assets/pet.png';
import ActionButton from '../components/ActionButton';
import PetStats from '../components/PetStats';
import './Pet.css';

const Pet = () => {
  const [petStats, setPetStats] = useState({
    health: 100,
    happiness: 100,
    energy: 100,
  });

  useEffect(() => {
    // Example: Fetch stats from backend
  }, []);

  const handleAction = (actionType) => {
    setPetStats((prevStats) => {
      const newStats = { ...prevStats };
      if (actionType === 'feed') newStats.health += 10;
      if (actionType === 'play') newStats.happiness += 10;
      if (actionType === 'rest') newStats.energy += 10;
      return newStats;
    });
  };

  return (
    <div className="pet-container">
      <h2>Your Pet</h2>
      <img src={petImage} alt="Virtual Pet" className="pet-image" />
      <PetStats stats={petStats} />
      <div className="actions">
        <ActionButton label="Feed" onClick={() => handleAction('feed')} />
        <ActionButton label="Play" onClick={() => handleAction('play')} />
        <ActionButton label="Rest" onClick={() => handleAction('rest')} />
      </div>
    </div>
  );
};

export default Pet;
