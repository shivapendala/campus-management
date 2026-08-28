/**
 * Comprehensive Placement Drives Database - Part 10
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v10 = {
  drives: [
    {
      id: "DRV-2026-043",
      company: "Walmart Global Tech India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-20", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Walmart CodeHers Hackathon", date: "2026-11-23", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-11-28", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-11-29", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 10000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-044",
      company: "Walmart Global Tech India v2",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-22", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Walmart CodeHers Hackathon v2", date: "2026-11-25", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-30", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 10000, locations: ["Bangalore"] }
    }
  ]
};

export default comprehensivePlacementDrives_v10;
