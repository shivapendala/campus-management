/**
 * Comprehensive Placement Drives Database - Part 6
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v6 = {
  drives: [
    {
      id: "DRV-2026-026",
      company: "Flipkart India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 7.8, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-28", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Flipkart GRiD Coding Test", date: "2026-10-31", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-11-05", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-11-06", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 22.0, gross_salary_pm: 150000, stocks_val_usd: 5000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-027",
      company: "Salesforce India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.2, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-30", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Salesforce Online Assessment", date: "2026-11-02", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-07", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 26.0, gross_salary_pm: 175000, stocks_val_usd: 12000, locations: ["Hyderabad", "Bangalore"] }
    },
    {
      id: "DRV-2026-028",
      company: "Oracle India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 7.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-01", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Oracle Coding & SQL Test", date: "2026-11-04", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-09", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 15.5, gross_salary_pm: 110000, stocks_val_usd: 0, locations: ["Bangalore", "Hyderabad", "Noida"] }
    },
    {
      id: "DRV-2026-029",
      company: "Goldman Sachs",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-03", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "GS Coderade Coding Test", date: "2026-11-06", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-11", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 24.0, gross_salary_pm: 165000, stocks_val_usd: 10000, locations: ["Bangalore", "Hyderabad"] }
    },
    {
      id: "DRV-2026-030",
      company: "Morgan Stanley",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-05", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Morgan Stanley Coding Challenge", date: "2026-11-08", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-13", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 21.0, gross_salary_pm: 145000, stocks_val_usd: 8000, locations: ["Mumbai", "Bangalore"] }
    }
  ]
};

export default comprehensivePlacementDrives_v6;
