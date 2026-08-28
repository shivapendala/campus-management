"""
EduCore Framework - Library Dewey Decimal Classification (DDC) Service

Provides suggested Cutter number generation and shelf location mappings
according to DDC classification codes.
"""

import re
from typing import Dict, Any, Optional

class DDCClassifierService:
    def __init__(self):
        # Master mapping of DDC divisions to general subjects
        self.ddc_divisions: Dict[str, str] = {
            "000": "Computer Science, Information & General Works",
            "100": "Philosophy & Psychology",
            "200": "Religion",
            "300": "Social Sciences",
            "400": "Language",
            "500": "Natural Sciences & Mathematics",
            "600": "Technology & Applied Sciences",
            "700": "Arts & Recreation",
            "800": "Literature",
            "900": "History & Geography"
        }

    def suggest_subject_area(self, ddc_code: str) -> str:
        """
        Suggests the core subject area based on the first digit of the DDC code.
        """
        match = re.match(r"^(\d)", ddc_code)
        if not match:
            return "Unknown Classification"
        
        prefix = f"{match.group(1)}00"
        return self.ddc_divisions.get(prefix, "General Library Stack")

    def generate_cutter_number(self, author_last_name: str, title: str) -> str:
        """
        Generates a simplified Cutter-Sanborn number:
        First letter of Author's last name + numeric code (based on letter positions) + first letter of title in lowercase.
        e.g., author_last_name='Cormen', title='Introduction to Algorithms' -> 'C67i'
        """
        if not author_last_name:
            return "X11"
            
        first_letter = author_last_name[0].upper()
        
        # Calculate numeric hash based on name characters
        val = 0
        for char in author_last_name[1:4]:
            val += ord(char.lower()) - 96
            
        # Map values to a standard 2-digit pad
        numeric_pad = str(max(10, min(val * 3, 99)))
        
        # Title code: first letter of first word (excluding 'A', 'An', 'The')
        words = [w for w in title.split() if w.lower() not in {"a", "an", "the"}]
        title_char = words[0][0].lower() if words else "t"
        
        return f"{first_letter}{numeric_pad}{title_char}"

    def assign_shelf_location(self, ddc_code: str) -> str:
        """
        Maps a DDC code to a library physical rack location.
        """
        try:
            val = float(ddc_code)
        except ValueError:
            return "RACK-GENERAL-01"
            
        if 0.0 <= val < 100.0:
            return "RACK-COMP-SCI-01"
        elif 100.0 <= val < 200.0:
            return "RACK-PHILOSOPHY-02"
        elif 300.0 <= val < 400.0:
            return "RACK-SOCIAL-SCI-03"
        elif 500.0 <= val < 600.0:
            return "RACK-MATHEMATICS-05"
        elif 600.0 <= val < 700.0:
            if 620.0 <= val < 621.38:
                return "RACK-ENGINEERING-MECH"
            elif 621.38 <= val < 622.0:
                return "RACK-ENGINEERING-ECE-EEE"
            return "RACK-TECHNOLOGY-06"
        return "RACK-GENERAL-09"
