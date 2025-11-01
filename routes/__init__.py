from .home import router as home_router
from .about import router as about_router
from .events import router as events_router
from .resources import router as resources_router
from .contact import router as contact_router
from .blog import router as blog_router

def all_routes(app):
    app.include_router(home_router)
    app.include_router(about_router)
    app.include_router(events_router)
    app.include_router(resources_router)
    app.include_router(contact_router)
    app.include_router(blog_router)
