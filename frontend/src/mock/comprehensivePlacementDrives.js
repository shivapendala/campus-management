/**
 * Comprehensive Placement Drives Database
 * Mapped to corporate hiring matrices and student eligibility filters.
 */

export const comprehensivePlacementDrives = {
  drives: [
    {
      id: "DRV-2026-001",
      company: "Google India",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.5, backlogs_allowed: 0, departments: ["CSE", "ECE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-05", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Online Coding Test", date: "2026-09-08", venue: "Online Coding Lab 1 & 2", status: "SCHEDULED" },
        { phase: "Technical Interview Round 1", date: "2026-09-12", venue: "Placement Block Cabin A", status: "SCHEDULED" },
        { phase: "Technical Interview Round 2", date: "2026-09-12", venue: "Placement Block Cabin B", status: "SCHEDULED" },
        { phase: "HR & Leadership Round", date: "2026-09-13", venue: "Placement Block Cabin C", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 32.5, gross_salary_pm: 220000, stocks_val_usd: 25000, locations: ["Bangalore", "Hyderabad"] }
    },
    {
      id: "DRV-2026-002",
      company: "Microsoft Corporation",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.2, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-06", venue: "Central Auditorium", status: "SCHEDULED" },
        { phase: "Online Coding Test", date: "2026-09-09", venue: "Online Coding Lab 3 & 4", status: "SCHEDULED" },
        { phase: "Technical Interview Round 1", date: "2026-09-14", venue: "Placement Block Cabin D", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 28.0, gross_salary_pm: 185000, stocks_val_usd: 20000, locations: ["Bangalore", "Noida"] }
    },
    {
      id: "DRV-2026-003",
      company: "NVIDIA Corp.",
      tier: "Dream Option",
      eligibility: { cgpa_min: 8.0, backlogs_allowed: 0, departments: ["CSE", "ECE", "EEE", "AIML"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-10", venue: "Seminar Hall 2", status: "SCHEDULED" },
        { phase: "Hardware Architecture Test", date: "2026-09-12", venue: "VLSI Center Lab", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 24.5, gross_salary_pm: 160000, stocks_val_usd: 15000, locations: ["Bangalore", "Pune"] }
    },
    {
      id: "DRV-2026-004",
      company: "Robert Bosch",
      tier: "Tier 1",
      eligibility: { cgpa_min: 7.0, backlogs_allowed: 1, departments: ["CSE", "ECE", "EEE", "MECH"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-15", venue: "Seminar Hall 1", status: "SCHEDULED" },
        { phase: "Aptitude and Technical Test", date: "2026-09-18", venue: "Online Coding Labs", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 8.5, gross_salary_pm: 65000, stocks_val_usd: 0, locations: ["Bangalore", "Coimbatore"] }
    },
    {
      id: "DRV-2026-005",
      company: "L&T Construction",
      tier: "Tier 1",
      eligibility: { cgpa_min: 6.8, backlogs_allowed: 2, departments: ["CIVIL", "MECH", "EEE"] },
      schedules: [
        { phase: "Pre-Placement Talk", date: "2026-09-20", venue: "Seminar Hall 3", status: "SCHEDULED" },
        { phase: "Structural Design Test", date: "2026-09-22", venue: "CAD Lab", status: "SCHEDULED" }
      ],
      offers: { ctc_lpa: 6.5, gross_salary_pm: 50000, stocks_val_usd: 0, locations: ["Chennai", "Mumbai"] }
    }
  ]
};

export default comprehensivePlacementDrives;
