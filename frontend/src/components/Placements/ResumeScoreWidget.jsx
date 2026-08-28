import React from 'react';

const ResumeScoreWidget = ({ score = 88, matched = [], missing = [] }) => {
  return (
    <div className="card border-0 shadow-sm p-3">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h6 className="fw-bold mb-0 text-dark">
          <i className="bi bi-file-earmark-code me-2 text-primary"></i>ATS Keyword Matcher
        </h6>
        <span className="badge bg-success fs-6">{score}% Match</span>
      </div>

      <div className="mb-3">
        <label className="small text-muted fw-semibold mb-1">Matched Keywords ({matched.length})</label>
        <div className="d-flex flex-wrap gap-1">
          {matched.map((kw, idx) => (
            <span key={idx} className="badge bg-success-subtle text-success small">{kw}</span>
          ))}
        </div>
      </div>

      <div>
        <label className="small text-muted fw-semibold mb-1">Recommended Skill Additions ({missing.length})</label>
        <div className="d-flex flex-wrap gap-1">
          {missing.map((kw, idx) => (
            <span key={idx} className="badge bg-warning-subtle text-dark small">+{kw}</span>
          ))}
        </div>
      </div>
    </div>
  );
};

export default ResumeScoreWidget;
