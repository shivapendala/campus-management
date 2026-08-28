import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const ExamModerationConsole = () => {
  const [courseCode, setCourseCode] = useState('');
  const [rawMean, setRawMean] = useState('');
  const [rawStdDev, setRawStdDev] = useState('');
  const [moderationResult, setModerationResult] = useState(null);

  const initialModerationSchemes = [
    { id: 'MOD-001', course: 'MA101 Mathematics I', mean: 52.4, stdDev: 14.2, targetMean: 65.0, status: 'COMPLETED' },
    { id: 'MOD-002', course: 'CS302 Design & Analysis of Algorithms', mean: 45.8, stdDev: 18.5, targetMean: 62.0, status: 'PENDING_APPROVAL' }
  ];

  const columns = [
    { key: 'id', label: 'Scheme ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'course', label: 'Course Title' },
    { key: 'mean', label: 'Raw Class Mean' },
    { key: 'stdDev', label: 'Raw Std Dev' },
    { key: 'targetMean', label: 'Target Moderated Mean' },
    { key: 'status', label: 'Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleModerationSimulate = (e) => {
    e.preventDefault();
    const mean = parseFloat(rawMean) || 0;
    const sdev = parseFloat(rawStdDev) || 0;

    // Simulate shifts in grade distributions
    const shift = 65.0 - mean;
    const adjustedMean = mean + shift;
    
    setModerationResult({
      originalMean: mean,
      originalStdDev: sdev,
      moderatedMean: adjustedMean,
      moderatedStdDev: sdev * 0.95,
      shiftApplied: shift > 0 ? `+${shift.toFixed(2)} Points Linear Shift` : `${shift.toFixed(2)} Points Shift`
    });
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-bar-chart-steps me-2"></i>Examination Marks Moderation Console
          </h2>
          <p className="text-muted mb-0">
            Apply normal distribution curves, adjust difficulty weight offsets, and run statistical marks moderation templates.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-calculator me-2"></i>Gaussian Curve Simulator</h5>
            <form onSubmit={handleModerationSimulate}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Course Code / Title</label>
                <input
                  type="text"
                  className="form-control"
                  value={courseCode}
                  onChange={(e) => setCourseCode(e.target.value)}
                  placeholder="e.g. CS501"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Current Raw Class Mean</label>
                <input
                  type="number"
                  step="0.1"
                  className="form-control"
                  value={rawMean}
                  onChange={(e) => setRawMean(e.target.value)}
                  placeholder="e.g. 52.4"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Current Raw Std Dev</label>
                <input
                  type="number"
                  step="0.1"
                  className="form-control"
                  value={rawStdDev}
                  onChange={(e) => setRawStdDev(e.target.value)}
                  placeholder="e.g. 14.2"
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-calculator-fill me-1"></i>Simulate Marks Moderation
              </button>
            </form>

            {moderationResult && (
              <div className="mt-4 p-3 bg-light rounded-3 border-start border-primary border-4">
                <h6 className="fw-bold mb-2">Simulated Moderation Slabs:</h6>
                <ul className="small mb-2 ps-3">
                  <li>Original Mean: {moderationResult.originalMean}</li>
                  <li>Original Std Dev: {moderationResult.originalStdDev}</li>
                  <li>Moderated Mean: {moderationResult.moderatedMean}</li>
                  <li>Moderated Std Dev: {moderationResult.moderatedStdDev.toFixed(2)}</li>
                </ul>
                <div className="fw-bold text-success border-top pt-2 mt-2">
                  Shift Applied: {moderationResult.shiftApplied}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-file-earmark-check me-2"></i>Moderation Registers</h5>
            <AdvancedDataTable columns={columns} data={initialModerationSchemes} searchPlaceholder="Search schemes..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default ExamModerationConsole;
