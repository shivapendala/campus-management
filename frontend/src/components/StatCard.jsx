import React from 'react';

export const StatCard = ({ title, value, change, isPositive, icon, gradientClass }) => {
  return (
    <div className="campus-card campus-card-interactive p-4 h-100">
      <div className="d-flex align-items-center justify-content-between">
        <div>
          <span className="text-uppercase fw-semibold text-secondary small d-block mb-1">
            {title}
          </span>
          <h3 className="fw-bold mb-1 text-dark">{value}</h3>
          {change && (
            <span className={`small fw-medium ${isPositive ? 'text-success' : 'text-danger'}`}>
              <i className={`bi ${isPositive ? 'bi-arrow-up-short' : 'bi-arrow-down-short'} fs-6`}></i>
              {change}
            </span>
          )}
        </div>
        <div className={`stat-icon-wrapper text-white ${gradientClass || 'bg-gradient-primary'}`}>
          <i className={`bi ${icon || 'bi-bar-chart'}`}></i>
        </div>
      </div>
    </div>
  );
};

export default StatCard;
