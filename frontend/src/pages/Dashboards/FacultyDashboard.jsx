import React, { useState } from 'react';
import StatCard from '../../components/StatCard';
import { Link } from 'react-router-dom';

export const FacultyDashboard = ({ user }) => {
  const [markedToday, setMarkedToday] = useState(false);

  return (
    <div className="container-fluid p-4">
      {/* Faculty Header Banner */}
      <div className="campus-card p-4 mb-4 text-white border-0 shadow-md" style={{ background: 'linear-gradient(135deg, #4f46e5 0%, #3730a3 100%)' }}>
        <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
          <div>
            <span className="badge bg-white text-primary mb-2 fw-bold px-3 py-1">
              👨‍🏫 Faculty Instructor Portal
            </span>
            <h2 className="fw-bold mb-1">Hello, Prof. {user?.first_name || user?.username || 'Instructor'}!</h2>
            <p className="mb-0 text-white-50 small">
              Manage assigned lectures, record student attendance, and evaluate submissions.
            </p>
          </div>
          <div className="d-flex gap-2">
            <button
              onClick={() => setMarkedToday(true)}
              className="btn btn-warning btn-sm fw-semibold text-dark shadow-sm"
            >
              <i className="bi bi-calendar-check me-1"></i> {markedToday ? '✓ Attendance Recorded' : 'Mark Daily Attendance'}
            </button>
            <Link to="/courses" className="btn btn-outline-light btn-sm fw-semibold">
              <i className="bi bi-file-earmark-text me-1"></i> Course Materials
            </Link>
          </div>
        </div>
      </div>

      {/* Faculty KPI Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="My Courses"
            value="3"
            change="CS-101, CS-204, CS-305"
            isPositive={true}
            icon="bi-journal-code"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Enrolled Students"
            value="145"
            change="Across 3 sections"
            isPositive={true}
            icon="bi-people"
            gradientClass="bg-gradient-cyan"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Pending Grading"
            value="12"
            change="Assignment 1 Submissions"
            isPositive={false}
            icon="bi-inbox-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Class Avg Attendance"
            value="91.8%"
            change="Lecture Session 18"
            isPositive={true}
            icon="bi-check-circle-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>
      </div>

      {/* Courses & Teaching Schedule */}
      <div className="row g-4 mb-4">
        <div className="col-12 col-lg-7">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Active Teaching Courses</h5>
            <div className="d-flex flex-column gap-3">
              <div className="p-3 bg-light rounded-3 border d-flex justify-content-between align-items-center">
                <div>
                  <h6 className="fw-bold text-primary mb-1">CS-101: Data Structures & Algorithms</h6>
                  <small className="text-muted">Section A • Mon, Wed, Fri (10:00 AM - 11:30 AM) • Room Turing-101</small>
                </div>
                <span className="badge bg-primary px-3 py-2">60 Students</span>
              </div>

              <div className="p-3 bg-light rounded-3 border d-flex justify-content-between align-items-center">
                <div>
                  <h6 className="fw-bold text-primary mb-1">CS-204: Distributed Cloud Architectures</h6>
                  <small className="text-muted">Section B • Tue, Thu (02:00 PM - 03:30 PM) • Room Cloud Lab 2</small>
                </div>
                <span className="badge bg-info text-dark px-3 py-2">45 Students</span>
              </div>

              <div className="p-3 bg-light rounded-3 border d-flex justify-content-between align-items-center">
                <div>
                  <h6 className="fw-bold text-primary mb-1">CS-305: Artificial Intelligence Foundations</h6>
                  <small className="text-muted">Section A • Fri (02:00 PM - 05:00 PM) • AI Seminar Hall</small>
                </div>
                <span className="badge bg-secondary px-3 py-2">40 Students</span>
              </div>
            </div>
          </div>
        </div>

        <div className="col-12 col-lg-5">
          <div className="campus-card p-4 h-100">
            <h5 className="fw-bold text-dark mb-3">Today's Class Schedule</h5>
            <ul className="list-group list-group-flush small">
              <li className="list-group-item px-0 py-3 d-flex justify-content-between align-items-center">
                <div>
                  <span className="fw-bold text-dark d-block">10:00 AM - 11:30 AM</span>
                  <span className="text-muted">CS-101 Lecture: AVL Tree Rotations</span>
                </div>
                <span className="badge bg-success">Completed</span>
              </li>
              <li className="list-group-item px-0 py-3 d-flex justify-content-between align-items-center">
                <div>
                  <span className="fw-bold text-dark d-block">02:00 PM - 03:30 PM</span>
                  <span className="text-muted">CS-204 Lab: Kubernetes Deployment</span>
                </div>
                <span className="badge bg-primary">Upcoming</span>
              </li>
              <li className="list-group-item px-0 py-3 d-flex justify-content-between align-items-center">
                <div>
                  <span className="fw-bold text-dark d-block">04:00 PM - 05:00 PM</span>
                  <span className="text-muted">Office Hours: Student Mentoring</span>
                </div>
                <span className="badge bg-light text-secondary border">Scheduled</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FacultyDashboard;
