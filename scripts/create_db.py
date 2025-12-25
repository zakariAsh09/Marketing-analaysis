import os
import sqlite3
import pandas as pd

# Loyihaning asosiy yo'li
BASE_PATH = r"D:\Diplom ishi Proweb\marketing_data"
RAW_PATH = os.path.join(BASE_PATH, "raw_data")

# SQLite bazani yaratamiz
db_path = os.path.join(BASE_PATH, "marketing.db")
conn = sqlite3.connect(db_path)

print("📂 Database yaratildi yoki ochildi:", db_path)

# CSV fayllarni o'qib, SQLite ichiga yozamiz
tables = {
    "campaigns": "campaigns.csv",
    "campaign_performance": "campaign_performance.csv",
    "ad_spend": "ad_spend.csv",
    "conversions": "conversions.csv",
    "customers_acquired": "customers_acquired.csv",
    "ab_test_results": "ab_test_results.csv"
}

for table_name, file_name in tables.items():
    csv_path = os.path.join(RAW_PATH, file_name)
    print(f"➡ {file_name} fayli yuklanmoqda -> {table_name} jadvaliga...")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"✅ {table_name} jadvali yaratildi. Satrlari: {len(df)}")

conn.close()
print("🎉 Hammasi tugadi, marketing.db tayyor.")
