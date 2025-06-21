from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Signal(BaseModel):
    symbol: str
    action: str
    confidence: float

signals = []

@app.get("/")
def read_root():
    return {"message": "API de señales activa"}

@app.post("/signal")
def receive_signal(signal: Signal):
    signals.append(signal)
    return {"message": "Señal recibida", "signal": signal}

@app.get("/signals")
def get_signals():
    return signals

@app.get("/estatus")
def get_status():
    return {"status": "funcionando"}

@app.get("/logs")
def get_logs():
    return signals[-5:] if len(signals) > 5 else signals

@app.get("/historico")
def get_history():
    return {"historico": signals}
