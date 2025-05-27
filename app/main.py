from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request as FastAPIRequest
from app.src.router.building import get_buildings
from app.src.router.Favorite.building import fav_building, unfav_building
from app.src.router.Favorite.room import fav_room, unfav_room
from app.src.router.room import get_all_room, get_room
from app.src.router.user import login, sign_up, user_profile


app = FastAPI()

#MARK: - 커스텀 예외 핸들러
@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: FastAPIRequest, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error":exc.detail}
    )
# 라우터 등록
app.include_router(get_buildings.app)
app.include_router(fav_room.app)
app.include_router(fav_building.app)
app.include_router(unfav_building.app)
app.include_router(unfav_room.app)
app.include_router(get_room.app)
app.include_router(get_all_room.app)
app.include_router(user_profile.app)
app.include_router(login.app)
app.include_router(sign_up.app)