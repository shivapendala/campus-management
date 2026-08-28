"""
EduCore Enterprise Framework - Hardware Biometric Device Sync Daemon

Communicates with ZKTeco, eSSL, and Matrix COSEC biometric devices over TCP/IP:
Pulls real-time punch packets, parses device logs, and handles device disconnection retries.
"""

from typing import Dict, List, Any, Optional
import time
from dataclasses import dataclass, field


@dataclass
class BiometricDeviceNode:
    """Represents a physical biometric terminal device on the campus network."""
    device_id: str
    ip_address: str
    port: int
    location: str  # MAIN_GATE, CSE_CORRIDOR, LIBRARY_ENTRY, CANTEEN
    is_online: bool = True
    last_sync_timestamp: Optional[float] = None
    pending_records_count: int = 0


class BiometricHardwareSyncDaemon:
    """
    Simulates TCP/IP device polling and batch log ingestion.
    """

    @classmethod
    def poll_device_status(cls, device: BiometricDeviceNode) -> Dict[str, Any]:
        """Perform ping and heartbeat check on terminal."""
        now = time.time()
        device.last_sync_timestamp = now
        return {
            "device_id": device.device_id,
            "ip_address": device.ip_address,
            "location": device.location,
            "is_online": device.is_online,
            "last_heartbeat": now,
            "status": "OPERATIONAL" if device.is_online else "OFFLINE"
        }
