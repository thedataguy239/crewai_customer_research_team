# 👔 Customer Intel Agent — CrewAI + Local LLM (FREE)

Interactive agentic demo you can run **for free** on **Hugging Face Spaces (CPU)**.
The app uses:
- **CrewAI** to orchestrate 3 agents (Researcher, Analyst, Strategist).
- A **local LLM** via `llama-cpp-python` (no API keys).
- **DuckDuckGo Search** (no key) for public web intel.
- A local **CRM Excel** + mock **usage/tickets CSVs** to analyze account health.

## One‑click Deploy (Hugging Face Spaces)
1. Create a new **Space** → **SDK: Streamlit** → Name it e.g. `customer-intel-agent`.
2. Upload this entire repo (drag-drop or push via Git).
3. Choose **Hardware: CPU Basic** (free).
4. Wait for the first build. The app will download a small GGUF model on first run.
5. Open the Space. Enter a company name and click **Run analysis**.

> First generation may take ~10–20s on CPU. Subsequent runs are faster due to model caching.

## Local Run (optional)
```bash
python -m venv .venv && source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Repo Layout
```
customer-intel-agent/
├─ app.py
├─ crew_setup.py
├─ local_llm.py
├─ tools/
│  ├─ crm_tool.py
│  ├─ account_data_tool.py
│  └─ web_search_tool.py
├─ data/
│  ├─ crm.xlsx
│  ├─ usage.csv
│  └─ tickets.csv
├─ prompts/
│  ├─ researcher.md
│  ├─ analyst.md
│  └─ strategist.md
├─ scripts/
│  └─ make_sample_data.py
├─ requirements.txt
├─ huggingface.yaml
└─ README_SPACE.md
```

## Troubleshooting (HF Spaces)
- If `llama-cpp-python` build fails on Space: restart the Space; the prebuilt wheel is usually picked.
- If downloads fail due to timeouts, click **Restart** from the Space UI; the model is small but the Hub sometimes throttles.
- You can switch to an even smaller GGUF (1–2B) in `local_llm.py` for snappier CPU inference.

## License
MIT (for the demo code).
