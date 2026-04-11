from transformers import AutoTokenizer, AutoModelForCausalLM


class DebugAgent:

    def __init__(self):

        model_path = "Qwen/Qwen2.5-3B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(model_path)

        self.model = AutoModelForCausalLM.from_pretrained(model_path)

    def analyze_error(self, error):

        prompt = f"""
You are a Python debugging assistant.

The following error occurred in a machine learning pipeline.

Error:
{error}

Explain the problem and suggest a fix in simple Python terms.
Do NOT generate unrelated code.
"""

        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(**inputs, max_new_tokens=300)

        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)