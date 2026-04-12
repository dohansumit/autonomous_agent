FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/mlruns /app/models /app/dataset

EXPOSE 8000
EXPOSE 5000

CMD bash -c "
mlflow server 
--host 0.0.0.0 
--port 5000 
--backend-store-uri sqlite:///mlflow.db 
--default-artifact-root ./mlruns & 
sleep 5 && 
uvicorn api.app:app --host 0.0.0.0 --port 8000"
