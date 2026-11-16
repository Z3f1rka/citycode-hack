from fastapi import FastAPI

def create_app() -> FastAPI:
    from app.api.endpoints import test
    from app.core.config import settings
    
    app = FastAPI(
        title="Citycode Hackathon Backend", 
        version="1.0.0",
        openapi_url="/openapi.json"
    )
    
    app.include_router(test.router)
    
    @app.get("/health")
    async def health_check():
        return {"status": "ok"}
        
    return app