"""
Pytest configuration and fixtures for CNCF Kathmandu Website
"""
import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    """Create a test client for the application"""
    return TestClient(app)


@pytest.fixture
def sample_event():
    """Sample event data for testing"""
    return {
        "id": 1,
        "title": "Kubernetes Workshop",
        "date": "2024-11-15",
        "speaker": "John Doe",
        "description": "Learn Kubernetes from scratch",
        "status": "upcoming"
    }


@pytest.fixture
def sample_team_member():
    """Sample team member data for testing"""
    return {
        "name": "John Doe",
        "role": "Organizer",
        "bio": "Cloud Native enthusiast"
    }

