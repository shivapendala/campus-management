import React from 'react';

const StatusBadge = ({ status = 'ACTIVE', size = 'normal' }) => {
  const normalized = String(status || '').toUpperCase().trim();

  const getStyle = () => {
    switch (normalized) {
      case 'ACTIVE':
      case 'PRESENT':
      case 'PAID':
      case 'RESOLVED':
      case 'PLACED':
      case 'ACCEPTED':
      case 'EXEMPLARY':
      case 'OPTIMAL':
      case 'SATISFIED':
      case 'CLEARED':
      case 'FINALIZED':
        return { bg: 'bg-success-subtle', text: 'text-success', icon: 'bi-check-circle-fill' };

      case 'PENDING':
      case 'MODERATE':
      case 'REVIEW_REQUIRED':
      case 'UNDER_UTILIZED':
      case 'DEVELOPING':
      case 'APPLIED':
      case 'HALF_DAY':
        return { bg: 'bg-warning-subtle', text: 'text-warning-emphasis', icon: 'bi-hourglass-split' };

      case 'OVERDUE':
      case 'ABSENT':
      case 'CRITICAL':
      case 'HIGH':
      case 'DETAINED':
      case 'REJECTED':
      case 'DEFICIENT':
      case 'CONGESTED':
      case 'EXPELLED':
      case 'SUSPENDED':
        return { bg: 'bg-danger-subtle', text: 'text-danger', icon: 'bi-exclamation-octagon-fill' };

      case 'LATE':
      case 'CONDONATION_REQUIRED':
      case 'PROBATION':
        return { bg: 'bg-orange-subtle text-orange', text: 'text-dark', icon: 'bi-clock-history' };

      case 'GRADUATED':
      case 'ALUMNUS':
      case 'COMPLETED':
        return { bg: 'bg-primary-subtle', text: 'text-primary', icon: 'bi-mortarboard-fill' };

      default:
        return { bg: 'bg-secondary-subtle', text: 'text-secondary', icon: 'bi-info-circle-fill' };
    }
  };

  const style = getStyle();
  const paddingClass = size === 'small' ? 'px-2 py-0.5 small' : 'px-2.5 py-1';

  return (
    <span className={`badge ${style.bg} ${style.text} rounded-pill d-inline-flex align-items-center gap-1 ${paddingClass}`}>
      <i className={`bi ${style.icon}`}></i>
      <span>{normalized.replace(/_/g, ' ')}</span>
    </span>
  );
};

export default StatusBadge;
