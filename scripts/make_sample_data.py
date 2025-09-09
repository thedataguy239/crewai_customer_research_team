import pandas as pd
from pathlib import Path
Path("data").mkdir(exist_ok=True)

# CRM
crm = pd.DataFrame([
    {"account_id": 1001, "company": "Acme Corp", "domain": "acme.com", "industry": "Manufacturing", "arr_band": "100k-250k", "owner": "Jane Smith", "notes": "Strategic"},
    {"account_id": 1002, "company": "Globex Inc", "domain": "globex.com", "industry": "Logistics", "arr_band": "250k-500k", "owner": "Michael Adams", "notes": "Expansion"},
    {"account_id": 1003, "company": "Initech", "domain": "initech.com", "industry": "Software", "arr_band": "25k-50k", "owner": "Samir Nagheenanajar", "notes": "New pilot"}
])
crm.to_excel("data/crm.xlsx", index=False)

# Usage
usage_rows = []
for month in ["2025-04","2025-05","2025-06","2025-07","2025-08","2025-09"]:
    usage_rows += [
        {"account_id":1001,"month":month,"active_users":50+hash(month)%7,"feature":"dashboards","events":1200+hash(month)%200},
        {"account_id":1001,"month":month,"active_users":50+hash(month)%7,"feature":"exports","events":300+hash(month)%60},
        {"account_id":1002,"month":month,"active_users":120+hash(month)%10,"feature":"dashboards","events":4200+hash(month)%400},
        {"account_id":1002,"month":month,"active_users":120+hash(month)%10,"feature":"alerts","events":900+hash(month)%120},
    ]
pd.DataFrame(usage_rows).to_csv("data/usage.csv", index=False)

# Tickets
tickets = pd.DataFrame([
    {"account_id":1001,"ticket_id":"AC-100","category":"billing","age_days":12,"csat":4.6},
    {"account_id":1001,"ticket_id":"AC-101","category":"performance","age_days":5,"csat":4.1},
    {"account_id":1002,"ticket_id":"GB-201","category":"integration","age_days":35,"csat":4.8},
    {"account_id":1002,"ticket_id":"GB-202","category":"permissions","age_days":2,"csat":4.2},
    {"account_id":1002,"ticket_id":"GB-203","category":"performance","age_days":14,"csat":3.9}
])
tickets.to_csv("data/tickets.csv", index=False)

print("Sample data written to data/")
