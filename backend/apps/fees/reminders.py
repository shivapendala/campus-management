"""
EduCore Enterprise Framework - Automated Fee Due Reminder Escalation Scheduler

Computes escalating reminder alerts based on days relative to due date:
- T-14 Days: Friendly Reminder (Email & In-App)
- T-3 Days: Urgent Due Notice (SMS & Email)
- T+1 Day: Grace Period Warning (Late fee begins in 7 days)
- T+8 Days: Overdue Escalation Notice (Parent Notification + Hall ticket withholding warning)
"""

from typing import Dict, List, Any, Optional
import datetime


class FeeReminderEscalationEngine:
    """
    Evaluates fee due calendar and triggers appropriate message templates.
    """

    @classmethod
    def evaluate_reminder_trigger(
        cls,
        due_date_iso: str,
        balance_due: float,
        student_roll: str,
        current_date_iso: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Determine if a notification trigger matches today's date.
        """
        if balance_due <= 0.0:
            return None

        due_dt = datetime.date.fromisoformat(due_date_iso)
        curr_dt = datetime.date.fromisoformat(current_date_iso) if current_date_iso else datetime.date.today()
        days_to_due = (due_dt - curr_dt).days

        if days_to_due == 14:
            return {
                "stage": "ADVANCE_REMINDER",
                "days_offset": 14,
                "urgency": "NORMAL",
                "message": f"Reminder: Semester fee installment of Rs. {balance_due:,.2f} is due on {due_date_iso}.",
                "channels": ["IN_APP", "EMAIL"]
            }
        elif days_to_due == 3:
            return {
                "stage": "URGENT_DUE_NOTICE",
                "days_offset": 3,
                "urgency": "HIGH",
                "message": f"Urgent: Fee payment of Rs. {balance_due:,.2f} is due in 3 days on {due_date_iso}.",
                "channels": ["IN_APP", "EMAIL", "SMS"]
            }
        elif days_to_due == -1:
            return {
                "stage": "GRACE_PERIOD_ACTIVE",
                "days_offset": -1,
                "urgency": "HIGH",
                "message": f"Your fee payment of Rs. {balance_due:,.2f} was due yesterday. Grace period ends in 6 days.",
                "channels": ["IN_APP", "EMAIL", "SMS"]
            }
        elif days_to_due <= -8:
            return {
                "stage": "OVERDUE_ESCALATION",
                "days_offset": days_to_due,
                "urgency": "CRITICAL",
                "message": f"OVERDUE: Fee balance Rs. {balance_due:,.2f} is {abs(days_to_due)} days overdue. Late fine applicable.",
                "channels": ["IN_APP", "EMAIL", "SMS"]
            }

        return None
