from crewai.tools import BaseTool
import os, json

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: ("Search the public web for recent info about a company. "
                  "Prefer recent news, funding, exec changes, product launches. "
                  "Return a JSON list of {title, href, snippet}.")

    def _run(self, query: str) -> str:
        results = []
        try:
            tavily_key = os.getenv("TAVILY_API_KEY")
            if tavily_key:
                from tavily import TavilyClient
                tv = TavilyClient(api_key=tavily_key)
                r = tv.search(query=query, max_results=8, include_answer=False)
                for item in r.get("results", []):
                    results.append({
                        "title": item.get("title"),
                        "href": item.get("url"),
                        "snippet": item.get("content")
                    })
            else:
                from duckduckgo_search import DDGS
                with DDGS() as ddgs:
                    for r in ddgs.text(query, max_results=8):
                        results.append({
                            "title": r.get("title"),
                            "href": r.get("href"),
                            "snippet": r.get("body")
                        })
        except Exception as e:
            return json.dumps({"error": str(e), "partial": results})
        return json.dumps(results)
