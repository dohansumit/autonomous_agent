import os

from agents.planner_agent import PlannerAgent
from agents.data_agent import DataAgent
from agents.eda_agent import EDAAgent
from agents.training_agent import TrainingAgent
from agents.api_agent import APIAgent
from agents.docker_agent import DockerAgent
from agents.hyperparameter_agent import HyperparameterAgent
from agents.deployment_agent import DeploymentAgent
from agents.debug_agent import DebugAgent
from agents.research_agent import ResearchAgent
from agents.git_agent import GitAgent


class Orchestrator:

    def __init__(self):

        self.planner = PlannerAgent()

        self.data_agent = DataAgent()
        self.eda_agent = EDAAgent()
        self.training_agent = TrainingAgent()
        self.hyper_agent = HyperparameterAgent()
        self.api_agent = APIAgent()
        self.docker_agent = DockerAgent()
        self.deployment_agent = DeploymentAgent()
        self.research_agent = ResearchAgent()
        self.git_agent = GitAgent()

        self.debug_agent = DebugAgent()

    def execute_task(self, task):

        if task == "research":
            print("🔎 Running Research Agent")
            self.research_agent.find_data_source()

        elif task == "data":
            print("📥 Running Data Agent")
            self.data_agent.run()

        elif task == "eda":
            print("📊 Running EDA Agent")
            self.eda_agent.run()

        elif task == "training":
            print("🚀 Running Training Agent")
            self.training_agent.run()

        elif task == "tuning":
            print("⚙ Running Hyperparameter Agent")
            self.hyper_agent.tune()

        elif task == "api":
            print("🌐 Running API Agent")
            self.api_agent.run()

        elif task == "docker":
            print("🐳 Running Docker Agent")
            self.docker_agent.run()

        elif task == "deploy":
            print("🚀 Running Deployment Agent")
            self.deployment_agent.deploy()

    def run(self, prompt):

        print("Planning project...")

        tasks = self.planner.plan(prompt)

        for task in tasks:

            try:

                self.execute_task(task)

            except Exception as e:

                print("\n❌ Error occurred while executing:", task)
                print("Error:", e)

                print("\n🤖 Debug Agent analyzing error...")

                fix = self.debug_agent.analyze_error(str(e))

                print("\n💡 Suggested Fix:\n")
                print(fix)

                try:
                    print("\n🔁 Retrying task:", task)
                    self.execute_task(task)

                except Exception as e:
                    print("⚠ Retry failed. Skipping task:", task)
                    print("Error:", e)

        # Push to GitHub only when NOT inside CI
        if not os.getenv("GITHUB_ACTIONS"):

            try:
                print("📦 Running Git Agent")
                self.git_agent.run()

            except Exception as e:
                print("⚠ Git push failed:", e)