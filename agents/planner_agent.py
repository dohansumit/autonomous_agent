from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os


class PlannerAgent:

    def __init__(self):

        model_path = "Qwen/Qwen2.5-3B-Instruct"

        # Skip model loading in CI or Docker
        if os.getenv("GITHUB_ACTIONS") or os.getenv("RUN_PIPELINE"):
            print("⚠ Skipping LLM loading in CI/Docker")
            self.model = None
            self.tokenizer = None
            return

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float32
        )

    def plan(self, prompt):

        if self.model is None:

            return [
                "research",
                "data",
                "eda",
                "training",
                "api",
                "docker"
            ]

        system_prompt = f"""
Break this ML task into steps:

research
data
eda
training
api
docker

Task:
{prompt}
"""

        inputs = self.tokenizer(system_prompt, return_tensors="pt")

        outputs = self.model.generate(**inputs, max_new_tokens=200)

        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        steps = []

        for step in ["research","data","eda","training","api","docker"]:
            if step in text:
                steps.append(step)

        return steps