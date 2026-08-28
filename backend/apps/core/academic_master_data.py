"""
EduCore Enterprise Framework - Master Academic Programs, Curricula, and Course Specifications

Comprehensive canonical definitions for 5 Engineering Undergraduate Programs:
- B.Tech in Computer Science & Engineering (CSE)
- B.Tech in Electronics & Communication Engineering (ECE)
- B.Tech in Electrical & Electronics Engineering (EEE)
- B.Tech in Mechanical Engineering (MECH)
- B.Tech in Civil Engineering (CIVIL)
Each with semester course maps, credit structures, contact hours, and course objectives.
"""

from typing import Dict, List, Any

ACADEMIC_PROGRAMS_MASTER_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "BTECH_CSE": {
        "program_code": "BTECH_CSE",
        "program_title": "Bachelor of Technology in Computer Science & Engineering",
        "department": "Computer Science & Engineering",
        "duration_years": 4,
        "total_semesters": 8,
        "total_credits_required": 160,
        "program_educational_objectives": [
            {
                "peo_id": "PEO1",
                "title": "Core Competency in Computing",
                "description": "Graduates will establish successful professional careers in computing and software engineering, applying foundational principles of mathematical algorithms, computer architecture, systems software, and data structures."
            },
            {
                "peo_id": "PEO2",
                "title": "Technical Innovation & Research",
                "description": "Graduates will innovate novel computational architectures, algorithms, and applications in Artificial Intelligence, Cloud Infrastructure, Cyber-Physical Systems, and Data Engineering."
            },
            {
                "peo_id": "PEO3",
                "title": "Professional Ethics & Leadership",
                "description": "Graduates will demonstrate professional leadership, multidisciplinary teamwork, intellectual integrity, and commitment to statutory data privacy, ethical artificial intelligence, and societal sustainable development."
            }
        ],
        "program_outcomes": [
            {"po_id": "PO1", "title": "Engineering Knowledge", "description": "Apply the knowledge of mathematics, science, engineering fundamentals, and an engineering specialization to the solution of complex computer engineering problems."},
            {"po_id": "PO2", "title": "Problem Analysis", "description": "Identify, formulate, review research literature, and analyze complex computer engineering problems reaching substantiated conclusions using first principles of mathematics, natural sciences, and engineering sciences."},
            {"po_id": "PO3", "title": "Design/Development of Solutions", "description": "Design solutions for complex computer engineering problems and design system components or processes that meet the specified needs with appropriate consideration for the public health and safety, and the cultural, societal, and environmental considerations."},
            {"po_id": "PO4", "title": "Conduct Investigations of Complex Problems", "description": "Use research-based knowledge and research methods including design of experiments, analysis and interpretation of data, and synthesis of the information to provide valid conclusions."},
            {"po_id": "PO5", "title": "Modern Tool Usage", "description": "Create, select, and apply appropriate techniques, resources, and modern engineering and IT tools including prediction and modeling to complex computer engineering activities with an understanding of the limitations."},
            {"po_id": "PO6", "title": "The Engineer and Society", "description": "Apply reasoning informed by the contextual knowledge to assess societal, health, safety, legal and cultural issues and the consequent responsibilities relevant to the professional engineering practice."},
            {"po_id": "PO7", "title": "Environment and Sustainability", "description": "Understand the impact of the professional engineering solutions in societal and environmental contexts, and demonstrate the knowledge of, and need for sustainable development."},
            {"po_id": "PO8", "title": "Ethics", "description": "Apply ethical principles and commit to professional ethics and responsibilities and norms of the engineering practice."},
            {"po_id": "PO9", "title": "Individual and Team Work", "description": "Function effectively as an individual, and as a member or leader in diverse teams, and in multidisciplinary settings."},
            {"po_id": "PO10", "title": "Communication", "description": "Communicate effectively on complex engineering activities with the engineering community and with society at large, such as, being able to comprehend and write effective reports and design documentation, make effective presentations, and give and receive clear instructions."},
            {"po_id": "PO11", "title": "Project Management and Finance", "description": "Demonstrate knowledge and understanding of the engineering and management principles and apply these to one's own work, as a member and leader in a team, to manage projects and in multidisciplinary environments."},
            {"po_id": "PO12", "title": "Life-long Learning", "description": "Recognize the need for, and have the preparation and ability to engage in independent and life-long learning in the broadest context of technological change."}
        ]
    },
    "BTECH_ECE": {
        "program_code": "BTECH_ECE",
        "program_title": "Bachelor of Technology in Electronics & Communication Engineering",
        "department": "Electronics & Communication Engineering",
        "duration_years": 4,
        "total_semesters": 8,
        "total_credits_required": 160,
        "program_educational_objectives": [
            {
                "peo_id": "PEO1",
                "title": "Hardware & Systems Engineering",
                "description": "Graduates will excel in VLSI circuit design, digital signal processing, wireless communications, and embedded microelectronic systems."
            },
            {
                "peo_id": "PEO2",
                "title": "Industrial Automation & IoT",
                "description": "Graduates will pioneer next-generation RF transceivers, automotive embedded controllers, optical fiber backbones, and Internet of Things sensors."
            }
        ]
    },
    "BTECH_MECH": {
        "program_code": "BTECH_MECH",
        "program_title": "Bachelor of Technology in Mechanical Engineering",
        "department": "Mechanical Engineering",
        "duration_years": 4,
        "total_semesters": 8,
        "total_credits_required": 160,
        "program_educational_objectives": [
            {
                "peo_id": "PEO1",
                "title": "Thermal & Manufacturing Design",
                "description": "Graduates will design energy-efficient thermodynamic cycles, computational fluid dynamics models, and automated additive manufacturing lines."
            }
        ]
    }
}
