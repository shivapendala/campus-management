/**
 * Standard Campus Placement Drives & Corporate Recruitment Mock Data Store
 */

export const mockCorporatePlacementsData = [
  {
    company_id: 'CMP-01',
    company_name: 'Google India Pvt Ltd',
    tier: 'SUPER_DREAM',
    job_role: 'Software Development Engineer I (SDE-1)',
    ctc_lpa: 32.5,
    drive_date: '2026-09-05',
    eligibility_criteria: {
      min_cgpa: 8.5,
      max_active_backlogs: 0,
      allowed_departments: ['CSE', 'ECE'],
      tenth_twelfth_min_pct: 80.0,
    },
    hiring_rounds: ['Online Coding Challenge (LeetCode Hard)', 'Technical Interview 1 (DSA)', 'Technical Interview 2 (System Design)', 'Googlyness & Leadership HR'],
    registered_candidates_count: 145,
    shortlisted_candidates_count: 18,
    offers_extended_count: 4,
    status: 'SCHEDULED_DAY_0',
  },
  {
    company_id: 'CMP-02',
    company_name: 'Microsoft IDC Bangalore',
    tier: 'SUPER_DREAM',
    job_role: 'Software Engineer',
    ctc_lpa: 28.0,
    drive_date: '2026-09-08',
    eligibility_criteria: {
      min_cgpa: 8.0,
      max_active_backlogs: 0,
      allowed_departments: ['CSE', 'ECE', 'EEE'],
      tenth_twelfth_min_pct: 75.0,
    },
    hiring_rounds: ['Online Assessment', 'Technical Round 1', 'Technical Round 2', 'AA Round'],
    registered_candidates_count: 180,
    shortlisted_candidates_count: 24,
    offers_extended_count: 6,
    status: 'SCHEDULED_DAY_0',
  },
  {
    company_id: 'CMP-03',
    company_name: 'Oracle India Development Center',
    tier: 'SUPER_DREAM',
    job_role: 'Member Technical Staff (Cloud)',
    ctc_lpa: 18.5,
    drive_date: '2026-09-12',
    eligibility_criteria: {
      min_cgpa: 7.5,
      max_active_backlogs: 0,
      allowed_departments: ['CSE', 'ECE', 'EEE', 'MECH'],
      tenth_twelfth_min_pct: 70.0,
    },
    hiring_rounds: ['Online Test', 'Technical Interview', 'Managerial Interview'],
    registered_candidates_count: 240,
    shortlisted_candidates_count: 35,
    offers_extended_count: 8,
    status: 'SCHEDULED_DAY_1',
  },
  {
    company_id: 'CMP-04',
    company_name: 'TCS Digital',
    tier: 'DREAM',
    job_role: 'System Architect & Specialist Programmer',
    ctc_lpa: 7.5,
    drive_date: '2026-09-20',
    eligibility_criteria: {
      min_cgpa: 6.5,
      max_active_backlogs: 1,
      allowed_departments: ['ALL'],
      tenth_twelfth_min_pct: 60.0,
    },
    hiring_rounds: ['TCS National Qualifier Test (NQT)', 'Technical Interview', 'HR Interview'],
    registered_candidates_count: 450,
    shortlisted_candidates_count: 110,
    offers_extended_count: 42,
    status: 'ACTIVE',
  },
];

export default mockCorporatePlacementsData;
