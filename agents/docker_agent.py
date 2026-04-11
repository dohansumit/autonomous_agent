class DockerAgent:

    def run(self):

        print("🐳 Running Docker Agent")

        dockerfile = """
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
EXPOSE 5000

CMD ["bash", "-c", "mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns & uvicorn api.app:app --host 0.0.0.0 --port 8000"]
"""

        with open("Dockerfile", "w") as f:
            f.write(dockerfile)

        print("Dockerfile created")