from fastapi import FastAPI


app = FastAPI(title="Tarot app API", openapi_url="/openapi.json")

# OPENSEARCH_PORT = os.environ.get("OPENSEARCH_PORT")


@app.get("/", status_code=200)
def root(
) -> dict:
    """
    Root GET
    """
    return (
        {"msg": "Hello World"})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
