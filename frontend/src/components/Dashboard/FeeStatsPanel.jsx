import React from 'react';
import FeeCollectionBarChart from '../Charts/FeeCollectionBarChart';

export const FeeStatsPanel = () => {
  return (
    <div className="campus-card p-4 h-100 shadow-sm border-0">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <h5 className="fw-bold text-dark mb-1">
            <i className="bi bi-cash-stack text-success me-2"></i>
            Fee Collections & Dues
          </h5>
          <p className="text-muted small mb-0">Fall 2026 tuition and departmental invoicing</p>
        </div>
        <div className="text-end">
          <span className="badge bg-primary text-white fw-bold px-3 py-1">
            85.3% Collected
          </span>
          <small className="text-muted d-block" style={{ fontSize: '11px' }}>$1.85M of $2.17M</small>
        </div>
      </div>

      <FeeCollectionBarChart />

      <div className="row g-2 mt-3 pt-3 border-top">
        <div className="col-6">
          <div className="p-2 bg-light rounded-3 text-center">
            <small className="text-muted d-block">Pending Dues Volume</small>
            <strong className="text-danger fs-6">$320,000.00</strong>
          </div>
        </div>
        <div className="col-6">
          <div className="p-2 bg-light rounded-3 text-center">
            <small className="text-muted d-block">Pending Students</small>
            <strong className="text-warning fs-6">320 Invoices</strong>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FeeStatsPanel;
