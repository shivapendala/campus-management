/**
 * Comprehensive Placement Drives Database - Part 3
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives_v3 = {
  drives: [
    {
      id: "DRV-2026-011",
      company: "Capgemini India",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-05", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Capgemini Cognitive Test", date: "2026-10-08", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical Interview", date: "2026-10-12", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "HR Interview", date: "2026-10-13", venue: "Placement Block Cabin B", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 4.2, gross_salary_pm: 34000, stocks_val_usd: 0, locations: ["Bangalore", "Mumbai", "Pune"] }
    },
    {
      id: "DRV-2026-012",
      company: "Accenture India",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-06", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Accenture Cognitive & Technical Test", date: "2026-10-09", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-14", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 4.5, gross_salary_pm: 36000, stocks_val_usd: 0, locations: ["Bangalore", "Hyderabad", "Pune"] }
    },
    {
      id: "DRV-2026-013",
      company: "Tech Mahindra",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-07", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "TechM Aptitude Test", date: "2026-10-10", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-15", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.2, gross_salary_pm: 25000, stocks_val_usd: 0, locations: ["Pune", "Chennai", "Hyderabad"] }
    },
    {
      id: "DRV-2026-014",
      company: "Mindtree Limited",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-08", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Mindtree Recruitment Test", date: "2026-10-11", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-16", venue: "Placement Block Cabin E", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 4.0, gross_salary_pm: 32000, stocks_val_usd: 0, locations: ["Bangalore", "Bhubaneswar", "Pune"] }
    },
    {
      id: "DRV-2026-015",
      company: "DXC Technology",
      tier: "Mass Recruiter",
      eligibility: { cgpa_min: 6.0, backlogs_allowed: 2, departments: ["CSE", "ECE", "EEE", "MECH", "CIVIL", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-10-09", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "DXC Cognitive Test", date: "2026-10-12", venue: "Central Computer Center", status: "SCHEDULED" },
        { phase: "Technical & HR Interview", date: "2026-10-17", venue: "Placement Block Cabin F", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 3.6, gross_salary_pm: 28000, stocks_val_usd: 0, locations: ["Bangalore", "Noida", "Chennai"] }
    }
  ]
};

export default comprehensivePlacementDrives_v3;
