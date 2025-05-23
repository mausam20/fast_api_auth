from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = False
    role: str

class UserInDB(User):
    hashed_password: str
