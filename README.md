# ERIFY™ Analytics Dashboard

Real-time analytics and video recaps dashboard for ERIFY campaigns, built with React + Vite and luxury dark branding.

## 🚀 Features

- **Real-time Analytics**: GA4 metrics (Users, Sessions, Conversions) and custom events
- **Video Recaps**: Automatically parsed from `docs/video-previews.md`
- **Luxury Dark Branding**: Deep gradients, gold accents, subtle animations
- **Split View Layout**: Analytics on the left, video recaps on the right
- **Automated Data Sync**: GitHub Action updates data hourly
- **Cloudflare Pages Deployment**: Optimized for fast global delivery

## 📊 Dashboard Components

### Analytics Panel
- Total Users, Sessions, Conversions
- Custom Events (Video Clicks, App Opens)
- Page Views, Bounce Rate, Session Duration
- Real-time data refresh every 5 minutes

### Videos Panel
- Video recaps with thumbnails and metadata
- Category filtering (Launch, Tutorial, Highlights)
- View counts and publication dates
- Direct links to video content

## 🛠️ Development

### Prerequisites
- Node.js 18+
- npm or yarn

### Local Development
```bash
# Install dependencies
npm install

# Start development server (React + Vite)
npm run dev

# Start Express API server (optional)
npm run server

# Sync data manually
npm run sync-data
```

### Building for Production
```bash
# Build the React app
npm run build

# Preview production build
npm run preview
```

## 🔧 Configuration

### Google Analytics 4 Integration
Set up the following GitHub secrets for GA4 data sync:

- `GA4_PROPERTY_ID`: Your GA4 property ID
- `GA4_SERVICE_ACCOUNT_JSON`: Service account credentials JSON

### Cloudflare Pages Deployment
Configure these secrets for automatic deployment:

- `CLOUDFLARE_API_TOKEN`: Cloudflare API token
- `CLOUDFLARE_ACCOUNT_ID`: Your Cloudflare account ID

## 📹 Video Management

Videos are managed through `docs/video-previews.md`. Add new videos using this format:

```markdown
## Video Title
**Description:** Video description
**Duration:** 5:30
**Views:** 1,250
**Category:** tutorial
**URL:** https://youtube.com/watch?v=example
**Published:** 2025-01-15
**Tags:** tag1, tag2, tag3
```

The GitHub Action automatically parses this file and updates `public/latest-videos.json`.

## 🔄 Automated Data Sync

The dashboard uses a GitHub Action (`.github/workflows/dashboard-sync.yaml`) that:

- Runs hourly to sync fresh data
- Can be triggered manually with different sync types
- Fetches GA4 metrics via the Google Analytics Data API
- Parses video data from the markdown file
- Commits updated JSON files to the repository

## 🎨 Branding

The dashboard features ERIFY's luxury dark branding:

- **Colors**: Deep gradients (#0A0B0F to #1A1B23), cyan (#11C9FF), gold (#FFD700)
- **Typography**: Inter font family with gradient text effects
- **Animations**: Subtle hover effects, loading states, slide-in animations
- **Layout**: Responsive grid system with mobile-first approach

## 📱 Responsive Design

Fully responsive design that works on:
- Desktop (1400px+ optimal)
- Tablet (768px - 1024px)
- Mobile (320px - 768px)

## 🚀 Deployment

### Cloudflare Pages (Recommended)
1. Connect your GitHub repository to Cloudflare Pages
2. Set build command: `npm run build`
3. Set output directory: `dist`
4. Configure environment variables for GA4 integration

### Manual Deployment
```bash
npm run build
# Deploy the `dist` folder to your hosting provider
```

## 📊 Data Structure

### Analytics Data (`public/analytics.json`)
```json
{
  "users": 15420,
  "sessions": 18750,
  "conversions": 847,
  "videoClicks": 3240,
  "appOpens": 1580,
  "pageViews": 42350,
  "bounceRate": 34.2,
  "sessionDuration": "3m 24s",
  "lastUpdated": "2025-01-16T10:30:00Z"
}
```

### Video Data (`public/latest-videos.json`)
```json
{
  "videos": [...],
  "totalVideos": 6,
  "totalViews": 63280,
  "categories": ["launch", "tutorial", "highlights"],
  "lastUpdated": "2025-01-16T10:30:00Z"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add videos to `docs/video-previews.md` or update components
4. Test your changes locally
5. Submit a pull request

## 📄 License

© 2025 ERIFY™. All rights reserved.

---

## Alternate Visuals — ERIFY™ Neon Crown Series

This section includes the latest visuals and improvements for the ERIFY™ Neon Crown Series. The analytics dashboard complements these branding assets with real-time performance tracking.