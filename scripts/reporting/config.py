"""
Configuration settings for ERIFY campaign performance reporting
"""

import os
from typing import Dict, List, Optional

class ReportingConfig:
    """Configuration class for campaign performance reporting"""
    
    # API Endpoints and Keys
    GOOGLE_ANALYTICS_API_KEY = os.getenv('GA_API_KEY')
    TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
    TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
    LINKEDIN_API_KEY = os.getenv('LINKEDIN_API_KEY')
    FACEBOOK_API_KEY = os.getenv('FACEBOOK_API_KEY')
    
    # Email Configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', '587'))
    EMAIL_USER = os.getenv('EMAIL_USER')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    
    # Report Recipients
    REPORT_RECIPIENTS = [
        'team@erify.com',
        'marketing@erify.com'
    ]
    
    # UTM Tracking Configuration
    UTM_CAMPAIGNS = [
        'erify-supreme4-launch',
        'erify-vip-referral',
        'erify-luxury-fintech',
        'erify-neon-crown-series'
    ]
    
    # Social Media Accounts
    SOCIAL_ACCOUNTS = {
        'twitter': '@erify_official',
        'linkedin': 'company/erify',
        'facebook': 'erify.official'
    }
    
    # Report Schedule Configuration
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
    
    # Metrics to Track
    ENGAGEMENT_METRICS = [
        'likes',
        'comments',
        'shares',
        'clicks',
        'impressions',
        'reach',
        'engagement_rate'
    ]
    
    UTM_METRICS = [
        'sessions',
        'users',
        'pageviews',
        'bounce_rate',
        'avg_session_duration',
        'conversions',
        'conversion_rate'
    ]
    
    # Thresholds for Alerts
    ALERT_THRESHOLDS = {
        'engagement_rate_drop': 0.2,  # 20% drop triggers alert
        'traffic_drop': 0.3,          # 30% drop triggers alert
        'conversion_rate_drop': 0.25   # 25% drop triggers alert
    }

# Load environment-specific configurations
def load_config() -> ReportingConfig:
    """Load configuration based on environment"""
    return ReportingConfig()