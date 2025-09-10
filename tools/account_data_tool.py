from crewai.tools import BaseTool
import pandas as pd
class AccountDataInsightsTool(BaseTool):
    name="account_data_insights"
    description="Analyze usage and tickets CSV for account_id."
    def _run(self, account_id:str)->str:
        try: usage=pd.read_csv("data/usage.csv")
        except: return "usage.csv missing"
        try: tickets=pd.read_csv("data/tickets.csv")
        except: tickets=pd.DataFrame()
        u=usage[usage["account_id"].astype(str)==str(account_id)]
        out={}
        if not u.empty:
            out["features_top"]=u.groupby("feature")["events"].sum().head(3).to_dict()
        return str(out)
