from passlib.context import CryptContext
from .models import UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users_db = {
    "alice": UserInDB(username="alice", full_name="Alice W", role="admin", hashed_password=pwd_context.hash("alice123")),
    "bob": UserInDB(username="bob", full_name="Bob B", role="user", hashed_password=pwd_context.hash("bob123")),
}

def get_user(username: str):
    return fake_users_db.get(username)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
