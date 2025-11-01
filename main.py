"""
CNCF Kathmandu Community Website
A community website for Cloud Native Computing Foundation (CNCF) Kathmandu Chapter
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import all_routes # all_routes function defined under routes dir in file __init__.py

app = FastAPI(
    title="CNCF Kathmandu",
    description="Official website for CNCF Kathmandu Community",
    version="1.0.0",
)

year = datetime.datetime.now().year

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

all_routes(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
