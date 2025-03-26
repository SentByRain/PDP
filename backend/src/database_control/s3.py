from minio import Minio
from src.config import CONFIG

from typing import BinaryIO

import minio
from minio import Minio


class MinioHandler:
    def __init__(self, bucket: str):
        self.client = Minio(
            endpoint=CONFIG.MINIO_ENDPOINT,
            access_key=CONFIG.MINIO_ROOT_USER,
            secret_key=CONFIG.MINIO_ROOT_PASSWORD,
            secure=False
        )
        self.bucket = bucket

        # Проверяем, существует ли бакет, и создаем, если нет
        if not self.client.bucket_exists(self.bucket):
            self.client.make_bucket(self.bucket)
            print(f"Bucket '{self.bucket}' был создан.")
        else:
            print(f"Bucket '{self.bucket}' уже существует.")

    def upload_file(self, name: str, file: BinaryIO, length: int):
        """Загружает файл и возвращает ссылку на него"""
        result = self.client.put_object(self.bucket, name, file, length=length)
        return self.get_presigned_url(name)

    def get_presigned_url(self, name: str, expires=7*24*60*60) -> str:
        """
        Генерирует временную ссылку для скачивания файла
        :param name: имя файла
        :param expires: время жизни ссылки в секундах (по умолчанию 7 дней)
        :return: временная ссылка для скачивания
        """
        try:
            return self.client.presigned_get_object(self.bucket, name, expires=expires)
        except Exception as e:
            raise Exception(f"Ошибка при генерации ссылки: {str(e)}")

    def list(self):
        objects = list(self.client.list_objects(self.bucket))
        return [{"name": i.object_name, "last_modified": i.last_modified} for i in objects]

    def stats(self, name: str) -> minio.api.Object:
        return self.client.stat_object(self.bucket, name)

    def download_file(self, name: str):
        info = self.client.stat_object(self.bucket, name)
        total_size = info.size
        offset = 0
        while True:
            response = self.client.get_object(self.bucket, name, offset=offset, length=2048)
            yield response.read()
            offset = offset + 2048
            if offset >= total_size:
                break

MinioClient = MinioHandler(bucket=CONFIG.MINIO_FILES_BUCKET_NAME)