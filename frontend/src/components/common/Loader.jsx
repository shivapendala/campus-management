import React from 'react';

export const Loader = ({
  fullScreen = false,
  message = 'Loading data...',
  size = 'md', // sm, md, lg
}) => {
  const spinnerSize = size === 'sm' ? 'spinner-border-sm' : size === 'lg' ? 'style={{ width: "3rem", height: "3rem" }}' : '';

  if (fullScreen) {
    return (
      <div
        className="d-flex flex-column align-items-center justify-content-center min-vh-100 position-fixed top-0 start-0 w-100 bg-white"
        style={{ zIndex: 99999, opacity: 0.95 }}
      >
        <div className="spinner-border text-primary mb-3" style={{ width: '3.5rem', height: '3.5rem' }} role="status">
          <span className="visually-hidden">Loading...</span>
        </div>
        <h6 className="fw-semibold text-dark mb-0">{message}</h6>
      </div>
    );
  }

  return (
    <div className="d-flex flex-column align-items-center justify-content-center py-5 text-center">
      <div className={`spinner-border text-primary mb-2 ${spinnerSize}`} role="status">
        <span className="visually-hidden">Loading...</span>
      </div>
      {message && <small className="text-muted fw-medium">{message}</small>}
    </div>
  );
};

export default Loader;
