import os, subprocess, threading, time
from huggingface_hub import snapshot_download
from pathlib import Path

# A small, CPU-friendly instruct model in GGUF format.
# Swap to another GGUF if you prefer.
MODEL_REPO = os.getenv("GGUF_REPO", "bartowski/Llama-3.2-3B-Instruct-GGUF")
MODEL_FILE = os.getenv("GGUF_FILE", "Llama-3.2-3B-Instruct-Q4_K_M.gguf")
PORT = int(os.getenv("LLM_PORT", "8000"))

def ensure_model():
    cache_dir = Path("models")
    cache_dir.mkdir(exist_ok=True)
    snapshot_download(
        repo_id=MODEL_REPO,
        allow_patterns=[MODEL_FILE],
        local_dir=cache_dir
    )
    return str(cache_dir / MODEL_FILE)

def launch_server():
    gguf_path = ensure_model()
    cmd = [
        "python", "-m", "llama_cpp.server",
        "--model", gguf_path,
        "--port", str(PORT),
        "--chat_format", "llama-3",
        "--n_ctx", "4096",
        "--host", "0.0.0.0"
    ]
    def _run():
        subprocess.call(cmd)
    t = threading.Thread(target=_run, daemon=True)
    t.start()
    time.sleep(3)  # give the server a moment

def get_base_url():
    return f"http://localhost:{PORT}/v1"
