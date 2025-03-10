// 1️⃣ Load environment variables
require("dotenv").config();

// 2️⃣ Import required modules
const express = require("express");
const cors = require("cors");
const { GoogleGenerativeAI } = require("@google/generative-ai");

// 3️⃣ Initialize Express app
const app = express();

// 4️⃣ Middleware setup
app.use(cors());
app.use(express.json());

// 5️⃣ Initialize Gemini AI
const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY); // Ensure correct API key

const MODEL_NAME = "gemini-1.5-pro"; // Use Gemini Pro for better results

// 6️⃣ Define the root route
app.get("/", (req, res) => {
    res.send("Server is running...");
});

// 7️⃣ Generate Logo Endpoint
app.post("/generate-logo", async (req, res) => {
    try {
        const { prompt } = req.body;
        const model = genAI.getGenerativeModel({ model: MODEL_NAME });

        const result = await model.generateContent({
            contents: [{ role: "user", parts: [{ text: `Create an SVG-based logo for: ${prompt}` }] }]
        });

        let response = result.response.candidates[0].content.parts[0].text;

        // ✅ Remove Markdown formatting (```xml ... ```) if present
        response = response.replace(/```xml|```/g, "").trim();

        res.json({ logoSvg: response }); // ✅ Send raw SVG as response
    } catch (error) {
        console.error("Error generating logo:", error);
        res.status(500).json({ error: "Failed to generate logo", details: error.message });
    }
});


// 8️⃣ Start the server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`🚀 Server is running on http://localhost:${PORT}`);
});
