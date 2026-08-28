/**
 * Comprehensive Placement Drives Database - Part 4
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v4 = {
  drives: [
    {
      id: "DRV-2026-016",
      company: "LTI Mindtree",
      tier: "Tier 1",
      eligibility: { cgpa_min: 6.5, backlogs_allowed: 1, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-10", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Logical Reasoning Test", date: "2026-10-13", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-10-18", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-10-19", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 5.0, gross_salary_pm: 40000, stocks_val_usd: 0, locations: ["Mumbai", "Bangalore", "Pune"] }
    },
    {
      id: "DRV-2026-017",
      company: "Cisco Systems",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-12", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Networking & Coding Test", date: "2026-10-15", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-20", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 18.5, gross_salary_pm: 130000, stocks_val_usd: 5000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-018",
      company: "Qualcomm India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.2, backlogs_allowed: 0, departments: ["ECE", "CSE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-13", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Hardware & Coding Test", date: "2026-10-16", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-21", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 8000, locations: ["Bangalore", "Hyderabad"] }
    },
    {
      id: "DRV-2026-019",
      company: "Intel India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["ECE", "CSE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-14", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "VLSI & Coding Test", date: "2026-10-17", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-22", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 20.0, gross_salary_pm: 140000, stocks_val_usd: 7000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-020",
      company: "AMD India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["ECE", "CSE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-15", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Silicon & Coding Test", date: "2026-10-18", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-23", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 19.5, gross_salary_pm: 135000, stocks_val_usd: 6000, locations: ["Bangalore", "Hyderabad"] }
    }
  ]
};

export default comprehensivePlacementDrives_v4;
