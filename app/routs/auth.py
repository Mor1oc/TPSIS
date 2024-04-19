from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(
    prefix="/logist",
    tags=['Logist']
)


@router.get("/auth")
async def authorization():
    return FileResponse("templates/authorization.html")