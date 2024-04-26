from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(
    prefix="/",
    tags=['auth']
)


@router.get("/auth")
async def authorization():
    return FileResponse("templates/authorization.html")


@router.get("/reg")
async def registration():
    return FileResponse("templates/registration.html")
