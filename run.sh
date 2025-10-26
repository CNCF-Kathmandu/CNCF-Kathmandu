#!/bin/bash
# Quick start script for CNCF Kathmandu Website

echo "🚀 Starting CNCF Kathmandu Website..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Run the application
echo "✅ Starting server at http://localhost:8000"
echo "📖 Visit http://localhost:8000/docs for API documentation"
echo ""

uvicorn main:app --reload

