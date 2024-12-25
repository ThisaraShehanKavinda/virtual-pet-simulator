import React, { useEffect, useState } from 'react';
import '../styles/Store.css';

const Store = () => {
  // State to hold the store items
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  // Fetch data from backend when component mounts
  useEffect(() => {
    fetch('http://127.0.0.1:5000/api/store')
      .then(response => response.json())
      .then(data => {
        setItems(data);  // Set the store items
        setLoading(false); // Set loading to false once data is fetched
      })
      .catch(error => {
        console.error('Error fetching store items:', error);
        setLoading(false);  // Stop loading in case of error
      });
  }, []); // Empty dependency array means this will run only once when the component mounts

  // Render the store items
  return (
    <div className="store-container">
      <h2>Item Store</h2>
      {loading ? (
        <p>Loading...</p> // Show loading message while fetching data
      ) : (
        <div className="store-items">
          {items.length > 0 ? (
            items.map(item => (
              <div key={item.id} className="store-item">
                <h3>{item.name}</h3>
                <p>Price: {item.price} coins</p>
              </div>
            ))
          ) : (
            <p>No items available in the store.</p> // Display message if no items
          )}
        </div>
      )}
    </div>
  );
};

export default Store;
