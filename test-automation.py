#!/usr/bin/env python3
"""
Test script for ERIFY Elite Launch Automation
Validates the automation system without requiring external API tokens.
"""

import os
import sys
import tempfile
import subprocess
from pathlib import Path


def test_simulation_mode():
    """Test automation in simulation mode."""
    print("🧪 Testing Simulation Mode...")
    
    # Set simulation environment
    env = os.environ.copy()
    env.update({
        'ERIFY_SIMULATION_MODE': 'true',
        'ERIFY_PRODUCTION_MODE': 'false',
        'SLACK_CHANNEL': '#erify-test',
        'EMAIL_TARGET': 'test@erify.com',
        'DISCORD_TARGET': 'test-server',
        'TARGET_BRANCH': 'launch-sim-test'
    })
    
    # Test README update
    result = subprocess.run([
        sys.executable, '.github/scripts/update-readme.py'
    ], env=env, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Simulation mode README update successful")
        return True
    else:
        print(f"❌ Simulation mode README update failed: {result.stderr}")
        return False


def test_production_mode():
    """Test automation in production mode."""
    print("🚀 Testing Production Mode...")
    
    # Set production environment
    env = os.environ.copy()
    env.update({
        'ERIFY_SIMULATION_MODE': 'false',
        'ERIFY_PRODUCTION_MODE': 'true',
        'SLACK_CHANNEL': '#erify-announcements',
        'EMAIL_TARGET': 'stakeholders@erify.com',
        'DISCORD_TARGET': 'live-community',
        'TARGET_BRANCH': 'main'
    })
    
    # Test README update
    result = subprocess.run([
        sys.executable, '.github/scripts/update-readme.py'
    ], env=env, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Production mode README update successful")
        return True
    else:
        print(f"❌ Production mode README update failed: {result.stderr}")
        return False


def test_mode_switching():
    """Test switching between modes."""
    print("🔄 Testing Mode Switching...")
    
    # Read initial README
    with open('README.md', 'r') as f:
        initial_content = f.read()
    
    # Test simulation -> production -> simulation
    sim_success = test_simulation_mode()
    prod_success = test_production_mode()
    sim2_success = test_simulation_mode()
    
    if sim_success and prod_success and sim2_success:
        print("✅ Mode switching test successful")
        return True
    else:
        print("❌ Mode switching test failed")
        return False


def validate_files():
    """Validate that all required files exist and are properly structured."""
    print("📁 Validating File Structure...")
    
    required_files = [
        '.github/workflows/erify-elite-launch-automation.yml',
        '.github/scripts/launch-automation.py',
        '.github/scripts/update-readme.py',
        '.env.simulation.example',
        '.env.production.example',
        'requirements.txt',
        'ERIFY-LAUNCH-AUTOMATION-GUIDE.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        return False
    else:
        print("✅ All required files present")
        return True


def main():
    """Run all validation tests."""
    print("🚀 ERIFY Elite Launch Automation - Validation Tests")
    print("=" * 60)
    
    tests = [
        ("File Structure", validate_files),
        ("Mode Switching", test_mode_switching)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        print("-" * 40)
        try:
            success = test_func()
            results.append(success)
            print(f"✅ {test_name}: {'PASSED' if success else 'FAILED'}")
        except Exception as e:
            print(f"❌ {test_name}: FAILED with error: {e}")
            results.append(False)
    
    print("\n" + "=" * 60)
    print("📊 Test Summary:")
    total_tests = len(results)
    passed_tests = sum(results)
    
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {total_tests - passed_tests}")
    print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    if all(results):
        print("\n🎉 All tests passed! Automation system is ready for deployment.")
        return True
    else:
        print(f"\n⚠️  {total_tests - passed_tests} test(s) failed. Please review and fix issues.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)