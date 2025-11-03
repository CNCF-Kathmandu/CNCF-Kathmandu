"""
Centralized constants for the CNCF Kathmandu Community Website.
This file contains all magic numbers and strings to promote
reusability, readability, and maintainability.
"""

import datetime

# --- General App Metadata ---
COMMUNITY_NAME = "CNCF Kathmandu"
APP_TITLE = "CNCF Kathmandu"
APP_DESCRIPTION = "Official website for CNCF Kathmandu Community"
APP_VERSION = "1.0.0"
CURRENT_YEAR = datetime.datetime.now().year

# --- Server Configuration ---
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

# --- Directory Configuration ---
STATIC_DIR = "static"
STATIC_URL_PATH = "/static"
STATIC_NAME = "static"
TEMPLATES_DIR = "templates"

# --- Page Titles ---
# Using a class to group related constants
class PageTitles:
    HOME = f"{COMMUNITY_NAME} - Home"
    ABOUT = f"About - {COMMUNITY_NAME}"
    EVENTS = f"Events - {COMMUNITY_NAME}"
    RESOURCES = f"Resources - {COMMUNITY_NAME}"
    CONTACT = f"Contact - {COMMUNITY_NAME}"

# --- Template File Names ---
class TemplateFiles:
    INDEX = "index.html"
    ABOUT = "about.html"
    EVENTS = "events.html"
    RESOURCES = "resources.html"
    CONTACT = "contact.html"

# --- Page Content & Display Strings ---
class PageContent:
    TAGLINE = "Building the Future of Cloud Native Computing"
    ABOUT_DESCRIPTION = "We are a community of cloud native enthusiasts in Kathmandu, Nepal. Our mission is to promote cloud native technologies and help developers learn and grow together."
    CONTACT_SUCCESS_MESSAGE = "Thank you for your message! We'll get back to you soon."

# --- Business Logic Constants ---
class EventStatus:
    UPCOMING = "upcoming"
    COMPLETED = "completed"

HOME_UPCOMING_EVENTS_LIMIT = 3
