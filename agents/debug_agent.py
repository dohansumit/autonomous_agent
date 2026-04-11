import re


class DebugAgent:

    def analyze_error(self, error):

        print("🤖 Debug Agent analyzing error...")

        # simple automatic fixes

        if "label" in error:

            print("🔧 Fixing column name issue automatically...")

            file_path = "agents/hyperparameter_agent.py"

            with open(file_path, "r") as f:
                code = f.read()

            code = code.replace('df["label"]', 'df["sentiment"]')

            with open(file_path, "w") as f:
                f.write(code)

            print("✅ Column name fixed in hyperparameter_agent.py")

            return "Replaced label with sentiment"

        return "No automatic fix found"