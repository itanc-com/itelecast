import uvicorn

if __name__ == "__main__":
    # customize the host and port for production use listen to all interfaces
    uvicorn.run("app.api.init_api:app", host="0.0.0.0", port=8080, reload=True)
    