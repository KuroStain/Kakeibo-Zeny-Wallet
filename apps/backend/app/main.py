from fastapi import FastAPI

app = FastAPI(title="Kakeibo — Zeny Wallet (KZW)", version="0.1.0")

@app.get("/healthz")
def health_check():
    return {"status": "ok", "message": "KZW backend is running!"}
