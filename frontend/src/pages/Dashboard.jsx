import React, { useEffect, useState } from 'react';
import StatCard from '../components/StatCard';
import EnrollmentChart from '../components/Charts/EnrollmentChart';
import DepartmentChart from '../components/Charts/DepartmentChart';
import PerformanceChart from '../components/Charts/PerformanceChart';
import api from '../api/axios';

export const Dashboard = () => {
  const [summary, setSummary] = useState({
    total_students: 1240,
    total_faculty: 84,
    total_courses: 52,
    total_departments: 5,
    average_gpa: 3.65,
    average_attendance: 92.4,
    active_semester: 'Fall 2026',
  });
  const [enrollmentData, setEnrollmentData] = useState(null);
  const [deptData, setDeptData] = useState(null);
  const [gradeData, setGradeData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const [sumRes] = await Promise.allSettled([
          api.get('/reports/overview/'),
        ]);

        if (sumRes.status === 'fulfilled') setSummary(sumRes.value.data);
      } catch (err) {
        console.error('Error fetching dashboard analytics:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Campus Analytics & Overview</h2>
          <p className="text-muted mb-0">
            Real-time institutional performance metrics and academic insights for{' '}
            <span className="badge bg-primary-subtle text-primary fw-semibold">
              {summary.active_semester || 'Fall 2026'}
            </span>
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-secondary btn-sm d-flex align-items-center gap-2">
            <i className="bi bi-download"></i>
            <span>Export Report</span>
          </button>
          <button className="btn btn-primary btn-sm d-flex align-items-center gap-2">
            <i className="bi bi-plus-lg"></i>
            <span>Quick Action</span>
          </button>
        </div>
      </div>

      {/* KPI Cards Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Total Students"
            value={summary.total_students?.toLocaleString() || '1,240'}
            change="+8.4% from last term"
            isPositive={true}
            icon="bi-people-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Faculty Members"
            value={summary.total_faculty || '84'}
            change="+3 new joined"
            isPositive={true}
            icon="bi-person-workspace"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Active Courses"
            value={summary.total_courses || '52'}
            change="Across 5 Departments"
            isPositive={true}
            icon="bi-journal-bookmark-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Avg Attendance"
            value={`${summary.average_attendance || 92.4}%`}
            change="+1.2% this month"
            isPositive={true}
            icon="bi-calendar-check-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Charts Section */}
      <div className="row g-4 mb-4">
        {/* Enrollment Trends Line Chart */}
        <div className="col-12 col-lg-8">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">Enrollment Trends</h5>
                <p className="text-muted small mb-0">Monthly enrollment trajectory across all academic programs</p>
              </div>
              <span className="badge bg-light text-secondary border">2026 Year to Date</span>
            </div>
            <EnrollmentChart chartData={enrollmentData} />
          </div>
        </div>

        {/* Department Distribution Doughnut Chart */}
        <div className="col-12 col-lg-4">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">Departments</h5>
                <p className="text-muted small mb-0">Student distribution by department</p>
              </div>
            </div>
            <DepartmentChart chartData={deptData} />
          </div>
        </div>
      </div>

      {/* Performance & Quick Activities Row */}
      <div className="row g-4">
        {/* Performance Bar Chart */}
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <div>
                <h5 className="fw-bold text-dark mb-1">Grade Distribution</h5>
                <p className="text-muted small mb-0">Overall academic performance bracket summary</p>
              </div>
              <span className="badge bg-success-subtle text-success fw-semibold">
                Avg GPA: {summary.average_gpa || '3.65'}
              </span>
            </div>
            <PerformanceChart chartData={gradeData} />
          </div>
        </div>

        {/* Quick Notices / Campus Highlights */}
        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Campus Announcements</h5>
            <div className="d-flex flex-column gap-3">
              <div className="d-flex gap-3 align-items-start p-3 bg-light rounded-3 border">
                <div className="bg-primary text-white rounded-circle p-2 d-flex align-items-center justify-content-center" style={{ width: '36px', height: '36px' }}>
                  <i className="bi bi-calendar-event"></i>
                </div>
                <div>
                  <span className="d-block fw-semibold text-dark small">Fall 2026 Midterm Examination Schedule</span>
                  <span className="text-muted" style={{ fontSize: '0.8rem' }}>Examination schedules published for Engineering & Business faculties.</span>
                </div>
              </div>

              <div className="d-flex gap-3 align-items-start p-3 bg-light rounded-3 border">
                <div className="bg-success text-white rounded-circle p-2 d-flex align-items-center justify-content-center" style={{ width: '36px', height: '36px' }}>
                  <i className="bi bi-check-circle"></i>
                </div>
                <div>
                  <span className="d-block fw-semibold text-dark small">Course Registration Open</span>
                  <span className="text-muted" style={{ fontSize: '0.8rem' }}>Elective course enrollment opens for 4th and 6th semester students.</span>
                </div>
              </div>

              <div className="d-flex gap-3 align-items-start p-3 bg-light rounded-3 border">
                <div className="bg-warning text-dark rounded-circle p-2 d-flex align-items-center justify-content-center" style={{ width: '36px', height: '36px' }}>
                  <i className="bi bi-megaphone"></i>
                </div>
                <div>
                  <span className="d-block fw-semibold text-dark small">Annual Research Symposium</span>
                  <span className="text-muted" style={{ fontSize: '0.8rem' }}>Call for research papers and student poster submissions deadline in 2 weeks.</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
