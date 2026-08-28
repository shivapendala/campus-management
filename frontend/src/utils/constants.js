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
  ADMIN: 'Administrator',
  HOD: 'Head of Department',
  FACULTY: 'Faculty Member',
  STUDENT: 'Student',
  PLACEMENT_OFFICER: 'Placement Officer',
  ACCOUNTANT: 'Accountant / Bursar',
  LIBRARIAN: 'Librarian',
};

export const ROLE_BADGE_CLASSES = {
  ADMIN: 'bg-danger text-white',
  HOD: 'bg-indigo text-white',
  FACULTY: 'bg-primary text-white',
  STUDENT: 'bg-success text-white',
  PLACEMENT_OFFICER: 'bg-warning text-dark',
  ACCOUNTANT: 'bg-info text-dark',
  LIBRARIAN: 'bg-secondary text-white',
};

export const STATUS_BADGE_CLASSES = {
  ACTIVE: 'bg-success text-white',
  INACTIVE: 'bg-secondary text-white',
  GRADUATED: 'bg-info text-dark',
  SUSPENDED: 'bg-danger text-white',
  PENDING: 'bg-warning text-dark',
  OPEN: 'bg-danger text-white',
  UNDER_REVIEW: 'bg-warning text-dark',
  RESOLVED: 'bg-success text-white',
  CLOSED: 'bg-secondary text-white',
};

export const DEPARTMENTS = [
  { code: 'CSE', name: 'Computer Science & Engineering', building: 'Turing Block A' },
  { code: 'ECE', name: 'Electronics & Communication Engineering', building: 'Shannon Block B' },
  { code: 'EEE', name: 'Electrical & Electronics Engineering', building: 'Tesla Block C' },
  { code: 'MECH', name: 'Mechanical Engineering', building: 'Watt Block D' },
  { code: 'CIVIL', name: 'Civil Engineering', building: 'Smeaton Block E' },
];

export default {
  USER_ROLES,
  ROLE_LABELS,
  ROLE_BADGE_CLASSES,
  STATUS_BADGE_CLASSES,
  DEPARTMENTS,
};
