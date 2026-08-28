/**
 * Comprehensive Multi-Section Weekly Timetable Grid Store
 */

export const comprehensiveTimetablesStore = {
  CSE_SEM5_SEC_A: {
    department: 'Computer Science & Engineering',
    semester: 5,
    section: 'A',
    classroom: 'CR-101 (Aryabhatta Block)',
    schedule: [
      {
        day: 'Monday',
        periods: [
          { time: '09:00 - 10:00', course: 'CS501: Networks', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '10:00 - 11:00', course: 'CS502: Compiler Design', faculty: 'Dr. Sunita', room: 'CR-101' },
          { time: '11:15 - 12:15', course: 'CS503: Artificial Intelligence', faculty: 'Dr. Rajesh', room: 'CR-101' },
          { time: '01:15 - 02:15', course: 'CS_PE1: Cloud Computing', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '02:15 - 04:15', course: 'CS504: Networks Lab (Batch 1)', faculty: 'Prof. Arvind', room: 'LAB-1' },
        ],
      },
      {
        day: 'Tuesday',
        periods: [
          { time: '09:00 - 10:00', course: 'CS503: Artificial Intelligence', faculty: 'Dr. Rajesh', room: 'CR-101' },
          { time: '10:00 - 11:00', course: 'CS501: Networks', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '11:15 - 12:15', course: 'OE101: Operations Research', faculty: 'Math Faculty', room: 'CR-101' },
          { time: '01:15 - 02:15', course: 'CS502: Compiler Design', faculty: 'Dr. Sunita', room: 'CR-101' },
          { time: '02:15 - 04:15', course: 'CS505: AI & ML Lab (Batch 2)', faculty: 'Dr. Sunita', room: 'LAB-2' },
        ],
      },
      {
        day: 'Wednesday',
        periods: [
          { time: '09:00 - 10:00', course: 'CS502: Compiler Design', faculty: 'Dr. Sunita', room: 'CR-101' },
          { time: '10:00 - 11:00', course: 'CS_PE1: Cloud Computing', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '11:15 - 12:15', course: 'CS501: Networks', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '01:15 - 02:15', course: 'OE101: Operations Research', faculty: 'Math Faculty', room: 'CR-101' },
          { time: '02:15 - 03:15', course: 'Mentoring / Proctorial Hour', faculty: 'Proctor Team', room: 'CR-101' },
        ],
      },
      {
        day: 'Thursday',
        periods: [
          { time: '09:00 - 10:00', course: 'OE101: Operations Research', faculty: 'Math Faculty', room: 'CR-101' },
          { time: '10:00 - 11:00', course: 'CS503: Artificial Intelligence', faculty: 'Dr. Rajesh', room: 'CR-101' },
          { time: '11:15 - 12:15', course: 'CS_PE1: Cloud Computing', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '01:15 - 03:15', course: 'CS504: Networks Lab (Batch 2)', faculty: 'Prof. Arvind', room: 'LAB-1' },
          { time: '03:15 - 04:15', course: 'Library / Self Learning Hour', faculty: 'Librarian', room: 'CENTRAL_LIB' },
        ],
      },
      {
        day: 'Friday',
        periods: [
          { time: '09:00 - 10:00', course: 'CS501: Networks', faculty: 'Prof. Arvind', room: 'CR-101' },
          { time: '10:00 - 11:00', course: 'CS502: Compiler Design', faculty: 'Dr. Sunita', room: 'CR-101' },
          { time: '11:15 - 12:15', course: 'CS503: Artificial Intelligence', faculty: 'Dr. Rajesh', room: 'CR-101' },
          { time: '01:15 - 03:15', course: 'CS505: AI & ML Lab (Batch 1)', faculty: 'Dr. Sunita', room: 'LAB-2' },
          { time: '03:15 - 04:15', course: 'Sports / Co-Curricular Club Activity', faculty: 'Physical Dir', room: 'SPORTS_GROUND' },
        ],
      },
    ],
  },
};

export default comprehensiveTimetablesStore;
