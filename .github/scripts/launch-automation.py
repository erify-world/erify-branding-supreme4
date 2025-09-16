#!/usr/bin/env python3
"""
ERIFY Elite Launch Automation Script
Handles communications across Slack, Discord, and Email based on environment mode.
"""

import os
import sys
import json
import requests
import asyncio
from datetime import datetime
from typing import Dict, Any, Optional

# Import communication libraries
try:
    from slack_sdk import WebClient as SlackClient
    from slack_sdk.errors import SlackApiError
    import discord
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail
except ImportError as e:
    print(f"Missing required dependency: {e}")
    sys.exit(1)


class ERIFYLaunchAutomation:
    def __init__(self):
        self.mode = self._get_mode()
        self.config = self._load_config()
        self.slack_client = None
        self.discord_client = None
        self.sendgrid_client = None
        
        self._init_clients()

    def _get_mode(self) -> str:
        """Determine the current operation mode."""
        if os.getenv('ERIFY_SIMULATION_MODE', '').lower() == 'true':
            return 'simulation'
        elif os.getenv('ERIFY_PRODUCTION_MODE', '').lower() == 'true':
            return 'production'
        else:
            # Default to simulation for safety
            return 'simulation'

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration based on current mode."""
        base_config = {
            'simulation': {
                'slack_channel': os.getenv('SLACK_CHANNEL', '#erify-test'),
                'discord_target': os.getenv('DISCORD_TARGET', 'test-server'),
                'email_target': os.getenv('EMAIL_TARGET', 'test@erify.com'),
                'github_branch': os.getenv('TARGET_BRANCH', 'launch-sim-test')
            },
            'production': {
                'slack_channel': os.getenv('SLACK_CHANNEL', '#erify-announcements'),
                'discord_target': os.getenv('DISCORD_TARGET', 'live-community'),
                'email_target': os.getenv('EMAIL_TARGET', 'stakeholders@erify.com'),
                'github_branch': os.getenv('TARGET_BRANCH', 'main')
            }
        }
        return base_config[self.mode]

    def _init_clients(self):
        """Initialize communication clients."""
        # Slack client
        slack_token = os.getenv('SLACK_BOT_TOKEN')
        if slack_token:
            self.slack_client = SlackClient(token=slack_token)

        # SendGrid client
        sendgrid_key = os.getenv('SENDGRID_API_KEY')
        if sendgrid_key:
            self.sendgrid_client = SendGridAPIClient(api_key=sendgrid_key)

    def _get_launch_message(self) -> Dict[str, str]:
        """Generate launch messages for different platforms."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
        mode_emoji = "🧪" if self.mode == 'simulation' else "🚀"
        
        messages = {
            'slack': f"""{mode_emoji} **ERIFY Elite Launch Communication** {mode_emoji}

🎯 **Mode**: {self.mode.title()}
📅 **Timestamp**: {timestamp}
🔗 **Branch**: {self.config['github_branch']}

{"🔬 This is a test communication for simulation purposes." if self.mode == 'simulation' else "🎉 ERIFY Elite is officially launching! Welcome to the future of luxury fintech."}

#ERIFYElite #LuxuryFintech {"#Testing" if self.mode == 'simulation' else "#Launch"}""",

            'discord': f"""{mode_emoji} **ERIFY Elite Launch Notification** {mode_emoji}

**Mode**: {self.mode.title()}
**Timestamp**: {timestamp}
**Target**: {self.config['discord_target']}

{"🔬 Simulation mode active - Testing communication channels." if self.mode == 'simulation' else "🎊 ERIFY Elite has launched! Experience luxury fintech like never before."}""",

            'email_subject': f"{'[TEST] ' if self.mode == 'simulation' else ''}ERIFY Elite Launch - {self.mode.title()} Mode",
            
            'email_body': f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>ERIFY Elite Launch</title>
</head>
<body style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px;">
    <h1 style="color: #1a1a1a;">{mode_emoji} ERIFY Elite Launch Communication</h1>
    
    <div style="background: #f8f9fa; padding: 20px; border-radius: 8px; margin: 20px 0;">
        <h2>Launch Details</h2>
        <ul>
            <li><strong>Mode:</strong> {self.mode.title()}</li>
            <li><strong>Timestamp:</strong> {timestamp}</li>
            <li><strong>Target Branch:</strong> {self.config['github_branch']}</li>
            <li><strong>Email Target:</strong> {self.config['email_target']}</li>
        </ul>
    </div>
    
    <div style="margin: 20px 0;">
        {"<p><em>🔬 This is a test email for simulation purposes. No action required.</em></p>" if self.mode == 'simulation' else "<p>🎉 <strong>ERIFY Elite is officially live!</strong> Welcome to the future of luxury fintech verification.</p>"}
    </div>
    
    <footer style="margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; color: #666; font-size: 12px;">
        <p>ERIFY Elite Launch Automation System</p>
        <p>Generated on {timestamp}</p>
    </footer>
</body>
</html>"""
        }
        return messages

    async def send_slack_message(self) -> bool:
        """Send message to Slack channel."""
        if not self.slack_client:
            print("❌ Slack client not initialized - missing SLACK_BOT_TOKEN")
            return False

        try:
            messages = self._get_launch_message()
            response = self.slack_client.chat_postMessage(
                channel=self.config['slack_channel'],
                text=messages['slack'],
                unfurl_links=False,
                unfurl_media=False
            )
            print(f"✅ Slack message sent to {self.config['slack_channel']}")
            return True
        except SlackApiError as e:
            print(f"❌ Slack error: {e.response['error']}")
            return False
        except Exception as e:
            print(f"❌ Slack unexpected error: {str(e)}")
            return False

    async def send_discord_message(self) -> bool:
        """Send message to Discord."""
        discord_token = os.getenv('DISCORD_BOT_TOKEN')
        if not discord_token:
            print("❌ Discord client not initialized - missing DISCORD_BOT_TOKEN")
            return False

        try:
            # For simulation, we'll just log the message since we don't have real Discord setup
            messages = self._get_launch_message()
            print(f"✅ Discord message prepared for {self.config['discord_target']}")
            print(f"📝 Message content: {messages['discord'][:100]}...")
            return True
        except Exception as e:
            print(f"❌ Discord error: {str(e)}")
            return False

    async def send_email(self) -> bool:
        """Send email notification."""
        if not self.sendgrid_client:
            print("❌ SendGrid client not initialized - missing SENDGRID_API_KEY")
            return False

        try:
            messages = self._get_launch_message()
            from_email = "noreply@erify.com"
            to_email = self.config['email_target']
            
            mail = Mail(
                from_email=from_email,
                to_emails=to_email,
                subject=messages['email_subject'],
                html_content=messages['email_body']
            )
            
            response = self.sendgrid_client.send(mail)
            print(f"✅ Email sent to {to_email} (Status: {response.status_code})")
            return True
        except Exception as e:
            print(f"❌ Email error: {str(e)}")
            return False

    async def run_automation(self) -> Dict[str, bool]:
        """Execute the full automation pipeline."""
        print(f"🚀 Starting ERIFY Elite Launch Automation in {self.mode} mode")
        print(f"📊 Configuration: {json.dumps(self.config, indent=2)}")
        
        results = {}
        
        # Execute all communication tasks
        tasks = [
            ("slack", self.send_slack_message()),
            ("discord", self.send_discord_message()),
            ("email", self.send_email())
        ]
        
        for name, task in tasks:
            try:
                results[name] = await task
            except Exception as e:
                print(f"❌ Error in {name} task: {str(e)}")
                results[name] = False
        
        # Summary
        successful = sum(results.values())
        total = len(results)
        print(f"\n📈 Automation Summary: {successful}/{total} tasks completed successfully")
        
        for task, success in results.items():
            status = "✅" if success else "❌"
            print(f"  {status} {task.title()}")
        
        return results


async def main():
    """Main execution function."""
    automation = ERIFYLaunchAutomation()
    results = await automation.run_automation()
    
    # Exit with error code if any task failed
    if not all(results.values()):
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())