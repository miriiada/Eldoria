from fastapi import FastAPI
app = FastAPI(title="Eldoria Backend")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "eldoria-backend"}
