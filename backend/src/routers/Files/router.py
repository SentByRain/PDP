
from fastapi import APIRouter, HTTPException, UploadFile
from src.database_control.s3 import MinioHandler
from src.config import CONFIG       

PREFIX = '/files'


router = APIRouter(prefix=PREFIX, tags=['Files'])


@router.post("/file_upload")
async def upload_file(file: UploadFile):
    try:
        minio_handler = MinioHandler(bucket=CONFIG.MINIO_FILES_BUCKET_NAME)
        
        # Получаем содержимое файла
        file_content = await file.read()
        file_size = len(file_content)
        
        # Загружаем файл в MinIO и получаем ссылку
        url = minio_handler.upload_file(
            name=file.filename,
            file=file_content,
            length=file_size
        )
        
        return {"url": url}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка при загрузке файла: {str(e)}")
