import React from 'react';
import StatCard from '../../components/StatCard';
import { Link } from 'react-router-dom';

export const StudentDashboard = ({ user }) => {
  const studentCourses = [
    { code: 'CSE-101', title: 'Data Structures & Algorithms', instructor: 'Dr. Alan Smith', credits: 4, present: 40, total: 42, percentage: 95.2, grade: 'A+' },
    { code: 'CSE-202', title: 'Database Management Systems (DBMS)', instructor: 'Dr. Elena Rostova', credits: 4, present: 36, total: 38, percentage: 94.7, grade: 'A' },
    { code: 'CSE-301', title: 'Operating Systems', instructor: 'Dr. Alan Smith', credits: 4, present: 37, total: 40, percentage: 92.5, grade: 'A' },
    { code: 'CSE-302', title: 'Computer Networks', instructor: 'Dr. Elena Rostova', credits: 3, present: 33, total: 36, percentage: 91.7, grade: 'A-' },
    { code: 'CSE-401', title: 'Machine Learning & Neural Networks', instructor: 'Dr. Alan Smith', credits: 4, present: 32, total: 34, percentage: 94.1, grade: 'A+' },
  ];

  const totalPresent = studentCourses.reduce((acc, c) => acc + c.present, 0);
  const totalClasses = studentCourses.reduce((acc, c) => acc + c.total, 0);
  const aggregateAttendance = Math.round((totalPresent / totalClasses) * 100);

  return (
    <div className="container-fluid p-4">
      {/* Student Header Banner */}
      <div
        className="campus-card p-4 mb-4 text-white border-0 shadow-md"
        style={{ background: 'linear-gradient(135deg, #059669 0%, #047857 100%)' }}
      >
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-white text-success mb-2 fw-bold px-3 py-1">
              🎓 Student Academic Portal
            </span>
            <h2 className="fw-bold mb-1">Welcome back, {user?.first_name || user?.username || 'Student'}!</h2>
            <p className="mb-0 text-white-50 small">
              Student ID: <strong>STU-2026-001</strong> • Semester: <strong>4 (Fall 2026)</strong> • B.Tech Computer Science & Engineering
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/attendance" className="btn btn-light btn-sm fw-semibold text-success">
              <i className="bi bi-calendar-check-fill me-1"></i> Attendance Log
            </Link>
            <Link to="/courses" className="btn btn-outline-light btn-sm fw-semibold">
              <i className="bi bi-book me-1"></i> My Courses
            </Link>
          </div>
        </div>
      </div>

      {/* Student KPI Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Cumulative GPA"
            value="3.85"
            change="Top 5% of class"
            isPositive={true}
            icon="bi-trophy-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Overall Attendance"
            value={`${aggregateAttendance}%`}
            change={`${totalPresent}/${totalClasses} Classes (Threshold > 75%)`}
            isPositive={aggregateAttendance >= 75}
            icon="bi-pie-chart-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Enrolled Credits"
            value="19"
            change="5 Registered Courses"
            isPositive={true}
            icon="bi-mortarboard"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Fee Status"
            value="Paid in Full"
            change="Invoice #TXN-CAMPUS-982347"
            isPositive={true}
            icon="bi-check-circle-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Enrolled Courses & Attendance Breakdown */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <div className="d-flex justify-content-between align-items-center mb-3">
              <h5 className="fw-bold text-dark mb-0">Enrolled Courses & Attendance Breakdown</h5>
              <Link to="/attendance" className="btn btn-sm btn-link text-primary p-0">
                View Full Audit →
              </Link>
            </div>
            <div className="d-flex flex-column gap-3">
              {studentCourses.map((c, idx) => (
                <div key={idx} className="p-3 bg-light rounded-3 border">
                  <div className="d-flex justify-content-between align-items-center mb-1">
                    <h6 className="fw-bold text-dark mb-0">
                      {c.code}: {c.title}
                    </h6>
                    <span className="badge bg-success">Grade: {c.grade}</span>
                  </div>
                  <small className="text-muted d-block mb-2">
                    Instructor: {c.instructor} • {c.credits} Credits
                  </small>
                  <div className="d-flex justify-content-between small text-secondary mb-1">
                    <span>
                      Attendance: <strong>{c.percentage}%</strong>
                    </span>
                    <span>
                      {c.present}/{c.total} Lectures Attended
                    </span>
                  </div>
                  <div className="progress" style={{ height: '6px' }}>
                    <div
                      className={`progress-bar ${c.percentage >= 85 ? 'bg-success' : c.percentage >= 75 ? 'bg-warning' : 'bg-danger'}`}
                      style={{ width: `${c.percentage}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Quick Timetable & Notifications */}
        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Today's Class Schedule</h5>
            <div className="d-flex flex-column gap-3 mb-4">
              <div className="p-3 bg-light rounded-3 border-start border-4 border-primary">
                <div className="d-flex justify-content-between align-items-center">
                  <span className="badge bg-primary text-white">09:00 - 10:00</span>
                  <small className="text-muted">Turing-204</small>
                </div>
                <h6 className="fw-bold text-dark mt-2 mb-0">DBMS (CSE-202)</h6>
                <small className="text-secondary">Dr. Elena Rostova</small>
              </div>

              <div className="p-3 bg-light rounded-3 border-start border-4 border-info">
                <div className="d-flex justify-content-between align-items-center">
                  <span className="badge bg-info text-white">10:00 - 11:00</span>
                  <small className="text-muted">Turing-101</small>
                </div>
                <h6 className="fw-bold text-dark mt-2 mb-0">Operating Systems (CSE-301)</h6>
                <small className="text-secondary">Dr. Alan Smith</small>
              </div>

              <div className="p-3 bg-light rounded-3 border-start border-4 border-warning">
                <div className="d-flex justify-content-between align-items-center">
                  <span className="badge bg-warning text-dark">11:00 - 11:30</span>
                  <small className="text-muted">Campus Lounge</small>
                </div>
                <h6 className="fw-bold text-dark mt-2 mb-0">☕ Break / Recess</h6>
              </div>
            </div>

            <Link to="/timetable" className="btn btn-outline-primary btn-sm w-100 fw-semibold">
              <i className="bi bi-calendar3 me-1"></i> View Full Weekly Timetable
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentDashboard;
