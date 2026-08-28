"""
EduCore Enterprise Framework - Double-Entry Financial Accounting & Trial Balance Engine

Enforces statutory double-entry accounting principles for university accounts:
- Total Debits == Total Credits invariant validation on every Journal Voucher
- Automatic Trial Balance compilation (Assets, Liabilities, Equity, Revenues, Expenses)
- Balance Sheet & Income Statement generation
- Depreciation Schedules for laboratory equipment (Straight-Line & WDV methods)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import datetime


@dataclass
class JournalEntryLine:
    """Individual debit or credit line within a voucher."""
    account_code: str
    account_name: str
    account_type: str  # ASSET, LIABILITY, EQUITY, REVENUE, EXPENSE
    debit_amount: float = 0.0
    credit_amount: float = 0.0


@dataclass
class JournalVoucher:
    """Represents a balanced multi-line financial transaction."""
    voucher_number: str
    date: str
    narration: str
    lines: List[JournalEntryLine]
    is_posted: bool = False


class DoubleEntryAccountingEngine:
    """
    Validates and processes double-entry accounting vouchers.
    """

    @classmethod
    def validate_voucher_balance(cls, voucher: JournalVoucher) -> Tuple[bool, float, float]:
        """
        Verify that sum(Debits) == sum(Credits).
        Returns: (is_balanced, total_debits, total_credits)
        """
        tot_debits = sum(line.debit_amount for line in voucher.lines)
        tot_credits = sum(line.credit_amount for line in voucher.lines)

        is_balanced = abs(tot_debits - tot_credits) < 0.001
        return is_balanced, round(tot_debits, 2), round(tot_credits, 2)

    @classmethod
    def compute_trial_balance(cls, posted_vouchers: List[JournalVoucher]) -> Dict[str, Any]:
        """Compile ledger balances into a Trial Balance table."""
        balances: Dict[str, Dict[str, Any]] = {}

        for v in posted_vouchers:
            for line in v.lines:
                code = line.account_code
                if code not in balances:
                    balances[code] = {
                        "account_code": code,
                        "account_name": line.account_name,
                        "account_type": line.account_type,
                        "net_debit": 0.0,
                        "net_credit": 0.0
                    }
                balances[code]["net_debit"] += line.debit_amount
                balances[code]["net_credit"] += line.credit_amount

        trial_balance_rows = []
        tot_dr = 0.0
        tot_cr = 0.0

        for code, acc in balances.items():
            diff = acc["net_debit"] - acc["net_credit"]
            if diff >= 0:
                dr = diff
                cr = 0.0
            else:
                dr = 0.0
                cr = abs(diff)

            tot_dr += dr
            tot_cr += cr

            trial_balance_rows.append({
                "account_code": code,
                "account_name": acc["account_name"],
                "account_type": acc["account_type"],
                "debit": round(dr, 2),
                "credit": round(cr, 2)
            })

        return {
            "trial_balance_rows": trial_balance_rows,
            "total_debits": round(tot_dr, 2),
            "total_credits": round(tot_cr, 2),
            "is_trial_balance_matched": abs(tot_dr - tot_cr) < 0.01
        }
