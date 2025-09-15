# ERIFY™ Campaign Performance Reports Automation

Automated system for generating and distributing campaign performance reports using the engagement tracking dashboard. This Node.js application schedules daily and weekly report generation and sends summaries to designated ERIFY team members and stakeholders.

## Features

- **Automated Scheduling**: Daily and weekly report generation with configurable timing
- **Multi-Platform Data Collection**: Integrates with Google Analytics, social media APIs, and ERIFY dashboard
- **Comprehensive Metrics**: Tracks engagement, referrals, and user behavior
- **Smart Email Distribution**: Sends detailed reports to team and executive summaries to stakeholders
- **Error Handling**: Automated error notifications and robust error handling
- **HTML & Text Reports**: Professional HTML emails with plain text fallbacks

## Key Metrics Tracked

### Engagement
- Likes, comments, shares across Twitter/X, LinkedIn, Facebook
- ERIVOX platform interactions
- Engagement rates and trends

### Referrals
- UTM parameter tracking via Google Analytics
- Click-through rates and conversions
- Campaign performance analysis

### User Behavior
- Website analytics (page views, session duration, bounce rate)
- User journey analysis
- Conversion funnel metrics

## Installation

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and email settings
   ```

3. **Test the system**:
   ```bash
   npm test
   ```

## Configuration

### Email Settings
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASS=your-app-password

TEAM_EMAILS=team1@erify.com,team2@erify.com
STAKEHOLDER_EMAILS=stakeholder1@company.com,stakeholder2@company.com
```

### API Keys
```env
GOOGLE_ANALYTICS_API_KEY=your-ga-api-key
TWITTER_API_KEY=your-twitter-api-key
LINKEDIN_API_KEY=your-linkedin-api-key
FACEBOOK_API_KEY=your-facebook-api-key
ERIFY_API_KEY=your-erify-api-key
```

### Schedule Configuration
```env
DAILY_REPORT_TIME=09:00
WEEKLY_REPORT_DAY=monday
WEEKLY_REPORT_TIME=09:00
TIMEZONE=America/New_York
```

## Usage

### Start Scheduled Automation
```bash
npm start
```

### Generate Test Report
```bash
node src/app.js --test
```

### Development Mode (with file watching)
```bash
npm run dev
```

## Report Types

### Daily Reports
- **Audience**: ERIFY team + stakeholders
- **Content**: 24-hour performance metrics
- **Format**: Detailed team report + stakeholder summary
- **Delivery**: Every day at configured time

### Weekly Reports
- **Audience**: ERIFY team + executives
- **Content**: 7-day comprehensive analysis with trends
- **Format**: Full team report + executive summary
- **Delivery**: Weekly on configured day

## Email Recipients

### Team Members (Full Reports)
- Detailed metrics and technical data
- Error notifications and alerts
- Full API data and troubleshooting info

### Stakeholders (Executive Summaries)
- High-level performance indicators
- Key insights and recommendations
- Strategic growth metrics

## Data Sources Integration

Based on `ERIFY-Engagement-Tracking-Dashboard-Outline.md`:

### Google Analytics
- UTM parameter tracking for referral campaigns
- User behavior and conversion metrics
- Website performance data

### Social Media APIs
- **Twitter/X**: Engagement metrics, impressions, top-performing tweets
- **LinkedIn**: Professional network engagement, follower growth
- **Facebook**: Reach, engagement rates, post performance

### ERIFY Custom Dashboard
- ERIVOX platform metrics
- Internal campaign tracking
- Custom conversion events

## Error Handling

- **Graceful Degradation**: System continues if one data source fails
- **Error Notifications**: Team receives immediate alerts for system issues
- **Retry Logic**: Automatic retry for transient failures
- **Comprehensive Logging**: Detailed logs for troubleshooting

## Architecture

```
src/
├── app.js                 # Main application and scheduling
├── modules/
│   ├── dataCollector.js   # Multi-platform data collection
│   ├── reportGenerator.js # Report creation and formatting
│   └── emailNotifier.js   # Email distribution system
├── utils/
│   └── logger.js          # Logging utility
└── test.js               # Test suite
```

## Deployment

### Local Development
```bash
npm install
cp .env.example .env
# Configure .env
npm test
npm start
```

### Production Deployment
1. Set up production environment variables
2. Configure SMTP settings for email delivery
3. Set up API keys for all data sources
4. Deploy to server with process manager (PM2, Docker, etc.)
5. Configure monitoring and log aggregation

### GitHub Actions Integration
The existing GitHub Actions workflow can be extended to deploy the automation system:

```yaml
- name: Deploy Reports Automation
  run: |
    npm install --production
    # Set up production environment
    # Start automation service
```

## Monitoring

- **Health Checks**: Built-in system health monitoring
- **Email Delivery**: Confirmation of successful report delivery
- **API Status**: Monitoring of external API connections
- **Performance Metrics**: Report generation time and success rates

## Security

- **Environment Variables**: All credentials stored securely
- **Email Security**: SMTP with authentication
- **API Rate Limiting**: Respectful API usage patterns
- **Error Sanitization**: Sensitive data excluded from error reports

## Contributing

1. Fork the repository
2. Create a feature branch
3. Implement changes with tests
4. Submit pull request with detailed description

## Support

For questions or issues:
- Contact the ERIFY Team
- Check logs for troubleshooting
- Review API documentation for data sources

---

**ERIFY™ Campaign Performance Reports Automation**
*From the Ashes to the Stars ✨🔥💎*