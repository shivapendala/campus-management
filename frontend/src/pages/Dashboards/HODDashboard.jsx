import React, { useEffect, useState } from 'react';
import StatCard from '../../components/StatCard';
import api from '../../api/axios';
import { Link } from 'react-router-dom';

export const HODDashboard = ({ user }) => {
  const departmentName = user?.department_name || 'Computer Science & Engineering';

  return (
    <div className="container-fluid p-4">
      {/* HOD Header Banner */}
      <div className="campus-card p-4 mb-4 text-white border-0 shadow-md" style={{ background: 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)' }}>
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-white text-primary mb-2 fw-bold px-3 py-1">
              🏛️ Head of Department (HOD) Portal
            </span>
            <h2 className="fw-bold mb-1">Welcome, Dr. {user?.last_name || user?.first_name || 'Department Chair'}</h2>
            <p className="mb-0 text-white-50 small">
              Department Operations: <strong>{departmentName}</strong>
            </p>
          </div>
          <div className="d-flex gap-2">
            <Link to="/faculty" className="btn btn-light btn-sm fw-semibold text-primary">
              <i className="bi bi-person-badge-fill me-1"></i> Faculty Staff
            </Link>
            <Link to="/courses" className="btn btn-outline-light btn-sm fw-semibold">
              <i className="bi bi-journal-check me-1"></i> Syllabus & Courses
            </Link>
          </div>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Dept Students"
            value="420"
            change="Across 4 Batches"
            isPositive={true}
            icon="bi-people"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Faculty in Dept"
            value="18"
            change="14 Ph.D. Holders"
            isPositive={true}
            icon="bi-person-workspace"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Dept Attendance Avg"
            value="94.2%"
            change="+1.5% this month"
            isPositive={true}
            icon="bi-check-all"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Active Courses"
            value="14"
            change="Fall 2026 Term"
            isPositive={true}
            icon="bi-book-half"
            gradientClass="bg-gradient-amber"
          />
        </div>
      </div>

      {/* Department Quick Oversight */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Faculty Teaching Allocations</h5>
            <div className="table-responsive">
              <table className="table table-hover align-middle small mb-0">
                <thead className="table-light">
                  <tr>
                    <th>Faculty</th>
                    <th>Designation</th>
                    <th>Allocated Course</th>
                    <th>Attendance %</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>
                      <strong>Dr. Alan Smith</strong>
                    </td>
                    <td>Professor & HOD</td>
                    <td>CS-101 Data Structures</td>
                    <td><span className="badge bg-success-subtle text-success">96%</span></td>
                    <td><button className="btn btn-sm btn-outline-primary py-0">Review</button></td>
                  </tr>
                  <tr>
                    <td>
                      <strong>Dr. Elena Rostova</strong>
                    </td>
                    <td>Associate Professor</td>
                    <td>CS-204 Cloud Architectures</td>
                    <td><span className="badge bg-success-subtle text-success">93%</span></td>
                    <td><button className="btn btn-sm btn-outline-primary py-0">Review</button></td>
                  </tr>
                  <tr>
                    <td>
                      <strong>Prof. David Kumar</strong>
                    </td>
                    <td>Assistant Professor</td>
                    <td>CS-305 Machine Learning</td>
                    <td><span className="badge bg-warning-subtle text-warning">88%</span></td>
                    <td><button className="btn btn-sm btn-outline-primary py-0">Review</button></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Curriculum Progress</h5>
            <div className="mb-3">
              <div className="d-flex justify-content-between small fw-semibold mb-1">
                <span>CS-101 Data Structures & Algorithms</span>
                <span>78%</span>
              </div>
              <div className="progress" style={{ height: '8px' }}>
                <div className="progress-bar bg-primary" style={{ width: '78%' }}></div>
              </div>
            </div>

            <div className="mb-3">
              <div className="d-flex justify-content-between small fw-semibold mb-1">
                <span>CS-204 Distributed Cloud Architectures</span>
                <span>85%</span>
              </div>
              <div className="progress" style={{ height: '8px' }}>
                <div className="progress-bar bg-info" style={{ width: '85%' }}></div>
              </div>
            </div>

            <div className="mb-3">
              <div className="d-flex justify-content-between small fw-semibold mb-1">
                <span>CS-302 Database Management Systems</span>
                <span>65%</span>
              </div>
              <div className="progress" style={{ height: '8px' }}>
                <div className="progress-bar bg-warning" style={{ width: '65%' }}></div>
              </div>
            </div>

            <div className="p-3 bg-light rounded-3 border mt-4">
              <small className="text-muted d-block mb-1">Upcoming Exam Review:</small>
              <strong className="text-dark d-block">Fall 2026 Midterm Question Papers due in 4 days</strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HODDashboard;
