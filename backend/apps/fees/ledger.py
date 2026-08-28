"""
EduCore Enterprise Framework - Double-Entry Institutional Accounting Ledger

Maintains immutable journal entries (Debits & Credits) for student accounts,
revenue accounts (Tuition, Transport, Hostel, Lab), and bank settlement accounts.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class JournalEntryLine:
    """Represents a single debit or credit line in a double-entry transaction."""
    account_code: str  # 1010-CASH, 1020-BANK, 2010-STUDENT_DUES, 4010-TUITION_REVENUE
    account_name: str
    is_debit: bool
    amount: float


@dataclass
class AccountingTransaction:
    """Double-entry transaction balancing total debits and credits."""
    transaction_id: str
    timestamp: str
    reference_number: str  # Receipt No or Invoice No
    description: str
    lines: List[JournalEntryLine] = field(default_factory=list)

    @property
    def is_balanced(self) -> bool:
        """Verify that Sum(Debits) == Sum(Credits)."""
        debits = sum(line.amount for line in self.lines if line.is_debit)
        credits = sum(line.amount for line in self.lines if not line.is_debit)
        return abs(debits - credits) < 0.01


class InstitutionalLedgerManager:
    """
    Generates balanced accounting vouchers for institutional financial operations.
    """

    @classmethod
    def record_fee_payment_voucher(
        cls,
        receipt_number: str,
        student_roll: str,
        amount: float,
        payment_mode: str = "ONLINE"  # CASH, BANK_TRANSFER, ONLINE, CHEQUE
    ) -> AccountingTransaction:
        """
        Record student fee collection:
        Debit: Bank Account (Asset increases)
        Credit: Student Accounts Receivable (Asset decreases / Dues cleared)
        """
        import uuid
        tx_id = f"TX-{str(uuid.uuid4())[:8]}"
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()

        debit_acct = "1020-BANK-OPERATING" if payment_mode in ("ONLINE", "BANK_TRANSFER") else "1010-CASH-BURSAR"

        lines = [
            JournalEntryLine(account_code=debit_acct, account_name=f"Campus Operating Account ({payment_mode})", is_debit=True, amount=amount),
            JournalEntryLine(account_code="2010-AR-STUDENTS", account_name=f"Student Dues Receivable ({student_roll})", is_debit=False, amount=amount)
        ]

        return AccountingTransaction(
            transaction_id=tx_id,
            timestamp=now,
            reference_number=receipt_number,
            description=f"Tuition fee received for student {student_roll} via {payment_mode}",
            lines=lines
        )
