# visualizations.py

from load_data import load_raw_data, BASE_PATH
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Natijalar saqlanadigan papka
METRICS_PATH = os.path.join(BASE_PATH, "metrics")
os.makedirs(METRICS_PATH, exist_ok=True)

sns.set(style="whitegrid")


def generate_all_visuals():
    """
    campaign_performance ma'lumotlari asosida grafiklar yaratadi va
    metrics papkasiga PNG fayl sifatida saqlaydi.
    """

    data = load_raw_data()
    performance = data["campaign_performance"].copy()

    # Sana ustunini datetime formatga o'tkazish
    performance["date"] = pd.to_datetime(performance["date"])

    # Qo'shimcha vaqt ustunlari
    performance["month"] = performance["date"].dt.month
    performance["month_name"] = performance["date"].dt.strftime("%B")
    performance["weekday"] = performance["date"].dt.day_name()

    # ---------------------------------------------------------
    # 1. CTR by Month (Aylik CTR grafiki)
    # ---------------------------------------------------------
    monthly = performance.groupby("month").agg({
        "impressions": "sum",
        "clicks": "sum"
    })
    monthly["CTR"] = (monthly["clicks"] / monthly["impressions"]) * 100

    plt.figure(figsize=(12, 6))
    plt.plot(monthly.index, monthly["CTR"], marker="o")
    plt.title("CTR by Month")
    plt.xlabel("Month")
    plt.ylabel("CTR (%)")
    plt.grid(True)

    ctr_month_path = os.path.join(METRICS_PATH, "ctr_by_month.png")
    plt.savefig(ctr_month_path, bbox_inches="tight")
    plt.close()
    print("Saved:", ctr_month_path)

    # ---------------------------------------------------------
    # 2. ROAS by Month (Aylik ROAS)
    # ---------------------------------------------------------
    monthly_rev = performance.groupby("month").agg({
        "revenue_uzs": "sum",
        "cost_uzs": "sum"
    })
    monthly_rev["ROAS"] = monthly_rev["revenue_uzs"] / monthly_rev["cost_uzs"]

    plt.figure(figsize=(12, 6))
    plt.bar(monthly_rev.index, monthly_rev["ROAS"])
    plt.title("ROAS by Month")
    plt.xlabel("Month")
    plt.ylabel("ROAS")

    roas_month_path = os.path.join(METRICS_PATH, "roas_by_month.png")
    plt.savefig(roas_month_path, bbox_inches="tight")
    plt.close()
    print("Saved:", roas_month_path)

    # ---------------------------------------------------------
    # 3. Daily Conversions Trend (kunlik konversiyalar)
    # ---------------------------------------------------------
    daily = performance.groupby("date")["conversions"].sum().reset_index()

    plt.figure(figsize=(15, 6))
    plt.plot(daily["date"], daily["conversions"])
    plt.title("Daily Conversions Trend")
    plt.xlabel("Date")
    plt.ylabel("Conversions")

    daily_conv_path = os.path.join(METRICS_PATH, "daily_conversions_trend.png")
    plt.savefig(daily_conv_path, bbox_inches="tight")
    plt.close()
    print("Saved:", daily_conv_path)

    # ---------------------------------------------------------
    # 4. CTR by Weekday (Hafta kunlari bo‘yicha CTR)
    # ---------------------------------------------------------
    weekday = performance.groupby("weekday").agg({
        "impressions": "sum",
        "clicks": "sum"
    })
    weekday["CTR"] = (weekday["clicks"] / weekday["impressions"]) * 100

    order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday = weekday.reindex(order_days)

    plt.figure(figsize=(12, 6))
    plt.bar(weekday.index, weekday["CTR"])
    plt.title("CTR by Weekday")
    plt.xlabel("Weekday")
    plt.ylabel("CTR (%)")

    weekday_ctr_path = os.path.join(METRICS_PATH, "ctr_by_weekday.png")
    plt.savefig(weekday_ctr_path, bbox_inches="tight")
    plt.close()
    print("Saved:", weekday_ctr_path)

    # ---------------------------------------------------------
    # 5. ROAS Distribution (ROAS tarqalishi)
    # ---------------------------------------------------------
    roas_series = performance["revenue_uzs"] / performance["cost_uzs"]

    plt.figure(figsize=(12, 6))
    plt.hist(roas_series, bins=40)
    plt.title("ROAS Distribution")
    plt.xlabel("ROAS")
    plt.ylabel("Count")

    roas_dist_path = os.path.join(METRICS_PATH, "roas_distribution.png")
    plt.savefig(roas_dist_path, bbox_inches="tight")
    plt.close()
    print("Saved:", roas_dist_path)


if __name__ == "__main__":
    generate_all_visuals()
