from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class PlannerAgent:

    def __init__(self):

        model_path = "Qwen/Qwen2.5-3B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            dtype=torch.float32
        )

    def plan(self, prompt):

        system_prompt = f"""
Break this ML task into steps:

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

        for step in ["research","data","eda","training","tuning","api","docker"]:
            if step in text:
                steps.append(step)

        return steps