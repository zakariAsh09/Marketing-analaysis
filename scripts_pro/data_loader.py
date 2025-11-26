# data_loader.py
import os
import sqlite3
import pandas as pd
from config import BASE_PATH, RAW_PATH, CLEAN_PATH, DB_PATH


class DataLoader:
    """Raw / clean CSV fayllarni yuklash va SQLite DB yaratish uchun klass."""

    def load_raw_data(self) -> dict:
        """raw_data papkasidan barcha asosiy CSV fayllarni yuklaydi."""
        campaigns = pd.read_csv(os.path.join(RAW_PATH, "campaigns.csv"))
        campaign_performance = pd.read_csv(os.path.join(RAW_PATH, "campaign_performance.csv"))
        ad_spend = pd.read_csv(os.path.join(RAW_PATH, "ad_spend.csv"))
        conversions = pd.read_csv(os.path.join(RAW_PATH, "conversions.csv"))
        customers_acquired = pd.read_csv(os.path.join(RAW_PATH, "customers_acquired.csv"))
        ab_test_results = pd.read_csv(os.path.join(RAW_PATH, "ab_test_results.csv"))

        return {
            "campaigns": campaigns,
            "campaign_performance": campaign_performance,
            "ad_spend": ad_spend,
            "conversions": conversions,
            "customers_acquired": customers_acquired,
            "ab_test_results": ab_test_results,
        }

    def load_clean_data(self) -> dict:
        """marketing_data_clean papkasidan tozalangan CSV fayllarni yuklaydi."""
        campaigns = pd.read_csv(os.path.join(CLEAN_PATH, "campaigns_clean.csv"))
        campaign_performance = pd.read_csv(os.path.join(CLEAN_PATH, "campaign_performance_clean.csv"))
        ad_spend = pd.read_csv(os.path.join(CLEAN_PATH, "ad_spend_clean.csv"))
        conversions = pd.read_csv(os.path.join(CLEAN_PATH, "conversions_clean.csv"))
        customers_acquired = pd.read_csv(os.path.join(CLEAN_PATH, "customers_acquired_clean.csv"))
        ab_test_results = pd.read_csv(os.path.join(CLEAN_PATH, "ab_test_results_clean.csv"))

        return {
            "campaigns": campaigns,
            "campaign_performance": campaign_performance,
            "ad_spend": ad_spend,
            "conversions": conversions,
            "customers_acquired": customers_acquired,
            "ab_test_results": ab_test_results,
        }

    def create_database(self) -> None:
        """CSV fayllardan SQLite marketing.db bazasini yaratadi / yangilaydi."""
        conn = sqlite3.connect(DB_PATH)
        print("📂 Database ochildi:", DB_PATH)

        tables = {
            "campaigns": "campaigns.csv",
            "campaign_performance": "campaign_performance.csv",
            "ad_spend": "ad_spend.csv",
            "conversions": "conversions.csv",
            "customers_acquired": "customers_acquired.csv",
            "ab_test_results": "ab_test_results.csv",
        }

        for table_name, file_name in tables.items():
            csv_path = os.path.join(RAW_PATH, file_name)
            print(f"➡ {file_name} yuklanmoqda -> {table_name} ...")
            df = pd.read_csv(csv_path)
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"✅ {table_name} jadvali yaratildi. Satrlari: {len(df)}")

        conn.close()
        print("🎉 marketing.db tayyor.")
