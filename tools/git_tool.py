import subprocess


class GitTool:

    def init_repo(self):
        subprocess.run("git init", shell=True)

    def add_all(self):
        subprocess.run("git add .", shell=True)

    def commit(self, message="autonomous update"):
        subprocess.run(f'git commit -m "{message}"', shell=True)

    def push(self, branch="main"):
        subprocess.run(f"git push origin {branch}", shell=True)