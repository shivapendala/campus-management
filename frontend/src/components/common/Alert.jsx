import React from 'react';

export const Alert = ({
  type = 'info', // success, danger, warning, info
  message,
  onClose = null,
  dismissible = false,
  icon = true,
  className = '',
}) => {
  if (!message) return null;

  const iconMap = {
    success: 'bi-check-circle-fill',
    danger: 'bi-exclamation-triangle-fill',
    warning: 'bi-exclamation-circle-fill',
    info: 'bi-info-circle-fill',
  };

  return (
    <div
      className={`alert alert-${type} ${dismissible || onClose ? 'alert-dismissible fade show' : ''} d-flex align-items-center gap-2 small py-2 px-3 mb-3 ${className}`}
      role="alert"
    >
      {icon && <i className={`bi ${iconMap[type] || 'bi-info-circle-fill'} fs-5 flex-shrink-0`}></i>}
      <div className="flex-grow-1">{message}</div>
      {(dismissible || onClose) && (
        <button
          type="button"
          className="btn-close"
          aria-label="Close"
          onClick={onClose}
        ></button>
      )}
    </div>
  );
};

export default Alert;
