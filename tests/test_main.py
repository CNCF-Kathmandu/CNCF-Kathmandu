"""
Unit tests for main FastAPI application
"""
import pytest
from fastapi.testclient import TestClient


class TestHomePage:
    """Tests for the home page route"""
    
    def test_home_page_status_code(self, client):
        """Test that home page returns 200 status code"""
        response = client.get("/")
        assert response.status_code == 200
    
    def test_home_page_content(self, client):
        """Test that home page contains expected content"""
        response = client.get("/")
        assert b"CNCF Kathmandu" in response.content
        assert b"Welcome to CNCF Kathmandu" in response.content


class TestAboutPage:
    """Tests for the about page route"""
    
    def test_about_page_status_code(self, client):
        """Test that about page returns 200 status code"""
        response = client.get("/about")
        assert response.status_code == 200
    
    def test_about_page_content(self, client):
        """Test that about page contains expected content"""
        response = client.get("/about")
        assert b"About CNCF Kathmandu" in response.content


class TestEventsPage:
    """Tests for the events page route"""
    
    def test_events_page_status_code(self, client):
        """Test that events page returns 200 status code"""
        response = client.get("/events")
        assert response.status_code == 200
    
    def test_events_page_content(self, client):
        """Test that events page contains expected content"""
        response = client.get("/events")
        assert b"Events" in response.content


class TestResourcesPage:
    """Tests for the resources page route"""
    
    def test_resources_page_status_code(self, client):
        """Test that resources page returns 200 status code"""
        response = client.get("/resources")
        assert response.status_code == 200
    
    def test_resources_page_content(self, client):
        """Test that resources page contains expected content"""
        response = client.get("/resources")
        assert b"Resources" in response.content

class TestSpeakersPage:
    """Tests for the speakers page route"""

    def test_speakers_page_status_code(self, client):
        """Test that speakers page returns 200 status code"""
        response = client.get("/speakers")
        assert response.status_code == 200

    def test_speakers_page_content(self, client):
        """Test that speakers page contains expected content"""
        response = client.get("/speakers")
        assert b"Meet Our Speakers" in response.content
        assert b"Community Voices" in response.content

class TestContactPage:
    """Tests for the contact page route"""
    
    def test_contact_get_status_code(self, client):
        """Test that contact GET returns 200 status code"""
        response = client.get("/contact")
        assert response.status_code == 200
    
    def test_contact_get_content(self, client):
        """Test that contact page contains expected content"""
        response = client.get("/contact")
        assert b"Contact Us" in response.content
    
    def test_contact_post_success(self, client):
        """Test that contact form submission works"""
        form_data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message"
        }
        response = client.post("/contact", data=form_data)
        assert response.status_code == 200
        assert b"Thank you for your message" in response.content
    
    def test_contact_post_missing_fields(self, client):
        """Test that contact form validation works"""
        form_data = {
            "name": "Test User",
            "email": "test@example.com"
            # message is missing
        }
        # FastAPI will raise a validation error
        with pytest.raises(Exception):
            client.post("/contact", data=form_data)


class TestStaticFiles:
    """Tests for static file serving"""
    
    def test_static_css_file(self, client):
        """Test that CSS file is accessible"""
        response = client.get("/static/css/style.css")
        assert response.status_code == 200
        assert b"body {" in response.content or b":root {" in response.content


class TestAPIResponseFormat:
    """Tests for API response format"""
    
    def test_html_response(self, client):
        """Test that routes return HTML content"""
        response = client.get("/")
        assert "text/html" in response.headers["content-type"]
    
    def test_navigation_links(self, client):
        """Test that navigation links are present in HTML"""
        response = client.get("/")
        html = response.text
        assert 'href="/"' in html
        assert 'href="/about"' in html
        assert 'href="/events"' in html
        assert 'href="/speakers"' in html
        assert 'href="/resources"' in html
        assert 'href="/contact"' in html


class TestSampleData:
    """Tests for sample data structure"""
    
    def test_events_data_present(self, client):
        """Test that events data is displayed on events page"""
        response = client.get("/events")
        # Check if sample events are present
        assert b"Kubernetes" in response.content or b"Docker" in response.content
    
    def test_team_members_present(self, client):
        """Test that team members data is displayed on about page"""
        response = client.get("/about")
        assert b"Organizer" in response.content or b"Co-Organizer" in response.content
