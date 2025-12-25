# time_analysis.py
import os
import pandas as pd
from config import METRICS_PATH
from data_loader import DataLoader


class TimeAnalysisService:
    """Oylik va hafta kunlari bo'yicha performance tahlili."""

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def run_time_analysis(self) -> None:
        data = self.loader.load_raw_data()
        performance = data["campaign_performance"].copy()

        performance["date"] = pd.to_datetime(performance["date"])
        performance["year"] = performance["date"].dt.year
        performance["month"] = performance["date"].dt.month
        performance["month_name"] = performance["date"].dt.strftime("%B")
        performance["week"] = performance["date"].dt.isocalendar().week
        performance["weekday"] = performance["date"].dt.day_name()

        print("Vaqt ustunlari qo'shildi. Shakl:", performance.shape)

        # Oylik
        monthly_stats = performance.groupby("month").agg({
            "impressions": "sum",
            "clicks": "sum",
            "conversions": "sum",
            "cost_uzs": "sum",
            "revenue_uzs": "sum",
        }).reset_index()

        monthly_stats["CTR"] = (monthly_stats["clicks"] / monthly_stats["impressions"]) * 100
        monthly_stats["CR"] = (monthly_stats["conversions"] / monthly_stats["clicks"]) * 100
        monthly_stats["ROAS"] = monthly_stats["revenue_uzs"] / monthly_stats["cost_uzs"]

        # Haftalik
        weekday_stats = performance.groupby("weekday").agg({
            "impressions": "sum",
            "clicks": "sum",
            "conversions": "sum",
            "cost_uzs": "sum",
            "revenue_uzs": "sum",
        }).reset_index()

        weekday_stats["CTR"] = (weekday_stats["clicks"] / weekday_stats["impressions"]) * 100
        weekday_stats["CR"] = (weekday_stats["conversions"] / weekday_stats["clicks"]) * 100
        weekday_stats["ROAS"] = weekday_stats["revenue_uzs"] / weekday_stats["cost_uzs"]

        order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekday_stats["weekday"] = pd.Categorical(weekday_stats["weekday"], categories=order_days, ordered=True)
        weekday_stats = weekday_stats.sort_values("weekday")

        monthly_stats.to_csv(os.path.join(METRICS_PATH, "monthly_performance.csv"), index=False)
        weekday_stats.to_csv(os.path.join(METRICS_PATH, "weekday_performance.csv"), index=False)

        print("✅ Vaqt tahlili fayllari saqlandi.")
