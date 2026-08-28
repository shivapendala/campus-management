import React from 'react';

const ResearchProfileCard = ({ hIndex = 12, citations = 450, publicationsCount = 28 }) => {
  return (
    <div className="card border-0 shadow-sm p-3 bg-white">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h6 className="fw-bold mb-0 text-dark">
          <i className="bi bi-mortarboard-fill me-2 text-primary"></i>Research & Scholarly Profile
        </h6>
        <span className="badge bg-primary">Scopus Indexed</span>
      </div>

      <div className="row g-2 text-center">
        <div className="col-4">
          <div className="p-2 bg-light rounded">
            <span className="text-muted small d-block">h-index</span>
            <strong className="h5 text-primary mb-0">{hIndex}</strong>
          </div>
        </div>
        <div className="col-4">
          <div className="p-2 bg-light rounded">
            <span className="text-muted small d-block">Citations</span>
            <strong className="h5 text-success mb-0">{citations}</strong>
          </div>
        </div>
        <div className="col-4">
          <div className="p-2 bg-light rounded">
            <span className="text-muted small d-block">Papers</span>
            <strong className="h5 text-dark mb-0">{publicationsCount}</strong>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResearchProfileCard;
