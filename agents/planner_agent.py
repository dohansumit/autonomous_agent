from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import os


class PlannerAgent:

    def __init__(self):

        model_path = "Qwen/Qwen2.5-3B-Instruct"

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        # Skip heavy model loading in CI environments
        if os.getenv("CI") == "true":
            self.model = None
            return

        # Load model safely
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            torch_dtype=torch.float32,
            device_map="cpu"
        )

    def plan(self, prompt):

        system_prompt = f"""
Break this ML task into steps:

research
data
eda
training
tuning
api
docker

Task:
{prompt}
"""

        # If model is skipped (CI mode), return default plan
        if self.model is None:
            return ["research", "data", "eda", "training", "api", "docker"]

        inputs = self.tokenizer(system_prompt, return_tensors="pt")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=200
        )

        text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        steps = []

        for step in ["research", "data", "eda", "training", "tuning", "api", "docker"]:
            if step in text:
                steps.append(step)

        return steps