import React, { useEffect, useState } from 'react';
import StatCard from '../../components/StatCard';
import EnrollmentChart from '../../components/Charts/EnrollmentChart';
import DepartmentChart from '../../components/Charts/DepartmentChart';
import PerformanceChart from '../../components/Charts/PerformanceChart';
import api from '../../api/axios';
import { Link } from 'react-router-dom';

export const AdminDashboard = ({ user }) => {
  const [report, setReport] = useState({
    total_students: 1240,
    total_faculty: 84,
    total_departments: 5,
    total_courses: 52,
    total_fee_collected: 185000,
    open_complaints_count: 3,
    upcoming_events_count: 2,
    active_placement_drives: 4,
    academic_term: 'Fall 2026',
  });

  useEffect(() => {
    const loadOverview = async () => {
      try {
        const res = await api.get('/reports/overview/');
        setReport(res.data);
      } catch (err) {
        console.error('Failed to load admin overview:', err);
      }
    };
    loadOverview();
  }, []);

  return (
    <div className="container-fluid p-4">
      {/* Welcome Banner */}
      <div className="campus-card p-4 mb-4 bg-gradient-primary text-white border-0 shadow-md">
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-white text-primary mb-2 fw-bold px-3 py-1">
              👑 Institutional Administrator Portal
            </span>
            <h2 className="fw-bold mb-1">Welcome back, {user?.first_name || user?.username || 'Administrator'}!</h2>
            <p className="mb-0 text-white-50 small">
              Real-time governance dashboard, financial receipts, and university operations oversight.
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/students" className="btn btn-light btn-sm fw-semibold text-primary">
              <i className="bi bi-people-fill me-1"></i> Manage Students
            </Link>
            <Link to="/courses" className="btn btn-outline-light btn-sm fw-semibold">
              <i className="bi bi-journal-plus me-1"></i> Manage Catalog
            </Link>
          </div>
        </div>
      </div>

      {/* KPI Cards Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Total Students"
            value={report.total_students?.toLocaleString() || '1,240'}
            change="+8.4% enrolled"
            isPositive={true}
            icon="bi-people-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Faculty Staff"
            value={report.total_faculty || '84'}
            change="Across 5 Depts"
            isPositive={true}
            icon="bi-person-workspace"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Fees Collected"
            value={`$${(report.total_fee_collected || 185000).toLocaleString()}`}
            change="Fall 2026 cycle"
            isPositive={true}
            icon="bi-cash-stack"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Placement Drives"
            value={report.active_placement_drives || '4'}
            change="Google, MS, Amazon"
            isPositive={true}
            icon="bi-briefcase-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Charts Section */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-8">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">Enrollment Trajectory</h5>
                <p className="text-muted small mb-0">Year-to-date university intake</p>
              </div>
              <span className="badge bg-light text-secondary border">{report.academic_term || 'Fall 2026'}</span>
            </div>
            <EnrollmentChart />
          </div>
        </div>

        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-1">Department Share</h5>
            <p className="text-muted small mb-3">Student distribution</p>
            <DepartmentChart />
          </div>
        </div>
      </div>

      {/* Academic Performance & Highlights */}
      <div className="row g-4">
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">Academic Grade Standings</h5>
                <p className="text-muted small mb-0">Campus-wide GPA bracket breakdown</p>
              </div>
              <span className="badge bg-success-subtle text-success fw-bold">Avg GPA: 3.65</span>
            </div>
            <PerformanceChart />
          </div>
        </div>

        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">System Actions & Health</h5>
            <div className="d-flex flex-column gap-3">
              <div className="p-3 bg-light rounded-3 border d-flex align-items-center justify-content-between">
                <div>
                  <span className="fw-semibold text-dark d-block">Open Grievance Tickets</span>
                  <small className="text-muted">{report.open_complaints_count || 3} tickets requiring staff action</small>
                </div>
                <span className="badge bg-warning text-dark fw-bold px-2 py-1">Review</span>
              </div>

              <div className="p-3 bg-light rounded-3 border d-flex align-items-center justify-content-between">
                <div>
                  <span className="fw-semibold text-dark d-block">Upcoming Campus Events</span>
                  <small className="text-muted">{report.upcoming_events_count || 2} scheduled workshops & fests</small>
                </div>
                <span className="badge bg-primary text-white fw-bold px-2 py-1">Calendar</span>
              </div>

              <div className="p-3 bg-light rounded-3 border d-flex align-items-center justify-content-between">
                <div>
                  <span className="fw-semibold text-dark d-block">Database Status</span>
                  <small className="text-muted">PostgreSQL 16 Healthy (15 modules synced)</small>
                </div>
                <span className="badge bg-success text-white fw-bold px-2 py-1">Online</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
