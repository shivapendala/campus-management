import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const ExamOperations = () => {
  const [activeTab, setActiveTab] = useState('seating');

  const seatingGrid = [
    [
      { desk: 'D1-1', roll: '23CSE01', dept: 'CSE', subject: 'DBMS' },
      { desk: 'D1-2', roll: '23ECE01', dept: 'ECE', subject: 'DSP' },
      { desk: 'D1-3', roll: '23CSE02', dept: 'CSE', subject: 'DBMS' },
      { desk: 'D1-4', roll: '23ECE02', dept: 'ECE', subject: 'DSP' },
    ],
    [
      { desk: 'D2-1', roll: '23ECE03', dept: 'ECE', subject: 'DSP' },
      { desk: 'D2-2', roll: '23CSE03', dept: 'CSE', subject: 'DBMS' },
      { desk: 'D2-3', roll: '23ECE04', dept: 'ECE', subject: 'DSP' },
      { desk: 'D2-4', roll: '23CSE04', dept: 'CSE', subject: 'DBMS' },
    ],
    [
      { desk: 'D3-1', roll: '23CSE05', dept: 'CSE', subject: 'DBMS' },
      { desk: 'D3-2', roll: '23ECE05', dept: 'ECE', subject: 'DSP' },
      { desk: 'D3-3', roll: '23CSE06', dept: 'CSE', subject: 'DBMS' },
      { desk: 'D3-4', roll: '23ECE06', dept: 'ECE', subject: 'DSP' },
    ],
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-ui-checks me-2"></i>Examination Operations & Seating Matrix
          </h2>
          <p className="text-muted mb-0">
            Automated interleaved examination hall seating, Gaussian grading normalization, and digital hall ticket issuance.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-qr-code me-1"></i>Batch Hall Tickets
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-printer me-1"></i>Print Seating Charts
          </button>
        </div>
      </div>

      {/* Quick Metrics */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Exam Halls Booked"
            value="18 Halls"
            icon="bi-building"
            variant="primary"
            subtitle="720 Desks Configured"
            delta="Ready"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Hall Tickets Cleared"
            value="2,380 / 2,450"
            icon="bi-pass-fill"
            variant="success"
            subtitle="97.1% Students Cleared"
            delta="97.1%"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Withheld for Attendance"
            value="45 Students"
            icon="bi-exclamation-octagon"
            variant="danger"
            subtitle="Shortage < 65% Mandatory"
            delta="Withheld"
            deltaType="negative"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Invigilators Assigned"
            value="36 Faculty"
            icon="bi-person-check-fill"
            variant="info"
            subtitle="2 Faculty per 40 Students"
            delta="Assigned"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Visual Classroom Seating Chart */}
      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="fw-bold mb-0">
            <i className="bi bi-grid me-2 text-primary"></i>Lecture Hall LH-101: Interleaved Seating Plan
          </h5>
          <span className="badge bg-success-subtle text-success px-3 py-1">
            <i className="bi bi-shield-check me-1"></i>Zero Adjacent Same-Department Collisions
          </span>
        </div>
        <p className="text-muted small mb-4">
          Alternating checkerboard allocation (CSE vs ECE) prevents adjacent cheating during end-semester exams.
        </p>

        <div className="bg-light p-4 rounded-3 border">
          <div className="text-center fw-bold text-muted mb-3 py-1 bg-white border rounded">
            --- INSTRUCTOR / INVIGILATOR PODIUM & BLACKBOARD ---
          </div>

          <div className="d-flex flex-column gap-3">
            {seatingGrid.map((row, rIdx) => (
              <div key={rIdx} className="d-flex justify-content-around gap-2">
                {row.map((desk, dIdx) => (
                  <div
                    key={dIdx}
                    className={`card p-2 text-center shadow-sm flex-fill ${
                      desk.dept === 'CSE' ? 'bg-primary-subtle border-primary' : 'bg-success-subtle border-success'
                    }`}
                    style={{ maxWidth: '220px' }}
                  >
                    <div className="d-flex justify-content-between align-items-center mb-1">
                      <span className="badge bg-white text-dark small">{desk.desk}</span>
                      <span className={`badge ${desk.dept === 'CSE' ? 'bg-primary' : 'bg-success'}`}>{desk.dept}</span>
                    </div>
                    <div className="fw-bold small">{desk.roll}</div>
                    <small className="text-muted">{desk.subject}</small>
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExamOperations;
