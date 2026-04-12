FROM python:3.10-slim

WORKDIR /app

# Copy dependency file first for Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create required directories
RUN mkdir -p /app/mlruns /app/models /app/dataset

# Expose ports
EXPOSE 8000
EXPOSE 5000

# Start MLflow and FastAPI
CMD bash -c "mlflow server \
--host 0.0.0.0 \
--port 5000 \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns & \
uvicorn api.app:app --host 0.0.0.0 --port 8000"