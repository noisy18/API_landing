from fastapi import APIRouter, Depends, HTTPException, status

from app.db.dependencies import get_db
from app.utils.docs.tags import REQUESTS
from app.schemas.request import RequestCreateSchema, RequestResponseSchema
from app.db.db_manager import DB
from app.settings import get_current_time

router = APIRouter(
    tags=[REQUESTS]
)

@router.post("/requests", response_model=RequestResponseSchema)
async def post(request_data: RequestCreateSchema, db: DB = Depends(get_db)):
    request = await db.requests.get_request_by_email(email=request_data.email)
    if request:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Вы ранее уже записывались на пробный урок")
    
    data_with_timestamp = request_data.model_dump()
    data_with_timestamp["created_at"] = get_current_time()

    new_request = await db.requests.create_request(request=data_with_timestamp)
    return new_request