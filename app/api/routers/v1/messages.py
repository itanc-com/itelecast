from fastapi import APIRouter, HTTPException

from app.api.service.send_message import SendMessage

router = APIRouter(
    prefix="/messages",
    tags=["Messages"],
    responses={404: {"description": "Resource not found"}},
    )

router.post("/")
async def post_new_message():
    """
    Health check endpoint to verify if the service is running.
    """
    try:
        return {"new_message": "ok"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 