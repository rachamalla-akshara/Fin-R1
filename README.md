# Fin-R1 Chatbot UI (Full Project)

This project contains:
- Frontend (React + Vite + Tailwind + Three.js background)
- Backend (Node.js + Express API)

## Run instructions

### Backend
```bash
cd server
npm install
npm start
```
Runs on http://localhost:5000

### Frontend
```bash
cd ..
npm install
npm run dev
```
Runs on http://localhost:5173

## Usage
- Type messages in the chat window, they are sent to backend `/api/chat`.
- Backend currently simulates responses; replace logic in `server/index.js` to call your Fin-R1 model.
