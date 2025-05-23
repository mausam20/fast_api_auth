# 🔐 FastAPI Authentication App

This is a simple FastAPI application demonstrating **user authentication and authorization** using **OAuth2 with password flow** and **JSON Web Tokens (JWT)**. It supports user login, token generation, and secure access to protected routes.

## 🚀 Features

- User login with username & password
- JWT token generation and verification
- Protected endpoints with token-based access
- Dependency injection for user authentication
- Password hashing for secure storage

## 🛠️ Technologies & Libraries

- **FastAPI** – modern Python web framework for APIs
- **Pydantic** – data validation and serialization
- **passlib** – for secure password hashing
- **Python-Jose** – for JWT creation and validation
- **Uvicorn** – ASGI server for running the FastAPI app

## 📦 Installation

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt]
