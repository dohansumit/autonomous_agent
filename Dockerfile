FROM python:3.10

WORKDIR /app

# copy project files
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# create mlflow directories
RUN mkdir -p /app/mlruns

# expose ports
EXPOSE 8000
EXPOSE 5000

# run mlflow + fastapi
CMD bash -c "\
mlflow server \
--host 0.0.0.0 \
--port 5000 \
--backend-store-uri sqlite:///mlflow.db \
--default-artifact-root ./mlruns \
& \
uvicorn api.app:app --host 0.0.0.0 --port 8000"