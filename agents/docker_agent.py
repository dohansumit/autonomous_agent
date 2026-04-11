import os


class DockerAgent:

    def run(self):

        dockerfile = """
FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn scikit-learn joblib

CMD ["uvicorn","api.app:app","--host","0.0.0.0","--port","8000"]
"""

        with open("Dockerfile","w") as f:
            f.write(dockerfile)

        print("Dockerfile created")