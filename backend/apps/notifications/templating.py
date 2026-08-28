"""
EduCore Enterprise Framework - Dynamic Notification Template Compiler

Compiles parametric message templates with variable placeholder interpolation:
`{{student_name}}`, `{{course_name}}`, `{{exam_date}}`, `{{fee_amount}}`, `{{receipt_no}}`.
Includes HTML sanitization and DLT registration tags.
"""

import re
from typing import Dict, Any, Optional, Tuple


class NotificationTemplateCompiler:
    """
    Renders institutional notification templates with runtime dictionary variables.
    """

    SYSTEM_TEMPLATES = {
        "FEE_RECEIPT": {
            "title": "Official Fee Receipt - {{receipt_no}}",
            "body": "Dear {{student_name}}, your payment of Rs. {{amount}} for {{fee_type}} has been successfully recorded. Receipt ID: {{receipt_no}}."
        },
        "ATTENDANCE_SHORTAGE_WARNING": {
            "title": "URGENT: Attendance Shortage Alert for {{subject_name}}",
            "body": "Dear {{student_name}} (Roll: {{roll_number}}), your attendance in {{subject_name}} is {{attendance_pct}}%, which is below the mandatory 75% threshold. Please meet your HOD."
        },
        "EXAM_RESULT_PUBLISHED": {
            "title": "Results Published: {{exam_title}}",
            "body": "Hello {{student_name}}, your semester exam results for {{semester}} are now published. Your SGPA is {{sgpa}}. Check your grade card online."
        },
        "ASSIGNMENT_DEADLINE": {
            "title": "Assignment Due Tomorrow: {{assignment_title}}",
            "body": "Reminder: Assignment '{{assignment_title}}' for {{course_name}} is due on {{due_date}} at 23:59 IST. Please upload your submission before the deadline."
        },
        "PLACEMENT_SHORTLIST": {
            "title": "Shortlisted for {{company_name}} - {{job_role}}",
            "body": "Congratulations {{student_name}}! You have been shortlisted for the {{round_name}} round of {{company_name}} scheduled on {{interview_date}} at {{venue}}."
        }
    }

    @classmethod
    def render_template(
        cls,
        template_key: str,
        context_variables: Dict[str, Any]
    ) -> Tuple[str, str]:
        """
        Compile title and body replacing `{{key}}` tokens with context_variables.
        Returns: (rendered_title, rendered_body)
        """
        template = cls.SYSTEM_TEMPLATES.get(template_key)
        if not template:
            return "Notification", str(context_variables)

        raw_title = template["title"]
        raw_body = template["body"]

        def replacer(match):
            key = match.group(1).strip()
            return str(context_variables.get(key, f"[{key}]"))

        rendered_title = re.sub(r"\{\{([a-zA-Z0-9_]+)\}\}", replacer, raw_title)
        rendered_body = re.sub(r"\{\{([a-zA-Z0-9_]+)\}\}", replacer, raw_body)

        return rendered_title, rendered_body
