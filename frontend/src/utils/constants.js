/**
 * Application constants, roles, and status badge configurations.
 */

export const USER_ROLES = {
  ADMIN: 'ADMIN',
  HOD: 'HOD',
  FACULTY: 'FACULTY',
  STUDENT: 'STUDENT',
  PLACEMENT_OFFICER: 'PLACEMENT_OFFICER',
  ACCOUNTANT: 'ACCOUNTANT',
  LIBRARIAN: 'LIBRARIAN',
};

export const ROLE_LABELS = {
  ADMIN: 'System Administrator',
  HOD: 'Head of Department',
  FACULTY: 'Faculty Member',
  STUDENT: 'Student',
  PLACEMENT_OFFICER: 'Placement Officer',
  ACCOUNTANT: 'Accounts Officer',
  LIBRARIAN: 'Librarian',
};

export const ROLE_BADGE_CLASSES = {
  ADMIN: 'bg-danger text-white',
  HOD: 'bg-primary text-white',
  FACULTY: 'bg-info text-dark',
  STUDENT: 'bg-success text-white',
  PLACEMENT_OFFICER: 'bg-warning text-dark',
  ACCOUNTANT: 'bg-secondary text-white',
  LIBRARIAN: 'bg-dark text-white',
};

export const STATUS_BADGE_CLASSES = {
  ACTIVE: 'bg-success text-white',
  INACTIVE: 'bg-secondary text-white',
  SUSPENDED: 'bg-danger text-white',
  PENDING: 'bg-warning text-dark',
  GRADUATED: 'bg-info text-dark',
  SUCCESS: 'bg-success text-white',
  FAILED: 'bg-danger text-white',
  OPEN: 'bg-warning text-dark',
  RESOLVED: 'bg-success text-white',
};

export const DEPARTMENTS = [
  { code: 'CS', name: 'Computer Science & Engineering' },
  { code: 'EE', name: 'Electrical & Electronics Engineering' },
  { code: 'ME', name: 'Mechanical Engineering' },
  { code: 'BA', name: 'Business Administration' },
  { code: 'BIO', name: 'Biotechnology & Bioinformatics' },
];
