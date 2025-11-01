# CNCF Kathmandu Community Website 🌐

A community website for the Cloud Native Computing Foundation (CNCF) Kathmandu Chapter, built with FastAPI. This project is designed for Hacktoberfest participation, welcoming contributors of all skill levels.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Jinja2 Templates**: Dynamic HTML rendering
- **Modern UI**: Responsive design with beautiful styling
- **Docker Support**: Easy deployment with Docker
- **Testing**: Comprehensive test suite with pytest
- **CI/CD Ready**: GitHub Actions workflows for tests and linting
- **Community Focus**: Built for the CNCF Kathmandu community

## 📁 Project Structure

```
.
├── main.py                      # Main FastAPI application
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker configuration
├── docker-compose.yml           # Docker Compose setup
├── pytest.ini                  # Pytest configuration
├── conftest.py                 # Pytest fixtures
├── templates/                   # Jinja2 HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── events.html
│   ├── resources.html
│   └── contact.html
├── static/                      # Static files (CSS, JS, images)
│   └── css/
│       └── style.css
├── tests/                       # Test suite
│   ├── __init__.py
│   └── test_main.py
└── .github/
    └── workflows/
        ├── tests.yml            # CI test workflow
        └── lint.yml             # CI lint workflow
```

## 🛠️ Getting Started

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (optional)
- Git

### Installation

#### Using Python

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cncf-kathmandu.git
cd cncf-kathmandu
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

Visit http://localhost:8000 in your browser.

#### Using Docker

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cncf-kathmandu.git
cd cncf-kathmandu
```

2. Build and run with Docker Compose:
```bash
docker-compose up --build
```

Visit http://localhost:8000 in your browser.

## 🤝 Contributing

This project is open for Hacktoberfest contributions! We welcome beginners and experienced developers alike. Follow these steps to contribute:

1. Fork the repository
2. Create a branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

### Code of Conduct

- Be respectful and inclusive
- Help beginners learn
- Write clean, readable code
- Follow existing code style


## 🧪 Testing

The project includes a comprehensive test suite using pytest. To run tests:

```bash
# Install test dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run tests with coverage report
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_main.py

# Run tests with verbose output
pytest -v
```

View HTML coverage report:
```bash
# After running pytest --cov-report=html
open htmlcov/index.html
```

## Deployment

Need to setup dockerhub

1. Check .github/workflows/pipeline.yml --> check the recent deployment and click on it
Then, re-run all the jobs.

2. Create repository secrets under the repo settings with: DOCKER_USER, DOCKER_PASSWORD

Create docker password using dockerhub

3. This deployment worked on docker automation and checks for image vulnerabilities scans as well


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI community
- CNCF Global for inspiration
- All contributors

## 📞 Contact

- **Website**: [CNCF Kathmandu](http://localhost:8000)
- **GitHub**: [Your Repository](https://github.com/yourusername/cncf-kathmandu)
- **Community**: Join our Slack/Discord

## 🌟 Contributors

Thank you to all contributors! You make this project awesome.

<!-- Add contributors as they submit PRs -->

---

**Happy Hacking! 🎉**

*This project is perfect for Hacktoberfest. Start with beginner-friendly issues and work your way up!*

