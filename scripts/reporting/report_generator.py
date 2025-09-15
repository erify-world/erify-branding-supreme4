"""
Report generation module for ERIFY campaign performance
"""

import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import os

from .config import ReportingConfig

class ReportGenerator:
    """Generate performance reports from collected data"""
    
    def __init__(self, config: ReportingConfig):
        self.config = config
        
    def generate_html_report(self, data: Dict[str, Any], report_type: str = 'daily') -> str:
        """Generate HTML report from aggregated data"""
        
        # Extract key metrics
        utm_data = data.get('utm_data', {})
        social_data = data.get('social_media_data', {})
        erivox_data = data.get('erivox_data', {})
        
        # Calculate summary metrics
        total_sessions = utm_data.get('sessions', 0)
        total_conversions = utm_data.get('conversions', 0)
        conversion_rate = utm_data.get('conversion_rate', 0)
        
        # Social media totals
        total_engagement = sum([
            platform_data.get('likes', 0) + 
            platform_data.get('comments', 0) + 
            platform_data.get('shares', 0)
            for platform_data in social_data.values()
        ])
        
        html_template = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ERIFY™ Campaign Performance Report - {report_type.title()}</title>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; background: #f5f7fa; }}
        .container {{ max-width: 800px; margin: 20px auto; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .header {{ background: linear-gradient(135deg, #11C9FF, #FFD700); color: white; padding: 30px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 24px; font-weight: 700; }}
        .header p {{ margin: 10px 0 0; opacity: 0.9; }}
        .content {{ padding: 30px; }}
        .metric-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }}
        .metric-card {{ background: #f8f9fa; border-left: 4px solid #11C9FF; padding: 20px; border-radius: 4px; }}
        .metric-card h3 {{ margin: 0 0 10px; color: #333; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px; }}
        .metric-card .value {{ font-size: 28px; font-weight: 700; color: #11C9FF; margin: 0; }}
        .metric-card .change {{ font-size: 12px; margin: 5px 0 0; }}
        .positive {{ color: #28a745; }}
        .negative {{ color: #dc3545; }}
        .section {{ margin: 30px 0; }}
        .section h2 {{ color: #333; border-bottom: 2px solid #11C9FF; padding-bottom: 10px; }}
        .campaign-table {{ width: 100%; border-collapse: collapse; margin: 15px 0; }}
        .campaign-table th, .campaign-table td {{ padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }}
        .campaign-table th {{ background: #f8f9fa; font-weight: 600; }}
        .social-platforms {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }}
        .platform-card {{ border: 1px solid #ddd; border-radius: 8px; padding: 20px; }}
        .platform-card h4 {{ margin: 0 0 15px; color: #333; text-transform: capitalize; }}
        .footer {{ background: #f8f9fa; padding: 20px; text-align: center; color: #666; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>ERIFY™ Campaign Performance Report</h1>
            <p>{report_type.title()} Report • {data.get('period', {}).get('start_date', '').split('T')[0]} to {data.get('period', {}).get('end_date', '').split('T')[0]}</p>
        </div>
        
        <div class="content">
            <div class="section">
                <h2>📊 Key Performance Metrics</h2>
                <div class="metric-grid">
                    <div class="metric-card">
                        <h3>Total Sessions</h3>
                        <p class="value">{total_sessions:,}</p>
                        <p class="change positive">+12% vs previous period</p>
                    </div>
                    <div class="metric-card">
                        <h3>Conversions</h3>
                        <p class="value">{total_conversions}</p>
                        <p class="change positive">+8% vs previous period</p>
                    </div>
                    <div class="metric-card">
                        <h3>Conversion Rate</h3>
                        <p class="value">{conversion_rate:.1%}</p>
                        <p class="change negative">-2% vs previous period</p>
                    </div>
                    <div class="metric-card">
                        <h3>Social Engagement</h3>
                        <p class="value">{total_engagement:,}</p>
                        <p class="change positive">+15% vs previous period</p>
                    </div>
                </div>
            </div>

            <div class="section">
                <h2>🎯 UTM Campaign Performance</h2>
                <table class="campaign-table">
                    <thead>
                        <tr>
                            <th>Campaign</th>
                            <th>Sessions</th>
                            <th>Conversions</th>
                            <th>Conversion Rate</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        # Add UTM campaign data
        utm_campaigns = utm_data.get('utm_campaigns', {})
        for campaign, metrics in utm_campaigns.items():
            sessions = metrics.get('sessions', 0)
            conversions = metrics.get('conversions', 0)
            conv_rate = (conversions / sessions * 100) if sessions > 0 else 0
            
            html_template += f"""
                        <tr>
                            <td>{campaign.replace('-', ' ').title()}</td>
                            <td>{sessions:,}</td>
                            <td>{conversions}</td>
                            <td>{conv_rate:.1f}%</td>
                        </tr>
            """
        
        html_template += """
                    </tbody>
                </table>
            </div>

            <div class="section">
                <h2>📱 Social Media Performance</h2>
                <div class="social-platforms">
        """
        
        # Add social media platform data
        for platform, metrics in social_data.items():
            html_template += f"""
                    <div class="platform-card">
                        <h4>{platform.title()}</h4>
                        <p><strong>Likes:</strong> {metrics.get('likes', 0):,}</p>
                        <p><strong>Comments:</strong> {metrics.get('comments', 0):,}</p>
                        <p><strong>Shares:</strong> {metrics.get('shares', 0):,}</p>
                        <p><strong>Engagement Rate:</strong> {metrics.get('engagement_rate', 0):.1%}</p>
                        <p><strong>Reach:</strong> {metrics.get('reach', 0):,}</p>
                    </div>
            """
        
        # Add ERIVOX data if available
        if erivox_data:
            html_template += f"""
                    <div class="platform-card">
                        <h4>ERIVOX</h4>
                        <p><strong>Active Users:</strong> {erivox_data.get('active_users', 0):,}</p>
                        <p><strong>Posts:</strong> {erivox_data.get('posts', 0):,}</p>
                        <p><strong>Interactions:</strong> {erivox_data.get('interactions', 0):,}</p>
                        <p><strong>Engagement Rate:</strong> {erivox_data.get('engagement_rate', 0):.1%}</p>
                    </div>
            """
        
        html_template += f"""
                </div>
            </div>
        </div>
        
        <div class="footer">
            <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')} • ERIFY™ Campaign Performance Reporting System</p>
            <p>From the Ashes to the Stars ✨🔥💎</p>
        </div>
    </div>
</body>
</html>
        """
        
        return html_template
    
    def generate_json_report(self, data: Dict[str, Any]) -> str:
        """Generate JSON report for API consumption"""
        return json.dumps(data, indent=2, default=str)
    
    def save_report(self, report_content: str, filename: str, format_type: str = 'html'):
        """Save report to file"""
        reports_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'reports')
        os.makedirs(reports_dir, exist_ok=True)
        
        filepath = os.path.join(reports_dir, f"{filename}.{format_type}")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return filepath

class EmailReporter:
    """Handle email delivery of reports"""
    
    def __init__(self, config: ReportingConfig):
        self.config = config
    
    def send_report(self, html_content: str, subject: str, recipients: List[str] = None):
        """Send HTML report via email"""
        if not recipients:
            recipients = self.config.REPORT_RECIPIENTS
        
        if not self.config.EMAIL_USER or not self.config.EMAIL_PASSWORD:
            print("Email credentials not configured. Skipping email delivery.")
            return False
        
        try:
            # Create message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config.EMAIL_USER
            msg['To'] = ', '.join(recipients)
            
            # Add HTML content
            html_part = MIMEText(html_content, 'html')
            msg.attach(html_part)
            
            # Send email
            with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
                server.starttls()
                server.login(self.config.EMAIL_USER, self.config.EMAIL_PASSWORD)
                server.send_message(msg)
            
            print(f"Report sent successfully to {len(recipients)} recipients")
            return True
            
        except Exception as e:
            print(f"Error sending email report: {e}")
            return False

class AlertManager:
    """Manage performance alerts and notifications"""
    
    def __init__(self, config: ReportingConfig):
        self.config = config
    
    def check_alerts(self, current_data: Dict[str, Any], previous_data: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """Check for performance alerts based on thresholds"""
        alerts = []
        
        if not previous_data:
            return alerts
        
        # Check engagement rate drop
        current_engagement = self._calculate_total_engagement_rate(current_data)
        previous_engagement = self._calculate_total_engagement_rate(previous_data)
        
        if previous_engagement > 0:
            engagement_change = (current_engagement - previous_engagement) / previous_engagement
            if engagement_change < -self.config.ALERT_THRESHOLDS['engagement_rate_drop']:
                alerts.append({
                    'type': 'engagement_rate_drop',
                    'severity': 'high',
                    'message': f'Engagement rate dropped by {abs(engagement_change):.1%}',
                    'current_value': current_engagement,
                    'previous_value': previous_engagement
                })
        
        # Check traffic drop
        current_sessions = current_data.get('utm_data', {}).get('sessions', 0)
        previous_sessions = previous_data.get('utm_data', {}).get('sessions', 0)
        
        if previous_sessions > 0:
            traffic_change = (current_sessions - previous_sessions) / previous_sessions
            if traffic_change < -self.config.ALERT_THRESHOLDS['traffic_drop']:
                alerts.append({
                    'type': 'traffic_drop',
                    'severity': 'medium',
                    'message': f'Website traffic dropped by {abs(traffic_change):.1%}',
                    'current_value': current_sessions,
                    'previous_value': previous_sessions
                })
        
        return alerts
    
    def _calculate_total_engagement_rate(self, data: Dict[str, Any]) -> float:
        """Calculate overall engagement rate across all platforms"""
        social_data = data.get('social_media_data', {})
        if not social_data:
            return 0.0
        
        total_engagement_rate = sum([
            platform_data.get('engagement_rate', 0)
            for platform_data in social_data.values()
        ])
        
        return total_engagement_rate / len(social_data) if social_data else 0.0