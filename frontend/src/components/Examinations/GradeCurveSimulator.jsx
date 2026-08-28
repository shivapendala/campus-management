import React, { useState } from 'react';

const GradeCurveSimulator = ({ mean = 68.4, stdDev = 12.2 }) => {
  const [curveType, setCurveType] = useState('GAUSSIAN_RELATIVE');

  const gradeCutoffs = [
    { grade: 'O', pt: 10, range: `>= ${(mean + 1.5 * stdDev).toFixed(1)} marks (Top ~7%)` },
    { grade: 'A+', pt: 9, range: `${(mean + 1.0 * stdDev).toFixed(1)} - ${(mean + 1.5 * stdDev).toFixed(1)} marks` },
    { grade: 'A', pt: 8, range: `${(mean + 0.5 * stdDev).toFixed(1)} - ${(mean + 1.0 * stdDev).toFixed(1)} marks` },
    { grade: 'B+', pt: 7, range: `${mean.toFixed(1)} - ${(mean + 0.5 * stdDev).toFixed(1)} marks` },
    { grade: 'B', pt: 6, range: `${(mean - 0.5 * stdDev).toFixed(1)} - ${mean.toFixed(1)} marks` },
    { grade: 'C', pt: 5, range: `${(mean - 1.5 * stdDev).toFixed(1)} - ${(mean - 0.5 * stdDev).toFixed(1)} marks` },
    { grade: 'F', pt: 0, range: `< ${(mean - 1.5 * stdDev).toFixed(1)} marks (Fail / Remedial)` },
  ];

  return (
    <div className="card border-0 shadow-sm p-4">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h6 className="fw-bold mb-0 text-dark">
          <i className="bi bi-graph-up me-2 text-primary"></i>Gaussian Grading Curve Normalizer
        </h6>
        <div className="btn-group btn-group-sm">
          <button
            className={`btn ${curveType === 'GAUSSIAN_RELATIVE' ? 'btn-primary' : 'btn-outline-primary'}`}
            onClick={() => setCurveType('GAUSSIAN_RELATIVE')}
          >
            Relative (Gaussian)
          </button>
          <button
            className={`btn ${curveType === 'ABSOLUTE' ? 'btn-primary' : 'btn-outline-primary'}`}
            onClick={() => setCurveType('ABSOLUTE')}
          >
            Absolute Scale
          </button>
        </div>
      </div>

      <div className="row g-2 mb-3">
        <div className="col-6">
          <div className="p-2 bg-light rounded text-center small">
            <span className="text-muted">Cohort Mean (&mu;): </span>
            <strong>{mean}</strong>
          </div>
        </div>
        <div className="col-6">
          <div className="p-2 bg-light rounded text-center small">
            <span className="text-muted">Standard Dev (&sigma;): </span>
            <strong>{stdDev}</strong>
          </div>
        </div>
      </div>

      <div className="table-responsive">
        <table className="table table-sm table-hover align-middle mb-0">
          <thead className="table-light">
            <tr>
              <th>Letter Grade</th>
              <th>Grade Point</th>
              <th>Score Cutoff Window</th>
            </tr>
          </thead>
          <tbody>
            {gradeCutoffs.map((g, idx) => (
              <tr key={idx}>
                <td className="fw-bold text-primary">{g.grade}</td>
                <td>{g.pt} / 10</td>
                <td className="small text-muted">{g.range}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default GradeCurveSimulator;
