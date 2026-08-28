/**
 * Comprehensive Placement Drives Database - Part 8
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v8 = {
  drives: [
    {
      id: "DRV-2026-036",
      company: "Morgan Stanley India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-20", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Morgan Stanley Coding Challenge", date: "2026-11-23", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-11-28", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-11-29", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 21.0, gross_salary_pm: 145000, stocks_val_usd: 8000, locations: ["Mumbai", "Bangalore"] }
    },
    {
      id: "DRV-2026-037",
      company: "J.P. Morgan Chase",
      tier: "Dream Option",
      eligibility: { cgpa_min: 7.8, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-22", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "JPMC Code for Good hackathon", date: "2026-11-25", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-11-30", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 17.5, gross_salary_pm: 120000, stocks_val_usd: 5000, locations: ["Bangalore", "Hyderabad", "Mumbai"] }
    },
    {
      id: "DRV-2026-038",
      company: "Visa Inc.",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.2, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-24", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Visa Coding Assessment", date: "2026-11-27", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-12-02", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 24.0, gross_salary_pm: 160000, stocks_val_usd: 10000, locations: ["Bangalore"] }
    },
    {
      id: "DRV-2026-039",
      company: "American Express",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-26", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Amex CodeStreet Test", date: "2026-11-29", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-12-04", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 19.5, gross_salary_pm: 135000, stocks_val_usd: 6000, locations: ["Gurgaon", "Bangalore"] }
    },
    {
      id: "DRV-2026-040",
      company: "PayPal India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-11-28", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "PayPal Coding Challenge", date: "2026-12-01", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-12-06", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 23.0, gross_salary_pm: 155000, stocks_val_usd: 11000, locations: ["Bangalore", "Chennai"] }
    }
  ]
};

export default comprehensivePlacementDrives_v8;
