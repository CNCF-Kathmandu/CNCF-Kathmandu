"""
CNCF Kathmandu Community Website
A community website for Cloud Native Computing Foundation (CNCF) Kathmandu Chapter
"""

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import yaml
import os

app = FastAPI(
    title="CNCF Kathmandu",
    description="Official website for CNCF Kathmandu Community",
    version="1.0.0"
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Load data from YAML
with open("data.yaml", "r") as f:
    data = yaml.safe_load(f)

events_db = data.get("events_db", [])
team_members = data.get("team_members", [])
resources = data.get("resources", [])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page displaying community information"""
    context = {
        "request": request,
        "title": "CNCF Kathmandu - Home",
        "community_name": "CNCF Kathmandu",
        "tagline": "Building the Future of Cloud Native Computing",
        "upcoming_events": [e for e in events_db if e["status"] == "upcoming"][:3]
    }
    return templates.TemplateResponse("index.html", context)


@app.post("/subscribe", response_class=HTMLResponse)
async def subscribe(request: Request, name: str = Form(...), email: str = Form(...)):
    """
    Handles newsletter signup form submissions.
    Currently just displays a confirmation message.
    """
    # In production, this would save to a database or mailing list
    context = {
        "request": request,
        "title": "CNCF Kathmandu - Home",
        "community_name": "CNCF Kathmandu",
        "tagline": "Building the Future of Cloud Native Computing",
        "upcoming_events": [e for e in events_db if e["status"] == "upcoming"][:3],
        "message": f"Thank you {name}! You've been subscribed with {email}."
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    """About page with community information"""
    context = {
        "request": request,
        "title": "About - CNCF Kathmandu",
        "team_members": team_members,
        "description": "We are a community of cloud native enthusiasts in Kathmandu, Nepal. Our mission is to promote cloud native technologies and help developers learn and grow together."
    }
    return templates.TemplateResponse("about.html", context)


@app.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    """Events listing page"""
    context = {
        "request": request,
        "title": "Events - CNCF Kathmandu",
        "events": events_db
    }
    return templates.TemplateResponse("events.html", context)


@app.get("/resources", response_class=HTMLResponse)
async def resources_page(request: Request):
    """Resources page"""
    context = {
        "request": request,
        "title": "Resources - CNCF Kathmandu",
        "resources": resources
    }
    return templates.TemplateResponse("resources.html", context)


@app.get("/contact", response_class=HTMLResponse)
async def contact_get(request: Request):
    """Contact page (GET)"""
    context = {
        "request": request,
        "title": "Contact - CNCF Kathmandu",
        "message": None
    }
    return templates.TemplateResponse("contact.html", context)


@app.post("/contact", response_class=HTMLResponse)
async def contact_post(request: Request, name: str = Form(...), 
                       email: str = Form(...), message: str = Form(...)):
    """Contact page (POST)"""
    # In production, this would send an email or save to database
    context = {
        "request": request,
        "title": "Contact - CNCF Kathmandu",
        "message": "Thank you for your message! We'll get back to you soon."
    }
    return templates.TemplateResponse("contact.html", context)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
