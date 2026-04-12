FROM python:3.10-slim

WORKDIR /app

# Install dependencies first (better caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directories required by MLflow and model storage
RUN mkdir -p /app/mlruns /app/models /app/dataset

# Expose ports
EXPOSE 8000
EXPOSE 5000

# Start MLflow then FastAPI
CMD bash -c "\
mlflow server \
--host 0.0.0.0 \
--port 5000 \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns & \
sleep 5 && \
uvicorn api.app:app --host 0.0.0.0 --port 8000"