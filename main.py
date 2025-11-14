import pandas as pd
import os

# Fayllar yo'li
DATA_PATH = "path_to_data"  # agar /mnt/data bo'lsa, shuni yozasan

# 1. Kampaniyalar
campaigns = pd.read_csv(os.path.join(DATA_PATH, "campaigns.csv"))
print("campaigns:", campaigns.shape)
print(campaigns.head())
print(campaigns.info())

# 2. Kampaniya performance
campaign_performance = pd.read_csv(os.path.join(DATA_PATH, "campaign_performance.csv"))
print("\ncampaign_performance:", campaign_performance.shape)
print(campaign_performance.head())
print(campaign_performance.info())

# 3. Reklama xarajatlari
ad_spend = pd.read_csv(os.path.join(DATA_PATH, "ad_spend.csv"))
print("\nad_spend:", ad_spend.shape)
print(ad_spend.head())
print(ad_spend.info())

# 4. Konversiyalar
conversions = pd.read_csv(os.path.join(DATA_PATH, "conversions.csv"))
print("\nconversions:", conversions.shape)
print(conversions.head())
print(conversions.info())

# 5. Yangi mijozlar
customers_acquired = pd.read_csv(os.path.join(DATA_PATH, "customers_acquired.csv"))
print("\ncustomers_acquired:", customers_acquired.shape)
print(customers_acquired.head())
print(customers_acquired.info())

# 6. A/B test natijalari
ab_test_results = pd.read_csv(os.path.join(DATA_PATH, "ab_test_results.csv"))
print("\nab_test_results:", ab_test_results.shape)
print(ab_test_results.head())
print(ab_test_results.info())
