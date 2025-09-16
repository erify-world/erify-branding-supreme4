import React, { useState, useEffect } from 'react'
import StatCard from './StatCard'
import './AnalyticsPanel.css'

interface AnalyticsData {
  users: number
  sessions: number
  conversions: number
  videoClicks: number
  appOpens: number
  pageViews: number
  bounceRate: number
  sessionDuration: string
}

const AnalyticsPanel: React.FC = () => {
  const [data, setData] = useState<AnalyticsData | null>(null)
  const [loading, setLoading] = useState(true)
  const [lastUpdated, setLastUpdated] = useState<string>('')

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        setLoading(true)
        const response = await fetch('/analytics.json')
        if (response.ok) {
          const analyticsData = await response.json()
          setData(analyticsData)
          setLastUpdated(new Date().toLocaleString())
        } else {
          // Fallback to mock data if file doesn't exist yet
          setData({
            users: 15420,
            sessions: 18750,
            conversions: 847,
            videoClicks: 3240,
            appOpens: 1580,
            pageViews: 42350,
            bounceRate: 34.2,
            sessionDuration: '3m 24s'
          })
          setLastUpdated(new Date().toLocaleString())
        }
      } catch (error) {
        console.error('Failed to fetch analytics:', error)
        // Set mock data on error
        setData({
          users: 15420,
          sessions: 18750,
          conversions: 847,
          videoClicks: 3240,
          appOpens: 1580,
          pageViews: 42350,
          bounceRate: 34.2,
          sessionDuration: '3m 24s'
        })
        setLastUpdated(new Date().toLocaleString())
      } finally {
        setLoading(false)
      }
    }

    fetchAnalytics()
    
    // Refresh data every 5 minutes
    const interval = setInterval(fetchAnalytics, 5 * 60 * 1000)
    return () => clearInterval(interval)
  }, [])

  const formatNumber = (num: number): string => {
    if (num >= 1000000) {
      return (num / 1000000).toFixed(1) + 'M'
    }
    if (num >= 1000) {
      return (num / 1000).toFixed(1) + 'K'
    }
    return num.toString()
  }

  return (
    <div className="analytics-panel">
      <div className="analytics-panel__header">
        <h2 className="analytics-panel__title">
          📊 Analytics Overview
        </h2>
        <div className="analytics-panel__meta">
          <span className="analytics-panel__update-time">
            Last updated: {lastUpdated}
          </span>
          <button 
            className="analytics-panel__refresh-btn"
            onClick={() => window.location.reload()}
            disabled={loading}
          >
            🔄
          </button>
        </div>
      </div>

      <div className="analytics-panel__grid">
        <StatCard
          title="Total Users"
          value={data ? formatNumber(data.users) : '—'}
          change="+12.5%"
          changeType="positive"
          icon="👥"
          loading={loading}
        />
        
        <StatCard
          title="Sessions"
          value={data ? formatNumber(data.sessions) : '—'}
          change="+8.3%"
          changeType="positive"
          icon="🔥"
          loading={loading}
        />
        
        <StatCard
          title="Conversions"
          value={data ? formatNumber(data.conversions) : '—'}
          change="+15.7%"
          changeType="positive"
          icon="💎"
          loading={loading}
        />
        
        <StatCard
          title="Video Clicks"
          value={data ? formatNumber(data.videoClicks) : '—'}
          change="+22.1%"
          changeType="positive"
          icon="▶️"
          loading={loading}
        />
        
        <StatCard
          title="App Opens"
          value={data ? formatNumber(data.appOpens) : '—'}
          change="+9.4%"
          changeType="positive"
          icon="📱"
          loading={loading}
        />
        
        <StatCard
          title="Page Views"
          value={data ? formatNumber(data.pageViews) : '—'}
          change="+6.8%"
          changeType="positive"
          icon="📄"
          loading={loading}
        />
        
        <StatCard
          title="Bounce Rate"
          value={data ? `${data.bounceRate}%` : '—'}
          change="-2.3%"
          changeType="positive"
          icon="⚡"
          loading={loading}
        />
        
        <StatCard
          title="Avg. Session"
          value={data ? data.sessionDuration : '—'}
          change="+14s"
          changeType="positive"
          icon="⏱️"
          loading={loading}
        />
      </div>

      <div className="analytics-panel__footer">
        <div className="analytics-panel__powered-by">
          Powered by <span className="text-gradient">ERIFY™</span> Analytics Engine
        </div>
      </div>
    </div>
  )
}

export default AnalyticsPanel