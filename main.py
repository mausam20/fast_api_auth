from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from .auth import authenticate_user, create_access_token, get_current_active_user, get_admin_user
from .models import User

app = FastAPI()

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

@app.get("/admin/dashboard")
def admin_dashboard(current_user: User = Depends(get_admin_user)):
    return {"msg": f"Welcome Admin {current_user.full_name}"}
