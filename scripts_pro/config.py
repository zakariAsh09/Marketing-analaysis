# config.py
import os

# Loyihaning asosiy yo'li
BASE_PATH = r"E:\FayzullohData\Diplom ishi Proweb\marketing_data"


# Papkalar
RAW_PATH = os.path.join(BASE_PATH, "raw_data")
CLEAN_PATH = os.path.join(BASE_PATH, "marketing_data_clean")
METRICS_PATH = os.path.join(BASE_PATH, "metrics")
DB_PATH = os.path.join(BASE_PATH, "marketing.db")

# Kerakli papkalarni yaratib qo'yamiz
os.makedirs(METRICS_PATH, exist_ok=True)
