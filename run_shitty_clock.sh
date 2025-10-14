#!/bin/bash

# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                                                           ║
# ║                    🕐 THE SHITTY CLOCK APPLICATION 🕐                      ║
# ║                                                                           ║
# ║  Licensed under the Overprotective License (OPL-∞)                       ║
# ║  "All rights aggressively reserved. Including the right to tell time."   ║
# ║                                                                           ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

# Set terminal title (works on most terminals)
echo -e "\033]0;The Shitty Clock Application - Licensed Under OPL-∞\007"

# Colors for better output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${CYAN}"
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║                    🕐 THE SHITTY CLOCK APPLICATION 🕐                      ║"
echo "║                                                                           ║"
echo "║  Licensed under the Overprotective License (OPL-∞)                       ║"
echo "║  \"All rights aggressively reserved. Including the right to tell time.\"   ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python is installed
if ! command_exists python3 && ! command_exists python; then
    echo -e "${RED}🚨 ERROR: Python is not installed or not in PATH${NC}"
    echo
    echo "Please install Python 3.6+ from https://python.org"
    echo "Or install via package manager:"
    echo "  • Ubuntu/Debian: sudo apt install python3"
    echo "  • CentOS/RHEL: sudo yum install python3"
    echo "  • macOS: brew install python3"
    echo "  • Arch Linux: sudo pacman -S python"
    echo
    echo -e "${YELLOW}⚖️  LEGAL NOTICE:${NC}"
    echo "   This error constitutes a violation of Article I, Clause 1"
    echo "   \"Failure to have Python installed is prohibited use\""
    echo
    read -p "Press Enter to exit..."
    exit 1
fi

# Determine Python command
PYTHON_CMD=""
if command_exists python3; then
    PYTHON_CMD="python3"
elif command_exists python; then
    PYTHON_CMD="python"
fi

# Check if the Python script exists
if [ ! -f "src/shitty_clock.py" ]; then
    echo -e "${RED}🚨 ERROR: shitty_clock.py not found in src/ directory${NC}"
    echo
    echo -e "${YELLOW}⚖️  LEGAL NOTICE:${NC}"
    echo "   This error violates Article VIII, Clause 16"
    echo "   \"Missing source files constitute unauthorized modification\""
    echo
    read -p "Press Enter to exit..."
    exit 1
fi

echo -e "${GREEN}✅ Python detected: $($PYTHON_CMD --version)${NC}"
echo -e "${GREEN}✅ Source files found${NC}"
echo
echo -e "${YELLOW}⚠️  WARNING: Unauthorized execution detected!${NC}"
echo "   You are about to violate approximately 17 clauses of the OPL-∞ license"
echo
echo -e "${PURPLE}📋 License violations that will occur:${NC}"
echo "   • Article I, Clause 1 (Prohibited Use)"
echo "   • Article VI, Clause 13 (Temporal Restrictions)"
echo "   • Article IX, Clause 17 (License Incompatibility)"
echo "   • The vibes"
echo
echo -e "${CYAN}💳 Trial period: 5 minutes${NC}"
echo -e "${CYAN}💰 After trial: \$999.99 + \$49.99/hour + unauthorized use fees${NC}"
echo
echo -e "${BLUE}Press Enter to continue (and accept the consequences)...${NC}"
read -r

echo
echo -e "${GREEN}🚀 Launching The Shitty Clock Application...${NC}"
echo "   Loading legal disclaimers..."
echo "   Calculating unauthorized use fees..."
echo "   Preparing countdown timer..."
echo

# Run the Python application
$PYTHON_CMD src/shitty_clock.py

# After the application exits
echo
echo -e "${RED}"
echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                           ║"
echo "║                    ⚠️  APPLICATION TERMINATED  ⚠️                        ║"
echo "║                                                                           ║"
echo "║  You have violated Article I, Clause 1 by exiting the application.      ║"
echo "║  This constitutes unauthorized termination of licensed software.        ║"
echo "║                                                                           ║"
echo "║  Your violation has been logged.                                         ║"
echo "║  (Not really. We don't track anything. But you should feel bad.)        ║"
echo "║                                                                           ║"
echo "║  Please report to 404 Not Found Street for processing.                   ║"
echo "║                                                                           ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo
echo -e "${BLUE}Press Enter to exit...${NC}"
read -r
