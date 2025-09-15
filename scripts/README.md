# ERIFY Campaign Performance Reporting System

An automated system for generating and delivering daily and weekly campaign performance reports for ERIFY's marketing campaigns.

## 🚀 Features

- **Automated Daily Reports**: Daily engagement, referral, and user behavior metrics
- **Comprehensive Weekly Reports**: Weekly summaries with trends, demographics, and strategic insights
- **Multiple Delivery Methods**: Email and Slack integration
- **Platform Integration**: Twitter/X, LinkedIn, Facebook, ERIVOX, Google Analytics
- **Customizable Metrics**: Configurable tracking based on campaign goals
- **Alert System**: Performance threshold monitoring and notifications
- **Professional Templates**: Beautiful HTML email and Slack message templates

## 📊 Metrics Tracked

### Engagement Metrics
- Likes, comments, shares across all platforms
- Engagement rates and reach
- Top-performing content analysis
- Platform-specific performance comparison

### Referral & Conversion Metrics
- UTM campaign performance
- Click-through rates
- Conversion funnel analysis
- Revenue attribution
- ROI calculations

### User Behavior Analytics
- Session analytics and bounce rates
- User demographics and geographic distribution
- Device usage patterns
- Engagement timing and frequency

## 🛠 Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Access to social media platform APIs
- Google Analytics account
- SMTP server for email delivery
- Slack workspace with webhook access

### 2. Installation

```bash
# Clone the repository
git clone https://github.com/erify-world/erify-branding-supreme4.git
cd erify-branding-supreme4/scripts

# Install dependencies
pip install -r requirements.txt

# Copy environment configuration
cp .env.example .env
```

### 3. Configuration

Edit the `.env` file with your actual API keys and configuration:

```bash
# Configure data sources
GA_VIEW_ID=your_google_analytics_view_id
TWITTER_API_KEY=your_twitter_api_key
LINKEDIN_CLIENT_ID=your_linkedin_client_id
# ... (see .env.example for full configuration)

# Configure delivery methods
SMTP_USERNAME=your_email@company.com
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK
REPORT_EMAIL_RECIPIENTS=team@erify.com,analytics@erify.com
```

### 4. Testing

```bash
# Test daily report generation
cd reports
python generate_daily_report.py

# Test weekly report generation
python generate_weekly_report.py
```

## 📅 Automation Setup

### GitHub Actions (Recommended)

The system includes a pre-configured GitHub Actions workflow (`.github/workflows/campaign-reporting.yml`) that:

- Runs daily reports at 9:00 AM UTC
- Runs weekly reports at 10:00 AM UTC every Monday
- Allows manual triggering for testing

#### Configure Secrets

In your GitHub repository settings, add these secrets:

```
GA_VIEW_ID
TWITTER_API_KEY
TWITTER_BEARER_TOKEN
LINKEDIN_CLIENT_ID
LINKEDIN_CLIENT_SECRET
FACEBOOK_APP_ID
FACEBOOK_APP_SECRET
ERIFY_DASHBOARD_API
ERIFY_API_KEY
SMTP_SERVER
SMTP_USERNAME
SMTP_PASSWORD
REPORT_EMAIL_RECIPIENTS
SLACK_WEBHOOK_URL
```

### Manual Scheduling

For non-GitHub environments, use cron jobs:

```bash
# Daily reports at 9:00 AM
0 9 * * * cd /path/to/scripts/reports && python generate_daily_report.py

# Weekly reports at 10:00 AM every Monday
0 10 * * 1 cd /path/to/scripts/reports && python generate_weekly_report.py
```

## 📧 Report Delivery

### Email Reports

- **Format**: Professional HTML templates with embedded metrics
- **Attachments**: JSON data files for further analysis
- **Recipients**: Configurable list of stakeholders

### Slack Reports

- **Format**: Rich message blocks with key metrics
- **Channel**: Configurable channel (default: #campaign-reports)
- **Mentions**: Optional team mentions for important alerts

## 🎯 Campaign Integration

The reporting system is designed to work with ERIFY's existing tracking dashboard and supports:

### Current Campaigns
- Supreme 4PW Crown Seal launch
- VIP Referral Program
- Neon Crown Series
- ERIVOX platform growth

### UTM Tracking
- Automatic UTM parameter analysis
- Campaign source attribution
- Conversion path tracking

### Platform APIs
- Real-time data from social platforms
- Google Analytics integration
- Custom ERIFY dashboard metrics

## 📈 Sample Reports

### Daily Report Metrics
- Total daily engagement: 442 interactions
- Platform breakdown: Twitter (150), LinkedIn (89), Facebook (203)
- Conversions: 135 signups, 23 premium upgrades
- Top performing content identification

### Weekly Report Insights
- Weekly engagement trends and growth rates
- Demographic analysis and user behavior patterns
- Campaign performance comparison and ROI
- Strategic recommendations for optimization

## 🔧 Customization

### Adding New Metrics

1. Edit `config.yml` to add new metric categories
2. Implement data collection methods in the generator scripts
3. Update email/Slack templates to display new metrics

### Platform Integration

1. Add new platform configuration to `config.yml`
2. Implement platform-specific API methods
3. Update report templates with new platform data

### Alert Thresholds

Customize performance alerts in `config.yml`:

```yaml
alerts:
  engagement_drop_threshold: 15  # Alert if engagement drops by 15%
  conversion_rate_threshold: 2   # Alert if conversion rate drops below 2%
  traffic_spike_threshold: 50    # Alert if traffic increases by 50%
```

## 🔍 Troubleshooting

### Common Issues

1. **API Rate Limits**: Implement proper rate limiting and retry logic
2. **Email Delivery**: Check SMTP settings and app passwords
3. **Slack Integration**: Verify webhook URL and permissions
4. **Data Accuracy**: Validate API connections and data sources

### Log Files

Reports generate detailed logs for debugging:

```bash
# View recent logs
tail -f /var/log/erify-reports.log

# Debug mode
DEBUG_MODE=true python generate_daily_report.py
```

## 📋 Report Schedule

| Report Type | Frequency | Time (UTC) | Day | Content |
|------------|-----------|------------|-----|---------|
| Daily | Every day | 9:00 AM | All | Engagement, conversions, user behavior |
| Weekly | Weekly | 10:00 AM | Monday | Comprehensive analysis, trends, recommendations |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Test with sample data
5. Submit a pull request

## 📞 Support

For questions or issues:

- **Technical Support**: reports@erify.com
- **Dashboard Access**: dashboard.erify.com
- **Documentation**: github.com/erify-world/erify-branding-supreme4

## 📄 License

© 2025 ERIFY™. All rights reserved.

---

**Next Steps:**
1. Configure your API keys and delivery settings
2. Test report generation locally
3. Deploy automation workflow
4. Monitor and optimize based on team feedback