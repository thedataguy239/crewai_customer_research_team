import os
from crewai import Agent, Task, Crew, Process
from tools.crm_tool import CRMLookupTool
from tools.account_data_tool import AccountDataInsightsTool
from tools.web_search_tool import WebSearchTool
from llm_hf_space import CrewAIHFLLM

llm = CrewAIHFLLM()

crm_tool = CRMLookupTool()
acct_tool = AccountDataInsightsTool()
web_tool = WebSearchTool()

with open("prompts/researcher.md") as f: researcher_sys = f.read()
with open("prompts/analyst.md") as f: analyst_sys = f.read()
with open("prompts/strategist.md") as f: strategist_sys = f.read()

researcher = Agent(role="Customer Researcher", goal="Find intel", backstory="OSINT", tools=[web_tool, crm_tool], llm=llm)
analyst = Agent(role="Data Analyst", goal="Turn telemetry into KPIs", backstory="Analytics", tools=[acct_tool, crm_tool], llm=llm)
strategist = Agent(role="Strategist", goal="Synthesize into brief", backstory="AE", tools=[], llm=llm)

def build_crew(company_query: str):
    t1 = Task(description=(researcher_sys+f"\nTarget: {company_query}"), agent=researcher)
    t2 = Task(description=(analyst_sys+f"\nIf CRM row found for {company_query}, analyze data."), agent=analyst)
    t3 = Task(description=(strategist_sys+"\nUse Researcher and Analyst outputs."), agent=strategist)
    return Crew(agents=[researcher,analyst,strategist], tasks=[t1,t2,t3], process=Process.sequential)
