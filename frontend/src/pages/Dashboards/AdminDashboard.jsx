import React, { useEffect, useState } from 'react';
import StatCard from '../../components/StatCard';
import AttendanceStatsPanel from '../../components/Dashboard/AttendanceStatsPanel';
import FeeStatsPanel from '../../components/Dashboard/FeeStatsPanel';
import PlacementStatsPanel from '../../components/Dashboard/PlacementStatsPanel';
import RecentActivities from '../../components/Dashboard/RecentActivities';
import ComplaintsDoughnutChart from '../../components/Charts/ComplaintsDoughnutChart';
import DepartmentChart from '../../components/Charts/DepartmentChart';
import api from '../../api/axios';
import { Link } from 'react-router-dom';

export const AdminDashboard = ({ user }) => {
  const [report, setReport] = useState({
    total_students: 2450,
    total_faculty: 180,
    total_courses: 95,
    pending_fees_count: 320,
    open_complaints_count: 25,
    placements_count: 145,
    academic_term: 'Fall 2026',
  });

  useEffect(() => {
    const loadOverview = async () => {
      try {
        const res = await api.get('/reports/overview/');
        if (res.data) {
          setReport((prev) => ({
            ...prev,
            ...res.data,
            total_students: res.data.total_students || 2450,
            total_faculty: res.data.total_faculty || 180,
            total_courses: res.data.total_courses || 95,
            pending_fees_count: res.data.pending_fees_count || 320,
            open_complaints_count: res.data.open_complaints_count || 25,
            placements_count: res.data.placements_count || 145,
          }));
        }
      } catch (err) {
        console.error('Failed to load admin overview:', err);
      }
    };
    loadOverview();
  }, []);

  return (
    <div className="container-fluid p-4">
      {/* Welcome Banner */}
      <div
        className="campus-card p-4 mb-4 text-white border-0 shadow-md"
        style={{ background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #312e81 100%)' }}
      >
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-primary text-white mb-2 fw-bold px-3 py-1">
              👑 Institutional Executive Portal
            </span>
            <h2 className="fw-bold mb-1">
              Welcome, {user?.first_name || user?.username || 'Administrator'}!
            </h2>
            <p className="mb-0 text-white-50 small">
              Live University Operations & Governance Dashboard • Term: <strong>{report.academic_term}</strong>
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/students" className="btn btn-primary btn-sm fw-semibold shadow-sm px-3">
              <i className="bi bi-people-fill me-1"></i> Student Register
            </Link>
            <Link to="/courses" className="btn btn-outline-light btn-sm fw-semibold px-3">
              <i className="bi bi-journal-plus me-1"></i> Catalog Management
            </Link>
          </div>
        </div>
      </div>

      {/* 6 Core Requested Metric Cards */}
      <div className="row g-3 mb-4">
        {/* 1. Students: 2,450 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Students"
            value="2,450"
            change="+12.4% enrolled"
            isPositive={true}
            icon="bi-people-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>

        {/* 2. Faculty: 180 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Faculty"
            value="180"
            change="Across 5 Depts"
            isPositive={true}
            icon="bi-person-workspace"
            gradientClass="bg-gradient-cyan"
          />
        </div>

        {/* 3. Courses: 95 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Courses"
            value="95"
            change="Active Catalog"
            isPositive={true}
            icon="bi-journal-bookmark-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>

        {/* 4. Pending Fees: 320 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Pending Fees"
            value="320"
            change="$320K to Collect"
            isPositive={false}
            icon="bi-cash-coin"
            gradientClass="bg-gradient-amber"
          />
        </div>

        {/* 5. Complaints: 25 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Complaints"
            value="25"
            change="Open / In-Review"
            isPositive={false}
            icon="bi-chat-left-dots-fill"
            gradientClass="bg-gradient-rose"
          />
        </div>

        {/* 6. Placements: 145 */}
        <div className="col-12 col-sm-6 col-xl-2">
          <StatCard
            title="Placements"
            value="145"
            change="Avg 18.5 LPA"
            isPositive={true}
            icon="bi-briefcase-fill"
            gradientClass="bg-gradient-indigo"
          />
        </div>
      </div>

      {/* Row 1: Attendance Statistics & Fee Statistics Panels */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-6">
          <AttendanceStatsPanel />
        </div>
        <div className="col-12 col-lg-6">
          <FeeStatsPanel />
        </div>
      </div>

      {/* Row 2: Placement Statistics & Grievance Distribution */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-4">
          <PlacementStatsPanel />
        </div>

        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">
                  <i className="bi bi-pie-chart-fill text-danger me-2"></i>
                  Grievances by Category
                </h5>
                <p className="text-muted small mb-0">25 Open Tickets Distribution</p>
              </div>
              <span className="badge bg-danger text-white fw-bold px-2 py-1">Active</span>
            </div>
            <ComplaintsDoughnutChart />
          </div>
        </div>

        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">
                  <i className="bi bi-buildings-fill text-info me-2"></i>
                  Department Enrolment
                </h5>
                <p className="text-muted small mb-0">2,450 Students Breakdown</p>
              </div>
              <span className="badge bg-info text-dark fw-bold px-2 py-1">5 Depts</span>
            </div>
            <DepartmentChart />
          </div>
        </div>
      </div>

      {/* Row 3: Live Recent Activities Timeline */}
      <div className="row g-4">
        <div className="col-12">
          <RecentActivities />
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
