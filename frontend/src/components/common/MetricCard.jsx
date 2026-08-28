import React from 'react';

const MetricCard = ({
  title,
  value,
  icon = 'bi-activity',
  variant = 'primary',
  subtitle = '',
  delta = '',
  deltaType = 'positive', // 'positive', 'negative', 'neutral'
  onClick = null
}) => {
  const getBadgeClass = () => {
    if (deltaType === 'positive') return 'bg-success-subtle text-success';
    if (deltaType === 'negative') return 'bg-danger-subtle text-danger';
    return 'bg-secondary-subtle text-secondary';
  };

  return (
    <div
      className={`card border-0 shadow-sm rounded-3 p-3 h-100 metric-card transition-all ${
        onClick ? 'cursor-pointer' : ''
      }`}
      onClick={onClick}
      style={{ borderLeft: `4px solid var(--bs-${variant})` }}
    >
      <div className="d-flex justify-content-between align-items-start mb-2">
        <span className="text-muted small fw-medium text-uppercase">{title}</span>
        <div
          className={`rounded-circle d-flex align-items-center justify-content-center bg-${variant}-subtle text-${variant}`}
          style={{ width: '38px', height: '38px' }}
        >
          <i className={`bi ${icon} fs-5`}></i>
        </div>
      </div>

      <div className="d-flex align-items-baseline gap-2 mb-1">
        <h3 className="fw-bold mb-0 text-dark">{value}</h3>
        {delta && (
          <span className={`badge ${getBadgeClass()} rounded-pill px-2 py-1 small`}>
            {delta}
          </span>
        )}
      </div>

      {subtitle && <p className="text-muted small mb-0">{subtitle}</p>}
    </div>
  );
};

export default MetricCard;
