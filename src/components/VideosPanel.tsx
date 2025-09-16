import React, { useState, useEffect } from 'react'
import './VideosPanel.css'

interface VideoData {
  id: string
  title: string
  description: string
  thumbnail: string
  duration: string
  views: number
  publishedAt: string
  url: string
  category: string
}

const VideosPanel: React.FC = () => {
  const [videos, setVideos] = useState<VideoData[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedCategory, setSelectedCategory] = useState<string>('all')

  useEffect(() => {
    const fetchVideos = async () => {
      try {
        setLoading(true)
        const response = await fetch('/latest-videos.json')
        if (response.ok) {
          const videoData = await response.json()
          setVideos(videoData.videos || [])
        } else {
          // Fallback to mock data
          setVideos([
            {
              id: '1',
              title: 'ERIFY Supreme 4 Launch Event',
              description: 'Exclusive behind-the-scenes look at the Supreme 4 Crown Seal launch event featuring luxury fintech innovations.',
              thumbnail: '/images/video-thumb-1.jpg',
              duration: '4:32',
              views: 15420,
              publishedAt: '2025-01-15T10:30:00Z',
              url: 'https://youtube.com/watch?v=example1',
              category: 'launch'
            },
            {
              id: '2',
              title: 'VIP Referral Program Deep Dive',
              description: 'Complete walkthrough of the ERIFY VIP referral system and how to maximize your earnings.',
              thumbnail: '/images/video-thumb-2.jpg',
              duration: '6:15',
              views: 8750,
              publishedAt: '2025-01-14T15:45:00Z',
              url: 'https://youtube.com/watch?v=example2',
              category: 'tutorial'
            },
            {
              id: '3',
              title: 'Luxury Fintech Challenge Highlights',
              description: 'Best moments from our recent luxury fintech challenge featuring top participants.',
              thumbnail: '/images/video-thumb-3.jpg',
              duration: '3:28',
              views: 12340,
              publishedAt: '2025-01-13T09:20:00Z',
              url: 'https://youtube.com/watch?v=example3',
              category: 'highlights'
            },
            {
              id: '4',
              title: 'Analytics Dashboard Tutorial',
              description: 'Learn how to navigate and interpret your ERIFY analytics dashboard for maximum insights.',
              thumbnail: '/images/video-thumb-4.jpg',
              duration: '5:47',
              views: 6890,
              publishedAt: '2025-01-12T14:10:00Z',
              url: 'https://youtube.com/watch?v=example4',
              category: 'tutorial'
            }
          ])
        }
      } catch (error) {
        console.error('Failed to fetch videos:', error)
        setVideos([])
      } finally {
        setLoading(false)
      }
    }

    fetchVideos()
  }, [])

  const formatViews = (views: number): string => {
    if (views >= 1000000) {
      return (views / 1000000).toFixed(1) + 'M'
    }
    if (views >= 1000) {
      return (views / 1000).toFixed(1) + 'K'
    }
    return views.toString()
  }

  const formatDate = (dateString: string): string => {
    const date = new Date(dateString)
    const now = new Date()
    const diffTime = Math.abs(now.getTime() - date.getTime())
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))
    
    if (diffDays === 0) return 'Today'
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    return date.toLocaleDateString()
  }

  const categories = ['all', 'launch', 'tutorial', 'highlights']
  
  const filteredVideos = selectedCategory === 'all' 
    ? videos 
    : videos.filter(video => video.category === selectedCategory)

  return (
    <div className="videos-panel">
      <div className="videos-panel__header">
        <h2 className="videos-panel__title">
          🎬 Video Recaps
        </h2>
        
        <div className="videos-panel__filters">
          {categories.map(category => (
            <button
              key={category}
              className={`videos-panel__filter ${selectedCategory === category ? 'videos-panel__filter--active' : ''}`}
              onClick={() => setSelectedCategory(category)}
            >
              {category.charAt(0).toUpperCase() + category.slice(1)}
            </button>
          ))}
        </div>
      </div>

      <div className="videos-panel__content">
        {loading ? (
          <div className="videos-panel__loading">
            {[...Array(4)].map((_, index) => (
              <div key={index} className="video-card video-card--loading">
                <div className="video-card__thumbnail-skeleton"></div>
                <div className="video-card__content">
                  <div className="video-card__skeleton-line video-card__skeleton-line--title"></div>
                  <div className="video-card__skeleton-line video-card__skeleton-line--description"></div>
                  <div className="video-card__skeleton-line video-card__skeleton-line--meta"></div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="videos-panel__grid">
            {filteredVideos.map((video, index) => (
              <div 
                key={video.id} 
                className="video-card"
                style={{ animationDelay: `${index * 0.1}s` }}
                onClick={() => window.open(video.url, '_blank')}
              >
                <div className="video-card__thumbnail">
                  <div className="video-card__thumbnail-placeholder">
                    🎥
                  </div>
                  <div className="video-card__duration">{video.duration}</div>
                  <div className="video-card__play-overlay">
                    <div className="video-card__play-button">▶</div>
                  </div>
                </div>
                
                <div className="video-card__content">
                  <h3 className="video-card__title">{video.title}</h3>
                  <p className="video-card__description">{video.description}</p>
                  
                  <div className="video-card__meta">
                    <span className="video-card__views">
                      👁️ {formatViews(video.views)} views
                    </span>
                    <span className="video-card__date">
                      📅 {formatDate(video.publishedAt)}
                    </span>
                  </div>
                </div>
              </div>
            ))}
            
            {filteredVideos.length === 0 && !loading && (
              <div className="videos-panel__empty">
                <div className="videos-panel__empty-icon">🎬</div>
                <p className="videos-panel__empty-text">
                  No videos found for the selected category
                </p>
              </div>
            )}
          </div>
        )}
      </div>

      <div className="videos-panel__footer">
        <div className="videos-panel__powered-by">
          Powered by <span className="text-gradient">ERIFY™</span> Video Engine
        </div>
      </div>
    </div>
  )
}

export default VideosPanel