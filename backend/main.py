import uvicorn

from src.config import CONFIG

if __name__ == "__main__":
    try:
        print("Server is running...")
        uvicorn.run(
            app="src.app:app",
            host=CONFIG.APP_HOST,
            port=CONFIG.APP_PORT,
            reload=True,
            workers=CONFIG.APP_WORKERS,
        )
    except Exception as e:
        print(f"Failed start server: {e}")
    finally:
        print("Server is shutting down...")
