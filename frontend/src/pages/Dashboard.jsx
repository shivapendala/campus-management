import React from 'react';
import { useAuth } from '../context/AuthContext';
import AdminDashboard from './Dashboards/AdminDashboard';
import HODDashboard from './Dashboards/HODDashboard';
import FacultyDashboard from './Dashboards/FacultyDashboard';
import StudentDashboard from './Dashboards/StudentDashboard';

export const Dashboard = () => {
  const { user, role } = useAuth();
  const activeRole = role || user?.role || 'ADMIN';

  switch (activeRole) {
    case 'HOD':
      return <HODDashboard user={user} />;
    case 'FACULTY':
      return <FacultyDashboard user={user} />;
    case 'STUDENT':
      return <StudentDashboard user={user} />;
    case 'ADMIN':
    case 'PLACEMENT_OFFICER':
    case 'ACCOUNTANT':
    case 'LIBRARIAN':
    default:
      return <AdminDashboard user={user} />;
  }
};

export default Dashboard;
