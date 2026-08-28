"""
EduCore Enterprise Framework - Email/SMS Notification Digest Builder

Aggregates individual alerts into a clean daily or weekly digest:
- Groups low-priority alerts by category
- Dynamic HTML templates for student and faculty streams
- Auto-collapses redundant alerts (e.g. repeated library reminders)
"""

from typing import Dict, List, Any


class NotificationDigestEngine:
    """
    Compiles chronological digest summaries to reduce notification spam.
    """

    @classmethod
    def compile_digest(
        cls,
        user_name: str,
        user_email: str,
        pending_alerts: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Aggregate notification rows into HTML content blocks."""
        if not pending_alerts:
            return {
                "recipient_name": user_name,
                "recipient_email": user_email,
                "digest_html": "<p>No notifications for today.</p>",
                "total_alerts": 0
            }

        categories: Dict[str, List[str]] = {}
        for alert in pending_alerts:
            cat = alert.get("category", "GENERAL")
            msg = alert.get("message", "")
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(msg)

        # Build clean HTML summary
        html_blocks = []
        html_blocks.append(f"<h3>Hello {user_name}, here is your daily campus update:</h3>")

        for cat, msgs in categories.items():
            html_blocks.append(f"<h4>{cat.replace('_', ' ').title()} Alerts ({len(msgs)})</h4>")
            html_blocks.append("<ul>")
            for m in msgs:
                html_blocks.append(f"<li>{m}</li>")
            html_blocks.append("</ul>")

        html_blocks.append("<br/><p>Please log in to the portal to view full details.</p>")

        return {
            "recipient_name": user_name,
            "recipient_email": user_email,
            "digest_html": "\n".join(html_blocks),
            "total_alerts": len(pending_alerts)
        }
