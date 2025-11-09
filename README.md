FinChatGPT — Local AI Finance Chat Assistant

A simple financial Q&A chatbot powered by Flask + Ollama (local LLM). It can answer finance, reasoning, and stock-market questions — including Apple stock analysis.

System Requirements
Your system must have:

🐍 Python 3.10 or above — Download

🧠 Ollama (for local AI model) — Download Ollama

🌐 An internet browser (Chrome / Edge)

💻 Minimum 8 GB RAM (for model loading)

Setup Steps Step 1 — Open folder in VS Code or Terminal cd "C:\Users<YourName>\finchatgpt"
Step 2 — Create and activate virtual environment python -m venv venv venv\Scripts\activate

Step 3 — Install dependencies pip install -r requirements.txt

Step 4 — Run Ollama in the background

(Keep this window open)

ollama serve

If you haven’t downloaded a model yet:

ollama pull llama3.2:1b

or use a lighter one if RAM is low:

ollama pull gemma:2b

Step 5 — Run the Flask app

Open a new terminal (keep Ollama running) and type:

python app.py

You should see something like:

Running on http://127.0.0.1:5000

Step 6 — Open in browser

Go to → http://127.0.0.1:5000

How to Use
Register with any username & password.

Login to open chat interface.

Ask anything, for example:

“What is ROI?”

“Explain Apple’s Q4 2024 performance.”

“What is the P/E ratio of Apple stock?”

“Compare Apple and Microsoft’s growth in the last 5 years.”

Troubleshooting Problem Solution ⚠️ “Ollama port already in use” Close all Ollama windows → open a new terminal → ollama serve again ❌ “127.0.0.1 refused to connect” Make sure Flask app is running (python app.py) 🧠 “Model requires more memory” Use lighter model ollama pull gemma:2b ⏳ “No response” Restart Ollama service & rerun Flask app 🔒 “Username already exists” Use a different username on registration

To Stop Everything

Press Ctrl + C in the Flask terminal to stop the server.

Press Ctrl + C in the Ollama terminal to stop the model.
