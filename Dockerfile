FROM python:3.10-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# create folders
RUN mkdir -p /app/mlruns /app/models /app/dataset

# expose ports
EXPOSE 8000
EXPOSE 5000

# environment variable for CI
ENV RUN_PIPELINE=true

# start services
CMD ["bash", "-c", "mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlruns & sleep 10 && python main.py && uvicorn api.app:app --host 0.0.0.0 --port 8000"]