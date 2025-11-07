import React, { useState, useEffect, useRef } from 'react';

export default function Chat() {
  const [messages, setMessages] = useState(() => {
    try { return JSON.parse(localStorage.getItem('finr1_chat')) || []; } catch { return []; }
  });
  const [input, setInput] = useState('');
  const messagesRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('finr1_chat', JSON.stringify(messages));
    messagesRef.current?.scrollTo({ top: messagesRef.current.scrollHeight, behavior: 'smooth' });
  }, [messages]);

  function addMessage(from, text) {
    setMessages(prev => [...prev, { from, text, time: new Date().toISOString() }]);
  }

  async function handleSend(e) {
    e?.preventDefault();
    if (!input.trim()) return;

    const text = input.trim();
    addMessage('User', text);
    setInput('');
    addMessage('Fin-R1', '…thinking');

    try {
      const response = await fetch("http://localhost:5000/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: text }),
      });
      const data = await response.json();
      setMessages(prev => prev.map(m =>
        m.text === '…thinking' ? { ...m, text: data.answer } : m
      ));
    } catch {
      setMessages(prev => prev.map(m =>
        m.text === '…thinking' ? { ...m, text: '⚠️ Error connecting to backend' } : m
      ));
    }
  }

  function clearChat() {
    setMessages([]);
    localStorage.removeItem('finr1_chat');
  }

  return (
    <div className="flex flex-col h-[60vh]">
      <div ref={messagesRef} className="flex-1 overflow-auto p-3 space-y-3 rounded border border-white/10 bg-gradient-to-b from-white/5 to-transparent">
        {messages.length === 0 && <div className="text-sm opacity-70">Start chatting with Fin-R1…</div>}
        {messages.map((m, i) => (
          <div key={i} className={`p-3 rounded-lg max-w-[85%] ${m.from==='User' ? 'bg-indigo-600 ml-auto text-right' : 'bg-white/10 text-left'}`}>
            <div className="text-xs opacity-80">{m.from}</div>
            <div className="text-sm whitespace-pre-wrap">{m.text}</div>
          </div>
        ))}
      </div>
      <form onSubmit={handleSend} className="mt-3 flex gap-2">
        <input value={input} onChange={(e)=>setInput(e.target.value)} placeholder="Type your message..." className="flex-1 p-2 rounded bg-white/10 text-sm" />
        <button type="submit" className="px-4 py-2 rounded bg-sky-500 hover:bg-sky-600">Send</button>
        <button type="button" onClick={clearChat} className="px-4 py-2 rounded bg-red-500 hover:bg-red-600">Clear</button>
      </form>
    </div>
  );
}
