from fastapi import APIRouter

from app.api.routers.v1.bot import router as bot_routers
from app.api.routers.v1.messages import router as messages_routers
from app.api.routers.v1.users import router as users_routers

router = APIRouter()

# Include all routers
router.include_router(bot_routers)
router.include_router(messages_routers)
router.include_router(users_routers)
 