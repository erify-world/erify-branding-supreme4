#!/usr/bin/env node

const fs = require('fs')
const path = require('path')

// Import sync modules
const syncGA4 = require('./sync-ga4')
const syncVideos = require('./sync-videos')

async function syncAllData() {
  console.log('🚀 Starting ERIFY Analytics Dashboard data sync...')
  console.log('⏰ Timestamp:', new Date().toISOString())
  
  const results = {
    analytics: null,
    videos: null,
    errors: []
  }

  try {
    // Sync GA4 Analytics Data
    console.log('\n📊 Syncing Google Analytics 4 data...')
    try {
      const analyticsData = await syncGA4()
      results.analytics = analyticsData
      console.log('✅ GA4 data sync completed successfully')
    } catch (error) {
      console.error('❌ GA4 data sync failed:', error.message)
      results.errors.push({ type: 'analytics', error: error.message })
    }

    // Sync Video Data
    console.log('\n🎬 Syncing video data from docs/video-previews.md...')
    try {
      const videosData = await syncVideos()
      results.videos = videosData
      console.log('✅ Video data sync completed successfully')
    } catch (error) {
      console.error('❌ Video data sync failed:', error.message)
      results.errors.push({ type: 'videos', error: error.message })
    }

    // Save sync log
    const logPath = path.join(__dirname, '..', 'public', 'sync-log.json')
    const logData = {
      lastSync: new Date().toISOString(),
      success: results.errors.length === 0,
      results: results,
      errors: results.errors
    }
    
    fs.writeFileSync(logPath, JSON.stringify(logData, null, 2))
    console.log('\n📝 Sync log saved to public/sync-log.json')

    // Summary
    console.log('\n📈 Sync Summary:')
    console.log(`   Analytics: ${results.analytics ? '✅ Success' : '❌ Failed'}`)
    console.log(`   Videos: ${results.videos ? '✅ Success' : '❌ Failed'}`)
    console.log(`   Total Errors: ${results.errors.length}`)
    
    if (results.errors.length > 0) {
      console.log('\n❌ Errors encountered:')
      results.errors.forEach((error, index) => {
        console.log(`   ${index + 1}. ${error.type}: ${error.error}`)
      })
      process.exit(1)
    } else {
      console.log('\n🎉 All data sync operations completed successfully!')
      process.exit(0)
    }

  } catch (error) {
    console.error('\n💥 Critical error during sync process:', error)
    process.exit(1)
  }
}

// Run if called directly
if (require.main === module) {
  syncAllData().catch(error => {
    console.error('💥 Unhandled error:', error)
    process.exit(1)
  })
}

module.exports = syncAllData