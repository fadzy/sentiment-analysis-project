import React, { useState } from "react";
import axios from "axios";
import "./styles.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const analyzeSentiment = async () => {
    if (!text) return;

    try {
      // Send the text to the Flask API with the correct format (tweet)
      const response = await axios.post("http://127.0.0.1:5000/analyze", { tweet: text });
      
      // Set the result in the state
      setResult(response.data);
    } catch (error) {
      console.error("Error during sentiment analysis:", error);
    }
  };

  return (
    <div className="container">
      <h1>Tweet Sentiment Analyzer</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter a tweet..."
        rows="5" // Make it bigger for more text
      />
      <button onClick={analyzeSentiment}>Analyze</button>

      {result && (
        <div className="result">
          <h3>Sentiment: {result.sentiment}</h3>
          <p>{result.error || "Sentiment analysis was successful!"}</p>
        </div>
      )}
    </div>
  );
}

export default App;
