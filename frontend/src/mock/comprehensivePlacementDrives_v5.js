/**
 * Comprehensive Placement Drives Database - Part 5
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v5 = {
  drives: [
    {
      id: "DRV-2026-021",
      company: "Samsung R&D Institute",
      tier: "Dream Option",
      eligibility: { cgpa_min: 7.8, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-18", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Samsung Global Software Test", date: "2026-10-21", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-10-26", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-10-27", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 16.0, gross_salary_pm: 110000, stocks_val_usd: 3000, locations: ["Bangalore", "Noida"] }
    },
    {
      id: "DRV-2026-022",
      company: "Amazon Development Center",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-20", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Amazon Online Assessment", date: "2026-10-23", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-28", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 30.0, gross_salary_pm: 200000, stocks_val_usd: 22000, locations: ["Bangalore", "Hyderabad", "Chennai"] }
    },
    {
      id: "DRV-2026-023",
      company: "Walmart Global Tech",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-22", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Walmart CodeHers Test", date: "2026-10-25", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-30", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 10000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-024",
      company: "Adobe Systems",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-24", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Adobe Coding Assessment", date: "2026-10-27", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-01", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 28.5, gross_salary_pm: 190000, stocks_val_usd: 18000, locations: ["Noida", "Bangalore"] }
    },
    {
      id: "DRV-2026-025",
      company: "Uber India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.8, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-26", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Uber Coding Challenge", date: "2026-10-29", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-03", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 35.0, gross_salary_pm: 240000, stocks_val_usd: 30000, locations: ["Bangalore", "Hyderabad"] }
    }
  ]
};

export default comprehensivePlacementDrives_v5;
