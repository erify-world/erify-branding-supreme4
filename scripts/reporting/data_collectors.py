"""
Data collection modules for campaign performance metrics
"""

import requests
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod

class DataCollector(ABC):
    """Abstract base class for data collectors"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = ""
    
    @abstractmethod
    def collect_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Collect data for the specified date range"""
        pass

class GoogleAnalyticsCollector(DataCollector):
    """Collect UTM tracking data from Google Analytics"""
    
    def __init__(self, api_key: str, view_id: str):
        super().__init__(api_key)
        self.base_url = "https://analyticsreporting.googleapis.com/v4/reports:batchGet"
        self.view_id = view_id
    
    def collect_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Collect UTM tracking data from Google Analytics"""
        try:
            # Mock data structure for demonstration
            # In production, this would make actual API calls
            utm_data = {
                'sessions': 1250,
                'users': 980,
                'pageviews': 3400,
                'bounce_rate': 0.35,
                'avg_session_duration': 145.6,
                'conversions': 45,
                'conversion_rate': 0.036,
                'utm_campaigns': {
                    'erify-supreme4-launch': {
                        'sessions': 450,
                        'conversions': 18
                    },
                    'erify-vip-referral': {
                        'sessions': 320,
                        'conversions': 15
                    },
                    'erify-luxury-fintech': {
                        'sessions': 280,
                        'conversions': 8
                    },
                    'erify-neon-crown-series': {
                        'sessions': 200,
                        'conversions': 4
                    }
                }
            }
            return utm_data
        except Exception as e:
            print(f"Error collecting Google Analytics data: {e}")
            return {}

class SocialMediaCollector(DataCollector):
    """Collect engagement metrics from social media platforms"""
    
    def __init__(self, platform: str, api_key: str, account_id: str):
        super().__init__(api_key)
        self.platform = platform
        self.account_id = account_id
        self._set_base_url()
    
    def _set_base_url(self):
        """Set the base URL based on platform"""
        urls = {
            'twitter': 'https://api.twitter.com/2',
            'linkedin': 'https://api.linkedin.com/v2',
            'facebook': 'https://graph.facebook.com/v18.0'
        }
        self.base_url = urls.get(self.platform, '')
    
    def collect_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Collect engagement data from social media platform"""
        try:
            # Mock data structure for demonstration
            # In production, this would make actual API calls to each platform
            engagement_data = {
                'platform': self.platform,
                'likes': 450,
                'comments': 89,
                'shares': 156,
                'clicks': 234,
                'impressions': 15600,
                'reach': 12400,
                'engagement_rate': 0.047,
                'top_posts': [
                    {
                        'id': 'post_1',
                        'content': 'ERIFY Supreme 4PW Crown Seal Launch',
                        'likes': 120,
                        'shares': 45,
                        'engagement_rate': 0.065
                    },
                    {
                        'id': 'post_2',
                        'content': 'VIP Referral Program Announcement',
                        'likes': 98,
                        'shares': 32,
                        'engagement_rate': 0.052
                    }
                ]
            }
            return engagement_data
        except Exception as e:
            print(f"Error collecting {self.platform} data: {e}")
            return {}

class ERIVOXCollector(DataCollector):
    """Collect engagement metrics from ERIVOX platform"""
    
    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.base_url = "https://api.erivox.com/v1"
    
    def collect_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Collect engagement data from ERIVOX platform"""
        try:
            # Mock data structure for ERIVOX platform
            erivox_data = {
                'platform': 'erivox',
                'active_users': 890,
                'posts': 156,
                'interactions': 1240,
                'voice_messages': 89,
                'live_sessions': 12,
                'engagement_rate': 0.078,
                'growth_metrics': {
                    'new_users': 45,
                    'user_retention': 0.84,
                    'daily_active_users': 340
                }
            }
            return erivox_data
        except Exception as e:
            print(f"Error collecting ERIVOX data: {e}")
            return {}

class DataAggregator:
    """Aggregate data from multiple collectors"""
    
    def __init__(self):
        self.collectors = []
    
    def add_collector(self, collector: DataCollector):
        """Add a data collector"""
        self.collectors.append(collector)
    
    def collect_all_data(self, start_date: datetime, end_date: datetime) -> Dict[str, Any]:
        """Collect data from all registered collectors"""
        aggregated_data = {
            'collection_date': datetime.now().isoformat(),
            'period': {
                'start_date': start_date.isoformat(),
                'end_date': end_date.isoformat()
            },
            'utm_data': {},
            'social_media_data': {},
            'erivox_data': {}
        }
        
        for collector in self.collectors:
            try:
                data = collector.collect_data(start_date, end_date)
                
                if isinstance(collector, GoogleAnalyticsCollector):
                    aggregated_data['utm_data'] = data
                elif isinstance(collector, SocialMediaCollector):
                    platform = data.get('platform', 'unknown')
                    aggregated_data['social_media_data'][platform] = data
                elif isinstance(collector, ERIVOXCollector):
                    aggregated_data['erivox_data'] = data
                    
            except Exception as e:
                print(f"Error collecting data from {type(collector).__name__}: {e}")
        
        return aggregated_data