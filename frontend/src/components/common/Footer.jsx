import React from 'react';

export const Footer = () => {
  return (
    <footer className="footer bg-white border-top py-3 px-4 mt-auto">
      <div className="container-fluid p-0 d-flex flex-column flex-sm-row justify-content-between align-items-center gap-2 text-muted small">
        <div>
          © 2026 <strong>EduCore Campus Management System</strong>. All rights reserved.
        </div>
        <div className="d-flex align-items-center gap-3">
          <span>Version 2.0.0</span>
          <span>•</span>
          <span>PostgreSQL 16 & Django REST</span>
          <span>•</span>
          <span className="text-success fw-medium">
            <i className="bi bi-shield-check me-1"></i> JWT Secured
          </span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
