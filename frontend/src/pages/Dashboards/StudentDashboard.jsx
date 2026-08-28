import React from 'react';
import StatCard from '../../components/StatCard';
import { Link } from 'react-router-dom';

export const StudentDashboard = ({ user }) => {
  return (
    <div className="container-fluid p-4">
      {/* Student Header Banner */}
      <div className="campus-card p-4 mb-4 text-white border-0 shadow-md" style={{ background: 'linear-gradient(135deg, #059669 0%, #047857 100%)' }}>
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-white text-success mb-2 fw-bold px-3 py-1">
              🎓 Student Academic Portal
            </span>
            <h2 className="fw-bold mb-1">Welcome back, {user?.first_name || user?.username || 'Student'}!</h2>
            <p className="mb-0 text-white-50 small">
              Student ID: <strong>STU-2026-001</strong> • Semester: <strong>4 (Fall 2026)</strong> • B.Tech Computer Science
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/courses" className="btn btn-light btn-sm fw-semibold text-success">
              <i className="bi bi-book me-1"></i> My Courses
            </Link>
            <button className="btn btn-outline-light btn-sm fw-semibold">
              <i className="bi bi-file-earmark-arrow-down me-1"></i> Grade Card
            </button>
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
            title="Attendance Rate"
            value="94.6%"
            change="Safe (Threshold > 75%)"
            isPositive={true}
            icon="bi-pie-chart-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Enrolled Credits"
            value="18"
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
            change="Invoice #TXN-982347"
            isPositive={true}
            icon="bi-check-circle-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Enrolled Courses & Upcoming Assessments */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Enrolled Courses & Progress</h5>
            <div className="d-flex flex-column gap-3">
              <div className="p-3 bg-light rounded-3 border">
                <div className="d-flex justify-content-between align-items-center mb-1">
                  <h6 className="fw-bold text-dark mb-0">CS-101: Data Structures & Algorithms</h6>
                  <span className="badge bg-success">Grade: A+</span>
                </div>
                <small className="text-muted d-block mb-2">Instructor: Dr. Alan Smith • 4 Credits</small>
                <div className="d-flex justify-content-between small text-secondary mb-1">
                  <span>Attendance: 96%</span>
                  <span>18/20 Lectures Attended</span>
                </div>
                <div className="progress" style={{ height: '6px' }}>
                  <div className="progress-bar bg-success" style={{ width: '96%' }}></div>
                </div>
              </div>

              <div className="p-3 bg-light rounded-3 border">
                <div className="d-flex justify-content-between align-items-center mb-1">
                  <h6 className="fw-bold text-dark mb-0">CS-204: Distributed Cloud Architectures</h6>
                  <span className="badge bg-primary">Grade: A</span>
                </div>
                <small className="text-muted d-block mb-2">Instructor: Dr. Elena Rostova • 3 Credits</small>
                <div className="d-flex justify-content-between small text-secondary mb-1">
                  <span>Attendance: 92%</span>
                  <span>14/15 Lectures Attended</span>
                </div>
                <div className="progress" style={{ height: '6px' }}>
                  <div className="progress-bar bg-primary" style={{ width: '92%' }}></div>
                </div>
              </div>

              <div className="p-3 bg-light rounded-3 border">
                <div className="d-flex justify-content-between align-items-center mb-1">
                  <h6 className="fw-bold text-dark mb-0">EE-201: Embedded Microcontroller Systems</h6>
                  <span className="badge bg-info text-dark">Grade: A</span>
                </div>
                <small className="text-muted d-block mb-2">Instructor: Dr. Rajesh Kumar • 4 Credits</small>
                <div className="d-flex justify-content-between small text-secondary mb-1">
                  <span>Attendance: 90%</span>
                  <span>12/14 Lectures Attended</span>
                </div>
                <div className="progress" style={{ height: '6px' }}>
                  <div className="progress-bar bg-info" style={{ width: '90%' }}></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Upcoming Examinations & Deadlines</h5>
            <div className="d-flex flex-column gap-3">
              <div className="p-3 bg-light rounded-3 border-start border-4 border-danger">
                <div className="d-flex justify-content-between">
                  <strong className="text-dark">Midterm Exam: CS-101</strong>
                  <span className="badge bg-danger">In 14 Days</span>
                </div>
                <small className="text-muted d-block">Auditorium Hall 1 • Max Marks: 100</small>
              </div>

              <div className="p-3 bg-light rounded-3 border-start border-4 border-warning">
                <div className="d-flex justify-content-between">
                  <strong className="text-dark">Assignment 1 Submission</strong>
                  <span className="badge bg-warning text-dark">Due in 5 Days</span>
                </div>
                <small className="text-muted d-block">Graph Traversal BFS & DFS Algorithms</small>
              </div>

              <div className="p-3 bg-light rounded-3 border-start border-4 border-success">
                <div className="d-flex justify-content-between">
                  <strong className="text-dark">Google Cloud Placement Drive</strong>
                  <span className="badge bg-success">Shortlisted</span>
                </div>
                <small className="text-muted d-block">Associate Cloud Solutions Engineer • 24.5 LPA</small>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentDashboard;
