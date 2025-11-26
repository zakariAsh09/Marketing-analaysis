# demographic_analysis.py
import os
import pandas as pd
from config import METRICS_PATH
from data_loader import DataLoader


class DemographicService:
    """Conversions + customers_acquired bo'yicha demografik tahlil servisi."""

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def run_demographic_analysis(self) -> None:
        data = self.loader.load_raw_data()
        conversions = data["conversions"]
        customers = data["customers_acquired"]

        customers_small = customers[["customer_id", "age_group", "gender", "device", "lifetime_value"]]

        merged = conversions.merge(customers_small, on="customer_id", how="left")
        print("Birlashtirilgan jadval shakli:", merged.shape)

        # Gender
        gender_stats = (
            merged.groupby("gender")
            .agg({"conversion_id": "count", "lifetime_value": "mean"})
            .rename(columns={"conversion_id": "total_conversions", "lifetime_value": "avg_ltv"})
            .reset_index()
        )

        # Age
        age_stats = (
            merged.groupby("age_group")
            .agg({"conversion_id": "count", "lifetime_value": "mean"})
            .rename(columns={"conversion_id": "total_conversions", "lifetime_value": "avg_ltv"})
            .reset_index()
        )

        # Device
        device_stats = (
            merged.groupby("device")
            .agg({"conversion_id": "count", "lifetime_value": "mean"})
            .rename(columns={"conversion_id": "total_conversions", "lifetime_value": "avg_ltv"})
            .reset_index()
        )

        merged.to_csv(os.path.join(METRICS_PATH, "demographic_merged.csv"), index=False)
        gender_stats.to_csv(os.path.join(METRICS_PATH, "demographic_gender_stats.csv"), index=False)
        age_stats.to_csv(os.path.join(METRICS_PATH, "demographic_age_stats.csv"), index=False)
        device_stats.to_csv(os.path.join(METRICS_PATH, "demographic_device_stats.csv"), index=False)

        print("✅ Demografik tahlil fayllari saqlandi.")
