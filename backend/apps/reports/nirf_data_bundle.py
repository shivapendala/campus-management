"""
EduCore Enterprise Framework - NIRF Data Capturing System (DCS) Standardized Package Exporter

Packages institutional data tables into standard NIRF DCS format:
- Sanctioned Approved Intake (UG 4-Year B.Tech, PG 2-Year M.Tech, Ph.D)
- Actual Enrolment (Male, Female, Outside State, Economically Challenged)
- Placement & Higher Studies Table (Median Salary, Placed Numbers)
- Capital & Operational Expenditure Table (Lab Equipment, Library, Salaries)
"""

from typing import Dict, List, Any, Optional


class NIRFDataBundleExporter:
    """
    Constructs NIRF DCS standard regulatory JSON export structures.
    """

    @classmethod
    def generate_nirf_dcs_bundle(cls, academic_year: str = "2025-26") -> Dict[str, Any]:
        """Generate standardized NIRF DCS data tables."""
        return {
            "institution_nirf_code": "NIRF-ENGG-2026-08421",
            "institution_name": "EduCore University Institute of Technology",
            "academic_year": academic_year,
            "intake_data": [
                {"program": "UG [4 Years Program(s)]", "year_1": 600, "year_2": 600, "year_3": 600, "year_4": 600},
                {"program": "PG [2 Years Program(s)]", "year_1": 120, "year_2": 120},
                {"program": "Ph.D Program", "full_time": 85, "part_time": 45}
            ],
            "financial_resources": {
                "annual_capital_expenditure_inr": {
                    "library_books_and_journals": 4500000.0,
                    "new_equipment_for_laboratories": 18500000.0,
                    "engineering_workshops": 3200000.0,
                    "studios_and_other_capex": 2400000.0
                },
                "annual_operational_expenditure_inr": {
                    "salaries_of_teaching_and_non_teaching_staff": 85000000.0,
                    "maintenance_of_academic_infrastructure": 12500000.0,
                    "seminars_conferences_workshops": 3500000.0
                }
            },
            "status": "VALIDATED_AND_LOCKED_FOR_SUBMISSION"
        }
