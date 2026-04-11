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

        # Core planning
        self.planner = PlannerAgent()

        # Agents
        self.data_agent = DataAgent()
        self.eda_agent = EDAAgent()
        self.training_agent = TrainingAgent()
        self.hyper_agent = HyperparameterAgent()
        self.api_agent = APIAgent()
        self.docker_agent = DockerAgent()
        self.deployment_agent = DeploymentAgent()
        self.research_agent = ResearchAgent()
        self.git_agent = GitAgent()

        # Debugging
        self.debug_agent = DebugAgent()

    def run(self, prompt):

        print("Planning project...")

        tasks = self.planner.plan(prompt)

        for task in tasks:

            try:

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

            except Exception as e:

                print("\n❌ Error occurred while executing:", task)
                print("Error:", e)

                print("\n🤖 Debug Agent analyzing error...")

                fix = self.debug_agent.analyze_error(str(e))

                print("\n💡 Suggested Fix from LLM:\n")
                print(fix)

                print("\nContinuing execution...\n")

        # Always push updates to Git at the end
        try:
            print("📦 Running Git Agent (CI/CD step)")
            self.git_agent.run()

        except Exception as e:
            print("⚠ Git push failed:", e)