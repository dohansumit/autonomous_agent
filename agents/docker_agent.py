import os


class DockerAgent:

    def run(self):

        print("🐳 Running Docker Agent")

        dockerfile = """
FROM python:3.10-slim

WORKDIR /app

# Install dependencies first (better Docker caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Create required directories
RUN mkdir -p mlruns models dataset

# Expose ports
EXPOSE 8000
EXPOSE 5000

# Start MLflow + FastAPI
CMD ["bash", "-c", "mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns & uvicorn api.app:app --host 0.0.0.0 --port 8000"]
"""

        with open("Dockerfile", "w") as f:
            f.write(dockerfile)

        print("✅ Dockerfile created")

        # Ensure runtime folders exist locally
        os.makedirs("mlruns", exist_ok=True)
        os.makedirs("models", exist_ok=True)
        os.makedirs("dataset", exist_ok=True)

        print("📁 Required folders ensured (mlruns, models, dataset)")