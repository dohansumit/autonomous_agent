from tools.shell_tool import run_shell


class EDAAgent:

    def run(self):

        print("Running EDA...")

        run_shell("python scripts/eda.py")