
FROM python:3.10

WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Create MLflow directory
RUN mkdir -p /app/mlruns

# Expose ports
EXPOSE 8000
EXPOSE 5000

# Start MLflow + FastAPI
CMD bash -c "mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns & uvicorn api.app:app --host 0.0.0.0 --port 8000"
