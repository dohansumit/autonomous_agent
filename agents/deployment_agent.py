import subprocess
import socket


class DeploymentAgent:

    def deploy(self):

        print("🚀 Starting Deployment Agent")

        image_name = "news-sentiment-agent"

        # Build Docker image
        print("📦 Building Docker image...")
        subprocess.run(
            f"docker build -t {image_name}:latest .",
            shell=True,
            check=True
        )

        # Stop existing container if running
        subprocess.run(
            f"docker rm -f {image_name}",
            shell=True
        )

        # Run container
        print("🐳 Running Docker container...")
        subprocess.run(
            f"docker run -d -p 8000:8000 --name {image_name} {image_name}:latest",
            shell=True,
            check=True
        )

        # Print API URL
        ip = socket.gethostbyname(socket.gethostname())

        print("\n✅ Deployment complete")
        print(f"API available at: http://{ip}:8000/docs")