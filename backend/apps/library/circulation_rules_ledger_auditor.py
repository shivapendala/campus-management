"""
EduCore Framework - Library Circulation Rules Ledger Auditor

Audits rules allocations to prevent conflicting max book limits.
"""

from typing import Dict, List, Any

class CirculationRulesLedgerAuditor:
    def __init__(self):
        self.conflicts: List[str] = []

    def audit_rules(self, rules: List[Dict[str, Any]]) -> List[str]:
        types_logged = set()
        for r in rules:
            m_type = r["membership_type"]
            if m_type in types_logged:
                self.conflicts.append(f"Duplicate rules configuration: '{m_type}' has multiple limits registered.")
            types_logged.add(m_type)
        return self.conflicts
