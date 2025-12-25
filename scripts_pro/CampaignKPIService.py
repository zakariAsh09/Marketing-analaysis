# scripts_pro/campaign_kpi.py ichida, KPI hisoblagandan keyin:
import pandas as pd

df["month"] = pd.to_datetime(df["start_date"]).dt.month

powerbi_cols = [
    "campaign_id", "campaign_name", "channel", "campaign_type",
    "start_date", "end_date",
    "impressions", "clicks", "conversions",
    "cost_uzs", "amount_spent", "total_cost",
    "revenue_uzs", "CTR", "CPC", "Conversion_Rate",
    "ROAS", "Profit", "month"
]

powerbi_master = df[powerbi_cols]

powerbi_master.to_csv(os.path.join(METRICS_PATH, "powerbi_master.csv"), index=False)
print("✅ Power BI uchun master jadval saqlandi: powerbi_master.csv")
