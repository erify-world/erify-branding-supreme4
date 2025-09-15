#!/bin/bash

# ERIFY Campaign Reporting System Setup Script
# This script sets up the automated campaign reporting system

set -e

echo "🚀 Setting up ERIFY Campaign Reporting System..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_color() {
    printf "${1}${2}${NC}\n"
}

print_header() {
    echo ""
    print_color $BLUE "===================================================="
    print_color $BLUE "$1"
    print_color $BLUE "===================================================="
    echo ""
}

print_step() {
    print_color $GREEN "✓ $1"
}

print_warning() {
    print_color $YELLOW "⚠ $1"
}

print_error() {
    print_color $RED "✗ $1"
}

# Check if Python is installed
print_header "Checking Prerequisites"

if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    print_step "Python 3 found: $PYTHON_VERSION"
else
    print_error "Python 3 is required but not installed."
    exit 1
fi

if command -v pip3 &> /dev/null; then
    print_step "pip3 found"
else
    print_error "pip3 is required but not installed."
    exit 1
fi

# Create virtual environment
print_header "Setting up Python Environment"

if [ ! -d "venv" ]; then
    print_step "Creating virtual environment..."
    python3 -m venv venv
else
    print_step "Virtual environment already exists"
fi

print_step "Activating virtual environment..."
source venv/bin/activate

print_step "Upgrading pip..."
pip install --upgrade pip

print_step "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
print_header "Creating Directory Structure"

mkdir -p reports
mkdir -p logs
mkdir -p config

print_step "Created reports directory"
print_step "Created logs directory"
print_step "Created config directory"

# Set up configuration
print_header "Configuration Setup"

if [ ! -f ".env" ]; then
    print_step "Creating .env file from template..."
    cp .env.example .env
    print_warning "Please edit .env file with your actual API keys and settings"
else
    print_step ".env file already exists"
fi

# Make scripts executable
print_header "Setting Permissions"

chmod +x reports/generate_daily_report.py
chmod +x reports/generate_weekly_report.py

print_step "Made report scripts executable"

# Test configuration
print_header "Testing Configuration"

cd reports

print_step "Testing daily report configuration..."
if python3 -c "
import sys
sys.path.append('..')
from generate_daily_report import DailyReportGenerator
try:
    generator = DailyReportGenerator()
    print('✓ Daily report configuration loaded successfully')
except Exception as e:
    print(f'✗ Error loading daily report configuration: {e}')
    sys.exit(1)
"; then
    print_step "Daily report configuration test passed"
else
    print_error "Daily report configuration test failed"
fi

print_step "Testing weekly report configuration..."
if python3 -c "
import sys
sys.path.append('..')
from generate_weekly_report import WeeklyReportGenerator
try:
    generator = WeeklyReportGenerator()
    print('✓ Weekly report configuration loaded successfully')
except Exception as e:
    print(f'✗ Error loading weekly report configuration: {e}')
    sys.exit(1)
"; then
    print_step "Weekly report configuration test passed"
else
    print_error "Weekly report configuration test failed"
fi

cd ..

# Create sample cron jobs file
print_header "Automation Setup"

cat > cron_jobs_sample.txt << EOF
# ERIFY Campaign Reporting Cron Jobs
# Add these to your crontab with: crontab -e

# Daily reports at 9:00 AM UTC
0 9 * * * cd $(pwd)/reports && $(pwd)/venv/bin/python generate_daily_report.py >> ../logs/daily_reports.log 2>&1

# Weekly reports at 10:00 AM UTC every Monday  
0 10 * * 1 cd $(pwd)/reports && $(pwd)/venv/bin/python generate_weekly_report.py >> ../logs/weekly_reports.log 2>&1

# Clean up old reports (monthly)
0 2 1 * * find $(pwd)/reports/reports -name "*.json" -mtime +90 -delete >> ../logs/cleanup.log 2>&1
EOF

print_step "Created sample cron jobs file (cron_jobs_sample.txt)"

# Create a test script
cat > test_reports.sh << 'EOF'
#!/bin/bash

echo "🧪 Testing ERIFY Campaign Reports..."

# Activate virtual environment
source venv/bin/activate

# Test daily report
echo "Testing daily report generation..."
cd reports
python3 generate_daily_report.py --test-mode

# Test weekly report
echo "Testing weekly report generation..."
python3 generate_weekly_report.py --test-mode

echo "✅ Report testing completed!"
EOF

chmod +x test_reports.sh
print_step "Created test script (test_reports.sh)"

# Setup complete
print_header "Setup Complete!"

print_color $GREEN "🎉 ERIFY Campaign Reporting System setup completed successfully!"
echo ""
print_color $BLUE "Next Steps:"
echo "1. Edit .env file with your actual API keys and configuration"
echo "2. Run './test_reports.sh' to test the system"
echo "3. Set up automation using GitHub Actions or cron jobs"
echo "4. Monitor reports in the reports/ directory"
echo ""
print_color $YELLOW "Important Files:"
echo "- .env: Configuration file (EDIT THIS!)"
echo "- reports/config.yml: Report configuration"
echo "- cron_jobs_sample.txt: Sample cron jobs for automation"
echo "- test_reports.sh: Test script to verify setup"
echo ""
print_color $BLUE "Documentation:"
echo "- README.md: Complete setup and usage guide"
echo "- scripts/README.md: Detailed technical documentation"
echo ""
print_color $GREEN "For support, visit: https://github.com/erify-world/erify-branding-supreme4"
echo ""

deactivate