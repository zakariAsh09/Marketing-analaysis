# main.py

from campaign_kpi import calculate_campaign_kpi
from demographic_analysis import run_demographic_analysis
from time_analysis import run_time_analysis
from visualizations import generate_all_visuals
from load_data import BASE_PATH
import os


def run_full_pipeline():
    """
    Diplom ishi uchun barcha asosiy bosqichlarni ketma-ket bajaradi:
    1) Kampaniya KPI larini hisoblash
    2) Demografik tahlil
    3) Vaqt bo'yicha tahlil
    4) Grafiklarni yaratish
    """

    print("📂 Loyihaning asosiy papkasi:", BASE_PATH)
    print("🚀 Pipeline ishga tushdi...\n")

    # 1. Kampaniya KPI
    print("1️⃣ Kampaniya KPI hisoblanmoqda...")
    calculate_campaign_kpi()
    print("✅ Kampaniya KPI tugadi.\n")

    # 2. Demografik tahlil
    print("2️⃣ Demografik tahlil bajarilmoqda...")
    run_demographic_analysis()
    print("✅ Demografik tahlil tugadi.\n")

    # 3. Vaqt bo'yicha tahlil
    print("3️⃣ Vaqt (oy/hafta kunlari) tahlili bajarilmoqda...")
    run_time_analysis()
    print("✅ Vaqt tahlili tugadi.\n")

    # 4. Grafiklar
    print("4️⃣ Grafiklar yaratilmoqda...")
    generate_all_visuals()
    print("✅ Grafiklar yaratildi.\n")

    print("🎉 BARCHA BOSQICHLAR MUVAFFAQIYATLI YAKUNLANDI!")
    print("Natijalar 'metrics' papkasida saqlangan.")


if __name__ == "__main__":
    run_full_pipeline()
