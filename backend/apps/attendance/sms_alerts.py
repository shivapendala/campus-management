"""
EduCore Enterprise Framework - Daily Absenteeism Parent SMS Alert Dispatcher

Automatically triggers DLT-compliant SMS notifications to parents when student is absent in Period 1:
- Sender ID: EDUCOR
- Regulatory DLT Template: "Dear Parent, your ward [Name] (Roll: [Roll]) was marked ABSENT today [Date]. - EduCore College"
"""

from typing import Dict, List, Any, Optional
import datetime


class DailyAbsenteeismNotifier:
    """
    Scans morning roll call and dispatches parent alerts.
    """

    @classmethod
    def generate_absent_alerts(
        cls,
        absent_students: List[Dict[str, str]]  # [{"roll": "...", "name": "...", "parent_phone": "..."}]
    ) -> List[Dict[str, Any]]:
        """Construct SMS dispatch queue payloads."""
        today_str = datetime.date.today().strftime("%d-%b-%Y")
        messages = []

        for s in absent_students:
            msg_text = f"Dear Parent, your ward {s.get('name')} (Roll: {s.get('roll')}) was marked ABSENT on {today_str}. Please verify. - EduCore College"
            messages.append({
                "recipient_phone": s.get("parent_phone"),
                "student_roll": s.get("roll"),
                "message_text": msg_text,
                "dlt_template_id": "1107161523421109",
                "status": "QUEUED_FOR_SMS_GATEWAY"
            })

        return messages
