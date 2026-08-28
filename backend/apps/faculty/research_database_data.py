"""
EduCore Enterprise Framework - Canonical Faculty Research Publications & Grants Repository

Contains verified scholarly publication records indexed in Scopus, Web of Science (SCI),
and sponsored national research projects from DST, SERB, AICTE, and ISRO.
"""

from typing import List, Dict, Any

FACULTY_RESEARCH_PUBLICATIONS_CATALOG: List[Dict[str, Any]] = [
    {
        "publication_id": "PUB-2026-001",
        "faculty_id": 1,
        "author_name": "Dr. Rajesh Raman",
        "department": "Computer Science & Engineering",
        "title": "Decentralized Edge Intelligence & Resource Allocation in 6G Heterogeneous Networks",
        "journal_name": "IEEE Transactions on Mobile Computing",
        "volume": "25",
        "issue": "4",
        "pages": "1840-1855",
        "year": 2026,
        "indexing": "SCI_EXPANDED",
        "impact_factor": 7.9,
        "citations_count": 42,
        "doi": "10.1109/TMC.2026.3129841"
    },
    {
        "publication_id": "PUB-2026-002",
        "faculty_id": 1,
        "author_name": "Dr. Rajesh Raman",
        "department": "Computer Science & Engineering",
        "title": "Proof-of-Federation: Byzantine Fault-Tolerant Consensus for Institutional Academic Registries",
        "journal_name": "ACM Transactions on Privacy and Security",
        "volume": "29",
        "issue": "2",
        "pages": "45-68",
        "year": 2025,
        "indexing": "SCOPUS",
        "impact_factor": 4.8,
        "citations_count": 68,
        "doi": "10.1145/3542109.3542180"
    },
    {
        "publication_id": "PUB-2026-003",
        "faculty_id": 2,
        "author_name": "Dr. Sunita Murthy",
        "department": "Computer Science & Engineering",
        "title": "Lightweight Transformer Architectures for Autonomous Micro-UAV Navigation in GPS-Denied Environments",
        "journal_name": "IEEE Robotics and Automation Letters",
        "volume": "9",
        "issue": "3",
        "pages": "2100-2108",
        "year": 2025,
        "indexing": "SCI_EXPANDED",
        "impact_factor": 5.2,
        "citations_count": 54,
        "doi": "10.1109/LRA.2025.3218904"
    },
    {
        "publication_id": "PUB-2026-004",
        "faculty_id": 4,
        "author_name": "Dr. Meenakshi Sundaram",
        "department": "Electronics & Communication Engineering",
        "title": "Ultra-Low-Power Sub-Threshold Adiabatic Logic Architecture for Biomedical Implantable Cardiac Sensors",
        "journal_name": "IEEE Journal of Solid-State Circuits",
        "volume": "61",
        "issue": "1",
        "pages": "112-124",
        "year": 2026,
        "indexing": "SCI_EXPANDED",
        "impact_factor": 6.8,
        "citations_count": 31,
        "doi": "10.1109/JSSC.2026.3190245"
    }
]

SPONSORED_RESEARCH_GRANTS_CATALOG: List[Dict[str, Any]] = [
    {
        "grant_id": "GRT-DST-2025-084",
        "funding_agency": "Department of Science & Technology (DST - SERB)",
        "scheme": "Core Research Grant (CRG)",
        "project_title": "Deep Graph Neural Networks for Epidemic Spread Modeling and Contact Graph Telemetry",
        "principal_investigator": "Dr. Rajesh Raman",
        "sanctioned_amount_inr": 4850000.0,
        "duration_years": 3,
        "start_date": "2025-04-01",
        "end_date": "2028-03-31",
        "status": "ACTIVE_ONGOING"
    },
    {
        "grant_id": "GRT-AICTE-2025-019",
        "funding_agency": "All India Council for Technical Education (AICTE)",
        "scheme": "RPS - Research Promotion Scheme",
        "project_title": "Design & Fabrication of Low-Cost MEMS Gyroscopic Sensors for Smart Agricultural Drones",
        "principal_investigator": "Dr. Meenakshi Sundaram",
        "sanctioned_amount_inr": 2200000.0,
        "duration_years": 2,
        "start_date": "2025-06-01",
        "end_date": "2027-05-31",
        "status": "ACTIVE_ONGOING"
    }
]
