"""
EduCore Enterprise Framework - Canonical Library MARC21 & Dewey Decimal Accession Records

Contains standard bibliographic metadata records conforming to MARC21 and Dublin Core schemas:
- Dewey Decimal Classification (DDC 000 to 900)
- Library of Congress Control Numbers (LCCN)
- Standard ISBN-13 barcoded book accessions
"""

from typing import List, Dict, Any

CANONICAL_LIBRARY_ACCESSIONS_CATALOG: List[Dict[str, Any]] = [
    {
        "accession_number": "ACC-2026-0001",
        "isbn_13": "978-0134685991",
        "title": "Effective Java",
        "edition": "3rd Edition",
        "author": "Joshua Bloch",
        "publisher": "Addison-Wesley Professional",
        "publication_year": 2018,
        "ddc_class": "005.133",
        "category": "COMPUTER_SCIENCE",
        "shelf_location": "STACKS-CSE-ROW-04-SHELF-B",
        "total_copies": 10,
        "available_copies": 4,
        "is_reference_only": False,
        "purchase_price_inr": 3450.0
    },
    {
        "accession_number": "ACC-2026-0002",
        "isbn_13": "978-0262033848",
        "title": "Introduction to Algorithms",
        "edition": "3rd Edition (CLRS)",
        "author": "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
        "publisher": "MIT Press",
        "publication_year": 2009,
        "ddc_class": "005.1",
        "category": "COMPUTER_SCIENCE",
        "shelf_location": "STACKS-CSE-ROW-02-SHELF-A",
        "total_copies": 15,
        "available_copies": 2,
        "is_reference_only": False,
        "purchase_price_inr": 4890.0
    },
    {
        "accession_number": "ACC-2026-0003",
        "isbn_13": "978-0078022159",
        "title": "Database System Concepts",
        "edition": "7th Edition",
        "author": "Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
        "publisher": "McGraw-Hill Education",
        "publication_year": 2020,
        "ddc_class": "005.74",
        "category": "COMPUTER_SCIENCE",
        "shelf_location": "STACKS-CSE-ROW-05-SHELF-C",
        "total_copies": 12,
        "available_copies": 0,
        "is_reference_only": False,
        "purchase_price_inr": 3950.0
    },
    {
        "accession_number": "ACC-2026-0004",
        "isbn_13": "978-0133594140",
        "title": "Operating System Concepts",
        "edition": "10th Edition",
        "author": "Abraham Silberschatz, Peter B. Galvin, Greg Gagne",
        "publisher": "Wiley",
        "publication_year": 2018,
        "ddc_class": "005.43",
        "category": "COMPUTER_SCIENCE",
        "shelf_location": "STACKS-CSE-ROW-03-SHELF-D",
        "total_copies": 10,
        "available_copies": 5,
        "is_reference_only": False,
        "purchase_price_inr": 4120.0
    },
    {
        "accession_number": "ACC-2026-0005",
        "isbn_13": "978-0132126953",
        "title": "Computer Networks",
        "edition": "5th Edition",
        "author": "Andrew S. Tanenbaum, David J. Wetherall",
        "publisher": "Pearson",
        "publication_year": 2013,
        "ddc_class": "004.6",
        "category": "COMPUTER_SCIENCE",
        "shelf_location": "STACKS-CSE-ROW-06-SHELF-A",
        "total_copies": 14,
        "available_copies": 6,
        "is_reference_only": False,
        "purchase_price_inr": 3650.0
    }
]
