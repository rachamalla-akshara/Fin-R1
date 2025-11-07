import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

// Replace with real Fin-R1 API call later
async function getFinR1Reply(prompt) {
  return `Fin-R1 backend simulated reply: "${prompt}"`;
}

app.post("/api/chat", async (req, res) => {
  try {
    const { prompt } = req.body;
    if (!prompt) return res.status(400).json({ error: "Missing prompt" });

    const answer = await getFinR1Reply(prompt);
    res.json({ answer });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () =>
  console.log(`✅ Backend running at http://localhost:${PORT}`)
);
