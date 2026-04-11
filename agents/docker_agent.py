import subprocess
import os


class DockerAgent:

    def create_dockerfile(self):

        dockerfile = """
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
CMD bash -c "mlflow server \
--host 0.0.0.0 \
--port 5000 \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
& \
uvicorn api.app:app --host 0.0.0.0 --port 8000"
"""

        with open("Dockerfile", "w") as f:
            f.write(dockerfile)

        print("✅ Dockerfile created")

    def build_image(self):

        print("🐳 Building Docker image...")

        subprocess.run(
            "docker build -t autonomous-agent:latest .",
            shell=True
        )

        print("✅ Docker image built")

    def run_container(self):

        print("🚀 Starting Docker container...")

        # stop old container if exists
        subprocess.run(
            "docker stop autonomous-agent || true",
            shell=True
        )

        subprocess.run(
            "docker rm autonomous-agent || true",
            shell=True
        )

        # run new container
        subprocess.run(
            """
docker run -d \
--name autonomous-agent \
--restart always \
-p 8000:8000 \
-p 5000:5000 \
autonomous-agent:latest
""",
            shell=True
        )

        print("✅ Container running")

    def run(self):

        print("🐳 Running Docker Agent")

        self.create_dockerfile()

        # Build image
        self.build_image()

        # Run container
        self.run_container()