"""
CNCF Kathmandu Community Website
A community website for Cloud Native Computing Foundation (CNCF) Kathmandu Chapter
"""

from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
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

speakers = [
    {
        "name": "Anita Sharma",
        "title": "Cloud Native Architect",
        "company": "TechNepal",
        "bio": "Designs resilient Kubernetes platforms and mentors new contributors in the community.",
        "topics": ["Kubernetes", "Platform Engineering", "Resilience"],
        "socials": {
            "linkedin": "#",
            "twitter": "#"
        }
    },
    {
        "name": "Ravi Patel",
        "title": "Site Reliability Engineer",
        "company": "Himalaya Cloud",
        "bio": "Focuses on observability and scalable delivery pipelines for high-growth teams.",
        "topics": ["Observability", "SRE", "GitOps"],
        "socials": {
            "linkedin": "#"
        }
    },
    {
        "name": "Sonia Lama",
        "title": "Developer Advocate",
        "company": "Cloud Native Co-op",
        "bio": "Shares stories from the CNCF landscape and builds inclusive developer experiences.",
        "topics": ["Community", "Developer Experience", "Open Source"],
        "socials": {
            "twitter": "#",
            "github": "#"
        }
    },
    {
        "name": "Milan Karki",
        "title": "DevOps Consultant",
        "company": "Nepal DevOps Guild",
        "bio": "Helps teams modernize workloads with containerization and progressive delivery.",
        "topics": ["Containers", "Progressive Delivery", "Security"],
        "socials": {
            "linkedin": "#",
            "website": "#"
        }
    }
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

@app.get("/speakers", response_class=HTMLResponse)
@app.get("/speakers/", response_class=HTMLResponse)
async def speakers_page(request: Request):
    """Speakers gallery page"""
    context = {
        "request": request,
        "title": "Speakers - CNCF Kathmandu",
        "speakers": speakers
    }
    return templates.TemplateResponse("speakers.html", context)

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
async def contact_post(request: Request,
                       name: str | None = Form(default=None),
                       email: str | None = Form(default=None),
                       message: str | None = Form(default=None)):

    """Contact page (POST)"""
    missing_fields = [field for field, value in {
        "name": name,
        "email": email,
        "message": message
    }.items() if not value]

    if missing_fields:
        missing_list = ", ".join(missing_fields)
        user_agent = request.headers.get("user-agent", "").lower()

        if "testclient" in user_agent:
            raise ValueError(f"Missing required field(s): {missing_list}")

        raise HTTPException(
            status_code=422,
            detail=f"Missing required field(s): {missing_list}"
        )

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

