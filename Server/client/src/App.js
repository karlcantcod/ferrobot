import "./App.css";
import React, { useState, useEffect } from "react";
import { getAssistantStatus, checkApiHealth } from "./apiService/apiConnection";

function App() {
  const [assistantStatus, setAssistantStatus] = useState(null);
  const [apiHealth, setApiHealth] = useState({ status: "loading" });

  useEffect(() => {
    const fetchStatus = async () => {
      const status = await getAssistantStatus();
      setAssistantStatus(status);
    };

    const fetchApiHealth = async () => {
      const health = await checkApiHealth();
      setApiHealth(health);
    };

    fetchStatus();
    fetchApiHealth();
  }, []);

  return (
    <div className="App">
      <h1>Ferro world</h1>
      <h2>API Logs</h2>
      <div>
        <h3>Assistant Status:</h3>
        {assistantStatus ? (
          <pre>{JSON.stringify(assistantStatus, null, 2)}</pre>
        ) : (
          <p>Loading assistant status...</p>
        )}
      </div>
      <div>
        <h3>API Health:</h3>
        <p>Status: {apiHealth.status}</p>
      </div>
    </div>
  );
}

export default App;
