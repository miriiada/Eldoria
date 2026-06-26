from fastapi import FastAPI, status
from pydantic import BaseModel, EmailStr
app = FastAPI(title="Eldoria Backend")

class NewsletterRequest(BaseModel):
    email: EmailStr

class NewsletterResponse(BaseModel):
    message: str
    email: EmailStr
@app.get("/health")
def health_check():
    return {"status": "ok", "service": "eldoria-backend"}

@app.post(
    "/newsletter",
    status_code=status.HTTP_201_CREATED,
    response_model=NewsletterResponse,
)
def subscribe_to_newsletter(payload: NewsletterRequest):
    return {
        "message": "Email accepted",
        "email": payload. email,
    }