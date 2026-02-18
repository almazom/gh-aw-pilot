#!/bin/bash
# Setup script for GH-AW pilot project

set -e

echo "🚀 GH-AW Pilot Project Setup"
echo "============================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit"
    echo "✅ Git repository initialized"
else
    echo "✅ Git already initialized"
fi

# Check gh CLI
echo ""
echo "🔍 Checking GitHub CLI..."
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) not found"
    echo "   Install from: https://cli.github.com/"
    exit 1
fi
echo "✅ GitHub CLI found"

# Check gh aw extension
echo ""
echo "🔍 Checking GH-AW extension..."
if ! gh aw --version &> /dev/null; then
    echo "📦 Installing GH-AW extension..."
    gh extension install github/gh-aw
    echo "✅ GH-AW extension installed"
else
    echo "✅ GH-AW extension already installed"
    gh aw --version
fi

# Compile workflow
echo ""
echo "🔨 Compiling workflow..."
gh aw compile
echo "✅ Workflow compiled"

# Show results
echo ""
echo "📁 Generated files:"
ls -la .github-agentic/workflows/ 2>/dev/null || echo "   (none yet)"
ls -la package-lock.json 2>/dev/null || echo "   (none yet)"

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create GitHub repo: gh repo create gh-aw-pilot --public --source=. --push"
echo "2. Create an Issue on GitHub"
echo "3. Comment: @agent hello"
echo "4. Watch Actions tab for execution"
