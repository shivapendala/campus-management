/**
 * Comprehensive Placement Drives Database - Part 2
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v2 = {
  drives: [
    {
      id: "DRV-2026-006",
      company: "Cognizant Technology Solutions",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-25", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Aptitude & Logical Test", date: "2026-09-28", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-10-02", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-10-03", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 4.0, gross_salary_pm: 32000, stocks_val_usd: 0, locations: ["Bangalore", "Chennai", "Pune"] }
    },
    {
      id: "DRV-2026-007",
      company: "Tata Consultancy Services (TCS)",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-26", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "TCS National Qualifier Test", date: "2026-09-29", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-04", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.6, gross_salary_pm: 28000, stocks_val_usd: 0, locations: ["Bangalore", "Hyderabad", "Kolkata"] }
    },
    {
      id: "DRV-2026-008",
      company: "Wipro Technologies",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-27", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Wipro Elite NTH Test", date: "2026-10-01", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-05", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.5, gross_salary_pm: 27000, stocks_val_usd: 0, locations: ["Bangalore", "Chennai", "Kochi"] }
    },
    {
      id: "DRV-2026-009",
      company: "Infosys Limited",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-28", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Infosys Certification Test", date: "2026-10-02", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-06", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.6, gross_salary_pm: 28000, stocks_val_usd: 0, locations: ["Bangalore", "Mysore", "Pune"] }
    },
    {
      id: "DRV-2026-010",
      company: "HCL Technologies",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-29", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "HCL Recruitment Test", date: "2026-10-03", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-07", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.5, gross_salary_pm: 27000, stocks_val_usd: 0, locations: ["Noida", "Chennai", "Bangalore"] }
    }
  ]
};

export default comprehensivePlacementDrives_v2;
