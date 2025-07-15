#!/usr/bin/env python3
"""
Setup script for development environment.
"""
import subprocess
import sys
import os


def run_command(command):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {command}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed: {command}")
        print(f"Error: {e.stderr}")
        return None


def main():
    """Main setup function."""
    print("Setting up development environment...")
    
    # Check if virtual environment exists
    if not os.path.exists(".venv"):
        print("Creating virtual environment...")
        run_command("python -m venv .venv")
    
    # Install dependencies
    print("Installing dependencies...")
    if os.name == 'nt':  # Windows
        run_command(".venv\\Scripts\\pip install -e .")
    else:  # Unix/Linux/macOS
        run_command(".venv/bin/pip install -e .")
    
    print("Setup complete! 🎉")
    print("To activate the virtual environment, run:")
    if os.name == 'nt':
        print("  .venv\\Scripts\\activate")
    else:
        print("  source .venv/bin/activate")


if __name__ == "__main__":
    main() 