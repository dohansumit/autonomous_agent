from orchestrator import Orchestrator
import os


def main():

    prompt = """
    Build a news sentiment ML pipeline.
    Steps:
    - Collect news data
    - Perform EDA
    - Train sentiment model
    - Create FastAPI inference service
    - Build Docker image
    """

    orchestrator = Orchestrator()

    # If running inside docker
    if os.getenv("RUN_PIPELINE") == "true":
        orchestrator.run(prompt)
    else:
        print("Skipping pipeline execution")


if __name__ == "__main__":
    main()