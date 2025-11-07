import React from 'react';
import Finance3D from './components/Finance3D';
import Chat from './components/Chat';

export default function App() {
  return (
    <div className="h-screen w-screen bg-gradient-to-br from-slate-900 via-indigo-900 to-sky-900 text-white overflow-hidden">
      <Finance3D />
      <div className="absolute inset-0 flex items-center justify-center">
        <div className="backdrop-blur-xl bg-white/10 border border-white/20 rounded-2xl shadow-2xl max-w-xl w-full mx-4 p-6">
          <h1 className="text-3xl font-bold mb-4 text-center tracking-wide">Fin-R1 Chatbot</h1>
          <p className="text-center text-sm mb-4 opacity-80">
            Ask financial questions and get responses powered by Fin-R1.
          </p>
          <Chat />
        </div>
      </div>
    </div>
  );
}
