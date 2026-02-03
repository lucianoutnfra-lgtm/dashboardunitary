FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# ACÁ CAMBIAMOS: Ejecuta dashboard.py en vez de app.py
CMD ["chainlit", "run", "dashboard.py", "-w", "--host", "0.0.0.0", "--port", "8000"]

