import subprocess
import socket
import os


class DeploymentAgent:

    def deploy(self):

        print("🚀 Starting Deployment Agent")

        image_name = "news-sentiment-agent"

        # Skip deployment if running in GitHub Actions
        if os.getenv("GITHUB_ACTIONS"):
            print("⚠ Running inside CI/CD - skipping container deployment")
            return

        # Stop existing container if running
        subprocess.run(
            f"docker rm -f {image_name}",
            shell=True
        )

        # Run container
        print("🐳 Running Docker container...")

        subprocess.run(
            f"docker run -d -p 8000:8000 -p 5000:5000 --name {image_name} {image_name}:latest",
            shell=True,
            check=True
        )

        ip = socket.gethostbyname(socket.gethostname())

        print("\n✅ Deployment complete")
        print(f"FastAPI: http://{ip}:8000/docs")
        print(f"MLflow:  http://{ip}:5000") #