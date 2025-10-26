from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/contact", response_class=HTMLResponse)
async def contact_get(request: Request):
    """Contact page (GET)"""
    context = {
        "request": request,
        "title": "Contact - CNCF Kathmandu",
        "message": None
    }
    return templates.TemplateResponse("contact.html", context)
