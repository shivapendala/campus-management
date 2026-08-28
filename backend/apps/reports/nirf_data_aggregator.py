"""
EduCore Framework - National Institutional Ranking Framework (NIRF) Aggregator

Compiles required metrics: graduation outcomes (GPHD, GUE), financial resource utilization (FRU),
and research publications output summaries.
"""

from typing import Dict, List, Any

class NIRFDataAggregator:
    def __init__(self, target_year: str):
        self.target_year = target_year
        self.graduation_outcomes: Dict[str, Any] = {}
        self.expenditure_records: Dict[str, Any] = {}

    def log_graduation_metrics(self, category: str, intake: int, graduated_on_time: int, average_ctc: float) -> None:
        self.graduation_outcomes[category] = {
            "intake_strength": intake,
            "graduated_minimum_time": graduated_on_time,
            "graduation_percentage": round((graduated_on_time / intake * 100.0), 2) if intake > 0 else 0.0,
            "median_salary_ctc": average_ctc
        }

    def log_financial_utilization(self, capital_expenditure: float, operational_expenditure: float) -> None:
        self.expenditure_records = {
            "capital_expenditure": capital_expenditure,
            "operational_expenditure": operational_expenditure,
            "total_expenditure": capital_expenditure + operational_expenditure
        }

    def generate_nirf_metrics_report(self) -> Dict[str, Any]:
        return {
            "nirf_reporting_year": self.target_year,
            "graduation_metrics": self.graduation_outcomes,
            "expenditure_summary": self.expenditure_records
        }
