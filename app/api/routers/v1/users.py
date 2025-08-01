from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Resource not found"}},
    )

router.get("/count")
async def get_users_count():
    """
    Health check endpoint to verify if the service is running.
    """
    try:
        return {"value": 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 