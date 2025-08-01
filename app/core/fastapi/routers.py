from fastapi import APIRouter

from app.api.routers.v1_routers import router as v1_router

router_v1 = APIRouter(prefix="/v1")

"""Include to router all api rest routes with version prefix"""
router_v1.include_router(v1_router)
 
