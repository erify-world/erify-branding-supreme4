# ERIFY Elite Launch Automation Patches

This repository contains two distinct automation patches for ERIFY Elite launch communications, designed for easy switching between simulation and production modes.

## 🎯 Overview

The automation system provides seamless communication management across multiple platforms:
- **Slack** integration for team notifications
- **Discord** integration for community announcements  
- **Email** integration for stakeholder communications
- **GitHub** integration for documentation updates

## 🔀 Automation Patches

### 🧪 Simulation Patch (ERIFY_SIMULATION_MODE)
Safe testing environment for validating communication workflows:
- **Slack**: Posts to `#erify-test` channel
- **Discord**: Posts to private test server
- **Email**: Sends to `test@erify.com`
- **GitHub**: Updates README on `launch-sim-test` branch

### 🚀 Production Patch (ERIFY_PRODUCTION_MODE)  
Live production environment for actual launch communications:
- **Slack**: Posts to `#erify-announcements` channel
- **Discord**: Posts to live community server
- **Email**: Sends to full stakeholders list (`stakeholders@erify.com`)
- **GitHub**: Updates README on `main` branch

## ⚙️ Setup Instructions

### 1. Configure GitHub Secrets
Set the following secrets in your GitHub repository settings (`Settings > Secrets and variables > Actions`):

```
SLACK_BOT_TOKEN          # Your Slack bot token (xoxb-...)
DISCORD_BOT_TOKEN        # Your Discord bot token
SENDGRID_API_KEY         # Your SendGrid API key for email
```

### 2. Environment Configuration
The system automatically configures based on the selected mode:

**For Simulation Mode:**
```bash
ERIFY_SIMULATION_MODE=true
ERIFY_PRODUCTION_MODE=false
TARGET_BRANCH=launch-sim-test
SLACK_CHANNEL=#erify-test
EMAIL_TARGET=test@erify.com
DISCORD_TARGET=test-server
```

**For Production Mode:**
```bash
ERIFY_SIMULATION_MODE=false  
ERIFY_PRODUCTION_MODE=true
TARGET_BRANCH=main
SLACK_CHANNEL=#erify-announcements
EMAIL_TARGET=stakeholders@erify.com
DISCORD_TARGET=live-community
```

### 3. Branch Setup
Ensure the following branches exist:
- `main` - Production branch
- `launch-sim-test` - Simulation testing branch (created automatically if needed)

## 🚀 Usage

### Manual Execution
1. Go to **Actions** tab in your GitHub repository
2. Select **ERIFY Elite Launch Automation** workflow
3. Click **Run workflow** 
4. Choose your mode:
   - `simulation` - Safe testing mode
   - `production` - Live launch mode
5. Optionally enable **Force run** to bypass schedule restrictions

### Scheduled Execution  
The automation runs automatically at **9:00 AM UTC daily** using the following cron schedule:
```yaml
schedule:
  - cron: '0 9 * * *'
```

### Command Line Testing
For local development and testing:

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variables for simulation
export ERIFY_SIMULATION_MODE=true
export ERIFY_PRODUCTION_MODE=false
export SLACK_CHANNEL="#erify-test"
export EMAIL_TARGET="test@erify.com"
export DISCORD_TARGET="test-server"
export TARGET_BRANCH="launch-sim-test"

# Run the automation script
python .github/scripts/launch-automation.py

# Update README
python .github/scripts/update-readme.py
```

## 🔄 Switching Between Modes

### Via GitHub Actions UI
1. Navigate to **Actions > ERIFY Elite Launch Automation**
2. Click **Run workflow**
3. Select desired mode from dropdown
4. Click **Run workflow**

### Via Environment Variables
Set the appropriate environment variables in your workflow or local environment:

```bash
# Switch to Simulation Mode
export ERIFY_SIMULATION_MODE=true
export ERIFY_PRODUCTION_MODE=false

# Switch to Production Mode  
export ERIFY_SIMULATION_MODE=false
export ERIFY_PRODUCTION_MODE=true
```

## 📊 Monitoring and Logs

### GitHub Actions Logs
- View execution logs in the **Actions** tab
- Each step provides detailed output and status
- Summary report shows successful/failed tasks

### Execution Summary
The automation provides a comprehensive summary including:
- Selected mode and configuration
- Target channels and recipients  
- Success/failure status for each communication channel
- Timestamp and branch information

## 🛡️ Safety Features

### Default Simulation Mode
- System defaults to simulation mode for safety
- Production mode must be explicitly selected
- Environment validation prevents accidental production runs

### Validation Checks
- Token validation before execution
- Channel/recipient verification
- Branch existence validation
- Error handling and rollback capabilities

## 📁 File Structure

```
.github/
├── workflows/
│   └── erify-elite-launch-automation.yml    # Main workflow
└── scripts/
    ├── launch-automation.py                 # Core automation logic
    └── update-readme.py                     # README update script

.env.simulation.example                      # Simulation environment template
.env.production.example                      # Production environment template  
requirements.txt                             # Python dependencies
ERIFY-LAUNCH-AUTOMATION-GUIDE.md            # This guide
```

## 🔧 Customization

### Modifying Messages
Edit the `_get_launch_message()` method in `launch-automation.py` to customize:
- Message content and formatting
- Platform-specific messaging
- Branding and tone

### Adding New Channels
Extend the automation by:
1. Adding new communication methods to `launch-automation.py`
2. Including configuration in environment variables
3. Adding corresponding secrets to GitHub

### Schedule Modification
Update the cron schedule in `erify-elite-launch-automation.yml`:
```yaml
schedule:
  - cron: '0 9 * * *'  # Modify this line
```

## 🚨 Troubleshooting

### Common Issues

**Authentication Errors:**
- Verify all required secrets are set in GitHub repository settings
- Check token permissions and scopes
- Ensure tokens are not expired

**Branch Errors:**
- Verify `launch-sim-test` branch exists or can be created
- Check GitHub token permissions for branch operations
- Ensure target branches are accessible

**Communication Failures:**
- Validate channel names and permissions
- Check API rate limits and quotas
- Verify recipient email addresses and Discord servers

### Debug Mode
Enable debug output by adding environment variable:
```bash
DEBUG=true
```

## 📞 Support

For issues with the automation system:
1. Check GitHub Actions logs for error details
2. Verify all secrets and environment variables are properly configured
3. Test in simulation mode before production deployment
4. Review API documentation for third-party services

---

**ERIFY Elite Launch Automation** - Seamless communication management for luxury fintech launches.