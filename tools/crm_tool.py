from crewai.tools import BaseTool
import pandas as pd
from pathlib import Path

class CRMLookupTool(BaseTool):
    name: str = "crm_lookup"
    description: str = ("Look up a company in the local CRM Excel file (data/crm.xlsx). "
                        "Input: company name or domain. Returns a JSON row if found.")

    def _run(self, query: str) -> str:
        f = Path("data/crm.xlsx")
        if not f.exists():
            return "CRM file not found"
        df = pd.read_excel(f)
        q = str(query).strip().lower()
        mask = df.apply(lambda s: s.astype(str).str.lower().str.contains(q, na=False))
        hits = df[mask.any(axis=1)]
        return hits.to_json(orient="records")
