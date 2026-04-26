#Se implementó un sistema con tres servicios orquestados con Docker Compose. Un worker incrementa un contador en Redis periódicamente, mientras que un 
#servidor web consulta ese valor y lo expone mediante un endpoint HTTP. Redis actúa como almacenamiento compartido entre ambos servicios.
import redis
import time
import os

redis_host = os.getenv("REDIS_HOST", "redis")

# esperar a Redis
while True:
    try:
        r = redis.Redis(host=redis_host, port=6379)
        r.ping()
        print("✅ Worker conectado a Redis")
        break
    except:
        print("⏳ Worker esperando Redis...")
        time.sleep(1)

# loop infinito
while True:
    valor = r.incr("contador")
    print(f"Worker incrementó: {valor}")
    time.sleep(1)