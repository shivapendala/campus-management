/**
 * Comprehensive Placement Drives Database - Part 7
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v7 = {
  drives: [
    {
      id: "DRV-2026-031",
      company: "Adobe Inc.",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-10", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Adobe Cognitive & Coding Test", date: "2026-11-13", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-11-18", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-11-19", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 28.5, gross_salary_pm: 190000, stocks_val_usd: 15000, locations: ["Noida", "Bangalore"] }
    },
    {
      id: "DRV-2026-032",
      company: "Cisco Systems India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-12", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Networking & Coding Challenge", date: "2026-11-15", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-20", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 19.0, gross_salary_pm: 130000, stocks_val_usd: 5000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-033",
      company: "Samsung R&D Institute Bangalore",
      tier: "Dream Option",
      eligibility: { cgpa_min: 7.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-14", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Samsung Global Software Test", date: "2026-11-17", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-22", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 16.0, gross_salary_pm: 110000, stocks_val_usd: 3000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-034",
      company: "Qualcomm India Private Limited",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["ECE", "CSE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-16", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Hardware & Coding Assessment", date: "2026-11-19", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-24", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 8000, locations: ["Hyderabad", "Bangalore"] }
    },
    {
      id: "DRV-2026-035",
      company: "Intuit India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.2, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-18", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Intuit Software Challenge", date: "2026-11-21", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-26", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 25.5, gross_salary_pm: 170000, stocks_val_usd: 12000, locations: ["Bangalore"] }
    }
  ]
};

export default comprehensivePlacementDrives_v7;
