/**
 * Comprehensive Campus Events & Conferences Mock Store
 */

export const comprehensiveEventsStore = [
  {
    event_code: 'EVT-2026-01',
    title: 'INNOVA 2026: National Technical Symposium & Hackathon',
    category: 'TECHNICAL_SYMPOSIUM',
    start_date: '2026-09-15',
    end_date: '2026-09-17',
    venue: 'Main University Auditorium & CS Laboratories',
    expected_attendees: 850,
    sanctioned_budget_inr: 450000.0,
    sponsorship_raised_inr: 320000.0,
    convener: 'Dr. Rajesh Raman',
    co_convener: 'Dr. Sunita Murthy',
    status: 'CONFIRMED_SCHEDULED',
    schedule_highlights: [
      { time: 'Day 1: 09:30 AM', activity: 'Inaugural Keynote by Google Cloud Director' },
      { time: 'Day 1: 02:00 PM', activity: '24-Hour Hackathon Kickoff' },
      { time: 'Day 2: 02:00 PM', activity: 'Hackathon Project Demos & Pitching' },
      { time: 'Day 3: 04:00 PM', activity: 'Valedictory & Prize Distribution (Rs. 1.5L Cash Prizes)' },
    ],
  },
  {
    event_code: 'EVT-2026-02',
    title: 'RHYTHM 2026: Annual Inter-Collegiate Cultural Festival',
    category: 'CULTURAL_FEST',
    start_date: '2026-10-02',
    end_date: '2026-10-04',
    venue: 'Open Air Theatre (OAT)',
    expected_attendees: 2200,
    sanctioned_budget_inr: 1200000.0,
    sponsorship_raised_inr: 850000.0,
    convener: 'Prof. Arvind Swaminathan',
    co_convener: 'Student Council President',
    status: 'CONFIRMED_SCHEDULED',
    schedule_highlights: [
      { time: 'Day 1: 06:00 PM', activity: 'Battle of the Bands' },
      { time: 'Day 2: 07:00 PM', activity: 'Choreo Night (Inter-College Dance)' },
      { time: 'Day 3: 08:00 PM', activity: 'Celebrity Musical Concert (Pro-Nite)' },
    ],
  },
  {
    event_code: 'EVT-2026-03',
    title: 'IEEE International Conference on Edge AI & IoT Systems (IC-EAI 2026)',
    category: 'INTERNATIONAL_CONFERENCE',
    start_date: '2026-11-10',
    end_date: '2026-11-12',
    venue: 'Seminar Hall A & Virtual Zoom Tracks',
    expected_attendees: 320,
    sanctioned_budget_inr: 600000.0,
    sponsorship_raised_inr: 450000.0,
    convener: 'Dr. Meenakshi Sundaram',
    co_convener: 'Dr. Rajesh Raman',
    status: 'ACTIVE_CALL_FOR_PAPERS',
    schedule_highlights: [
      { time: 'Track 1', activity: 'Deep Learning on Edge Hardware' },
      { time: 'Track 2', activity: 'Next-Gen Wireless Sensor Networks' },
      { time: 'Track 3', activity: 'Security & Privacy in Smart Cities' },
    ],
  },
];

export default comprehensiveEventsStore;
