const express = require('express')
const path = require('path')
const fs = require('fs')

const app = express()
const PORT = process.env.PORT || 3001

// Middleware for CORS and JSON parsing
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*')
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
  next()
})

app.use(express.json())
app.use(express.static('public'))

// Serve static files from dist during production
if (process.env.NODE_ENV === 'production') {
  app.use(express.static('dist'))
}

// API Routes
app.get('/api/analytics', (req, res) => {
  try {
    const analyticsPath = path.join(__dirname, 'public', 'analytics.json')
    if (fs.existsSync(analyticsPath)) {
      const data = fs.readFileSync(analyticsPath, 'utf8')
      res.json(JSON.parse(data))
    } else {
      // Return mock data if file doesn't exist
      res.json({
        users: 15420,
        sessions: 18750,
        conversions: 847,
        videoClicks: 3240,
        appOpens: 1580,
        pageViews: 42350,
        bounceRate: 34.2,
        sessionDuration: '3m 24s',
        lastUpdated: new Date().toISOString()
      })
    }
  } catch (error) {
    console.error('Error reading analytics data:', error)
    res.status(500).json({ error: 'Failed to fetch analytics data' })
  }
})

app.get('/api/videos', (req, res) => {
  try {
    const videosPath = path.join(__dirname, 'public', 'latest-videos.json')
    if (fs.existsSync(videosPath)) {
      const data = fs.readFileSync(videosPath, 'utf8')
      res.json(JSON.parse(data))
    } else {
      // Return mock data if file doesn't exist
      res.json({
        videos: [
          {
            id: '1',
            title: 'ERIFY Supreme 4 Launch Event',
            description: 'Exclusive behind-the-scenes look at the Supreme 4 Crown Seal launch event.',
            thumbnail: '/images/video-thumb-1.jpg',
            duration: '4:32',
            views: 15420,
            publishedAt: new Date().toISOString(),
            url: 'https://youtube.com/watch?v=example1',
            category: 'launch'
          }
        ],
        lastUpdated: new Date().toISOString()
      })
    }
  } catch (error) {
    console.error('Error reading videos data:', error)
    res.status(500).json({ error: 'Failed to fetch videos data' })
  }
})

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ 
    status: 'healthy', 
    timestamp: new Date().toISOString(),
    service: 'ERIFY Analytics Dashboard API'
  })
})

// Serve React app for all other routes (SPA support)
app.get('*', (req, res) => {
  if (process.env.NODE_ENV === 'production') {
    res.sendFile(path.join(__dirname, 'dist', 'index.html'))
  } else {
    res.status(404).json({ 
      error: 'Development mode - use Vite dev server for React app',
      suggestion: 'Run: npm run dev'
    })
  }
})

// Error handling middleware
app.use((error, req, res, next) => {
  console.error('Server error:', error)
  res.status(500).json({ 
    error: 'Internal server error',
    message: process.env.NODE_ENV === 'development' ? error.message : 'Something went wrong'
  })
})

// Start server
app.listen(PORT, () => {
  console.log(`🚀 ERIFY Analytics Dashboard API running on port ${PORT}`)
  console.log(`📊 Analytics endpoint: http://localhost:${PORT}/api/analytics`)
  console.log(`🎬 Videos endpoint: http://localhost:${PORT}/api/videos`)
  console.log(`❤️ Health check: http://localhost:${PORT}/api/health`)
  
  if (process.env.NODE_ENV !== 'production') {
    console.log(`\n💡 For development, also run: npm run dev`)
    console.log(`   This will start the Vite dev server for React`)
  }
})

module.exports = app