from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers import auth, students

# 🔹 Import models BEFORE create_all
import models.user
import models.student

# 🔹 Create DB tables
Base.metadata.create_all(bind=engine)

# 🔹 Initialize app
app = FastAPI(
    title="Student Management API",
    version="1.0.0"
)

# 🔥 CORS CONFIG (FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ✅ allow all (best for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/students", tags=["Students"])

# 🔹 Root test route
@app.get("/")
def root():
    return {"message": "Student API is running"}