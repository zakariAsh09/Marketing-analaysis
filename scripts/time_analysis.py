# time_analysis.py

from load_data import load_raw_data, BASE_PATH
import os
import pandas as pd

METRICS_PATH = os.path.join(BASE_PATH, "metrics")
os.makedirs(METRICS_PATH, exist_ok=True)


def run_time_analysis():
    """
    Vaqt (oy va hafta kunlari) bo'yicha kampaniya performance tahlili.
    Natijalarni monthly_performance.csv va weekday_performance.csv sifatida saqlaydi.
    """
    data = load_raw_data()
    performance = data["campaign_performance"].copy()

    # 1. Sana ustunini datetime formatga o'tkazish
    performance["date"] = pd.to_datetime(performance["date"])

    # 2. Qo'shimcha vaqt ustunlari
    performance["year"] = performance["date"].dt.year
    performance["month"] = performance["date"].dt.month
    performance["month_name"] = performance["date"].dt.strftime("%B")
    performance["week"] = performance["date"].dt.isocalendar().week
    performance["weekday"] = performance["date"].dt.day_name()

    print("Vaqt ustunlari qo'shildi. Shakl:", performance.shape)

    # 3. Oylar bo'yicha agregatsiya
    monthly_stats = performance.groupby("month").agg({
        "impressions": "sum",
        "clicks": "sum",
        "conversions": "sum",
        "cost_uzs": "sum",
        "revenue_uzs": "sum"
    }).reset_index()

    # KPI lar
    monthly_stats["CTR"] = (monthly_stats["clicks"] / monthly_stats["impressions"]) * 100
    monthly_stats["CR"] = (monthly_stats["conversions"] / monthly_stats["clicks"]) * 100
    monthly_stats["ROAS"] = monthly_stats["revenue_uzs"] / monthly_stats["cost_uzs"]

    # 4. Haftaning kunlari bo'yicha agregatsiya
    weekday_stats = performance.groupby("weekday").agg({
        "impressions": "sum",
        "clicks": "sum",
        "conversions": "sum",
        "cost_uzs": "sum",
        "revenue_uzs": "sum"
    }).reset_index()

    weekday_stats["CTR"] = (weekday_stats["clicks"] / weekday_stats["impressions"]) * 100
    weekday_stats["CR"] = (weekday_stats["conversions"] / weekday_stats["clicks"]) * 100
    weekday_stats["ROAS"] = weekday_stats["revenue_uzs"] / weekday_stats["cost_uzs"]

    # Kunlar tartibi (Monday → Sunday)
    order_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_stats["weekday"] = pd.Categorical(weekday_stats["weekday"], categories=order_days, ordered=True)
    weekday_stats = weekday_stats.sort_values("weekday")

    # 5. CSV fayllarni saqlash
    monthly_path = os.path.join(METRICS_PATH, "monthly_performance.csv")
    weekday_path = os.path.join(METRICS_PATH, "weekday_performance.csv")

    monthly_stats.to_csv(monthly_path, index=False)
    weekday_stats.to_csv(weekday_path, index=False)

    print("✅ Vaqt tahlili fayllari saqlandi:")
    print(" -", monthly_path)
    print(" -", weekday_path)


if __name__ == "__main__":
    run_time_analysis()
