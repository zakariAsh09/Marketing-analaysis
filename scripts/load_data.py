import pandas as pd
import os

# Asosiy yo'l: marketing_data papkang joylashgan manzil
BASE_PATH = r"D:\Diplom ishi Proweb\marketing_data"

# Xom ma'lumotlar (raw CSV fayllar) papkasi
RAW_PATH = os.path.join(BASE_PATH, "raw_data")

# Tozalangan ma'lumotlar (clean CSV fayllar) papkasi
CLEAN_PATH = os.path.join(BASE_PATH, "marketing_data_clean")


def load_raw_data():
    """
    Xom (raw_data) papkasidan barcha asosiy CSV fayllarni yuklaydi.
    Natijani dict ko'rinishida qaytaradi.
    """
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


def load_clean_data():
    """
    Agar tozalangan fayllardan foydalanmoqchi bo'lsang,
    shu funksiyadan foydalanasan.
    Fayl nomlarini *_clean.csv deb qildik.
    """
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


if __name__ == "__main__":
    # Test uchun ishlatish mumkin:
    data = load_raw_data()
    print("campaigns:", data["campaigns"].shape)
    print("campaign_performance:", data["campaign_performance"].shape)
