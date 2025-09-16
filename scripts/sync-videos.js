const fs = require('fs')
const path = require('path')

async function syncVideosData() {
  console.log('🎬 Parsing video data from docs/video-previews.md...')
  
  const videosData = {
    videos: [],
    lastUpdated: new Date().toISOString(),
    totalVideos: 0,
    totalViews: 0,
    categories: [],
    featuredVideo: null
  }

  try {
    // Check if video-previews.md exists
    const videoPreviewsPath = path.join(__dirname, '..', 'docs', 'video-previews.md')
    
    if (!fs.existsSync(videoPreviewsPath)) {
      console.log('📝 docs/video-previews.md not found, creating sample file...')
      await createSampleVideoPreviewsFile(videoPreviewsPath)
    }

    // Read and parse the markdown file
    const markdownContent = fs.readFileSync(videoPreviewsPath, 'utf8')
    const videos = parseVideoMarkdown(markdownContent)
    
    // Calculate statistics
    const totalViews = videos.reduce((sum, video) => sum + video.views, 0)
    const categories = [...new Set(videos.map(video => video.category))]
    const featuredVideo = videos.length > 0 
      ? videos.reduce((prev, current) => (prev.views > current.views) ? prev : current)
      : null

    videosData.videos = videos
    videosData.totalVideos = videos.length
    videosData.totalViews = totalViews
    videosData.categories = categories
    videosData.featuredVideo = featuredVideo ? {
      id: featuredVideo.id,
      reason: 'Most viewed this week'
    } : null

    // Save to public directory
    const outputPath = path.join(__dirname, '..', 'public', 'latest-videos.json')
    fs.writeFileSync(outputPath, JSON.stringify(videosData, null, 2))
    
    console.log(`✅ Parsed ${videos.length} videos and saved to public/latest-videos.json`)
    console.log(`📊 Total views: ${totalViews.toLocaleString()}`)
    console.log(`📂 Categories: ${categories.join(', ')}`)
    
    return videosData

  } catch (error) {
    console.error('❌ Error parsing video data:', error.message)
    console.log('📝 Falling back to mock video data')
    return await generateMockVideoData()
  }
}

function parseVideoMarkdown(content) {
  const videos = []
  
  // Split content into sections by video entries
  const videoBlocks = content.split(/^##\s+/m).filter(block => block.trim())
  
  videoBlocks.forEach((block, index) => {
    try {
      const lines = block.split('\n').map(line => line.trim()).filter(line => line)
      
      if (lines.length === 0) return
      
      // Extract title (first line)
      const title = lines[0].replace(/^#+\s*/, '').trim()
      
      // Initialize video object with defaults
      const video = {
        id: generateVideoId(title),
        title: title,
        description: '',
        thumbnail: `/images/video-thumb-${index + 1}.jpg`,
        duration: '0:00',
        views: 0,
        publishedAt: new Date().toISOString(),
        url: '',
        category: 'general',
        tags: []
      }
      
      // Parse remaining lines for metadata
      lines.slice(1).forEach(line => {
        if (line.startsWith('**Description:**') || line.startsWith('Description:')) {
          video.description = line.replace(/^\*\*Description:\*\*|^Description:/, '').trim()
        } else if (line.startsWith('**Duration:**') || line.startsWith('Duration:')) {
          video.duration = line.replace(/^\*\*Duration:\*\*|^Duration:/, '').trim()
        } else if (line.startsWith('**Views:**') || line.startsWith('Views:')) {
          const viewsMatch = line.match(/[\d,]+/)
          video.views = viewsMatch ? parseInt(viewsMatch[0].replace(/,/g, '')) : 0
        } else if (line.startsWith('**URL:**') || line.startsWith('URL:')) {
          video.url = line.replace(/^\*\*URL:\*\*|^URL:/, '').trim()
        } else if (line.startsWith('**Category:**') || line.startsWith('Category:')) {
          video.category = line.replace(/^\*\*Category:\*\*|^Category:/, '').trim().toLowerCase()
        } else if (line.startsWith('**Tags:**') || line.startsWith('Tags:')) {
          const tagsText = line.replace(/^\*\*Tags:\*\*|^Tags:/, '').trim()
          video.tags = tagsText.split(',').map(tag => tag.trim()).filter(tag => tag)
        } else if (line.startsWith('**Published:**') || line.startsWith('Published:')) {
          const publishedText = line.replace(/^\*\*Published:\*\*|^Published:/, '').trim()
          video.publishedAt = new Date(publishedText).toISOString()
        } else if (!video.description && line.length > 20) {
          // Use longer lines as description if not explicitly set
          video.description = line
        }
      })
      
      // Generate mock data if missing
      if (!video.description) {
        video.description = generateVideoDescription(video.title, video.category)
      }
      
      if (!video.duration || video.duration === '0:00') {
        video.duration = generateVideoDuration()
      }
      
      if (video.views === 0) {
        video.views = generateVideoViews()
      }
      
      if (!video.url) {
        video.url = `https://youtube.com/watch?v=${generateVideoId(video.title)}`
      }
      
      videos.push(video)
      
    } catch (error) {
      console.warn(`⚠️ Failed to parse video block ${index + 1}:`, error.message)
    }
  })
  
  return videos
}

function generateVideoId(title) {
  return title
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .substring(0, 50)
}

function generateVideoDescription(title, category) {
  const descriptions = {
    launch: `Exclusive ${title.toLowerCase()} featuring luxury fintech innovations and VIP announcements.`,
    tutorial: `Complete walkthrough of ${title.toLowerCase()} with proven strategies and expert tips.`,
    highlights: `Best moments from ${title.toLowerCase()} featuring top participants and exclusive content.`,
    general: `Comprehensive overview of ${title.toLowerCase()} with detailed insights and analysis.`
  }
  
  return descriptions[category] || descriptions.general
}

function generateVideoDuration() {
  const minutes = Math.floor(Math.random() * 8) + 2 // 2-10 minutes
  const seconds = Math.floor(Math.random() * 60)
  return `${minutes}:${seconds.toString().padStart(2, '0')}`
}

function generateVideoViews() {
  return Math.floor(Math.random() * 20000) + 1000 // 1K-21K views
}

async function createSampleVideoPreviewsFile(filePath) {
  const sampleContent = `# ERIFY Video Previews

This file contains video recaps and previews for the ERIFY Analytics Dashboard.

## ERIFY Supreme 4 Launch Event
**Description:** Exclusive behind-the-scenes look at the Supreme 4 Crown Seal launch event featuring luxury fintech innovations and VIP announcements.
**Duration:** 4:32
**Views:** 15,420
**Category:** launch
**URL:** https://youtube.com/watch?v=erify-supreme4-launch
**Published:** 2025-01-15

## VIP Referral Program Deep Dive
**Description:** Complete walkthrough of the ERIFY VIP referral system, commission structures, and how to maximize your earnings with proven strategies.
**Duration:** 6:15
**Views:** 8,750
**Category:** tutorial
**URL:** https://youtube.com/watch?v=vip-referral-deep-dive
**Published:** 2025-01-14

## Luxury Fintech Challenge Highlights
**Description:** Best moments from our recent luxury fintech challenge featuring top participants, innovative solutions, and exclusive prizes.
**Duration:** 3:28
**Views:** 12,340
**Category:** highlights
**URL:** https://youtube.com/watch?v=luxury-fintech-challenge
**Published:** 2025-01-13

## Analytics Dashboard Tutorial
**Description:** Learn how to navigate and interpret your ERIFY analytics dashboard for maximum insights, tracking performance, and data-driven decisions.
**Duration:** 5:47
**Views:** 6,890
**Category:** tutorial
**URL:** https://youtube.com/watch?v=analytics-dashboard-tutorial
**Published:** 2025-01-12

## ERIFY Brand Evolution Journey
**Description:** The complete story of ERIFY's brand transformation from startup to luxury fintech powerhouse, featuring exclusive interviews and insights.
**Duration:** 7:23
**Views:** 9,650
**Category:** highlights
**URL:** https://youtube.com/watch?v=erify-brand-evolution
**Published:** 2025-01-11
`

  // Create docs directory if it doesn't exist
  const docsDir = path.dirname(filePath)
  if (!fs.existsSync(docsDir)) {
    fs.mkdirSync(docsDir, { recursive: true })
  }
  
  fs.writeFileSync(filePath, sampleContent)
  console.log('✅ Created sample docs/video-previews.md file')
}

async function generateMockVideoData() {
  console.log('📊 Generating mock video data...')
  
  const mockVideos = [
    {
      id: 'erify-supreme4-launch',
      title: 'ERIFY Supreme 4 Launch Event',
      description: 'Exclusive behind-the-scenes look at the Supreme 4 Crown Seal launch event featuring luxury fintech innovations.',
      thumbnail: '/images/video-thumb-1.jpg',
      duration: '4:32',
      views: 15420,
      publishedAt: new Date(Date.now() - 24 * 60 * 60 * 1000).toISOString(),
      url: 'https://youtube.com/watch?v=erify-supreme4-launch',
      category: 'launch',
      tags: ['launch', 'supreme4', 'crown-seal']
    },
    {
      id: 'vip-referral-deep-dive',
      title: 'VIP Referral Program Deep Dive',
      description: 'Complete walkthrough of the ERIFY VIP referral system and commission structures.',
      thumbnail: '/images/video-thumb-2.jpg',
      duration: '6:15',
      views: 8750,
      publishedAt: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(),
      url: 'https://youtube.com/watch?v=vip-referral-deep-dive',
      category: 'tutorial',
      tags: ['referral', 'vip', 'tutorial']
    }
  ]
  
  const videosData = {
    videos: mockVideos,
    lastUpdated: new Date().toISOString(),
    totalVideos: mockVideos.length,
    totalViews: mockVideos.reduce((sum, video) => sum + video.views, 0),
    categories: ['launch', 'tutorial', 'highlights'],
    featuredVideo: {
      id: 'erify-supreme4-launch',
      reason: 'Most viewed this week'
    }
  }
  
  const outputPath = path.join(__dirname, '..', 'public', 'latest-videos.json')
  fs.writeFileSync(outputPath, JSON.stringify(videosData, null, 2))
  
  console.log('✅ Mock video data saved to public/latest-videos.json')
  return videosData
}

module.exports = syncVideosData