
from flask import Flask
import redis
import os
import time

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")

# esperar a Redis
while True:
    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
        print("✅ Web conectado a Redis")
        break
    except:
        print("⏳ Web esperando Redis...")
        time.sleep(1)

@app.route("/")
def home():
    valor = r.get("contador")
    return f"Contador actual: {valor.decode() if valor else 0}"

app.run(host="0.0.0.0", port=5000)