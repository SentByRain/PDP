from typing import Literal, List
from pydantic import BaseModel
from datetime import datetime

class HomeworkSchema(BaseModel):

    files_urls : List | None
    answer : str | None
    sent_files : List | None
    deadline : datetime | None