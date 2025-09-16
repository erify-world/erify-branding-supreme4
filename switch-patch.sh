#!/usr/bin/env bash
# ERIFY Elite Launch Automation - Manual Patch Switcher
# Quick script to switch between simulation and production modes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR" && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}============================================${NC}"
    echo -e "${BLUE} ERIFY Elite Launch Automation Switcher${NC}"
    echo -e "${BLUE}============================================${NC}"
}

print_mode_info() {
    local mode=$1
    echo -e "\n${YELLOW}📋 $mode Mode Configuration:${NC}"
    
    if [ "$mode" = "Simulation" ]; then
        echo "  🔬 Slack: #erify-test"
        echo "  🔬 Discord: Private test server"
        echo "  🔬 Email: test@erify.com"
        echo "  🔬 GitHub: launch-sim-test branch"
    else
        echo "  🚀 Slack: #erify-announcements"
        echo "  🚀 Discord: Live community server"
        echo "  🚀 Email: stakeholders@erify.com"
        echo "  🚀 GitHub: main branch"
    fi
}

apply_simulation_patch() {
    echo -e "\n${YELLOW}🧪 Applying Simulation Patch...${NC}"
    
    export ERIFY_SIMULATION_MODE=true
    export ERIFY_PRODUCTION_MODE=false
    export SLACK_CHANNEL="#erify-test"
    export EMAIL_TARGET="test@erify.com"
    export DISCORD_TARGET="test-server"
    export TARGET_BRANCH="launch-sim-test"
    
    print_mode_info "Simulation"
    
    echo -e "\n${BLUE}📝 Updating README.md...${NC}"
    python3 "$REPO_ROOT/.github/scripts/update-readme.py"
    
    echo -e "${GREEN}✅ Simulation patch applied successfully!${NC}"
    echo -e "${GREEN}🔬 System is now in TESTING mode${NC}"
}

apply_production_patch() {
    echo -e "\n${RED}⚠️  WARNING: Applying Production Patch${NC}"
    echo -e "${RED}This will switch to LIVE production mode!${NC}"
    
    read -p "Are you sure you want to continue? (type 'CONFIRM' to proceed): " confirmation
    
    if [ "$confirmation" != "CONFIRM" ]; then
        echo -e "${YELLOW}❌ Production patch application cancelled${NC}"
        return 1
    fi
    
    echo -e "\n${YELLOW}🚀 Applying Production Patch...${NC}"
    
    export ERIFY_SIMULATION_MODE=false
    export ERIFY_PRODUCTION_MODE=true
    export SLACK_CHANNEL="#erify-announcements"
    export EMAIL_TARGET="stakeholders@erify.com"
    export DISCORD_TARGET="live-community"
    export TARGET_BRANCH="main"
    
    print_mode_info "Production"
    
    echo -e "\n${BLUE}📝 Updating README.md...${NC}"
    python3 "$REPO_ROOT/.github/scripts/update-readme.py"
    
    echo -e "${GREEN}✅ Production patch applied successfully!${NC}"
    echo -e "${GREEN}🚀 System is now in LIVE production mode${NC}"
}

show_current_mode() {
    echo -e "\n${BLUE}📊 Current Mode Status:${NC}"
    
    if grep -q "🧪 ERIFY Elite Launch - Simulation Mode" "$REPO_ROOT/README.md"; then
        echo -e "${GREEN}Current Mode: 🧪 Simulation${NC}"
        print_mode_info "Simulation"
    elif grep -q "🚀 ERIFY Elite Launch - LIVE" "$REPO_ROOT/README.md"; then
        echo -e "${GREEN}Current Mode: 🚀 Production${NC}"
        print_mode_info "Production"
    else
        echo -e "${YELLOW}Current Mode: 📄 No automation mode detected${NC}"
    fi
}

run_validation() {
    echo -e "\n${BLUE}🔍 Running validation tests...${NC}"
    python3 "$REPO_ROOT/test-automation.py"
}

show_menu() {
    echo -e "\n${BLUE}Select an option:${NC}"
    echo "1) 🧪 Apply Simulation Patch (Safe Testing)"
    echo "2) 🚀 Apply Production Patch (Live Launch)"  
    echo "3) 📊 Show Current Mode"
    echo "4) 🔍 Run Validation Tests"
    echo "5) 📚 Show Usage Guide"
    echo "6) ❌ Exit"
    echo ""
}

show_usage_guide() {
    echo -e "\n${BLUE}📚 Usage Guide:${NC}"
    echo ""
    echo -e "${YELLOW}Simulation Mode:${NC}"
    echo "  - Safe for testing and development"
    echo "  - Uses test channels and recipients"
    echo "  - Updates launch-sim-test branch"
    echo "  - No impact on production systems"
    echo ""
    echo -e "${YELLOW}Production Mode:${NC}"
    echo "  - LIVE production environment"
    echo "  - Sends to real channels and stakeholders"
    echo "  - Updates main branch"
    echo "  - Requires confirmation to apply"
    echo ""
    echo -e "${YELLOW}GitHub Actions:${NC}"
    echo "  - Go to Actions tab > ERIFY Elite Launch Automation"
    echo "  - Click 'Run workflow'"
    echo "  - Select mode and click 'Run workflow'"
    echo ""
    echo -e "${YELLOW}Manual Testing:${NC}"
    echo "  - Use this script for local testing"
    echo "  - Run validation tests before deployment"
    echo "  - Always test in simulation mode first"
}

main() {
    print_header
    
    while true; do
        show_menu
        read -p "Enter your choice (1-6): " choice
        
        case $choice in
            1)
                apply_simulation_patch
                ;;
            2)
                apply_production_patch
                ;;
            3)
                show_current_mode
                ;;
            4)
                run_validation
                ;;
            5)
                show_usage_guide
                ;;
            6)
                echo -e "\n${GREEN}👋 Goodbye! Stay ERIFY Elite! 💎${NC}"
                exit 0
                ;;
            *)
                echo -e "${RED}❌ Invalid option. Please choose 1-6.${NC}"
                ;;
        esac
        
        echo -e "\n${BLUE}Press Enter to continue...${NC}"
        read
    done
}

# Check if we're in the right directory
if [ ! -f "$REPO_ROOT/.github/workflows/erify-elite-launch-automation.yml" ]; then
    echo -e "${RED}❌ Error: This script must be run from the repository root directory${NC}"
    echo -e "${RED}   Make sure you're in the erify-branding-supreme4 directory${NC}"
    exit 1
fi

# Run main function
main