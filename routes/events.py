from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.data import events_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/events", response_class=HTMLResponse)
async def events(request: Request):
    """Events listing page"""
    context = {
        "request": request,
        "title": "Events - CNCF Kathmandu",
        "events": events_db
    }
    return templates.TemplateResponse("events.html", context)

