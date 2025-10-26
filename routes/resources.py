from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.data import resources

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/resources", response_class=HTMLResponse)
async def resources_page(request: Request):
    """Resources page"""
    context = {
        "request": request,
        "title": "Resources - CNCF Kathmandu",
        "resources": resources
    }
    return templates.TemplateResponse("resources.html", context)
