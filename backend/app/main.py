from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
)
from app.api.api import api_router

app = FastAPI(title="Tarot API", openapi_url="/api/openapi.json")


@app.get("/api/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    """
    Get Swagger doc
    :return: HTML Page
    """
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url="/api" + app.swagger_ui_oauth2_redirect_url,
        swagger_favicon_url="#",
    )


@app.get("/api/redoc", include_in_schema=False)
async def redoc_html():
    """
    Redoc Swagger page
    :return: HTML Page
    """
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Redoc",
        redoc_favicon_url="#",
    )

origins = ["http://localhost", "http://frontend:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
def root(
) -> dict:
    """
    Root GET
    """
    return (
        {"msg": "Hello World"})


app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=842, reload=True)
