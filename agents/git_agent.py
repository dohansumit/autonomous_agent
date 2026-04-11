import subprocess
import json
import os


class GitAgent:

    CONFIG_PATH = "configs/git_config.json"

    def setup_git(self):

        if not os.path.exists("configs"):
            os.makedirs("configs")

        if not os.path.exists(self.CONFIG_PATH):

            repo = input("Enter your Git repository URL: ")
            branch = input("Enter branch name (default main): ") or "main"
            name = input("Enter your Git username: ")
            email = input("Enter your Git email: ")

            config = {
                "repo": repo,
                "branch": branch,
                "name": name,
                "email": email
            }

            with open(self.CONFIG_PATH, "w") as f:
                json.dump(config, f, indent=4)

            print("✅ Git configuration saved")

        else:

            with open(self.CONFIG_PATH) as f:
                config = json.load(f)

        # Initialize repo if not exists
        if not os.path.exists(".git"):
            subprocess.run("git init", shell=True)

        # Configure identity
        subprocess.run(
            f'git config --global user.name "{config["name"]}"',
            shell=True
        )

        subprocess.run(
            f'git config --global user.email "{config["email"]}"',
            shell=True
        )

        # Set branch
        subprocess.run(
            f'git branch -M {config["branch"]}',
            shell=True
        )

        # Check if remote exists
        result = subprocess.run(
            "git remote",
            shell=True,
            capture_output=True,
            text=True
        )

        if "origin" not in result.stdout:
            subprocess.run(
                f'git remote add origin {config["repo"]}',
                shell=True
            )

        return config

    def has_changes(self):

        result = subprocess.run(
            "git status --porcelain",
            shell=True,
            capture_output=True,
            text=True
        )

        return bool(result.stdout.strip())

    def run(self):

        config = self.setup_git()

        print("📦 Running Git Agent")

        subprocess.run("git add .", shell=True)

        # commit even first time
        subprocess.run(
            'git commit -m "Autonomous ML pipeline update"',
            shell=True
        )

        subprocess.run(
            f'git push -u origin {config["branch"]}',
            shell=True
        )

        print("✅ Code pushed to GitHub")