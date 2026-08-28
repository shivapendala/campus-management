import React, { useState } from 'react';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import MetricCard from '../components/common/MetricCard';
import StatusBadge from '../components/common/StatusBadge';
import TimelineView from '../components/common/TimelineView';

const Student360Portal = () => {
  const [activeTab, setActiveTab] = useState('progression');
  const [selectedStudent, setSelectedStudent] = useState({
    id: 1,
    roll_number: '23CSE01042',
    name: 'Rahul Sharma',
    father_name: 'Suresh Sharma',
    department: 'Computer Science & Engineering',
    semester: 6,
    section: 'A',
    cgpa: 8.42,
    sgpa_latest: 8.65,
    attendance_pct: 87.5,
    backlogs_count: 0,
    fee_balance: 0.0,
    conduct_score: 95,
  });

  const semesterHistory = [
    { sem: 'Semester 1', credits: 22, sgpa: 8.10, status: 'PASSED', backlogs: 0 },
    { sem: 'Semester 2', credits: 24, sgpa: 8.35, status: 'PASSED', backlogs: 0 },
    { sem: 'Semester 3', credits: 22, sgpa: 8.50, status: 'PASSED', backlogs: 0 },
    { sem: 'Semester 4', credits: 24, sgpa: 8.25, status: 'PASSED', backlogs: 0 },
    { sem: 'Semester 5', credits: 22, sgpa: 8.65, status: 'PASSED', backlogs: 0 },
  ];

  const studentTimeline = [
    { title: 'Semester 5 Grade Card Issued', timestamp: 'July 15, 2026', description: 'Secured SGPA 8.65 with 0 backlogs.', icon: 'bi-award', variant: 'success' },
    { title: 'Placement Drive Application: TCS Digital', timestamp: 'August 02, 2026', description: 'Application verified and shortlisted for Round 1 (OA).', icon: 'bi-briefcase', variant: 'primary' },
    { title: 'Tuition Fee Payment Cleared', timestamp: 'August 10, 2026', description: 'Paid Term 1 fees Rs. 65,000 via Razorpay (Tx: TX-98421).', icon: 'bi-credit-card', variant: 'info' },
    { title: 'NOC Issued for Summer Internship', timestamp: 'August 18, 2026', description: 'Dean Academics signed digital Bonafide & NOC for AWS Academy.', icon: 'bi-file-earmark-check', variant: 'warning' },
  ];

  return (
    <div className="container-fluid py-4">
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-person-badge-fill me-2"></i>Student 360° Academic Cockpit
          </h2>
          <p className="text-muted mb-0">
            Comprehensive student profile, degree audit, progression tracker, document vault, and scholarship evaluation.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary" onClick={() => window.print()}>
            <i className="bi bi-printer me-1"></i>Print Official Dossier
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-file-earmark-arrow-down me-1"></i>Download Digital Transcript
          </button>
        </div>
      </div>

      {/* Student Profile Card Banner */}
      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4 bg-primary-subtle border-start border-primary border-4">
        <div className="row align-items-center">
          <div className="col-auto">
            <div
              className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center fw-bold fs-3 shadow"
              style={{ width: '72px', height: '72px' }}
            >
              {selectedStudent.name.split(' ').map((n) => n[0]).join('')}
            </div>
          </div>
          <div className="col">
            <h4 className="fw-bold mb-1 text-dark">{selectedStudent.name}</h4>
            <div className="d-flex flex-wrap gap-3 text-muted small">
              <span><i className="bi bi-hash me-1"></i>Roll: <strong>{selectedStudent.roll_number}</strong></span>
              <span><i className="bi bi-building me-1"></i>{selectedStudent.department}</span>
              <span><i className="bi bi-calendar3 me-1"></i>Semester {selectedStudent.semester} (Section {selectedStudent.section})</span>
              <span><StatusBadge status="ACTIVE" size="small" /></span>
            </div>
          </div>
          <div className="col-auto text-end">
            <div className="h2 fw-bold text-primary mb-0">{selectedStudent.cgpa}</div>
            <span className="small text-muted text-uppercase fw-semibold">Cumulative CGPA</span>
          </div>
        </div>
      </div>

      {/* Metric Cards Row */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Attendance Discipline"
            value={`${selectedStudent.attendance_pct}%`}
            icon="bi-calendar-check-fill"
            variant="success"
            subtitle="Eligible for End-Sem Exams"
            delta="Safe"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Backlogs"
            value={selectedStudent.backlogs_count}
            icon="bi-exclamation-triangle"
            variant="info"
            subtitle="Satisfies Degree Promotion Rule"
            delta="Clear"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Fee Clearance Dues"
            value={`Rs. ${selectedStudent.fee_balance.toLocaleString()}`}
            icon="bi-cash-coin"
            variant="warning"
            subtitle="Hall Ticket Clearance Approved"
            delta="Zero Dues"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Conduct & Ethics Score"
            value={`${selectedStudent.conduct_score}/100`}
            icon="bi-shield-check"
            variant="primary"
            subtitle="Exemplary Institutional Standing"
            delta="Honors Track"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Tabs */}
      <ul className="nav nav-pills mb-4 gap-2 border-bottom pb-3">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'progression' ? 'active' : ''}`}
            onClick={() => setActiveTab('progression')}
          >
            <i className="bi bi-mortarboard me-1"></i>Academic Progression & Degree Audit
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'timeline' ? 'active' : ''}`}
            onClick={() => setActiveTab('timeline')}
          >
            <i className="bi bi-clock-history me-1"></i>Institutional Timeline & Activity Log
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'scholarship' ? 'active' : ''}`}
            onClick={() => setActiveTab('scholarship')}
          >
            <i className="bi bi-gift me-1"></i>Scholarships & Concessions
          </button>
        </li>
      </ul>

      {/* TAB CONTENT: Progression */}
      {activeTab === 'progression' && (
        <div className="row g-4">
          <div className="col-lg-8">
            <div className="card border-0 shadow-sm rounded-3 p-4">
              <h5 className="fw-bold mb-3">
                <i className="bi bi-journal-bookmark me-2 text-primary"></i>Semester Academic History
              </h5>
              <div className="table-responsive">
                <table className="table table-hover align-middle">
                  <thead className="table-light">
                    <tr>
                      <th>Semester</th>
                      <th>Credits</th>
                      <th>SGPA</th>
                      <th>Active Backlogs</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {semesterHistory.map((sem, idx) => (
                      <tr key={idx}>
                        <td className="fw-bold text-dark">{sem.sem}</td>
                        <td>{sem.credits} Credits</td>
                        <td><span className="fw-bold text-primary">{sem.sgpa.toFixed(2)}</span></td>
                        <td>{sem.backlogs}</td>
                        <td><StatusBadge status={sem.status} size="small" /></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          </div>

          <div className="col-lg-4">
            <div className="card border-0 shadow-sm rounded-3 p-4 bg-light">
              <h5 className="fw-bold mb-3 text-dark">
                <i className="bi bi-trophy-fill me-2 text-warning"></i>Degree Classification Forecast
              </h5>
              <div className="p-3 bg-white rounded border mb-3">
                <div className="text-muted small">Projected Degree Award</div>
                <div className="h5 fw-bold text-success mb-0">First Class with Distinction (Honors)</div>
              </div>
              <ul className="small text-muted ps-3 mb-0">
                <li>Total Earned Credits: 116 / 160 required</li>
                <li>Statutory Promotion Status: PROMOTED TO YEAR 4</li>
                <li>Eligible for Super Dream campus recruitment drives (&gt; 12 LPA)</li>
              </ul>
            </div>
          </div>
        </div>
      )}

      {/* TAB CONTENT: Timeline */}
      {activeTab === 'timeline' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-4">
            <i className="bi bi-hourglass-split me-2 text-primary"></i>Student Lifecycle Journey
          </h5>
          <TimelineView items={studentTimeline} />
        </div>
      )}

      {/* TAB CONTENT: Scholarship */}
      {activeTab === 'scholarship' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-3 text-success">
            <i className="bi bi-stars me-2"></i>Eligible Scholarship Schemes
          </h5>
          <div className="alert alert-success d-flex align-items-center gap-2">
            <i className="bi bi-check-circle-fill fs-4"></i>
            <div>
              <strong>Chancellor's Merit Gold Award:</strong> Eligible based on CGPA 8.42 &gt;= 8.00 and zero backlogs. Approved fee waiver: Rs. 50,000 (50% Tuition Concession).
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Student360Portal;
