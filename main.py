from orchestrator import Orchestrator

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
    orchestrator.run(prompt)


if __name__ == "__main__":
    main()