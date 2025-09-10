---
title: Customer Intel Agent
emoji: 👔
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: 1.36.0
app_file: app.py
pinned: false
---

# 👔 Customer Intel Agent — CrewAI + Hugging Face Space LLM

This is an interactive **portfolio demo** of an agentic workflow powered by [CrewAI](https://github.com/joaomdmoura/crewai).  
It shows how multi-agent AI can deliver **clear business value** by researching and analyzing customer accounts.

---

## 🚀 Features

- **CRM Lookup**: Searches a local Excel CRM (`data/crm.xlsx`) for account info.  
- **Account Analytics**: Analyzes mock `usage.csv` and `tickets.csv` for KPIs, trends, and risk signals.  
- **Web Research**: Searches the public web for company intel (recent news, funding, leadership changes, etc.).  
- **CrewAI Orchestration**:  
  - **Researcher Agent** → collects company intel.  
  - **Analyst Agent** → generates KPIs and insights from account data.  
  - **Strategist Agent** → synthesizes into a customer brief with opportunities, risks, and discovery questions.  
- **Free LLM Backend**: Uses `gradio_client` to call a public Hugging Face Space (`HuggingFaceH4/zephyr-7b-beta`) for reasoning.  

---

## 🌐 Live Demo

Once deployed, recruiters or stakeholders can access the app here:

