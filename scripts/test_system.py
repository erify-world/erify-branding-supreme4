#!/usr/bin/env python3
"""
Test script for ERIFY Campaign Performance Reporting System
Run this to verify the system is working correctly
"""

import sys
import os
from datetime import datetime, timedelta

# Add the script directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported"""
    print("Testing module imports...")
    
    try:
        from reporting.config import load_config, ReportingConfig
        from reporting.data_collectors import DataAggregator, GoogleAnalyticsCollector, SocialMediaCollector, ERIVOXCollector
        from reporting.report_generator import ReportGenerator, EmailReporter, AlertManager
        from reporting.scheduler import ReportScheduler
        print("✅ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_configuration():
    """Test configuration loading"""
    print("\nTesting configuration...")
    
    try:
        from reporting.config import load_config
        config = load_config()
        
        print(f"✅ Configuration loaded")
        print(f"   - UTM campaigns: {len(config.UTM_CAMPAIGNS)}")
        print(f"   - Social accounts: {len(config.SOCIAL_ACCOUNTS)}")
        print(f"   - Schedule configs: {len(config.SCHEDULE_CONFIGS)}")
        return True
    except Exception as e:
        print(f"❌ Configuration error: {e}")
        return False

def test_data_collection():
    """Test data collection with mock data"""
    print("\nTesting data collection...")
    
    try:
        from reporting.data_collectors import DataAggregator, GoogleAnalyticsCollector, SocialMediaCollector, ERIVOXCollector
        
        # Create aggregator and add mock collectors
        aggregator = DataAggregator()
        
        # Add collectors (these will use mock data)
        ga_collector = GoogleAnalyticsCollector("mock_key", "mock_view_id")
        twitter_collector = SocialMediaCollector("twitter", "mock_key", "@erify_official")
        erivox_collector = ERIVOXCollector("mock_key")
        
        aggregator.add_collector(ga_collector)
        aggregator.add_collector(twitter_collector)
        aggregator.add_collector(erivox_collector)
        
        # Test data collection
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)
        
        data = aggregator.collect_all_data(start_date, end_date)
        
        print("✅ Data collection successful")
        print(f"   - UTM data: {'✅' if data.get('utm_data') else '❌'}")
        print(f"   - Social media data: {'✅' if data.get('social_media_data') else '❌'}")
        print(f"   - ERIVOX data: {'✅' if data.get('erivox_data') else '❌'}")
        
        return True
    except Exception as e:
        print(f"❌ Data collection error: {e}")
        return False

def test_report_generation():
    """Test report generation"""
    print("\nTesting report generation...")
    
    try:
        from reporting.config import load_config
        from reporting.report_generator import ReportGenerator
        from reporting.data_collectors import DataAggregator, GoogleAnalyticsCollector, SocialMediaCollector, ERIVOXCollector
        
        # Load config and create report generator
        config = load_config()
        report_generator = ReportGenerator(config)
        
        # Create mock data
        aggregator = DataAggregator()
        ga_collector = GoogleAnalyticsCollector("mock_key", "mock_view_id")
        twitter_collector = SocialMediaCollector("twitter", "mock_key", "@erify_official")
        
        aggregator.add_collector(ga_collector)
        aggregator.add_collector(twitter_collector)
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=1)
        data = aggregator.collect_all_data(start_date, end_date)
        
        # Generate reports
        html_report = report_generator.generate_html_report(data, 'daily')
        json_report = report_generator.generate_json_report(data)
        
        print("✅ Report generation successful")
        print(f"   - HTML report length: {len(html_report)} characters")
        print(f"   - JSON report length: {len(json_report)} characters")
        
        # Save test reports
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        html_file = report_generator.save_report(html_report, f'test_report_{timestamp}', 'html')
        json_file = report_generator.save_report(json_report, f'test_report_{timestamp}', 'json')
        
        print(f"   - HTML report saved: {html_file}")
        print(f"   - JSON report saved: {json_file}")
        
        return True
    except Exception as e:
        print(f"❌ Report generation error: {e}")
        return False

def test_scheduler_creation():
    """Test scheduler creation (without starting)"""
    print("\nTesting scheduler creation...")
    
    try:
        from reporting.scheduler import ReportScheduler
        from reporting.config import load_config
        
        config = load_config()
        scheduler = ReportScheduler(config)
        
        print("✅ Scheduler created successfully")
        print(f"   - Data collectors: {len(scheduler.data_aggregator.collectors)}")
        
        return True
    except Exception as e:
        print(f"❌ Scheduler creation error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 ERIFY™ Campaign Performance Reporting System - Test Suite")
    print("=" * 70)
    
    tests = [
        test_imports,
        test_configuration,
        test_data_collection,
        test_report_generation,
        test_scheduler_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 70)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The system is ready to use.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)