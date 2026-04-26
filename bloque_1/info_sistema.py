
import os
import sys
import platform

print("="*40)

# Python
print(f"Python: {sys.version}")

# Sistema operativo
print(f"Sistema: {platform.system()} {platform.release()}")

# CPUs
print(f"CPUs: {os.cpu_count()}")

# Memoria (Linux)
try:
    with open('/proc/meminfo') as f:
        mem = f.readline()
    print(f"Memoria: {mem.strip()}")
except:
    print("Memoria: no disponible")

# Variables PYTHON
print("\nVariables PYTHON:")
for k, v in os.environ.items():
    if k.startswith("PYTHON"):
        print(f"{k}={v}")

print("="*40)