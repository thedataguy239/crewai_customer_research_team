from crewai.tools import BaseTool
import pandas as pd
from pathlib import Path
class CRMLookupTool(BaseTool):
    name="crm_lookup"
    description="Look up company in local CRM Excel (data/crm.xlsx)."
    def _run(self, query: str)->str:
        f=Path("data/crm.xlsx")
        if not f.exists(): return "CRM file not found"
        df=pd.read_excel(f)
        mask=df.apply(lambda s:s.astype(str).str.contains(query,case=False,na=False))
        return df[mask.any(axis=1)].to_json(orient="records")
