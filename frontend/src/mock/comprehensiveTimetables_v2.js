/**
 * Comprehensive Timetable Database - Multi-Department Semester Timetables
 * Defines lecture periods, laboratory slots, days, and classrooms.
 */

export const comprehensiveTimetables_v2 = {
  CSE: {
    semesters: [
      {
        semester: 1,
        slots: [
          { day: "MONDAY", period: 1, time: "09:00 - 10:00", course: "CS101: Python Programming", classroom: "LH-101", faculty: "FAC-CSE-001" },
          { day: "MONDAY", period: 2, time: "10:00 - 11:00", course: "MA101: Engineering Mathematics I", classroom: "LH-101", faculty: "FAC-MATH-001" },
          { day: "MONDAY", period: 3, time: "11:15 - 12:15", course: "PH101: Engineering Physics", classroom: "LH-101", faculty: "FAC-PHYS-001" },
          { day: "MONDAY", period: 4, time: "12:15 - 01:15", course: "CY101: Engineering Chemistry", classroom: "LH-101", faculty: "FAC-CHEM-001" },
          { day: "MONDAY", period: 5, time: "02:00 - 03:00", course: "GE101: Basic Engineering Sciences", classroom: "LH-101", faculty: "FAC-MECH-005" },
          { day: "MONDAY", period: 6, time: "03:00 - 04:00", course: "EN101: Professional English", classroom: "LH-101", faculty: "FAC-HUM-001" }
        ]
      },
      {
        semester: 2,
        slots: [
          { day: "TUESDAY", period: 1, time: "09:00 - 10:00", course: "CS201: Data Structures in C", classroom: "LH-102", faculty: "FAC-CSE-002" },
          { day: "TUESDAY", period: 2, time: "10:00 - 11:00", course: "MA102: Engineering Mathematics II", classroom: "LH-102", faculty: "FAC-MATH-002" },
          { day: "TUESDAY", period: 3, time: "11:15 - 12:15", course: "EE101: Basic Electrical Engineering", classroom: "LH-102", faculty: "FAC-EEE-003" },
          { day: "TUESDAY", period: 4, time: "12:15 - 01:15", course: "EC101: Basic Electronics Engineering", classroom: "LH-102", faculty: "FAC-ECE-005" },
          { day: "TUESDAY", period: 5, time: "02:00 - 05:00", course: "CS202: Data Structures Lab", classroom: "LAB-CSE-2", faculty: "FAC-CSE-002" }
        ]
      },
      {
        semester: 3,
        slots: [
          { day: "WEDNESDAY", period: 1, time: "09:00 - 10:00", course: "CS301: Database Management Systems", classroom: "LH-201", faculty: "FAC-CSE-001" },
          { day: "WEDNESDAY", period: 2, time: "10:00 - 11:00", course: "CS302: Design & Analysis of Algorithms", classroom: "LH-201", faculty: "FAC-CSE-004" },
          { day: "WEDNESDAY", period: 3, time: "11:15 - 12:15", course: "CS303: Computer Organization & Architecture", classroom: "LH-201", faculty: "FAC-CSE-006" },
          { day: "WEDNESDAY", period: 4, time: "12:15 - 01:15", course: "MA201: Discrete Mathematics", classroom: "LH-201", faculty: "FAC-MATH-003" },
          { day: "WEDNESDAY", period: 5, time: "02:00 - 05:00", course: "CS304: DBMS Lab", classroom: "LAB-CSE-3", faculty: "FAC-CSE-001" }
        ]
      },
      {
        semester: 4,
        slots: [
          { day: "THURSDAY", period: 1, time: "09:00 - 10:00", course: "CS401: Operating Systems", classroom: "LH-202", faculty: "FAC-CSE-003" },
          { day: "THURSDAY", period: 2, time: "10:00 - 11:00", course: "CS402: Software Engineering", classroom: "LH-202", faculty: "FAC-CSE-005" },
          { day: "THURSDAY", period: 3, time: "11:15 - 12:15", course: "CS403: Formal Languages & Automata", classroom: "LH-202", faculty: "FAC-CSE-007" },
          { day: "THURSDAY", period: 4, time: "12:15 - 01:15", course: "MA202: Probability & Statistics", classroom: "LH-202", faculty: "FAC-MATH-004" },
          { day: "THURSDAY", period: 5, time: "02:00 - 05:00", course: "CS404: Operating Systems Lab", classroom: "LAB-CSE-4", faculty: "FAC-CSE-003" }
        ]
      }
    ]
  },
  ECE: {
    semesters: [
      {
        semester: 3,
        slots: [
          { day: "MONDAY", period: 1, time: "09:00 - 10:00", course: "EC301: Electronic Circuits & Devices", classroom: "LH-301", faculty: "FAC-ECE-001" },
          { day: "MONDAY", period: 2, time: "10:00 - 11:00", course: "EC302: Network Analysis & Synthesis", classroom: "LH-301", faculty: "FAC-ECE-002" },
          { day: "MONDAY", period: 3, time: "11:15 - 12:15", course: "EC303: Signals & Systems", classroom: "LH-301", faculty: "FAC-ECE-003" },
          { day: "MONDAY", period: 4, time: "12:15 - 01:15", course: "MA203: Transform Techniques", classroom: "LH-301", faculty: "FAC-MATH-005" },
          { day: "MONDAY", period: 5, time: "02:00 - 05:00", course: "EC304: Electronic Devices Lab", classroom: "LAB-ECE-1", faculty: "FAC-ECE-001" }
        ]
      }
    ]
  }
};

export default comprehensiveTimetables_v2;
