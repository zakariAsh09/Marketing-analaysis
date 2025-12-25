# demographic_analysis.py

from load_data import load_raw_data, BASE_PATH
import os
import pandas as pd

# Natijalar uchun papka
METRICS_PATH = os.path.join(BASE_PATH, "metrics")
os.makedirs(METRICS_PATH, exist_ok=True)


def run_demographic_analysis():
    """
    conversions + customers_acquired jadvalini birlashtirib,
    gender, age_group va device bo'yicha tahlil qiladi.
    Natijani metrics papkasiga saqlaydi.
    """
    data = load_raw_data()
    conversions = data["conversions"]
    customers = data["customers_acquired"]

    # Faqat kerakli ustunlar
    customers_small = customers[["customer_id", "age_group", "gender", "device", "lifetime_value"]]

    # Birlashtirish
    merged = conversions.merge(
        customers_small,
        on="customer_id",
        how="left"
    )

    print("Birlashtirilgan jadval shakli:", merged.shape)

    # Gender bo'yicha tahlil
    gender_stats = merged.groupby("gender").agg({
        "conversion_id": "count",
        "lifetime_value": "mean"
    }).rename(columns={
        "conversion_id": "total_conversions",
        "lifetime_value": "avg_ltv"
    }).reset_index()

    # Age group bo'yicha tahlil
    age_stats = merged.groupby("age_group").agg({
        "conversion_id": "count",
        "lifetime_value": "mean"
    }).rename(columns={
        "conversion_id": "total_conversions",
        "lifetime_value": "avg_ltv"
    }).reset_index()

    # Device bo'yicha tahlil
    device_stats = merged.groupby("device").agg({
        "conversion_id": "count",
        "lifetime_value": "mean"
    }).rename(columns={
        "conversion_id": "total_conversions",
        "lifetime_value": "avg_ltv"
    }).reset_index()

    # Natijalarni CSV ga saqlash
    merged_path = os.path.join(METRICS_PATH, "demographic_merged.csv")
    gender_path = os.path.join(METRICS_PATH, "demographic_gender_stats.csv")
    age_path = os.path.join(METRICS_PATH, "demographic_age_stats.csv")
    device_path = os.path.join(METRICS_PATH, "demographic_device_stats.csv")

    merged.to_csv(merged_path, index=False)
    gender_stats.to_csv(gender_path, index=False)
    age_stats.to_csv(age_path, index=False)
    device_stats.to_csv(device_path, index=False)

    print("✅ Demografik tahlil fayllari saqlandi:")
    print(" -", merged_path)
    print(" -", gender_path)
    print(" -", age_path)
    print(" -", device_path)


if __name__ == "__main__":
    run_demographic_analysis()
