from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.data import blog_posts

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/blog", response_class=HTMLResponse)
async def blog_list(request: Request):
    """Blog listing page"""
    # Sort blog posts by date (newest first)
    sorted_posts = sorted(blog_posts, key=lambda x: x["date"], reverse=True)

    context = {
        "request": request,
        "title": "Blog - CNCF Kathmandu",
        "posts": sorted_posts
    }
    return templates.TemplateResponse("blog.html", context)


@router.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    """Individual blog post page"""
    # Find the post by slug
    post = next((p for p in blog_posts if p["slug"] == slug), None)

    if not post:
        raise HTTPException(status_code=404, detail="Blog post not found")

    # Get related posts (same tags, excluding current post)
    related_posts = [
        p for p in blog_posts
        if p["id"] != post["id"] and any(tag in post["tags"] for tag in p["tags"])
    ][:3]

    context = {
        "request": request,
        "title": f"{post['title']} - CNCF Kathmandu Blog",
        "post": post,
        "related_posts": related_posts
    }
    return templates.TemplateResponse("blog.html", context)
