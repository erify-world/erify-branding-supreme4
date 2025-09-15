#!/usr/bin/env python3
"""
ERIFY Campaign Performance Reporting - Main Entry Point
Automated scheduling and generation of campaign performance reports
"""

import argparse
import sys
import os
from datetime import datetime

# Add the script directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reporting.scheduler import ReportScheduler, main as scheduler_main
from reporting.config import load_config

def run_manual_report(report_type: str):
    """Run a manual report for testing purposes"""
    print(f"🚀 ERIFY™ Campaign Performance Report Generator")
    print(f"📊 Generating {report_type} report...")
    print(f"⏰ Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    
    try:
        config = load_config()
        scheduler = ReportScheduler(config)
        scheduler.run_manual_report(report_type)
        print("✅ Report generated successfully!")
        
    except Exception as e:
        print(f"❌ Error generating report: {e}")
        sys.exit(1)

def start_scheduler():
    """Start the automated scheduler"""
    print(f"🚀 ERIFY™ Campaign Performance Reporting System")
    print(f"📅 Starting automated scheduler...")
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print("Press Ctrl+C to stop the scheduler")
    
    scheduler_main()

def show_status():
    """Show system status and configuration"""
    print(f"🚀 ERIFY™ Campaign Performance Reporting System")
    print(f"📋 System Status")
    print("-" * 50)
    
    config = load_config()
    
    print(f"✅ Configuration loaded")
    print(f"📧 Email configured: {'Yes' if config.EMAIL_USER else 'No'}")
    print(f"📊 Report recipients: {len(config.REPORT_RECIPIENTS)}")
    print(f"🎯 UTM campaigns tracked: {len(config.UTM_CAMPAIGNS)}")
    print(f"📱 Social platforms: {len(config.SOCIAL_ACCOUNTS)}")
    
    # Show schedule configuration
    print("\n📅 Schedule Configuration:")
    for schedule_type, config_data in config.SCHEDULE_CONFIGS.items():
        status = "✅ Enabled" if config_data['enabled'] else "❌ Disabled"
        if schedule_type == 'weekly':
            print(f"  {schedule_type.title()}: {status} - {config_data['day']} at {config_data['time']}")
        elif schedule_type == 'monthly':
            print(f"  {schedule_type.title()}: {status} - Day {config_data['day']} at {config_data['time']}")
        else:
            print(f"  {schedule_type.title()}: {status} - {config_data['time']}")

def main():
    """Main CLI interface"""
    parser = argparse.ArgumentParser(
        description="ERIFY™ Campaign Performance Reporting System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s report daily       # Generate a daily report
  %(prog)s report weekly      # Generate a weekly report  
  %(prog)s report monthly     # Generate a monthly report
  %(prog)s scheduler          # Start the automated scheduler
  %(prog)s status             # Show system status
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate a manual report')
    report_parser.add_argument(
        'type', 
        choices=['daily', 'weekly', 'monthly'],
        help='Type of report to generate'
    )
    
    # Scheduler command
    scheduler_parser = subparsers.add_parser('scheduler', help='Start the automated scheduler')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show system status')
    
    # Parse arguments
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'report':
        run_manual_report(args.type)
    elif args.command == 'scheduler':
        start_scheduler()
    elif args.command == 'status':
        show_status()

if __name__ == "__main__":
    main()