import os
from crewai import Agent, Task, Crew, Process, LLM
from tools.crm_tool import CRMLookupTool
from tools.account_data_tool import AccountDataInsightsTool
from tools.web_search_tool import WebSearchTool

# Use an OpenAI-compatible client; OPENAI_API_BASE points to local llama server.
llm = LLM(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
          api_key=os.getenv("OPENAI_API_KEY", "sk-local-key"))

crm_tool = CRMLookupTool()
acct_tool = AccountDataInsightsTool()
web_tool = WebSearchTool()

with open("prompts/researcher.md", "r", encoding="utf-8") as f:
    researcher_sys = f.read()
with open("prompts/analyst.md", "r", encoding="utf-8") as f:
    analyst_sys = f.read()
with open("prompts/strategist.md", "r", encoding="utf-8") as f:
    strategist_sys = f.read()

researcher = Agent(
    role="Customer Researcher",
    goal="Find accurate, recent intel about a target company.",
    backstory="Analyst with OSINT chops; prioritizes credible citations.",
    tools=[web_tool, crm_tool],
    llm=llm,
    verbose=True
)

analyst = Agent(
    role="Data Analyst",
    goal="Turn account telemetry into actionable metrics and risks.",
    backstory="Product analytics pro.",
    tools=[acct_tool, crm_tool],
    llm=llm,
    verbose=True
)

strategist = Agent(
    role="Account Strategist",
    goal="Synthesize research + analytics into a crisp brief & next steps.",
    backstory="Enterprise AE crafting value narratives.",
    tools=[],
    llm=llm,
    verbose=True
)

def build_crew(company_query: str):
    t1 = Task(
        description=(researcher_sys + f"\n\nTarget: {company_query}"),
        agent=researcher,
        expected_output="JSON or markdown with citations/links"
    )
    t2 = Task(
        description=(analyst_sys + f"\n\nIf CRM row found for '{company_query}', use its account_id to analyze data."),
        agent=analyst,
        expected_output="KPIs + 3 insights"
    )
    t3 = Task(
        description=(strategist_sys + "\n\nUse findings from Researcher and Analyst."),
        agent=strategist,
        expected_output="One-page brief with bullets"
    )
    return Crew(
        agents=[researcher, analyst, strategist],
        tasks=[t1, t2, t3],
        process=Process.sequential,
        verbose=True
    )
