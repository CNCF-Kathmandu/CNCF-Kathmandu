"""
CNCF Kathmandu Community Website
A community website for Cloud Native Computing Foundation (CNCF) Kathmandu Chapter
"""

from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from typing import Optional
import os

app = FastAPI(
    title="CNCF Kathmandu",
    description="Official website for CNCF Kathmandu Community",
    version="1.0.0"
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Surface form validation issues to the caller."""
    raise exc

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Sample data storage (in production, this would be a database)
events_db = [
    {
        "id": 1,
        "title": "Kubernetes Workshop",
        "date": "2024-11-15",
        "speaker": "John Doe",
        "description": "Learn Kubernetes from scratch",
        "status": "upcoming"
    },
    {
        "id": 2,
        "title": "Docker Deep Dive",
        "date": "2024-10-20",
        "speaker": "Jane Smith",
        "description": "Advanced Docker concepts",
        "status": "completed"
    }
]

team_members = [
    {"name": "John Doe", "role": "Organizer", "bio": "Cloud Native enthusiast"},
    {"name": "Jane Smith", "role": "Co-Organizer", "bio": "Kubernetes expert"},
    {"name": "Bob Wilson", "role": "Community Lead", "bio": "DevOps advocate"}
]

resources = [
    {"title": "Getting Started with Kubernetes", "link": "#", "type": "Tutorial"},
    {"title": "Introduction to Cloud Native", "link": "#", "type": "Article"},
    {"title": "CNCF Landscape", "link": "#", "type": "Reference"}
]


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

@app.get("/search")
async def search(query: Optional[str] = None, q: Optional[str] = None):
    """Search events and resources by query string."""
    search_term = (query or q or "").strip().lower()

    if not search_term:
        return JSONResponse({"events": [], "resources": []})

    def matches_event(event: dict) -> bool:
        searchable_values = [
            event.get("title", ""),
            event.get("description", ""),
            event.get("speaker", ""),
            event.get("status", ""),
        ]
        return any(search_term in value.lower() for value in searchable_values)

    def matches_resource(resource: dict) -> bool:
        searchable_values = [
            resource.get("title", ""),
            resource.get("type", "")
        ]
        return any(search_term in value.lower() for value in searchable_values)

    matching_events = [event for event in events_db if matches_event(event)][:5]
    matching_resources = [resource for resource in resources if matches_resource(resource)][:5]

    return JSONResponse({
        "events": matching_events,
        "resources": matching_resources
    })

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

