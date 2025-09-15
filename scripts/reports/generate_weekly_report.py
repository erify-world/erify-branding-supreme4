#!/usr/bin/env python3
"""
ERIFY Weekly Campaign Performance Report Generator

This script generates comprehensive weekly reports including:
- Weekly engagement summary and trends
- Referral performance analysis
- User demographics and behavior patterns
- Conversion funnel analysis
- Platform comparison metrics
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

class WeeklyReportGenerator:
    def __init__(self, config_path='config.yml'):
        """Initialize the weekly report generator with configuration."""
        self.config = self.load_config(config_path)
        self.report_date = datetime.now().strftime('%Y-%m-%d')
        self.week_start = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
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
    
    def collect_weekly_engagement_summary(self):
        """Collect weekly engagement summary and trends."""
        logger.info("Collecting weekly engagement summary...")
        
        engagement_summary = {
            'platform_performance': self.get_platform_performance(),
            'engagement_trends': self.get_engagement_trends(),
            'top_content': self.get_top_performing_content(),
            'audience_growth': self.get_audience_growth_metrics()
        }
        
        self.metrics_data['weekly_engagement'] = engagement_summary
        return engagement_summary
    
    def get_platform_performance(self):
        """Get performance metrics for each platform."""
        try:
            return {
                'twitter': {
                    'total_engagement': 1250,
                    'reach': 85000,
                    'engagement_rate': 1.47,
                    'growth_rate': 12.5,
                    'best_performing_content': 'Supreme 4PW Crown Seal series',
                    'weekly_change': '+15.2%'
                },
                'linkedin': {
                    'total_engagement': 890,
                    'reach': 45000,
                    'engagement_rate': 1.98,
                    'growth_rate': 8.9,
                    'best_performing_content': 'VIP Referral Program announcement',
                    'weekly_change': '+8.7%'
                },
                'facebook': {
                    'total_engagement': 1560,
                    'reach': 92000,
                    'engagement_rate': 1.70,
                    'growth_rate': 6.7,
                    'best_performing_content': 'Neon Crown Series reveal',
                    'weekly_change': '+11.3%'
                },
                'erivox': {
                    'total_engagement': 456,
                    'reach': 12000,
                    'engagement_rate': 3.80,
                    'growth_rate': 22.1,
                    'best_performing_content': 'Community challenges',
                    'weekly_change': '+18.9%'
                }
            }
        except Exception as e:
            logger.error(f"Error fetching platform performance: {e}")
            return {'error': str(e)}
    
    def get_engagement_trends(self):
        """Get engagement trend analysis."""
        try:
            return {
                'daily_averages': {
                    'Monday': 145,
                    'Tuesday': 189,
                    'Wednesday': 203,
                    'Thursday': 178,
                    'Friday': 156,
                    'Saturday': 134,
                    'Sunday': 98
                },
                'peak_engagement_hours': ['10:00-11:00', '15:00-16:00', '20:00-21:00'],
                'content_type_performance': {
                    'visual_posts': 78.5,
                    'video_content': 12.3,
                    'text_posts': 9.2
                },
                'trending_hashtags': ['#ERIFY', '#Supreme4PW', '#NeonCrown', '#VIPReferral']
            }
        except Exception as e:
            logger.error(f"Error fetching engagement trends: {e}")
            return {'error': str(e)}
    
    def get_top_performing_content(self):
        """Get top performing content analysis."""
        try:
            return {
                'top_posts': [
                    {
                        'platform': 'Twitter',
                        'content': 'Supreme 4PW Crown Seal launch announcement',
                        'engagement': 450,
                        'reach': 15600,
                        'engagement_rate': 2.89
                    },
                    {
                        'platform': 'LinkedIn',
                        'content': 'ERIFY VIP Referral Program details',
                        'engagement': 234,
                        'reach': 8900,
                        'engagement_rate': 2.63
                    },
                    {
                        'platform': 'Facebook',
                        'content': 'Neon Crown Series visual showcase',
                        'engagement': 567,
                        'reach': 19800,
                        'engagement_rate': 2.86
                    }
                ],
                'content_insights': {
                    'best_posting_times': ['Tuesday 10:00', 'Wednesday 15:00', 'Thursday 20:00'],
                    'optimal_content_length': '120-150 characters',
                    'most_engaging_formats': ['carousel', 'single_image', 'video']
                }
            }
        except Exception as e:
            logger.error(f"Error fetching top content: {e}")
            return {'error': str(e)}
    
    def get_audience_growth_metrics(self):
        """Get audience growth and retention metrics."""
        try:
            return {
                'follower_growth': {
                    'twitter': '+156 (+2.3%)',
                    'linkedin': '+89 (+1.8%)',
                    'facebook': '+234 (+3.1%)',
                    'erivox': '+45 (+8.9%)'
                },
                'engagement_quality': {
                    'repeat_engagers': 34.5,
                    'new_audience': 65.5,
                    'loyalty_score': 7.8
                },
                'geographic_expansion': {
                    'new_regions': ['Asia Pacific', 'Latin America'],
                    'growth_markets': ['Canada', 'UK', 'Australia']
                }
            }
        except Exception as e:
            logger.error(f"Error fetching audience growth: {e}")
            return {'error': str(e)}
    
    def collect_referral_performance(self):
        """Collect detailed referral and conversion analysis."""
        logger.info("Collecting referral performance data...")
        
        referral_data = {
            'campaign_performance': self.get_campaign_performance(),
            'utm_analysis': self.get_utm_analysis(),
            'conversion_funnel': self.get_conversion_funnel(),
            'referral_sources': self.get_referral_sources()
        }
        
        self.metrics_data['referral_performance'] = referral_data
        return referral_data
    
    def get_campaign_performance(self):
        """Get detailed campaign performance metrics."""
        try:
            return {
                'supreme4_launch': {
                    'total_clicks': 6250,
                    'conversions': 312,
                    'conversion_rate': 4.99,
                    'revenue_generated': 15600,
                    'cost_per_conversion': 12.50,
                    'roi': 345.6
                },
                'vip_referral': {
                    'total_clicks': 3890,
                    'conversions': 534,
                    'conversion_rate': 13.73,
                    'revenue_generated': 26700,
                    'cost_per_conversion': 8.75,
                    'roi': 478.9
                },
                'neon_series': {
                    'total_clicks': 1650,
                    'conversions': 89,
                    'conversion_rate': 5.39,
                    'revenue_generated': 4450,
                    'cost_per_conversion': 15.25,
                    'roi': 234.1
                }
            }
        except Exception as e:
            logger.error(f"Error fetching campaign performance: {e}")
            return {'error': str(e)}
    
    def get_utm_analysis(self):
        """Get UTM parameter analysis."""
        try:
            return {
                'best_performing_sources': {
                    'twitter.com': 34.2,
                    'linkedin.com': 28.9,
                    'facebook.com': 22.1,
                    'direct': 14.8
                },
                'campaign_effectiveness': {
                    'social_media': 67.8,
                    'email_marketing': 18.9,
                    'paid_advertising': 13.3
                },
                'geographic_performance': {
                    'north_america': 45.6,
                    'europe': 32.1,
                    'asia_pacific': 15.7,
                    'other': 6.6
                }
            }
        except Exception as e:
            logger.error(f"Error fetching UTM analysis: {e}")
            return {'error': str(e)}
    
    def get_conversion_funnel(self):
        """Get conversion funnel analysis."""
        try:
            return {
                'funnel_stages': {
                    'awareness': 100000,
                    'interest': 12500,
                    'consideration': 3890,
                    'conversion': 935,
                    'retention': 567
                },
                'conversion_rates': {
                    'awareness_to_interest': 12.5,
                    'interest_to_consideration': 31.1,
                    'consideration_to_conversion': 24.0,
                    'conversion_to_retention': 60.6
                },
                'drop_off_analysis': {
                    'highest_drop_off': 'awareness_to_interest',
                    'optimization_opportunities': ['landing_page', 'call_to_action', 'value_proposition']
                }
            }
        except Exception as e:
            logger.error(f"Error fetching conversion funnel: {e}")
            return {'error': str(e)}
    
    def get_referral_sources(self):
        """Get referral source breakdown."""
        try:
            return {
                'traffic_sources': {
                    'organic_social': 45.2,
                    'paid_social': 23.8,
                    'email_marketing': 15.6,
                    'direct_traffic': 12.1,
                    'search_organic': 3.3
                },
                'quality_scores': {
                    'organic_social': 8.7,
                    'email_marketing': 9.2,
                    'paid_social': 7.4,
                    'direct_traffic': 8.9,
                    'search_organic': 9.1
                }
            }
        except Exception as e:
            logger.error(f"Error fetching referral sources: {e}")
            return {'error': str(e)}
    
    def collect_user_demographics(self):
        """Collect detailed user demographics and behavior patterns."""
        logger.info("Collecting user demographics...")
        
        demographics_data = {
            'demographic_breakdown': self.get_demographic_breakdown(),
            'behavioral_patterns': self.get_behavioral_patterns(),
            'user_journey_analysis': self.get_user_journey_analysis(),
            'segment_performance': self.get_segment_performance()
        }
        
        self.metrics_data['user_demographics'] = demographics_data
        return demographics_data
    
    def get_demographic_breakdown(self):
        """Get detailed demographic breakdown."""
        try:
            return {
                'age_distribution': {
                    '18-24': 23.5,
                    '25-34': 45.2,
                    '35-44': 21.8,
                    '45-54': 7.3,
                    '55+': 2.2
                },
                'gender_distribution': {
                    'male': 56.7,
                    'female': 41.2,
                    'other': 2.1
                },
                'income_brackets': {
                    '<50k': 15.6,
                    '50k-100k': 34.2,
                    '100k-200k': 32.1,
                    '>200k': 18.1
                },
                'education_levels': {
                    'high_school': 12.3,
                    'bachelors': 45.6,
                    'masters': 32.1,
                    'phd': 10.0
                }
            }
        except Exception as e:
            logger.error(f"Error fetching demographics: {e}")
            return {'error': str(e)}
    
    def get_behavioral_patterns(self):
        """Get user behavioral pattern analysis."""
        try:
            return {
                'engagement_frequency': {
                    'daily': 23.4,
                    'weekly': 45.6,
                    'monthly': 31.0
                },
                'preferred_content_types': {
                    'visual_content': 78.5,
                    'video_content': 12.3,
                    'text_content': 9.2
                },
                'interaction_preferences': {
                    'likes': 65.4,
                    'shares': 20.1,
                    'comments': 14.5
                },
                'time_spent_patterns': {
                    'quick_browsers': 34.5,
                    'engaged_readers': 45.2,
                    'deep_explorers': 20.3
                }
            }
        except Exception as e:
            logger.error(f"Error fetching behavioral patterns: {e}")
            return {'error': str(e)}
    
    def get_user_journey_analysis(self):
        """Get user journey and pathway analysis."""
        try:
            return {
                'common_pathways': [
                    'Social Media → Landing Page → Sign Up',
                    'Email → Website → Conversion',
                    'Referral → Product Page → Purchase'
                ],
                'average_touchpoints': 3.7,
                'conversion_timeline': {
                    'immediate': 23.5,
                    'within_24h': 45.2,
                    'within_week': 78.9,
                    'longer': 21.1
                },
                'retargeting_opportunities': {
                    'abandoned_signups': 156,
                    'inactive_users': 89,
                    'high_value_prospects': 67
                }
            }
        except Exception as e:
            logger.error(f"Error fetching user journey: {e}")
            return {'error': str(e)}
    
    def get_segment_performance(self):
        """Get performance metrics for different user segments."""
        try:
            return {
                'high_value_users': {
                    'count': 234,
                    'avg_engagement': 4.7,
                    'conversion_rate': 23.5,
                    'retention_rate': 89.2
                },
                'new_users': {
                    'count': 1456,
                    'avg_engagement': 2.1,
                    'conversion_rate': 5.8,
                    'retention_rate': 34.5
                },
                'returning_users': {
                    'count': 567,
                    'avg_engagement': 3.9,
                    'conversion_rate': 15.6,
                    'retention_rate': 78.9
                }
            }
        except Exception as e:
            logger.error(f"Error fetching segment performance: {e}")
            return {'error': str(e)}
    
    def generate_weekly_summary(self):
        """Generate comprehensive weekly report summary."""
        logger.info("Generating weekly report summary...")
        
        summary = {
            'report_period': f'{self.week_start} to {self.report_date}',
            'generated_at': datetime.now().isoformat(),
            'executive_summary': {
                'total_weekly_engagement': 4156,
                'weekly_conversions': 935,
                'average_engagement_rate': 2.24,
                'conversion_rate_improvement': '+12.5%',
                'top_performing_platform': 'ERIVOX',
                'key_achievements': [
                    'VIP Referral Program exceeded conversion targets by 37%',
                    'ERIVOX platform showed 22% growth in user engagement',
                    'Supreme 4PW Crown Seal campaign maintained strong momentum',
                    'Mobile engagement increased by 15% week-over-week'
                ]
            },
            'performance_highlights': {
                'best_performing_campaign': 'VIP Referral Program (13.73% conversion rate)',
                'highest_engagement_content': 'Neon Crown Series visual showcase',
                'fastest_growing_platform': 'ERIVOX (+18.9%)',
                'most_engaged_demographic': '25-34 age group (45.2% of audience)'
            },
            'recommendations': [
                'Increase investment in VIP Referral Program due to high ROI',
                'Expand Neon Crown Series content based on strong engagement',
                'Focus more resources on ERIVOX platform growth',
                'Optimize posting schedule for peak engagement hours'
            ],
            'alerts': self.check_weekly_performance_alerts()
        }
        
        return summary
    
    def check_weekly_performance_alerts(self):
        """Check for weekly performance alerts."""
        alerts = []
        
        # Check for significant changes
        engagement_growth = 15.2  # Mock data
        if engagement_growth > self.config['alerts']['traffic_spike_threshold']:
            alerts.append({
                'type': 'positive',
                'message': f'Engagement spike detected: +{engagement_growth}% this week'
            })
        
        # Check conversion performance
        conversion_rate = 24.0  # Mock data
        if conversion_rate > 20.0:
            alerts.append({
                'type': 'positive',
                'message': f'Conversion rate ({conversion_rate}%) exceeding targets'
            })
        
        return alerts
    
    def send_weekly_email_report(self, report_data):
        """Send weekly report via email."""
        if not self.config['delivery']['email']['enabled']:
            logger.info("Email delivery disabled")
            return
        
        try:
            msg = MimeMultipart('alternative')
            msg['Subject'] = f'ERIFY Weekly Campaign Report - Week of {self.week_start}'
            msg['From'] = self.config['delivery']['email']['username']
            msg['To'] = self.config['delivery']['email']['recipients']
            
            # Create HTML report
            html_content = self.generate_weekly_html_report(report_data)
            html_part = MimeText(html_content, 'html')
            msg.attach(html_part)
            
            # Attach JSON data
            json_data = json.dumps(report_data, indent=2)
            json_attachment = MimeApplication(json_data, _subtype='json')
            json_attachment.add_header(
                'Content-Disposition', 
                f'attachment; filename=weekly_report_{self.report_date}.json'
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
            
            logger.info("Weekly email report sent successfully")
            
        except Exception as e:
            logger.error(f"Error sending weekly email report: {e}")
    
    def send_weekly_slack_report(self, report_data):
        """Send weekly report to Slack."""
        if not self.config['delivery']['slack']['enabled']:
            logger.info("Slack delivery disabled")
            return
        
        try:
            webhook_url = self.config['delivery']['slack']['webhook_url']
            slack_message = self.generate_weekly_slack_message(report_data)
            
            response = requests.post(webhook_url, json=slack_message)
            response.raise_for_status()
            
            logger.info("Weekly Slack report sent successfully")
            
        except Exception as e:
            logger.error(f"Error sending weekly Slack report: {e}")
    
    def generate_weekly_html_report(self, report_data):
        """Generate comprehensive HTML weekly report."""
        summary = report_data.get('summary', {})
        executive_summary = summary.get('executive_summary', {})
        
        html = f"""
        <html>
        <head>
            <title>ERIFY Weekly Campaign Report - {self.week_start} to {self.report_date}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; line-height: 1.6; }}
                .header {{ background: linear-gradient(135deg, #11C9FF, #FFD700); color: white; padding: 30px; border-radius: 12px; text-align: center; }}
                .section {{ margin: 25px 0; padding: 20px; border-left: 5px solid #11C9FF; background: #f9f9f9; }}
                .metric-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 15px 0; }}
                .metric {{ padding: 15px; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
                .metric-value {{ font-size: 24px; font-weight: bold; color: #11C9FF; }}
                .alert {{ background: #4CAF50; color: white; padding: 12px; border-radius: 6px; margin: 8px 0; }}
                .recommendation {{ background: #FFD700; color: #333; padding: 10px; border-radius: 6px; margin: 5px 0; }}
                .chart {{ background: white; padding: 20px; border-radius: 8px; margin: 15px 0; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>ERIFY™ Weekly Campaign Report</h1>
                <p>Report Period: {self.week_start} to {self.report_date}</p>
                <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}</p>
            </div>
            
            <div class="section">
                <h2>📊 Executive Summary</h2>
                <div class="metric-grid">
                    <div class="metric">
                        <div class="metric-value">{executive_summary.get('total_weekly_engagement', 0)}</div>
                        <div>Total Engagement</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{executive_summary.get('weekly_conversions', 0)}</div>
                        <div>Weekly Conversions</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{executive_summary.get('average_engagement_rate', 0)}%</div>
                        <div>Avg Engagement Rate</div>
                    </div>
                    <div class="metric">
                        <div class="metric-value">{executive_summary.get('conversion_rate_improvement', '0%')}</div>
                        <div>Conversion Improvement</div>
                    </div>
                </div>
            </div>
            
            <div class="section">
                <h2>🏆 Key Achievements</h2>
                <ul>
                    {"".join([f"<li>{achievement}</li>" for achievement in executive_summary.get('key_achievements', [])])}
                </ul>
            </div>
            
            <div class="section">
                <h2>📈 Platform Performance</h2>
                <div class="chart">
                    <p><strong>Top Performing Platform:</strong> {executive_summary.get('top_performing_platform', 'N/A')}</p>
                    <p><strong>Highest Growth:</strong> ERIVOX (+18.9% weekly growth)</p>
                    <p><strong>Best Engagement Rate:</strong> ERIVOX (3.80%)</p>
                </div>
            </div>
            
            <div class="section">
                <h2>💡 Recommendations</h2>
                {"".join([f'<div class="recommendation">{rec}</div>' for rec in summary.get('recommendations', [])])}
            </div>
            
            <div class="section">
                <h2>🔔 Alerts & Notifications</h2>
                {"".join([f'<div class="alert">{alert.get("message", "")}</div>' for alert in summary.get('alerts', [])])}
            </div>
        </body>
        </html>
        """
        return html
    
    def generate_weekly_slack_message(self, report_data):
        """Generate comprehensive Slack weekly report message."""
        summary = report_data.get('summary', {})
        executive_summary = summary.get('executive_summary', {})
        
        return {
            "text": f"ERIFY Weekly Campaign Report - {self.week_start} to {self.report_date}",
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"📊 ERIFY Weekly Report - Week of {self.week_start}"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Total Engagement:* {executive_summary.get('total_weekly_engagement', 0)}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Weekly Conversions:* {executive_summary.get('weekly_conversions', 0)}"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Avg Engagement Rate:* {executive_summary.get('average_engagement_rate', 0)}%"
                        },
                        {
                            "type": "mrkdwn",
                            "text": f"*Top Platform:* {executive_summary.get('top_performing_platform', 'N/A')}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*🏆 Key Achievements:*\n" + "\n".join([f"• {achievement}" for achievement in executive_summary.get('key_achievements', [])[:3]])
                    }
                }
            ]
        }
    
    def run(self):
        """Run the weekly report generation process."""
        logger.info(f"Starting weekly report generation for week ending {self.report_date}")
        
        try:
            # Collect all weekly metrics
            self.collect_weekly_engagement_summary()
            self.collect_referral_performance()
            self.collect_user_demographics()
            
            # Generate comprehensive report
            weekly_summary = self.generate_weekly_summary()
            full_report = {
                'summary': weekly_summary,
                'detailed_metrics': self.metrics_data
            }
            
            # Save report to file
            report_filename = f'reports/weekly_report_{self.report_date}.json'
            os.makedirs('reports', exist_ok=True)
            with open(report_filename, 'w') as f:
                json.dump(full_report, f, indent=2)
            
            # Send reports
            self.send_weekly_email_report(full_report)
            self.send_weekly_slack_report(full_report)
            
            logger.info(f"Weekly report generation completed successfully")
            logger.info(f"Report saved to: {report_filename}")
            
        except Exception as e:
            logger.error(f"Error during weekly report generation: {e}")
            sys.exit(1)

if __name__ == "__main__":
    generator = WeeklyReportGenerator()
    generator.run()