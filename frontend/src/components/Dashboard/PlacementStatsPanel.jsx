import React from 'react';
import PlacementPieChart from '../Charts/PlacementPieChart';

export const PlacementStatsPanel = () => {
  return (
    <div className="campus-card p-4 h-100 shadow-sm border-0">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <h5 className="fw-bold text-dark mb-1">
            <i className="bi bi-briefcase-fill text-warning me-2"></i>
            Placement Statistics
          </h5>
          <p className="text-muted small mb-0">Graduating cohort employment & package breakdown</p>
        </div>
        <span className="badge bg-warning text-dark fw-bold px-3 py-1">
          145 Placed
        </span>
      </div>

      <PlacementPieChart />

      <div className="row g-2 mt-3 pt-3 border-top text-center">
        <div className="col-4">
          <small className="text-muted d-block">Average CTC</small>
          <strong className="text-primary fs-6">18.5 LPA</strong>
        </div>
        <div className="col-4">
          <small className="text-muted d-block">Highest CTC</small>
          <strong className="text-success fs-6">45.0 LPA</strong>
        </div>
        <div className="col-4">
          <small className="text-muted d-block">Top Partners</small>
          <strong className="text-dark fs-6">36 Companies</strong>
        </div>
      </div>
    </div>
  );
};

export default PlacementStatsPanel;
