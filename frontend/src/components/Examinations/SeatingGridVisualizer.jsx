import React from 'react';

const SeatingGridVisualizer = ({ hallName = 'LH-101', desks = [] }) => {
  return (
    <div className="seating-grid-card card border-0 shadow-sm p-4 bg-light">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h6 className="fw-bold mb-0 text-dark">
          <i className="bi bi-grid-3x3-gap-fill me-2 text-primary"></i>Desk Grid - {hallName}
        </h6>
        <span className="badge bg-primary-subtle text-primary">Interleaved Branch Pattern</span>
      </div>

      <div className="podium-banner text-center py-2 bg-white rounded border fw-bold text-muted small mb-4">
        --- BLACKBOARD / INVIGILATION DESK ---
      </div>

      <div className="row g-2">
        {desks.map((desk, idx) => (
          <div key={idx} className="col-3">
            <div className="card p-2 text-center border shadow-xs bg-white h-100">
              <span className="badge bg-light text-dark mb-1">{desk.code}</span>
              <div className="fw-bold small text-primary">{desk.roll}</div>
              <span className="badge bg-secondary-subtle text-secondary small">{desk.dept}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SeatingGridVisualizer;
