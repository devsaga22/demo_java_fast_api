import uvicorn
# loads the asgi web server and runs the FastAPI app defined in app1.py file inside the app folder



if __name__ == "__main__":
    # main()
    uvicorn.run("src.app1:app", host="0.0.0.0", port=8000, reload=True)
