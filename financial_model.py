import subprocess

# ✅ This version automatically switches to a smaller model if your system runs out of memory
# Works fully offline with Ollama

def get_financial_response(prompt, category="General Finance"):
    """
    Generates a financial reasoning + answer using Ollama locally.
    If model fails to load due to memory limits, automatically switches to smaller model.
    """

    # 💡 Models to try from large → small
    MODEL_CANDIDATES = ["llama3.2:1b", "gemma:2b"]

    ollama_path = r"C:\Users\RCP\AppData\Local\Programs\Ollama\ollama.exe"

    for model in MODEL_CANDIDATES:
        try:
            # Build prompt with reasoning style
            reasoning_prompt = f"""
You are FinChatGPT, a financial reasoning assistant.
Answer only finance-related questions (code, professional, reasoning, or conceptual).
If the question is unrelated to finance, politely refuse.

Respond in the following XML-style format:
<think>Step-by-step reasoning or calculations here</think>
<answer>Final financial answer here</answer>

Question Category: {category}
User Question: {prompt}
"""

            # Run Ollama model locally
            result = subprocess.run(
                [ollama_path, "run", model],
                input=reasoning_prompt.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=90
            )

            output = result.stdout.decode("utf-8", errors="ignore").strip()
            error = result.stderr.decode("utf-8", errors="ignore").strip()

            # If Ollama returned a valid answer
            if "Error" not in output and len(output) > 0:
                return output

            # If model failed due to memory issue, try next smaller one
            if "model requires more system memory" in error or "Internal Server Error" in error:
                print(f"⚠️ Model {model} too large, switching to smaller one...")
                continue

            # Other errors
            if error:
                return f"<think>Error</think><answer>{error}</answer>"

        except subprocess.TimeoutExpired:
            return "<think>Timeout</think><answer>Response took too long to generate.</answer>"
        except Exception as e:
            return f"<think>Error</think><answer>{str(e)}</answer>"

    return "<think>Fallback</think><answer>All models failed to load. Please start Ollama or free memory.</answer>"
