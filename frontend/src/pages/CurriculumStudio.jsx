import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const CurriculumStudio = () => {
  const [selectedCourse, setSelectedCourse] = useState('CS301');

  const benchmarkSyllabus = {
    course_code: 'CS301',
    course_title: 'Database Management Systems',
    regulation: 'R23 Autonomous',
    credits: 4,
    units: [
      { unit: 1, title: 'Database Architecture & ER Modeling', hours: 9, blooms: 'L1/L2', co: 'CO1' },
      { unit: 2, title: 'Relational Model, Algebra & Advanced SQL', hours: 9, blooms: 'L2/L3', co: 'CO2' },
      { unit: 3, title: 'Normalization & Schema Refinement (1NF to BCNF)', hours: 9, blooms: 'L3/L4', co: 'CO3' },
      { unit: 4, title: 'Transaction Processing, ACID & Concurrency (2PL)', hours: 9, blooms: 'L3/L4', co: 'CO4' },
      { unit: 5, title: 'B+ Tree Indexing & NoSQL Storage Foundations', hours: 9, blooms: 'L4/L5', co: 'CO5' },
    ],
  };

  const coPoMatrix = [
    { co: 'CO1', desc: 'Understand DBMS architecture and ER modeling concepts', po1: 3, po2: 2, po3: 1, po4: 0, po5: 2, pso1: 3 },
    { co: 'CO2', desc: 'Formulate relational algebra expressions and complex SQL queries', po1: 3, po2: 3, po3: 3, po4: 2, po5: 3, pso1: 3 },
    { co: 'CO3', desc: 'Apply schema normalization principles up to BCNF', po1: 3, po2: 3, po3: 3, po4: 2, po5: 2, pso1: 3 },
    { co: 'CO4', desc: 'Analyze ACID transactions and concurrency control mechanisms', po1: 3, po2: 2, po3: 2, po4: 1, po5: 2, pso1: 2 },
    { co: 'CO5', desc: 'Evaluate B+ tree indexing structures and NoSQL architectures', po1: 3, po2: 3, po3: 2, po4: 2, po5: 3, pso1: 3 },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-diagram-3-fill me-2"></i>Curriculum Studio & OBE Outcome Mapper
          </h2>
          <p className="text-muted mb-0">
            5-Unit Syllabus structures, Course Outcome to Program Outcome (CO-PO) attainment matrices, and prerequisite DAG graphs.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-diff me-1"></i>Curriculum Version Compare
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-download me-1"></i>Export NBA Course File (PDF)
          </button>
        </div>
      </div>

      {/* Benchmark Course Selector */}
      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4">
        <div className="d-flex justify-content-between align-items-center flex-wrap gap-3">
          <div>
            <span className="badge bg-primary px-3 py-1 mb-2">Selected Course</span>
            <h4 className="fw-bold mb-0">
              {benchmarkSyllabus.course_code}: {benchmarkSyllabus.course_title}
            </h4>
            <small className="text-muted">
              Regulation: <strong>{benchmarkSyllabus.regulation}</strong> | Total Contact Hours: <strong>45 hrs</strong> | Credits: <strong>{benchmarkSyllabus.credits}</strong>
            </small>
          </div>
          <div className="d-flex gap-2">
            <select
              className="form-select"
              value={selectedCourse}
              onChange={(e) => setSelectedCourse(e.target.value)}
            >
              <option value="CS301">CS301: Database Management Systems</option>
              <option value="CS201">CS201: Data Structures & Algorithms</option>
              <option value="CS401">CS401: Operating Systems</option>
              <option value="CS501">CS501: Computer Networks</option>
              <option value="CS601">CS601: Machine Learning</option>
            </select>
          </div>
        </div>
      </div>

      {/* 5-Unit Syllabus View */}
      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-list-ol me-2 text-primary"></i>5-Unit Syllabus Breakdown
        </h5>
        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>Unit</th>
                <th>Unit Title & Topics</th>
                <th>Lecture Hours</th>
                <th>Bloom's Taxonomy</th>
                <th>Mapped CO</th>
              </tr>
            </thead>
            <tbody>
              {benchmarkSyllabus.units.map((u, idx) => (
                <tr key={idx}>
                  <td className="fw-bold text-primary">Unit {u.unit}</td>
                  <td className="fw-semibold">{u.title}</td>
                  <td>{u.hours} Hours</td>
                  <td><span className="badge bg-info-subtle text-info">{u.blooms}</span></td>
                  <td><span className="badge bg-success-subtle text-success">{u.co}</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* NBA CO-PO Correlation Matrix */}
      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3 text-dark">
          <i className="bi bi-grid-3x3 me-2 text-primary"></i>Outcome-Based Education (OBE) CO-PO Correlation Matrix
        </h5>
        <p className="text-muted small mb-3">
          Correlation Levels: <strong>3</strong> (Substantial / High), <strong>2</strong> (Moderate / Medium), <strong>1</strong> (Slight / Low), <strong>-</strong> (No Correlation).
        </p>

        <div className="table-responsive">
          <table className="table table-bordered text-center align-middle">
            <thead className="table-light">
              <tr>
                <th className="text-start" style={{ width: '80px' }}>CO</th>
                <th className="text-start" style={{ minWidth: '280px' }}>Course Outcome Statement</th>
                <th>PO1 (Engineering Knowledge)</th>
                <th>PO2 (Problem Analysis)</th>
                <th>PO3 (Design Solutions)</th>
                <th>PO4 (Conduct Investigations)</th>
                <th>PO5 (Modern Tools)</th>
                <th>PSO1 (Software Dev)</th>
              </tr>
            </thead>
            <tbody>
              {coPoMatrix.map((row, idx) => (
                <tr key={idx}>
                  <td className="fw-bold text-primary text-start">{row.co}</td>
                  <td className="text-start small">{row.desc}</td>
                  <td><span className="badge bg-primary">{row.po1}</span></td>
                  <td><span className="badge bg-primary">{row.po2}</span></td>
                  <td><span className="badge bg-primary">{row.po3}</span></td>
                  <td>{row.po4 > 0 ? <span className="badge bg-primary-subtle text-primary">{row.po4}</span> : '-'}</td>
                  <td><span className="badge bg-primary">{row.po5}</span></td>
                  <td><span className="badge bg-success">{row.pso1}</span></td>
                </tr>
              ))}
              <tr className="table-light fw-bold">
                <td colSpan="2" className="text-start">Average Attainment Level</td>
                <td>3.0</td>
                <td>2.6</td>
                <td>2.2</td>
                <td>1.4</td>
                <td>2.4</td>
                <td>2.8</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default CurriculumStudio;
