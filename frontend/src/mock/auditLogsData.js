/**
 * Standard Security Audit Trail & Event Telemetry Mock Data Store
 */

export const mockAuditLogsStore = [
  {
    event_id: 'EVT-9801',
    timestamp: '2026-08-28 17:42:10 UTC',
    actor_username: 'admin_sys',
    actor_role: 'ADMIN',
    action_type: 'UPDATE',
    resource_type: 'FeeStructure',
    ip_address: '127.0.0.1',
    user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    severity: 'HIGH',
    status: 'SUCCESS',
    metadata: { changed_fields: ['tuition_fee_btech', 'hostel_fee_single_room'] },
  },
  {
    event_id: 'EVT-9802',
    timestamp: '2026-08-28 17:45:30 UTC',
    actor_username: 'hod_cse',
    actor_role: 'HOD',
    action_type: 'APPROVE',
    resource_type: 'ExamMarks',
    ip_address: '192.168.1.45',
    user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    severity: 'INFO',
    status: 'SUCCESS',
    metadata: { course_code: 'CS301', verified_students_count: 65 },
  },
  {
    event_id: 'EVT-9803',
    timestamp: '2026-08-28 17:50:00 UTC',
    actor_username: 'faculty_math',
    actor_role: 'FACULTY',
    action_type: 'MARK',
    resource_type: 'Attendance',
    ip_address: '192.168.1.88',
    user_agent: 'Mozilla/5.0 (Android 14; Mobile)',
    severity: 'INFO',
    status: 'SUCCESS',
    metadata: { period_slot: 'Period 1 (09:00 - 10:00)', present_count: 58, absent_count: 4 },
  },
  {
    event_id: 'EVT-9804',
    timestamp: '2026-08-28 18:02:15 UTC',
    actor_username: 'accountant',
    actor_role: 'ACCOUNTANT',
    action_type: 'CREATE',
    resource_type: 'FeeReceipt',
    ip_address: '192.168.1.12',
    user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    severity: 'INFO',
    status: 'SUCCESS',
    metadata: { receipt_no: 'REC-98421', amount_inr: 65000.0, payment_gateway: 'RAZORPAY' },
  },
];

export default mockAuditLogsStore;
