"""
EduCore Framework - NEP Credits Bank Auditor

Audits credits ledger balances against national ABC registries.
"""

from typing import Dict, List, Any

class NEPCreditsBankAuditor:
    def __init__(self, regulation_code: str):
        self.regulation_code = regulation_code
        self.audit_log: List[str] = []

    def audit_student_bank_balance(self, student_id: str, local_credits: int, abc_registry_credits: int) -> Dict[str, Any]:
        """
        Ensures credit counts in local ABC repository matches values inside National ABC Registry.
        """
        match = local_credits == abc_registry_credits
        deviation = abc_registry_credits - local_credits
        
        if not match:
            self.audit_log.append(
                f"Mismatch: Student '{student_id}' has {local_credits} local credits, but ABC Registry shows {abc_registry_credits}."
            )
            
        return {
            "student_id": student_id,
            "local_credits": local_credits,
            "abc_registry_credits": abc_registry_credits,
            "deviation": deviation,
            "synchronized": match
        }
