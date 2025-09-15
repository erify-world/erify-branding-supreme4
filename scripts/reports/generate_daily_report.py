#!/usr/bin/env python3
"""
ERIFY Daily Campaign Performance Report Generator

This script generates daily reports on campaign metrics including:
- Engagement rates across platforms
- Referral click-throughs and conversions
- User behavior analytics
- Real-time performance indicators
"""

import os
import sys
import yaml
import json
import requests
import smtplib
from datetime import datetime, timedelta
try:
    from email.mime.text import MimeText
    from email.mime.multipart import MimeMultipart
    from email.mime.application import MimeApplication
except ImportError:
    # Mock email classes for testing
    class MimeText:
        def __init__(self, *args, **kwargs): pass
    class MimeMultipart:
        def __init__(self, *args, **kwargs): pass
        def attach(self, *args): pass
        def __setitem__(self, key, value): pass
    class MimeApplication:
        def __init__(self, *args, **kwargs): pass
        def add_header(self, *args, **kwargs): pass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DailyReportGenerator:
    def __init__(self, config_path='config.yml'):
        """Initialize the report generator with configuration."""
        self.config = self.load_config(config_path)
        self.report_date = datetime.now().strftime('%Y-%m-%d')
        self.metrics_data = {}
        
    def load_config(self, config_path):
        """Load configuration from YAML file."""
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                # Replace environment variables
                config_str = yaml.dump(config)
                for key, value in os.environ.items():
                    config_str = config_str.replace(f'${{{key}}}', value)
                return yaml.safe_load(config_str)
        except FileNotFoundError:
            logger.error(f"Configuration file {config_path} not found")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            sys.exit(1)
    
    def collect_engagement_metrics(self):
        """Collect engagement metrics from social platforms."""
        logger.info("Collecting engagement metrics...")
        
        engagement_data = {
            'twitter': self.get_twitter_metrics(),
            'linkedin': self.get_linkedin_metrics(),
            'facebook': self.get_facebook_metrics(),
            'erivox': self.get_erivox_metrics()
        }
        
        self.metrics_data['engagement'] = engagement_data
        return engagement_data
    
    def get_twitter_metrics(self):
        """Fetch Twitter/X engagement metrics."""
        if not self.config['data_sources']['social_platforms']['twitter']['enabled']:
            return {'error': 'Twitter integration disabled'}
        
        try:
            # Mock data for demonstration - replace with actual API calls
            return {
                'likes': 150,
                'retweets': 45,
                'replies': 23,
                'impressions': 12500,
                'engagement_rate': 1.74,
                'top_performing_post': 'Supreme 4PW Crown Seal launch announcement'
            }
        except Exception as e:
            logger.error(f"Error fetching Twitter metrics: {e}")
            return {'error': str(e)}
    
    def get_linkedin_metrics(self):
        """Fetch LinkedIn engagement metrics."""
        if not self.config['data_sources']['social_platforms']['linkedin']['enabled']:
            return {'error': 'LinkedIn integration disabled'}
        
        try:
            # Mock data for demonstration - replace with actual API calls
            return {
                'likes': 89,
                'comments': 12,
                'shares': 34,
                'views': 8900,
                'engagement_rate': 1.52,
                'top_performing_post': 'ERIFY VIP Referral Program announcement'
            }
        except Exception as e:
            logger.error(f"Error fetching LinkedIn metrics: {e}")
            return {'error': str(e)}
    
    def get_facebook_metrics(self):
        """Fetch Facebook engagement metrics."""
        if not self.config['data_sources']['social_platforms']['facebook']['enabled']:
            return {'error': 'Facebook integration disabled'}
        
        try:
            # Mock data for demonstration - replace with actual API calls
            return {
                'likes': 203,
                'comments': 45,
                'shares': 67,
                'reach': 15600,
                'engagement_rate': 2.02,
                'top_performing_post': 'Neon Crown Series reveal'
            }
        except Exception as e:
            logger.error(f"Error fetching Facebook metrics: {e}")
            return {'error': str(e)}
    
    def get_erivox_metrics(self):
        """Fetch ERIVOX platform metrics."""
        try:
            # Mock data for ERIVOX platform
            return {
                'posts': 8,
                'engagement': 156,
                'user_interactions': 89,
                'platform_growth': 12.5,
                'engagement_rate': 3.21
            }
        except Exception as e:
            logger.error(f"Error fetching ERIVOX metrics: {e}")
            return {'error': str(e)}
    
    def collect_referral_metrics(self):
        """Collect referral and UTM tracking metrics."""
        logger.info("Collecting referral metrics...")
        
        referral_data = {
            'utm_campaigns': self.get_utm_metrics(),
            'conversion_tracking': self.get_conversion_metrics(),
            'click_through_rates': self.get_ctr_metrics()
        }
        
        self.metrics_data['referrals'] = referral_data
        return referral_data
    
    def get_utm_metrics(self):
        """Get UTM campaign performance metrics."""
        try:
            # Mock UTM tracking data - replace with Google Analytics API
            return {
                'supreme4_launch': {
                    'clicks': 890,
                    'conversions': 45,
                    'conversion_rate': 5.06
                },
                'vip_referral': {
                    'clicks': 567,
                    'conversions': 78,
                    'conversion_rate': 13.76
                },
                'neon_series': {
                    'clicks': 234,
                    'conversions': 12,
                    'conversion_rate': 5.13
                }
            }
        except Exception as e:
            logger.error(f"Error fetching UTM metrics: {e}")
            return {'error': str(e)}
    
    def get_conversion_metrics(self):
        """Get conversion tracking metrics."""
        try:
            return {
                'total_signups': 135,
                'verified_users': 89,
                'premium_upgrades': 23,
                'referral_rewards': 45
            }
        except Exception as e:
            logger.error(f"Error fetching conversion metrics: {e}")
            return {'error': str(e)}
    
    def get_ctr_metrics(self):
        """Get click-through rate metrics."""
        try:
            return {
                'email_campaigns': 12.5,
                'social_posts': 3.2,
                'website_ctas': 8.9,
                'average_ctr': 8.2
            }
        except Exception as e:
            logger.error(f"Error fetching CTR metrics: {e}")
            return {'error': str(e)}
    
    def collect_user_behavior_metrics(self):
        """Collect user behavior and analytics data."""
        logger.info("Collecting user behavior metrics...")
        
        behavior_data = {
            'session_analytics': self.get_session_metrics(),
            'user_demographics': self.get_demographic_data(),
            'engagement_patterns': self.get_engagement_patterns()
        }
        
        self.metrics_data['user_behavior'] = behavior_data
        return behavior_data
    
    def get_session_metrics(self):
        """Get session analytics data."""
        try:
            return {
                'total_sessions': 1250,
                'avg_session_duration': 145,
                'bounce_rate': 34.5,
                'pages_per_session': 2.8,
                'new_vs_returning': {
                    'new_users': 78.2,
                    'returning_users': 21.8
                }
            }
        except Exception as e:
            logger.error(f"Error fetching session metrics: {e}")
            return {'error': str(e)}
    
    def get_demographic_data(self):
        """Get user demographic information."""
        try:
            return {
                'age_groups': {
                    '18-24': 23.5,
                    '25-34': 45.2,
                    '35-44': 21.8,
                    '45+': 9.5
                },
                'geographic_distribution': {
                    'North America': 45.6,
                    'Europe': 32.1,
                    'Asia Pacific': 15.7,
                    'Other': 6.6
                },
                'device_usage': {
                    'mobile': 67.8,
                    'desktop': 28.9,
                    'tablet': 3.3
                }
            }
        except Exception as e:
            logger.error(f"Error fetching demographic data: {e}")
            return {'error': str(e)}
    
    def get_engagement_patterns(self):
        """Get user engagement pattern analysis."""
        try:
            return {
                'peak_hours': ['10:00-11:00', '15:00-16:00', '20:00-21:00'],
                'best_posting_days': ['Tuesday', 'Wednesday', 'Thursday'],
                'content_preferences': {
                    'visual_content': 78.5,
                    'text_posts': 21.5
                },
                'interaction_types': {
                    'likes': 65.4,
                    'shares': 20.1,
                    'comments': 14.5
                }
            }
        except Exception as e:
            logger.error(f"Error fetching engagement patterns: {e}")
            return {'error': str(e)}
    
    def generate_report_summary(self):
        """Generate a comprehensive report summary."""
        logger.info("Generating report summary...")
        
        summary = {
            'report_date': self.report_date,
            'generated_at': datetime.now().isoformat(),
            'overview': {
                'total_engagement': sum([
                    self.metrics_data.get('engagement', {}).get('twitter', {}).get('likes', 0),
                    self.metrics_data.get('engagement', {}).get('linkedin', {}).get('likes', 0),
                    self.metrics_data.get('engagement', {}).get('facebook', {}).get('likes', 0)
                ]),
                'total_conversions': self.metrics_data.get('referrals', {}).get('conversion_tracking', {}).get('total_signups', 0),
                'average_engagement_rate': 2.16,
                'key_highlights': [
                    'Supreme 4PW Crown Seal continues strong performance',
                    'VIP Referral Program showing excellent conversion rates',
                    'Mobile engagement increasing significantly'
                ]
            },
            'alerts': self.check_performance_alerts()
        }
        
        return summary
    
    def check_performance_alerts(self):
        """Check for performance alerts based on thresholds."""
        alerts = []
        
        # Check engagement rate threshold
        avg_engagement = 2.16  # Calculate from actual data
        if avg_engagement < 2.0:
            alerts.append({
                'type': 'warning',
                'message': f'Average engagement rate ({avg_engagement}%) below expected threshold'
            })
        
        # Check conversion rate
        conversion_rate = 8.5  # Calculate from actual data
        if conversion_rate < self.config['alerts']['conversion_rate_threshold']:
            alerts.append({
                'type': 'critical',
                'message': f'Conversion rate ({conversion_rate}%) below threshold'
            })
        
        return alerts
    
    def send_email_report(self, report_data):
        """Send report via email."""
        if not self.config['delivery']['email']['enabled']:
            logger.info("Email delivery disabled")
            return
        
        try:
            msg = MimeMultipart('alternative')
            msg['Subject'] = f'ERIFY Daily Campaign Report - {self.report_date}'
            msg['From'] = self.config['delivery']['email']['username']
            msg['To'] = self.config['delivery']['email']['recipients']
            
            # Create HTML report
            html_content = self.generate_html_report(report_data)
            html_part = MimeText(html_content, 'html')
            msg.attach(html_part)
            
            # Attach JSON data
            json_data = json.dumps(report_data, indent=2)
            json_attachment = MimeApplication(json_data, _subtype='json')
            json_attachment.add_header(
                'Content-Disposition', 
                f'attachment; filename=daily_report_{self.report_date}.json'
            )
            msg.attach(json_attachment)
            
            # Send email
            with smtplib.SMTP(
                self.config['delivery']['email']['smtp_server'],
                self.config['delivery']['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['delivery']['email']['username'],
                    self.config['delivery']['email']['password']
                )
                server.send_message(msg)
            
            logger.info("Email report sent successfully")
            
        except Exception as e:
            logger.error(f"Error sending email report: {e}")
    
    def send_slack_report(self, report_data):
        """Send report to Slack."""
        if not self.config['delivery']['slack']['enabled']:
            logger.info("Slack delivery disabled")
            return
        
        try:
            webhook_url = self.config['delivery']['slack']['webhook_url']
            slack_message = self.generate_slack_message(report_data)
            
            response = requests.post(webhook_url, json=slack_message)
            response.raise_for_status()
            
            logger.info("Slack report sent successfully")
            
        except Exception as e:
            logger.error(f"Error sending Slack report: {e}")
    
    def generate_html_report(self, report_data):
        """Generate HTML formatted report."""
        html = f"""
        <html>
        <head>
            <title>ERIFY Daily Campaign Report - {self.report_date}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background: #11C9FF; color: white; padding: 20px; border-radius: 8px; }}
                .section {{ margin: 20px 0; padding: 15px; border-left: 4px solid #11C9FF; }}
                .metric {{ display: inline-block; margin: 10px; padding: 10px; background: #f5f5f5; border-radius: 4px; }}
                .alert {{ background: #ff4444; color: white; padding: 10px; border-radius: 4px; margin: 5px 0; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>ERIFY™ Daily Campaign Report</h1>
                <p>Report Date: {self.report_date}</p>
            </div>
            
            <div class="section">
                <h2>📊 Engagement Overview</h2>
                <div class="metric">Twitter: {report_data.get('engagement', {}).get('twitter', {}).get('likes', 0)} likes</div>
                <div class="metric">LinkedIn: {report_data.get('engagement', {}).get('linkedin', {}).get('likes', 0)} likes</div>
                <div class="metric">Facebook: {report_data.get('engagement', {}).get('facebook', {}).get('likes', 0)} likes</div>
            </div>
            
            <div class="section">
                <h2>🔗 Referral Performance</h2>
                <p>Total Conversions: {report_data.get('referrals', {}).get('conversion_tracking', {}).get('total_signups', 0)}</p>
                <p>Premium Upgrades: {report_data.get('referrals', {}).get('conversion_tracking', {}).get('premium_upgrades', 0)}</p>
            </div>
            
            <div class="section">
                <h2>👥 User Behavior</h2>
                <p>Total Sessions: {report_data.get('user_behavior', {}).get('session_analytics', {}).get('total_sessions', 0)}</p>
                <p>Bounce Rate: {report_data.get('user_behavior', {}).get('session_analytics', {}).get('bounce_rate', 0)}%</p>
            </div>
        </body>
        </html>
        """
        return html
    
    def generate_slack_message(self, report_data):
        """Generate Slack formatted message."""
        total_engagement = sum([
            report_data.get('engagement', {}).get('twitter', {}).get('likes', 0),
            report_data.get('engagement', {}).get('linkedin', {}).get('likes', 0),
            report_data.get('engagement', {}).get('facebook', {}).get('likes', 0)
        ])
        
        return {
            "text": f"ERIFY Daily Campaign Report - {self.report_date}",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"🏆 ERIFY Daily Report - {self.report_date}"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Total Engagement:* {total_engagement}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Conversions:* {report_data.get('referrals', {}).get('conversion_tracking', {}).get('total_signups', 0)}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Sessions:* {report_data.get('user_behavior', {}).get('session_analytics', {}).get('total_sessions', 0)}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Avg Engagement Rate:* 2.16%"
                        }
                    ]
                }
            ]
        }
    
    def run(self):
        """Run the daily report generation process."""
        logger.info(f"Starting daily report generation for {self.report_date}")
        
        try:
            # Collect all metrics
            self.collect_engagement_metrics()
            self.collect_referral_metrics()
            self.collect_user_behavior_metrics()
            
            # Generate report
            report_summary = self.generate_report_summary()
            full_report = {
                'summary': report_summary,
                'detailed_metrics': self.metrics_data
            }
            
            # Save report to file
            report_filename = f'reports/daily_report_{self.report_date}.json'
            os.makedirs('reports', exist_ok=True)
            with open(report_filename, 'w') as f:
                json.dump(full_report, f, indent=2)
            
            # Send reports
            self.send_email_report(full_report)
            self.send_slack_report(full_report)
            
            logger.info(f"Daily report generation completed successfully")
            logger.info(f"Report saved to: {report_filename}")
            
        except Exception as e:
            logger.error(f"Error during report generation: {e}")
            sys.exit(1)

if __name__ == "__main__":
    generator = DailyReportGenerator()
    generator.run()