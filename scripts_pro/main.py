# main.py
from config import BASE_PATH
from data_loader import DataLoader
from campaign_kpi import CampaignKPIService
from demographic_analysis import DemographicService
from time_analysis import TimeAnalysisService
from visualizations import VisualizationService


class PipelineRunner:
    """Diplom ishi uchun to'liq marketing analytics pipeline."""

    def __init__(self):
        self.loader = DataLoader()
        self.kpi_service = CampaignKPIService(self.loader)
        self.demo_service = DemographicService(self.loader)
        self.time_service = TimeAnalysisService(self.loader)
        self.viz_service = VisualizationService(self.loader)

    def run_all(self) -> None:
        print("📂 Loyihaning asosiy papkasi:", BASE_PATH)
        print("🚀 Pipeline ishga tushdi...\n")

        # 0. (ixtiyoriy) DB yaratish
        # self.loader.create_database()

        print("1️⃣ Kampaniya KPI hisoblanmoqda...")
        self.kpi_service.calculate_campaign_kpi()
        print("✅ Kampaniya KPI tugadi.\n")

        print("2️⃣ Demografik tahlil bajarilmoqda...")
        self.demo_service.run_demographic_analysis()
        print("✅ Demografik tahlil tugadi.\n")

        print("3️⃣ Vaqt tahlili bajarilmoqda...")
        self.time_service.run_time_analysis()
        print("✅ Vaqt tahlili tugadi.\n")

        print("4️⃣ Grafiklar yaratilmoqda...")
        self.viz_service.generate_all_visuals()
        print("✅ Grafiklar yaratildi.\n")

        print("🎉 Barcha bosqichlar muvaffaqiyatli yakunlandi!")


if __name__ == "__main__":
    runner = PipelineRunner()
    runner.run_all()
