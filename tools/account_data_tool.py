from crewai.tools import BaseTool
import pandas as pd

class AccountDataInsightsTool(BaseTool):
    name: str = "account_data_insights"
    description: ("Given a customer 'account_id', analyze mock usage and tickets "
                  "from data/usage.csv and data/tickets.csv. Output concise KPIs: "
                  "trend deltas, feature adoption, ticket themes, CSAT.")

    def _run(self, account_id: str) -> str:
        try:
            usage = pd.read_csv("data/usage.csv")
        except Exception:
            usage = pd.DataFrame()
        try:
            tickets = pd.read_csv("data/tickets.csv")
        except Exception:
            tickets = pd.DataFrame()

        u = usage[usage["account_id"].astype(str)==str(account_id)] if not usage.empty else pd.DataFrame()
        t = tickets[tickets["account_id"].astype(str)==str(account_id)] if not tickets.empty else pd.DataFrame()
        if u.empty and t.empty:
            return "No data found for account_id."

        kpis = {}
        if not u.empty:
            by_month = (u.groupby("month")["active_users"]
                        .sum()
                        .sort_index())
            trend = int(by_month.iloc[-1] - by_month.iloc[0]) if len(by_month)>1 else 0
            kpis["active_users_last"] = int(by_month.iloc[-1])
            kpis["active_users_trend_delta"] = trend
            kpis["features_top"] = (u.groupby("feature")["events"]
                                      .sum().sort_values(ascending=False).head(5).to_dict())

        if not t.empty:
            kpis["tickets_30d"] = int((t["age_days"]<=30).sum())
            kpis["top_themes"] = (t["category"].value_counts().head(5).to_dict())
            if "csat" in t.columns and not t["csat"].isna().all():
                kpis["csat_avg"] = round(float(t["csat"].mean()), 2)

        return str(kpis)
