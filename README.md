# Virtual Pet Simulator

A fun and interactive virtual pet simulator built with a React frontend and a Flask backend. The app allows users to manage a virtual pet, visit a store, and play mini-games. Users can register, log in, and interact with pets securely using JWT authentication.

## Table of Contents
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Technologies
- Frontend: **React**, **React Router**, **CSS**
- Backend: **Flask**, **Flask-SQLAlchemy**, **Flask-CORS**, **Flask-Bcrypt**, **Flask-JWT-Extended**, **SQLite**
- Authentication: **JWT**
- Environment: **Python**, **Node.js**, **npm**




### Important Notes:
1. **Environment Variables**: Make sure to create a `.env` file in your backend folder with the required variables like `SECRET_KEY` and `DATABASE_URI`. This will help configure the Flask backend securely.
2. **Backend Dependencies**: The backend dependencies should be in the `requirements.txt` file. This file should include:
   ```plaintext
   Flask
   Flask-CORS
   Flask-SQLAlchemy
   Flask-Bcrypt
   Flask-JWT-Extended
   python-dotenv
