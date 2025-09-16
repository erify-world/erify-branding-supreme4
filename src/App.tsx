import React from 'react'
import AnalyticsPanel from './components/AnalyticsPanel'
import VideosPanel from './components/VideosPanel'
import './styles/App.css'

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <div className="header-content">
          <h1 className="app-title">
            <span className="erify-brand">ERIFY™</span> Analytics Dashboard
          </h1>
          <p className="app-subtitle">Real-time campaign performance & video recaps</p>
        </div>
      </header>
      
      <main className="app-main">
        <div className="dashboard-grid">
          <div className="analytics-section">
            <AnalyticsPanel />
          </div>
          <div className="videos-section">
            <VideosPanel />
          </div>
        </div>
      </main>
    </div>
  )
}

export default App