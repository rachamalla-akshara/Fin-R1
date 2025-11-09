import subprocess

def route_message(user_input):
    """
    Routes user's question to Ollama and returns a response.
    """
    try:
        process = subprocess.run(
            ["ollama", "run", "llama3.2:1b"],
            input=user_input.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        output = process.stdout.decode("utf-8", errors="replace").strip()
        errors = process.stderr.decode("utf-8", errors="replace").strip()

        if not output:
            if errors:
                return {"think": "Ollama error", "answer": errors}
            return {"think": "No response", "answer": "Model did not respond."}

        return {"think": f"Analyzing '{user_input}'", "answer": output}

    except subprocess.TimeoutExpired:
        return {"think": "Timeout", "answer": "Model took too long to respond."}

    except Exception as e:
        return {"think": "Error", "answer": str(e)}
