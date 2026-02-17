FROM python:3.11-slim

WORKDIR /app
COPY src/backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src .

CMD ["python", "main.py"]
