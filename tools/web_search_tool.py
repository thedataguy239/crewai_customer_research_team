from crewai.tools import BaseTool
import os,json
class WebSearchTool(BaseTool):
    name="web_search"
    description="DuckDuckGo or Tavily search."
    def _run(self,query:str)->str:
        try:
            from duckduckgo_search import DDGS
            with DDGS() as ddgs:
                results=[{"title":r["title"],"href":r["href"],"snippet":r["body"]} for r in ddgs.text(query,max_results=3)]
            return json.dumps(results)
        except Exception as e: return str(e)
