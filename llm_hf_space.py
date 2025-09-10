import os
from gradio_client import Client

DEFAULT_SPACE = os.getenv("HF_CHAT_SPACE", "HuggingFaceH4/zephyr-7b-beta")
DEFAULT_ENDPOINT = os.getenv("HF_CHAT_ENDPOINT", None)

class HFSpaceChatBackend:
    def __init__(self, space=DEFAULT_SPACE, endpoint=DEFAULT_ENDPOINT):
        self.client = Client(space, hf_token=os.getenv("HF_TOKEN", None))
        self.endpoint = endpoint
    def generate(self, messages):
        prompt = "\n".join([f"{m.get('role','user').upper()}: {m.get('content','')}" for m in messages])+"\nASSISTANT:"
        try:
            if self.endpoint:
                return str(self.client.predict(prompt, api_name=self.endpoint))
            else:
                return str(self.client.predict(prompt))
        except Exception as e:
            return f"Error contacting HF Space: {e}"

class CrewAIHFLLM:
    def __init__(self):
        self.backend = HFSpaceChatBackend()
    def invoke(self, messages, **kwargs):
        return {"content": self.backend.generate(messages)}
    __call__ = invoke
