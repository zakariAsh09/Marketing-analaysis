# visualizations.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from config import METRICS_PATH
from data_loader import DataLoader

sns.set(style="whitegrid")


class VisualizationService:
    """campaign_performance asosida barcha grafiklarni yaratadigan servis."""

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def generate_all_visuals(self) -> None:
        data = self.loader.load_raw_data()
        performance = data["campaign_performance"].copy()

        performance["date"] = pd.to_datetime(performance["date"])
        performance["month"] = performance["date"].dt.month
        performance["weekday"] = performance["date"].dt.day_name()

        # 1. CTR by Month
        monthly = performance.groupby("month").agg({
            "impressions": "sum",
            "clicks": "sum",
        })
        monthly["CTR"] = (monthly["clicks"] / monthly["impressions"]) * 100

        plt.figure(figsize=(12, 6))
        plt.plot(monthly.index, monthly["CTR"], marker="o")
        plt.title("CTR by Month")
        plt.xlabel("Month")
        plt.ylabel("CTR (%)")
        plt.grid(True)
        plt.savefig(os.path.join(METRICS_PATH, "ctr_by_month.png"), bbox_inches="tight")
        plt.close()

        # 2. ROAS by Month
        monthly_rev = performance.groupby("month").agg({
            "revenue_uzs": "sum",
            "cost_uzs": "sum",
        })
        monthly_rev["ROAS"] = monthly_rev["revenue_uzs"] / monthly_rev["cost_uzs"]

        plt.figure(figsize=(12, 6))
        plt.bar(monthly_rev.index, monthly_rev["ROAS"])
        plt.title("ROAS by Month")
        plt.xlabel("Month")
        plt.ylabel("ROAS")
        plt.savefig(os.path.join(METRICS_PATH, "roas_by_month.png"), bbox_inches="tight")
        plt.close()

        # 3. Daily Conversions Trend
        daily = performance.groupby("date")["conversions"].sum().reset_index()

        plt.figure(figsize=(15, 6))
        plt.plot(daily["date"], daily["conversions"])
        plt.title("Daily Conversions Trend")
        plt.xlabel("Date")
        plt.ylabel("Conversions")
        plt.savefig(os.path.join(METRICS_PATH, "daily_conversions_trend.png"), bbox_inches="tight")
        plt.close()

        # 4. CTR by Weekday
        weekday = performance.groupby("weekday").agg({
            "impressions": "sum",
            "clicks": "sum",
        })
        order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekday = weekday.reindex(order_days)
        weekday["CTR"] = (weekday["clicks"] / weekday["impressions"]) * 100

        plt.figure(figsize=(12, 6))
        plt.bar(weekday.index, weekday["CTR"])
        plt.title("CTR by Weekday")
        plt.xlabel("Weekday")
        plt.ylabel("CTR (%)")
        plt.savefig(os.path.join(METRICS_PATH, "ctr_by_weekday.png"), bbox_inches="tight")
        plt.close()

        # 5. ROAS Distribution
        roas_series = performance["revenue_uzs"] / performance["cost_uzs"]

        plt.figure(figsize=(12, 6))
        plt.hist(roas_series, bins=40)
        plt.title("ROAS Distribution")
        plt.xlabel("ROAS")
        plt.ylabel("Count")
        plt.savefig(os.path.join(METRICS_PATH, "roas_distribution.png"), bbox_inches="tight")
        plt.close()

        print("✅ Barcha grafiklar saqlandi.")
