"""
Scheduling system for automated campaign performance reports
"""

import schedule
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, Any, Callable
import logging

from .config import ReportingConfig, load_config
from .data_collectors import DataAggregator, GoogleAnalyticsCollector, SocialMediaCollector, ERIVOXCollector
from .report_generator import ReportGenerator, EmailReporter, AlertManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ReportScheduler:
    """Main scheduler for automated report generation"""
    
    def __init__(self, config: ReportingConfig = None):
        self.config = config or load_config()
        self.data_aggregator = DataAggregator()
        self.report_generator = ReportGenerator(self.config)
        self.email_reporter = EmailReporter(self.config)
        self.alert_manager = AlertManager(self.config)
        self.running = False
        self._setup_data_collectors()
        
    def _setup_data_collectors(self):
        """Initialize and configure data collectors"""
        # Google Analytics collector
        if self.config.GOOGLE_ANALYTICS_API_KEY:
            ga_collector = GoogleAnalyticsCollector(
                self.config.GOOGLE_ANALYTICS_API_KEY, 
                "GA_VIEW_ID"  # This would come from config in production
            )
            self.data_aggregator.add_collector(ga_collector)
        
        # Social media collectors
        social_platforms = ['twitter', 'linkedin', 'facebook']
        for platform in social_platforms:
            api_key = getattr(self.config, f'{platform.upper()}_API_KEY', None)
            if api_key:
                account_id = self.config.SOCIAL_ACCOUNTS.get(platform, '')
                collector = SocialMediaCollector(platform, api_key, account_id)
                self.data_aggregator.add_collector(collector)
        
        # ERIVOX collector
        erivox_collector = ERIVOXCollector("ERIVOX_API_KEY")
        self.data_aggregator.add_collector(erivox_collector)
    
    def generate_daily_report(self):
        """Generate and send daily performance report"""
        logger.info("Starting daily report generation...")
        
        try:
            # Set date range for daily report (yesterday)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=1)
            
            # Collect data
            data = self.data_aggregator.collect_all_data(start_date, end_date)
            
            # Generate report
            html_report = self.report_generator.generate_html_report(data, 'daily')
            json_report = self.report_generator.generate_json_report(data)
            
            # Save reports
            timestamp = datetime.now().strftime('%Y%m%d')
            self.report_generator.save_report(html_report, f'daily_report_{timestamp}', 'html')
            self.report_generator.save_report(json_report, f'daily_report_{timestamp}', 'json')
            
            # Send email report
            subject = f"ERIFY™ Daily Campaign Performance Report - {end_date.strftime('%Y-%m-%d')}"
            self.email_reporter.send_report(html_report, subject)
            
            logger.info("Daily report generated and sent successfully")
            
        except Exception as e:
            logger.error(f"Error generating daily report: {e}")
    
    def generate_weekly_report(self):
        """Generate and send weekly performance report"""
        logger.info("Starting weekly report generation...")
        
        try:
            # Set date range for weekly report (last 7 days)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=7)
            
            # Collect data
            data = self.data_aggregator.collect_all_data(start_date, end_date)
            
            # Generate report
            html_report = self.report_generator.generate_html_report(data, 'weekly')
            json_report = self.report_generator.generate_json_report(data)
            
            # Save reports
            timestamp = datetime.now().strftime('%Y%m%d')
            self.report_generator.save_report(html_report, f'weekly_report_{timestamp}', 'html')
            self.report_generator.save_report(json_report, f'weekly_report_{timestamp}', 'json')
            
            # Send email report
            subject = f"ERIFY™ Weekly Campaign Performance Report - Week of {end_date.strftime('%Y-%m-%d')}"
            self.email_reporter.send_report(html_report, subject)
            
            logger.info("Weekly report generated and sent successfully")
            
        except Exception as e:
            logger.error(f"Error generating weekly report: {e}")
    
    def generate_monthly_report(self):
        """Generate and send monthly performance report"""
        logger.info("Starting monthly report generation...")
        
        try:
            # Set date range for monthly report (last 30 days)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            
            # Collect data
            data = self.data_aggregator.collect_all_data(start_date, end_date)
            
            # Generate report
            html_report = self.report_generator.generate_html_report(data, 'monthly')
            json_report = self.report_generator.generate_json_report(data)
            
            # Save reports
            timestamp = datetime.now().strftime('%Y%m%d')
            self.report_generator.save_report(html_report, f'monthly_report_{timestamp}', 'html')
            self.report_generator.save_report(json_report, f'monthly_report_{timestamp}', 'json')
            
            # Send email report
            subject = f"ERIFY™ Monthly Campaign Performance Report - {end_date.strftime('%B %Y')}"
            self.email_reporter.send_report(html_report, subject)
            
            logger.info("Monthly report generated and sent successfully")
            
        except Exception as e:
            logger.error(f"Error generating monthly report: {e}")
    
    def setup_schedules(self):
        """Configure the reporting schedules"""
        schedule_configs = self.config.SCHEDULE_CONFIGS
        
        # Daily reports
        if schedule_configs['daily']['enabled']:
            schedule.every().day.at(schedule_configs['daily']['time']).do(self.generate_daily_report)
            logger.info(f"Daily reports scheduled for {schedule_configs['daily']['time']}")
        
        # Weekly reports
        if schedule_configs['weekly']['enabled']:
            day = schedule_configs['weekly']['day']
            time_str = schedule_configs['weekly']['time']
            getattr(schedule.every(), day).at(time_str).do(self.generate_weekly_report)
            logger.info(f"Weekly reports scheduled for {day} at {time_str}")
        
        # Monthly reports (run on the 1st of each month)
        if schedule_configs['monthly']['enabled']:
            schedule.every().day.at(schedule_configs['monthly']['time']).do(self._check_monthly_report)
            logger.info(f"Monthly reports scheduled for 1st of each month at {schedule_configs['monthly']['time']}")
    
    def _check_monthly_report(self):
        """Check if today is the first day of the month and run monthly report"""
        if datetime.now().day == self.config.SCHEDULE_CONFIGS['monthly']['day']:
            self.generate_monthly_report()
    
    def start_scheduler(self):
        """Start the background scheduler"""
        if self.running:
            logger.warning("Scheduler is already running")
            return
        
        self.setup_schedules()
        self.running = True
        
        def run_scheduler():
            logger.info("Report scheduler started")
            while self.running:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
            logger.info("Report scheduler stopped")
        
        # Run scheduler in background thread
        self.scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
        self.scheduler_thread.start()
        
        logger.info("Background scheduler thread started")
    
    def stop_scheduler(self):
        """Stop the background scheduler"""
        if not self.running:
            logger.warning("Scheduler is not running")
            return
        
        self.running = False
        schedule.clear()
        logger.info("Scheduler stopped and all jobs cleared")
    
    def run_manual_report(self, report_type: str = 'daily'):
        """Run a manual report generation for testing"""
        logger.info(f"Running manual {report_type} report...")
        
        if report_type == 'daily':
            self.generate_daily_report()
        elif report_type == 'weekly':
            self.generate_weekly_report()
        elif report_type == 'monthly':
            self.generate_monthly_report()
        else:
            logger.error(f"Unknown report type: {report_type}")

def main():
    """Main entry point for the scheduler"""
    logger.info("Initializing ERIFY Campaign Performance Reporting System")
    
    try:
        # Load configuration
        config = load_config()
        
        # Create and start scheduler
        scheduler = ReportScheduler(config)
        scheduler.start_scheduler()
        
        # Keep the main thread alive
        try:
            while True:
                time.sleep(10)
        except KeyboardInterrupt:
            logger.info("Shutting down scheduler...")
            scheduler.stop_scheduler()
            
    except Exception as e:
        logger.error(f"Error starting reporting system: {e}")

if __name__ == "__main__":
    main()