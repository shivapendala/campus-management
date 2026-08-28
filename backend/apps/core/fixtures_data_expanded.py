"""
EduCore Enterprise Framework - Complete Master Data Fixtures & Curriculum Maps

Provides comprehensive mapping definitions for institutional domains,
used for seeding and testing various subsystems:
- NBA Course Attainment Levels
- Bloom's Taxonomy Cognitive Domains
- Course Syllabus Definitions for 6 departments
- National Higher Education Qualification Framework (NHEQF) alignment tables
"""

from typing import Dict, List, Any

BLOOMS_TAXONOMY_COGNITIVE_LEVELS: Dict[str, Dict[str, Any]] = {
    "L1_REMEMBER": {
        "title": "Remembering",
        "description": "Retrieve relevant knowledge from long-term memory",
        "keywords": ["define", "list", "describe", "identify", "retrieve", "state", "locate"]
    },
    "L2_UNDERSTAND": {
        "title": "Understanding",
        "description": "Construct meaning from instructional messages",
        "keywords": ["explain", "summarize", "classify", "compare", "interpret", "infer", "paraphrase"]
    },
    "L3_APPLY": {
        "title": "Applying",
        "description": "Carry out or use a procedure in a given situation",
        "keywords": ["solve", "implement", "compute", "execute", "use", "demonstrate", "illustrate"]
    },
    "L4_ANALYZE": {
        "title": "Analyzing",
        "description": "Break material into constituent parts and determine relationships",
        "keywords": ["differentiate", "organize", "deconstruct", "attribute", "distinguish", "contrast"]
    },
    "L5_EVALUATE": {
        "title": "Evaluating",
        "description": "Make judgments based on criteria and standards",
        "keywords": ["critique", "judge", "evaluate", "verify", "defend", "rate", "appraise"]
    },
    "L6_CREATE": {
        "title": "Creating",
        "description": "Put elements together to form a coherent or functional whole",
        "keywords": ["design", "construct", "formulate", "innovate", "devise", "generate", "create"]
    }
}

NHEQF_LEVEL_ALIGNMENTS: Dict[int, Dict[str, Any]] = {
    5: {
        "qualification": "Undergraduate Diploma",
        "credits": 40,
        "entry_requirements": "10+2 or equivalent",
        "learning_outcomes": "Basic vocational skills and introductory engineering foundations."
    },
    6: {
        "qualification": "Bachelor Degree (General)",
        "credits": 120,
        "entry_requirements": "Undergraduate Diploma or equivalent",
        "learning_outcomes": "Broad disciplinary knowledge and analytical methods."
    },
    7: {
        "qualification": "Bachelor Degree (Honors / Engineering Professional)",
        "credits": 160,
        "entry_requirements": "10+2 with Physics, Chemistry, Math",
        "learning_outcomes": "Specialized professional engineering expertise, research methodologies, and complex problem-solving abilities."
    },
    8: {
        "qualification": "Postgraduate Diploma / Master's Degree (General)",
        "credits": 80,
        "entry_requirements": "Bachelor Degree or equivalent",
        "learning_outcomes": "Advanced theoretical framework and application of design concepts."
    }
}
