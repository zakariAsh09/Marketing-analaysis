# campaign_kpi.py
import os
import pandas as pd
from config import METRICS_PATH
from data_loader import DataLoader


class CampaignKPIService:
    """Har bir kampaniya uchun asosiy KPI larni hisoblaydigan servis."""

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def calculate_campaign_kpi(self) -> pd.DataFrame:
        """KPI larni hisoblab, CSV ga saqlaydi va DataFrame qaytaradi."""
        data = self.loader.load_raw_data()
        campaigns = data["campaigns"]
        performance = data["campaign_performance"]
        ad_spend = data["ad_spend"]

        # Performance agregatsiya
        perf_agg = performance.groupby("campaign_id").agg({
            "impressions": "sum",
            "clicks": "sum",
            "conversions": "sum",
            "cost_uzs": "sum",
            "revenue_uzs": "sum",
        }).reset_index()

        # Ad spend agregatsiya
        ad_spend_agg = ad_spend.groupby("campaign_id").agg({
            "amount_spent": "sum",
        }).reset_index()

        # Birlashtirish
        df = campaigns.merge(perf_agg, on="campaign_id", how="left")
        df = df.merge(ad_spend_agg, on="campaign_id", how="left")

        # KPI lar
        df["amount_spent"] = df["amount_spent"].fillna(0)
        df["total_cost"] = df["cost_uzs"] + df["amount_spent"]

        df["CTR"] = (df["clicks"] / df["impressions"]) * 100
        df["CPC"] = df["total_cost"] / df["clicks"]
        df["Conversion_Rate"] = (df["conversions"] / df["clicks"]) * 100
        df["ROAS"] = df["revenue_uzs"] / df["total_cost"]
        df["Profit"] = df["revenue_uzs"] - df["total_cost"]

        # Saqlash
        output_path = os.path.join(METRICS_PATH, "campaign_kpi_table.csv")
        df.to_csv(output_path, index=False)

        print("✅ Campaign KPI jadvali saqlandi:", output_path, "| Shakl:", df.shape)
        return df
