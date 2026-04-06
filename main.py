from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from analytics_service import AnalyticsService

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

service = AnalyticsService("data")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/kpi/pricing-summary")
def pricing():
    return service.pricing_summary()

@app.get("/kpi/revenue-by-section")
def revenue():
    return service.revenue_by_section()
