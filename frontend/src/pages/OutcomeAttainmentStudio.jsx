import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const OutcomeAttainmentStudio = () => {
  const [courseOutcome, setCourseOutcome] = useState('CO1');
  const [directScore, setDirectScore] = useState('');
  const [indirectScore, setIndirectScore] = useState('');
  const [attainmentResult, setAttainmentResult] = useState(null);

  const initialAttainments = [
    { id: 'ATN-001', course: 'CS303 Operating Systems', co: 'CO1', direct: 82.5, indirect: 78.0, integrated: 81.6, status: 'VERIFIED' },
    { id: 'ATN-002', course: 'EE502 Power Electronics', co: 'CO2', direct: 68.0, indirect: 72.0, integrated: 68.8, status: 'PENDING_AUDIT' }
  ];

  const columns = [
    { key: 'id', label: 'Attainment ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'course', label: 'Course Code & Name' },
    { key: 'co', label: 'CO reference' },
    { key: 'direct', label: 'Direct Attainment %' },
    { key: 'indirect', label: 'Indirect Attainment %' },
    { key: 'integrated', label: 'Integrated OBE Attainment %' },
    { key: 'status', label: 'Verification Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleAttainmentSimulate = (e) => {
    e.preventDefault();
    const dScore = parseFloat(directScore) || 0;
    const iScore = parseFloat(indirectScore) || 0;

    // Integrated attainment = direct * 0.8 + indirect * 0.2
    const integrated = dScore * 0.8 + iScore * 0.2;

    setAttainmentResult({
      co: courseOutcome,
      direct: dScore,
      indirect: iScore,
      integrated: integrated.toFixed(2),
      level: integrated >= 70.0 ? 'Level 3 (High)' : (integrated >= 60.0 ? 'Level 2 (Medium)' : (integrated >= 50.0 ? 'Level 1 (Low)' : 'Level 0 (Not Attained)'))
    });
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-graph-up-arrow me-2"></i>OBE Course Outcome Attainment Studio
          </h2>
          <p className="text-muted mb-0">
            Compute direct and indirect Course Outcome (CO) and Program Outcome (PO) attainment percentages based on university criteria weights.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-calculator me-2"></i>Attainment Compiler</h5>
            <form onSubmit={handleAttainmentSimulate}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Course Outcome Reference</label>
                <select className="form-select" value={courseOutcome} onChange={(e) => setCourseOutcome(e.target.value)}>
                  <option value="CO1">CO1: Remember & Understand Concepts</option>
                  <option value="CO2">CO2: Apply Mathematical Formulas</option>
                  <option value="CO3">CO3: Analyze System Performance</option>
                  <option value="CO4">CO4: Design & Synthesize Solutions</option>
                </select>
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Direct Attainment Percentage (Exams/Labs)</label>
                <input
                  type="number"
                  step="0.01"
                  className="form-control"
                  value={directScore}
                  onChange={(e) => setDirectScore(e.target.value)}
                  placeholder="e.g. 78.5"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Indirect Attainment Percentage (Surveys/Feedback)</label>
                <input
                  type="number"
                  step="0.01"
                  className="form-control"
                  value={indirectScore}
                  onChange={(e) => setIndirectScore(e.target.value)}
                  placeholder="e.g. 85.0"
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-gear-fill me-1"></i>Compile Integrated Attainment
              </button>
            </form>

            {attainmentResult && (
              <div className="mt-4 p-3 bg-light rounded-3 border-start border-primary border-4">
                <h6 className="fw-bold mb-2">Simulated OBE Attainment:</h6>
                <ul className="small mb-2 ps-3">
                  <li>Course Outcome: {attainmentResult.co}</li>
                  <li>Direct component contribution: {attainmentResult.direct}%</li>
                  <li>Indirect component contribution: {attainmentResult.indirect}%</li>
                </ul>
                <div className="fw-bold text-success border-top pt-2 mt-2">
                  Final Integrated Attainment: {attainmentResult.integrated}%
                </div>
                <div className="small text-muted">
                  NBA Attainment Level: {attainmentResult.level}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-list-check me-2"></i>Integrated Attainment Ledger</h5>
            <AdvancedDataTable columns={columns} data={initialAttainments} searchPlaceholder="Search ledger records..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default OutcomeAttainmentStudio;
