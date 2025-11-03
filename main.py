"""
CNCF Kathmandu Community Website
A community website for Cloud Native Computing Foundation (CNCF) Kathmandu Chapter
"""

from fastapi import BackgroundTasks, FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from email_validator import validate_email, EmailNotValidError

from tasks import send_welcome_email
from typing import Optional
import os

# Import all constants from the constants.py file
import constants

app = FastAPI(
    title=constants.APP_TITLE,
    description=constants.APP_DESCRIPTION,
    version=constants.APP_VERSION,
)

# Mount static files
app.mount(
    constants.STATIC_URL_PATH,
    StaticFiles(directory=constants.STATIC_DIR),
    name=constants.STATIC_NAME,
)

# Templates
templates = Jinja2Templates(directory=constants.TEMPLATES_DIR)

# Sample data storage (in production, this would be a database)
events_db = [
    {
        "id": 1,
        "title": "Kubernetes Workshop",
        "date": "2024-11-15",
        "speaker": "John Doe",
        "description": "Learn Kubernetes from scratch",
        "status": constants.EventStatus.UPCOMING,
    },
    {
        "id": 2,
        "title": "Docker Deep Dive",
        "date": "2024-10-20",
        "speaker": "Jane Smith",
        "description": "Advanced Docker concepts",
        "status": constants.EventStatus.COMPLETED,
    },
]

# Sample team members with random names, roles, and bios
team_members = [
    {"name": "John Doe", "role": "Organizer", "bio": "Cloud Native enthusiast"},
    {"name": "Jane Smith", "role": "Co-Organizer", "bio": "Kubernetes expert"},
    {"name": "Bob Wilson", "role": "Community Lead", "bio": "DevOps advocate"},
]

# Sample resources with random title, link, and type information
resources = [
    {"title": "Getting Started with Kubernetes", "link": "#", "type": "Tutorial"},
    {"title": "Introduction to Cloud Native", "link": "#", "type": "Article"},
    {"title": "CNCF Landscape", "link": "#", "type": "Reference"},
]


# Displays all upcoming events in the home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page displaying community information"""
    upcoming = [
        e
        for e in events_db
        if e["status"] == constants.EventStatus.UPCOMING
    ][: constants.HOME_UPCOMING_EVENTS_LIMIT]

    context = {
        "request": request,
        "title": constants.PageTitles.HOME,
        "year": constants.CURRENT_YEAR,
        "community_name": constants.COMMUNITY_NAME,
        "tagline": constants.PageContent.TAGLINE,
        "upcoming_events": upcoming,
    }
    return templates.TemplateResponse(constants.TemplateFiles.INDEX, context)


# Fills the about page with community information
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page with community information"""
    context = {
        "request": request,
        "title": constants.PageTitles.ABOUT,
        "team_members": team_members,
        "description": constants.PageContent.ABOUT_DESCRIPTION,
    }
    return templates.TemplateResponse(constants.TemplateFiles.ABOUT, context)


# Lists all the events in the listing page
@app.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    """Events listing page"""
    context = {
        "request": request,
        "title": constants.PageTitles.EVENTS,
        "events": events_db,
    }
    return templates.TemplateResponse(constants.TemplateFiles.EVENTS, context)


# This function gets the `resources.html` page
@app.get("/resources", response_class=HTMLResponse)
async def resources_page(request: Request):
    """Resources page"""
    context = {
        "request": request,
        "title": constants.PageTitles.RESOURCES,
        "resources": resources,
    }
    return templates.TemplateResponse(constants.TemplateFiles.RESOURCES, context)


# This functions gets the `contact.html` page
@app.get("/contact", response_class=HTMLResponse)
async def contact_get(request: Request):
    """Contact page (GET)"""
    context = {"request": request, "title": constants.PageTitles.CONTACT, "message": None}
    return templates.TemplateResponse(constants.TemplateFiles.CONTACT, context)


# This function posts the `contact.html` page
@app.post("/contact", response_class=HTMLResponse)
async def contact_post(
    request: Request,
    background_tasks: BackgroundTasks,
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...),
):
    """Contact page (POST)"""
    # In production, this would send an email or save to database
    context = {
        "request": request,
        "title": constants.PageTitles.CONTACT,
        "message": constants.PageContent.CONTACT_SUCCESS_MESSAGE,
        "is_error": False,
    }

    try:
        email_info = validate_email(email, check_deliverability=False)
        email = email_info.normalized

    except EmailNotValidError as e:
        context = {
            "request": request,
            "title": constants.PageTitles.CONTACT,
            "is_error": True,
            "message": str(e),
        }
        return templates.TemplateResponse(constants.TemplateFiles.CONTACT, context)

    background_tasks.add_task(send_welcome_email, email, name)

    return templates.TemplateResponse(constants.TemplateFiles.CONTACT, context)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app, host=constants.SERVER_HOST, port=constants.SERVER_PORT
    )
