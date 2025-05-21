# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow ESP32 to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your frontend/domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/data")
async def receive_data(request: Request):
    data = await request.json()
    print("Received:", data)
    # Optional: Save to DB or process it
    return {"message": "Data received", "data": data}
