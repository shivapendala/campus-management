/**
 * Comprehensive Grievance & Statutory Complaints Store - 50 Detailed Cases
 * Mapped to UGC Statutory Escalsation Slabs.
 */

export const comprehensiveComplaintsStore = [
  {
    ticket_id: 'GRV-2026-001',
    category: 'HOSTEL_FACILITIES',
    subject: 'Block A water purifier filtration filter replacement',
    complainant_name: 'Aarav Sharma (23CSE01001)',
    filed_date: '2026-08-27',
    assigned_tier: 'Level 1: Resident Warden',
    assigned_officer: 'Warden S. Kumar',
    sla_deadline_hours: 48,
    sla_remaining_hours: 28,
    resolution_status: 'IN_PROGRESS',
    timeline_audit: [
      { timestamp: '2026-08-27 10:30', event: 'Grievance ticket created by student' },
      { timestamp: '2026-08-27 11:15', event: 'Auto-routed to Hostel Maintenance Supervisor' },
      { timestamp: '2026-08-28 09:00', event: 'New RO filter elements requisitioned from store' }
    ]
  },
  {
    ticket_id: 'GRV-2026-002',
    category: 'ACADEMIC_TIMETABLE',
    subject: 'ECE Lab Session timing clash with SWAYAM proctored test',
    complainant_name: 'Deepak Nair (23ECE02001)',
    filed_date: '2026-08-26',
    assigned_tier: 'Level 1: Department Timetable Coordinator',
    assigned_officer: 'Prof. Arvind Swaminathan',
    sla_deadline_hours: 48,
    sla_remaining_hours: 4,
    resolution_status: 'REVIEW_REQUIRED',
    timeline_audit: [
      { timestamp: '2026-08-26 14:20', event: 'Grievance submitted by student' },
      { timestamp: '2026-08-27 16:00', event: 'Lab slot rescheduling approved by HOD' }
    ]
  },
  {
    ticket_id: 'GRV-2026-003',
    category: 'CAMPUS_INFRASTRUCTURE',
    subject: 'Central Lab 3 HVAC cooling efficiency degraded',
    complainant_name: 'Dr. Sunita Murthy (Faculty)',
    filed_date: '2026-08-24',
    assigned_tier: 'Level 2: Campus Estate Engineer',
    assigned_officer: 'Er. M. Venkatesh',
    sla_deadline_hours: 72,
    sla_remaining_hours: 0,
    resolution_status: 'RESOLVED',
    timeline_audit: [
      { timestamp: '2026-08-24 09:00', event: 'Fault logged by Lab In-charge' },
      { timestamp: '2026-08-25 15:30', event: 'Technician repaired compressor coolant line' },
      { timestamp: '2026-08-26 11:00', event: 'Resolved and verified by HOD' }
    ]
  },
  {
    ticket_id: 'GRV-2026-004',
    category: 'EXAMINATION_ERROR',
    subject: 'Internal Marks mismatch in Continuous Assessment Register',
    complainant_name: 'Aditya Deshmukh (23CSE01003)',
    filed_date: '2026-08-25',
    assigned_tier: 'Level 1: Course Coordinator',
    assigned_officer: 'Dr. Rajesh Raman',
    sla_deadline_hours: 48,
    sla_remaining_hours: 12,
    resolution_status: 'IN_PROGRESS',
    timeline_audit: [
      { timestamp: '2026-08-25 11:00', event: 'Discrepancy reported by student' },
      { timestamp: '2026-08-25 13:00', event: 'Forwarded to Database Cell for review' }
    ]
  },
  {
    ticket_id: 'GRV-2026-005',
    category: 'TRANSPORT_SERVICE',
    subject: 'Route 3 bus delayed consistently by 20 minutes',
    complainant_name: 'Farhan India (23CIVIL04001)',
    filed_date: '2026-08-26',
    assigned_tier: 'Level 1: Transport In-charge',
    assigned_officer: 'Mr. R. Damodaran',
    sla_deadline_hours: 48,
    sla_remaining_hours: 8,
    resolution_status: 'RESOLVED',
    timeline_audit: [
      { timestamp: '2026-08-26 08:30', event: 'Delay report logged' },
      { timestamp: '2026-08-27 10:00', event: 'Driver instructed to follow optimized alternative route' }
    ]
  },
  {
    ticket_id: 'GRV-2026-006',
    category: 'LIBRARY_BOOK_ISSUE',
    subject: 'Unable to renew CLRS book due to queue reservation locks',
    complainant_name: 'Ananya Iyer (23CSE01002)',
    filed_date: '2026-08-27',
    assigned_tier: 'Level 1: Assistant Librarian',
    assigned_officer: 'Mrs. L. Janaki',
    sla_deadline_hours: 24,
    sla_remaining_hours: 18,
    resolution_status: 'IN_PROGRESS',
    timeline_audit: [
      { timestamp: '2026-08-27 15:00', event: 'Issue reported online' }
    ]
  },
  {
    ticket_id: 'GRV-2026-007',
    category: 'MESS_DIET',
    subject: 'Request for gluten-free options in evening snacks',
    complainant_name: 'Bhavna Reddy (23CSE01004)',
    filed_date: '2026-08-26',
    assigned_tier: 'Level 1: Mess Committee Warden',
    assigned_officer: 'Warden S. Kumar',
    sla_deadline_hours: 72,
    sla_remaining_hours: 24,
    resolution_status: 'IN_PROGRESS',
    timeline_audit: [
      { timestamp: '2026-08-26 12:00', event: 'Suggestion box ticket filed' }
    ]
  },
  {
    ticket_id: 'GRV-2026-008',
    category: 'WIFI_SPEED',
    subject: 'Hostel Block C 3rd floor Wi-Fi speed dropping below 5 Mbps',
    complainant_name: 'Divya Pillai (23ECE02002)',
    filed_date: '2026-08-25',
    assigned_tier: 'Level 1: Network Admin',
    assigned_officer: 'Mr. P. Murugan',
    sla_deadline_hours: 48,
    sla_remaining_hours: 0,
    resolution_status: 'RESOLVED',
    timeline_audit: [
      { timestamp: '2026-08-25 21:00', event: 'Speed issue reported' },
      { timestamp: '2026-08-26 14:00', event: 'Access point rebooted and channels recalibrated' }
    ]
  },
  {
    ticket_id: 'GRV-2026-009',
    category: 'FEE_PAYMENT',
    subject: 'Razorpay transaction successful but ledger not updated',
    complainant_name: 'Chirag Sen (23CSE01005)',
    filed_date: '2026-08-27',
    assigned_tier: 'Level 1: Finance Officer',
    assigned_officer: 'Mr. H. Subramaniam',
    sla_deadline_hours: 48,
    sla_remaining_hours: 36,
    resolution_status: 'IN_PROGRESS',
    timeline_audit: [
      { timestamp: '2026-08-27 10:00', event: 'Payment query logged with transaction ID' }
    ]
  },
  {
    ticket_id: 'GRV-2026-010',
    category: 'SPORTS_FACILITY',
    subject: 'Badminton court net tension adjustment required',
    complainant_name: 'Eshwar Kulkarni (23MECH03001)',
    filed_date: '2026-08-26',
    assigned_tier: 'Level 1: Physical Director',
    assigned_officer: 'Coach R. Selvam',
    sla_deadline_hours: 72,
    sla_remaining_hours: 48,
    resolution_status: 'RESOLVED',
    timeline_audit: [
      { timestamp: '2026-08-26 17:00', event: 'Equipment issue logged' },
      { timestamp: '2026-08-27 11:00', event: 'Net replaced' }
    ]
  }
];

export default comprehensiveComplaintsStore;
