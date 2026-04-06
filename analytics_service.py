from pathlib import Path
import pandas as pd

class AnalyticsService:
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)

        self.transactions = pd.read_csv(self.data_dir / "transactions.csv")
        self.products = pd.read_csv(self.data_dir / "product_master.csv")
        self.accounts = pd.read_csv(self.data_dir / "account_master.csv")
        self.leads = pd.read_csv(self.data_dir / "lead_funnel.csv")
        self.audit = pd.read_csv(self.data_dir / "audit_log.csv")
        self.services = pd.read_csv(self.data_dir / "service_events.csv")

    def pricing_summary(self):
        df = self.transactions.copy()
        return {
            "total_revenue": float(df["revenue_usd"].sum()),
            "avg_price": float(df["negotiated_price_usd"].mean()),
            "avg_margin_pct": float(df["gross_margin_pct"].mean()),
            "compliance_rate": float(df["compliance_ok"].mean()),
            "transactions": int(len(df)),
        }

    def revenue_by_section(self):
        return self.transactions.groupby("section")["revenue_usd"].sum().reset_index().to_dict(orient="records")
