# ERIFY™ Campaign Performance Reporting System

## Overview

Automated scheduling and generation of campaign performance reports for ERIFY's marketing campaigns. This system tracks engagement metrics from social media platforms (Twitter/X, LinkedIn, Facebook, ERIVOX) and UTM tracking data from Google Analytics to provide comprehensive performance insights.

## Features

- **Automated Report Generation**: Daily, weekly, and monthly reports
- **Multi-Platform Data Collection**: 
  - Google Analytics (UTM tracking, conversions, sessions)
  - Twitter/X (engagement metrics, reach)
  - LinkedIn (professional engagement)
  - Facebook (social media reach)
  - ERIVOX (platform-specific metrics)
- **Professional HTML Reports**: Beautiful, branded email reports
- **Alert System**: Performance drop notifications
- **Flexible Scheduling**: Configurable report timing
- **GitHub Actions Integration**: Fully automated via CI/CD

## Quick Start

### 1. Installation

```bash
cd scripts
pip install -r requirements.txt
```

### 2. Configuration

Copy the example configuration file:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys and email configuration:
```bash
# Required for UTM tracking
GA_API_KEY=your_google_analytics_api_key
GA_VIEW_ID=your_ga_view_id

# Social media APIs (optional but recommended)
TWITTER_API_KEY=your_twitter_api_key
LINKEDIN_API_KEY=your_linkedin_api_key
FACEBOOK_API_KEY=your_facebook_api_key

# Email delivery
EMAIL_USER=your_email@example.com
EMAIL_PASSWORD=your_app_password
```

### 3. Generate Manual Report

Test the system by generating a manual report:
```bash
python campaign_reports.py report daily
```

### 4. Start Automated Scheduler

For continuous operation:
```bash
python campaign_reports.py scheduler
```

## Command Reference

### Generate Reports
```bash
# Generate specific report types
python campaign_reports.py report daily
python campaign_reports.py report weekly  
python campaign_reports.py report monthly
```

### System Management
```bash
# Check system status and configuration
python campaign_reports.py status

# Start automated scheduler
python campaign_reports.py scheduler
```

## GitHub Actions Automation

The system includes a GitHub Actions workflow (`.github/workflows/campaign-reports.yml`) that automatically:

- Runs daily reports at 9:00 AM UTC
- Runs weekly reports on Mondays at 9:00 AM UTC
- Runs monthly reports on the 1st of each month at 9:00 AM UTC
- Allows manual triggering via GitHub interface

### Required GitHub Secrets

Configure these secrets in your repository settings:

```
GA_API_KEY              # Google Analytics API key
TWITTER_API_KEY         # Twitter API key  
TWITTER_API_SECRET      # Twitter API secret
LINKEDIN_API_KEY        # LinkedIn API key
FACEBOOK_API_KEY        # Facebook API key
EMAIL_USER              # Email address for sending reports
EMAIL_PASSWORD          # Email password/app password
SMTP_SERVER             # SMTP server (optional, defaults to Gmail)
SMTP_PORT               # SMTP port (optional, defaults to 587)
```

## Report Features

### UTM Campaign Tracking
- Session counts and conversion tracking
- Campaign-specific performance metrics
- Conversion rate analysis
- Traffic source attribution

### Social Media Engagement
- Likes, comments, shares across platforms
- Engagement rate calculations
- Reach and impression metrics
- Top-performing content identification

### ERIVOX Platform Metrics
- Active user tracking
- Voice message analytics
- Live session metrics
- User retention analysis

### Performance Alerts
Automatic alerts for:
- Engagement rate drops (>20%)
- Traffic drops (>30%)
- Conversion rate drops (>25%)

## Report Output

Reports are generated in multiple formats:
- **HTML**: Professional email reports with ERIFY branding
- **JSON**: Machine-readable data for further processing
- **File Storage**: Reports saved to `reports/` directory

### Sample Report Content
- Key performance metrics dashboard
- UTM campaign performance table
- Social media platform breakdown
- Trend analysis and alerts
- Executive summary with actionable insights

## Configuration Options

### Schedule Customization
```python
SCHEDULE_CONFIGS = {
    'daily': {
        'time': '09:00',
        'timezone': 'UTC',
        'enabled': True
    },
    'weekly': {
        'day': 'monday', 
        'time': '09:00',
        'timezone': 'UTC',
        'enabled': True
    },
    'monthly': {
        'day': 1,
        'time': '09:00', 
        'timezone': 'UTC',
        'enabled': True
    }
}
```

### Campaign Tracking
```python
UTM_CAMPAIGNS = [
    'erify-supreme4-launch',
    'erify-vip-referral', 
    'erify-luxury-fintech',
    'erify-neon-crown-series'
]
```

## Architecture

```
scripts/
├── campaign_reports.py          # Main CLI entry point
├── requirements.txt             # Python dependencies
├── .env.example                # Configuration template
└── reporting/
    ├── __init__.py             # Module initialization
    ├── config.py               # Configuration management
    ├── data_collectors.py      # API data collection
    ├── report_generator.py     # Report generation & email
    └── scheduler.py            # Automated scheduling
```

## API Integration

### Google Analytics
- Uses Analytics Reporting API v4
- Tracks UTM parameters and conversions
- Provides session and user metrics

### Social Media APIs
- **Twitter API v2**: Tweet engagement, reach metrics
- **LinkedIn API**: Professional network engagement
- **Facebook Graph API**: Page insights and engagement

### ERIVOX Platform
- Custom API integration for platform-specific metrics
- Voice messaging and live session tracking

## Troubleshooting

### Common Issues

1. **Email not sending**: Check SMTP configuration and app passwords
2. **API errors**: Verify API keys and rate limits
3. **Schedule not running**: Ensure proper timezone configuration
4. **Missing data**: Check API permissions and account access

### Logging
The system provides detailed logging for troubleshooting:
```bash
# Check logs when running manually
python campaign_reports.py report daily

# For GitHub Actions, check the workflow logs
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

© 2025 ERIFY™. All rights reserved.

---

**From the Ashes to the Stars ✨🔥💎**