import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const FacultyPortal = () => {
  const [activeTab, setActiveTab] = useState('appraisal');
  const [selectedFaculty, setSelectedFaculty] = useState({
    id: 1,
    employee_code: 'FAC-CSE-001',
    name: 'Dr. Rajesh Raman',
    designation: 'Professor & Dean',
    department: 'Computer Science & Engineering',
    h_index: 12,
    total_publications: 28,
    total_citations: 450,
    weekly_hours_target: 14,
    weekly_hours_actual: 14.5,
    api_score_total: 248.5,
  });

  const publicationsData = [
    { title: 'Deep Learning for Edge AI in Smart Cities', journal: 'IEEE Transactions on Smart Grid', indexing: 'SCI', year: 2026, citations: 42, impact_factor: 7.8 },
    { title: 'Blockchain Consensus in Higher Education Records', journal: 'ACM Computing Surveys', indexing: 'SCOPUS', year: 2025, citations: 68, impact_factor: 10.2 },
    { title: 'Adaptive Timetable Graph Color Scheduling', journal: 'Journal of Systems and Software', indexing: 'SCI', year: 2024, citations: 29, impact_factor: 4.1 },
  ];

  const pubColumns = [
    { key: 'title', label: 'Paper Title' },
    { key: 'journal', label: 'Journal / Publisher' },
    { key: 'indexing', label: 'Indexing', render: (val) => <span className="badge bg-primary-subtle text-primary">{val}</span> },
    { key: 'impact_factor', label: 'Impact Factor', render: (val) => <span className="fw-bold">{val}</span> },
    { key: 'citations', label: 'Citations', render: (val) => <span className="fw-bold text-success">{val}</span> },
    { key: 'year', label: 'Year' },
  ];

  return (
    <div className="container-fluid py-4">
      {/* Header */}
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-person-workspace me-2"></i>Faculty Research & Performance Studio
          </h2>
          <p className="text-muted mb-0">
            PBAS annual performance appraisal, AICTE workload compliance, Scopus research ledger, and sponsored grant tracking.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-plus me-1"></i>Add Publication
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-award me-1"></i>Generate PBAS Dossier
          </button>
        </div>
      </div>

      {/* Metric Cards Row */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Annual PBAS API Score"
            value={`${selectedFaculty.api_score_total}/300`}
            icon="bi-trophy-fill"
            variant="success"
            subtitle="Qualifies for CAS Promotion (Band: Outstanding)"
            delta="Eligible"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Research H-Index"
            value={selectedFaculty.h_index}
            icon="bi-journal-code"
            variant="primary"
            subtitle="Scopus / Web of Science Index"
            delta="High Impact"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Citations"
            value={selectedFaculty.total_citations}
            icon="bi-quote"
            variant="info"
            subtitle="Across 28 Peer-Reviewed Works"
            delta="+85 this year"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Teaching Load Balance"
            value={`${selectedFaculty.weekly_hours_actual} hrs/wk`}
            icon="bi-clock-history"
            variant="warning"
            subtitle={`Target: ${selectedFaculty.weekly_hours_target} hrs (AICTE Statues)`}
            delta="Optimal"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Tabs */}
      <ul className="nav nav-pills mb-4 gap-2 border-bottom pb-3">
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'appraisal' ? 'active' : ''}`}
            onClick={() => setActiveTab('appraisal')}
          >
            <i className="bi bi-award me-1"></i>PBAS Annual Appraisal (API Breakdown)
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${activeTab === 'publications' ? 'active' : ''}`}
            onClick={() => setActiveTab('publications')}
          >
            <i className="bi bi-book me-1"></i>Scopus / SCI Research Publications
          </button>
        </li>
      </ul>

      {/* TAB CONTENT: Appraisal */}
      {activeTab === 'appraisal' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-3">
            <i className="bi bi-calculator me-2 text-primary"></i>UGC Academic Performance Indicator (API) Score Sheet
          </h5>
          <div className="table-responsive">
            <table className="table table-hover align-middle">
              <thead className="table-light">
                <tr>
                  <th>Category</th>
                  <th>Domain</th>
                  <th>Max Weightage</th>
                  <th>Attained Score</th>
                  <th>Attainment %</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td className="fw-bold text-primary">Category I</td>
                  <td>Teaching, Learning and Evaluation (Syllabus Coverage + Student Feedback 4.8/5)</td>
                  <td>100</td>
                  <td className="fw-bold">96.0</td>
                  <td>
                    <div className="progress" style={{ height: '6px' }}><div className="progress-bar bg-success" style={{ width: '96%' }}></div></div>
                  </td>
                  <td><StatusBadge status="EXEMPLARY" size="small" /></td>
                </tr>
                <tr>
                  <td className="fw-bold text-primary">Category II</td>
                  <td>Co-Curricular, Governance & Professional Development (IQAC Convener, FDP 10 Days)</td>
                  <td>50</td>
                  <td className="fw-bold">47.5</td>
                  <td>
                    <div className="progress" style={{ height: '6px' }}><div className="progress-bar bg-success" style={{ width: '95%' }}></div></div>
                  </td>
                  <td><StatusBadge status="OPTIMAL" size="small" /></td>
                </tr>
                <tr>
                  <td className="fw-bold text-primary">Category III</td>
                  <td>Research and Academic Contributions (3 SCI Papers, Rs. 45L DST Grant, 2 PhDs)</td>
                  <td>150</td>
                  <td className="fw-bold">105.0</td>
                  <td>
                    <div className="progress" style={{ height: '6px' }}><div className="progress-bar bg-primary" style={{ width: '70%' }}></div></div>
                  </td>
                  <td><StatusBadge status="ACTIVE" size="small" /></td>
                </tr>
                <tr className="table-light fw-bold">
                  <td colSpan="2">Total Composite API Score</td>
                  <td>300</td>
                  <td className="text-success h5 mb-0">248.5</td>
                  <td colSpan="2">
                    <span className="badge bg-success fs-6">Outstanding (Promotable)</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB CONTENT: Publications */}
      {activeTab === 'publications' && (
        <div className="card border-0 shadow-sm rounded-3 p-4">
          <h5 className="fw-bold mb-3">
            <i className="bi bi-journals me-2 text-primary"></i>Indexed Journal & Conference Papers
          </h5>
          <AdvancedDataTable
            columns={pubColumns}
            data={publicationsData}
            searchPlaceholder="Search papers by title or journal..."
          />
        </div>
      )}
    </div>
  );
};

export default FacultyPortal;
