#!/usr/bin/env python3
"""
README Update Script for ERIFY Elite Launch
Updates the README.md file based on the current launch mode.
"""

import os
import sys
from datetime import datetime


class READMEUpdater:
    def __init__(self):
        self.mode = self._get_mode()
        self.readme_path = "README.md"
        
    def _get_mode(self) -> str:
        """Determine the current operation mode."""
        if os.getenv('ERIFY_SIMULATION_MODE', '').lower() == 'true':
            return 'simulation'
        elif os.getenv('ERIFY_PRODUCTION_MODE', '').lower() == 'true':
            return 'production'
        else:
            return 'simulation'
    
    def _get_launch_content(self) -> str:
        """Generate launch content based on mode."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M UTC")
        mode_emoji = "🧪" if self.mode == 'simulation' else "🚀"
        
        if self.mode == 'simulation':
            return f"""
## {mode_emoji} ERIFY Elite Launch - Simulation Mode

**Status**: Testing Phase  
**Last Updated**: {timestamp}  
**Branch**: launch-sim-test  

🔬 **Simulation Mode Active**
- Testing communication channels
- Validating automation pipelines  
- Preparing for production launch

### Test Configuration
- Slack: #erify-test
- Discord: Private test server
- Email: test@erify.com
- GitHub: launch-sim-test branch

---
"""
        else:
            return f"""
## {mode_emoji} ERIFY Elite Launch - LIVE

**Status**: 🎉 **OFFICIALLY LAUNCHED!**  
**Launch Date**: {timestamp}  
**Branch**: main  

🚀 **ERIFY Elite is now live!**
- Elite verification services active
- Full stakeholder communications sent
- Production systems operational

### Production Configuration
- Slack: #erify-announcements
- Discord: Live community server
- Email: Full stakeholders list
- GitHub: main branch

---
"""
    
    def update_readme(self) -> bool:
        """Update the README.md file with launch information."""
        try:
            # Read current README
            if os.path.exists(self.readme_path):
                with open(self.readme_path, 'r', encoding='utf-8') as f:
                    current_content = f.read()
            else:
                current_content = "# README\n\n"
            
            # Generate new launch content
            launch_content = self._get_launch_content()
            
            # Remove any existing launch section
            lines = current_content.split('\n')
            filtered_lines = []
            skip_section = False
            
            for line in lines:
                if line.startswith('## 🧪 ERIFY Elite Launch - Simulation Mode') or \
                   line.startswith('## 🚀 ERIFY Elite Launch - LIVE'):
                    skip_section = True
                elif line.startswith('## ') and skip_section:
                    skip_section = False
                    filtered_lines.append(line)
                elif line.strip() == '---' and skip_section:
                    skip_section = False
                elif not skip_section:
                    filtered_lines.append(line)
            
            # Reconstruct content
            base_content = '\n'.join(filtered_lines).rstrip()
            
            # Add launch content after the main title
            title_line = -1
            for i, line in enumerate(filtered_lines):
                if line.startswith('# '):
                    title_line = i
                    break
            
            if title_line >= 0:
                # Insert after title and any immediate description
                insert_pos = title_line + 1
                while insert_pos < len(filtered_lines) and not filtered_lines[insert_pos].startswith('##'):
                    insert_pos += 1
                
                new_lines = filtered_lines[:insert_pos] + [launch_content] + filtered_lines[insert_pos:]
                new_content = '\n'.join(new_lines)
            else:
                # If no title found, prepend the content
                new_content = base_content + '\n' + launch_content
            
            # Write updated README
            with open(self.readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✅ README.md updated for {self.mode} mode")
            print(f"📝 Launch section added with timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}")
            return True
            
        except Exception as e:
            print(f"❌ Error updating README.md: {str(e)}")
            return False


def main():
    """Main execution function."""
    updater = READMEUpdater()
    success = updater.update_readme()
    
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()