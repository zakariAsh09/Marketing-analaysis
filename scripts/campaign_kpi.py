# campaign_kpi.py

from load_data import load_raw_data, BASE_PATH
import os
import pandas as pd

# Natijalar saqlanadigan papka
METRICS_PATH = os.path.join(BASE_PATH, "metrics")
os.makedirs(METRICS_PATH, exist_ok=True)


def calculate_campaign_kpi():
    """
    Har bir kampaniya uchun asosiy KPI larni hisoblaydi va
    metrics/campaign_kpi_table.csv fayliga saqlaydi.
    """
    # 1. Ma'lumotlarni yuklab olish
    data = load_raw_data()
    campaigns = data["campaigns"]
    performance = data["campaign_performance"]
    ad_spend = data["ad_spend"]

    # 2. Performance bo'yicha agregatsiya
    perf_agg = performance.groupby("campaign_id").agg({
        "impressions": "sum",
        "clicks": "sum",
        "conversions": "sum",
        "cost_uzs": "sum",
        "revenue_uzs": "sum"
    }).reset_index()

    # 3. Reklama xarajatlari bo'yicha agregatsiya
    ad_spend_agg = ad_spend.groupby("campaign_id").agg({
        "amount_spent": "sum"
    }).reset_index()

    # 4. Hammasini birlashtirish
    df = campaigns.merge(perf_agg, on="campaign_id", how="left")
    df = df.merge(ad_spend_agg, on="campaign_id", how="left")

    # 5. KPI larni hisoblash
    df["amount_spent"] = df["amount_spent"].fillna(0)
    df["total_cost"] = df["cost_uzs"] + df["amount_spent"]

    df["CTR"] = (df["clicks"] / df["impressions"]) * 100
    df["CPC"] = df["total_cost"] / df["clicks"]
    df["Conversion_Rate"] = (df["conversions"] / df["clicks"]) * 100
    df["ROAS"] = df["revenue_uzs"] / df["total_cost"]
    df["Profit"] = df["revenue_uzs"] - df["total_cost"]

    # 6. Natijani saqlash
    output_path = os.path.join(METRICS_PATH, "campaign_kpi_table.csv")
    df.to_csv(output_path, index=False)

    print("✅ Campaign KPI jadvali saqlandi:")
    print(output_path)
    print("Shakl:", df.shape)


if __name__ == "__main__":
    calculate_campaign_kpi()
