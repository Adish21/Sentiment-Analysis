import React from 'react';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <h1>Adish Bahatkar</h1>
      </header>
      <main className="app-main">
        <div className="form-card">
          <h2>Let's analyze the News Today</h2>
          <form>
            <input type="text" placeholder="Paste the news link here" className="form-input" />
            <p>or</p>
            <input type="file" accept=".pdf,.png,.jpg" className="file-input" />
            <button type="submit" className="analyze-button">Analyze</button>
          </form>
        </div>
      </main>
    </div>
  );
}

export default App;
