# Contributing to CNCF Kathmandu Website

Thank you for your interest in contributing to the CNCF Kathmandu community website! This document provides guidelines and instructions for contributing.

## Getting Started

1. **Fork the Repository**
   - Click the "Fork" button on GitHub
   - Clone your fork to your local machine

2. **Set Up Development Environment**
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/cncf-kathmandu.git
   cd cncf-kathmandu
   
   # Create and activate virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the application
   python main.py
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Contribution Guidelines

### Code Style

- Follow PEP 8 (Python style guide)
- Use meaningful variable and function names
- Keep functions small and focused
- Add comments for complex logic
- Follow existing code structure and patterns

### Commit Messages

Write clear, descriptive commit messages:
```bash
# Good
git commit -m "Add event search functionality"

# Better
git commit -m "feat: Add event search functionality with filtering"

# Bad
git commit -m "changes"
```

### Pull Request Process

1. **Push Your Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open a Pull Request**
   - Provide a clear title
   - Describe what you changed and why
   - Link any related issues
   - Add screenshots if UI changes

3. **Respond to Feedback**
   - Be open to suggestions
   - Make requested changes
   - Keep discussions respectful

## Issue Types

### 🐛 Bug Fixes
- Fix a specific bug or issue
- Include reproduction steps
- Test your fix thoroughly

### ✨ New Features
- Add functionality to the website
- Keep features focused and useful
- Consider backward compatibility

### 📚 Documentation
- Improve existing docs
- Add missing documentation
- Fix typos and grammar

### 🔧 Refactoring
- Improve code structure
- Optimize performance
- Clean up code

## Testing

Before submitting your pull request:

1. Test your changes locally
2. Make sure the website runs without errors
3. Check all pages and features
4. Test on different browsers if possible

## Beginner-Friendly Tasks

Start with these easy issues:
- Fix typos in documentation
- Add missing alt text to images
- Improve CSS styling
- Add comments to code
- Create new HTML pages

## Questions?

- Open an issue for questions
- Join our community Slack
- Contact the maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome new contributors
- Give constructive feedback
- Focus on what's best for the community

Thank you for contributing! 🎉

