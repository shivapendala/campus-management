/**
 * Comprehensive Placement Drives Database - Part 9
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v9 = {
  drives: [
    {
      id: "DRV-2026-041",
      company: "Uber Technologies India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-20", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Uber Hackathon Coding Challenge", date: "2026-11-23", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-11-28", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-11-29", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 35.0, gross_salary_pm: 240000, stocks_val_usd: 25000, locations: ["Bangalore", "Hyderabad"] }
    },
    {
      id: "DRV-2026-042",
      company: "Morgan Stanley Services",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-22", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Morgan Stanley Coding Challenge", date: "2026-11-25", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-30", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 21.0, gross_salary_pm: 145000, stocks_val_usd: 8000, locations: ["Mumbai", "Bangalore"] }
    }
  ]
};

export default comprehensivePlacementDrives_v9;
