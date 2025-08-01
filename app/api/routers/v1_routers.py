from fastapi import APIRouter

from .v1.messages import router as messages_routers
from .v1.users import router as users_routers

router = APIRouter(
    prefix="/v1",
)

# Include all routers
router.include_router(messages_routers)
router.include_router(users_routers)
 