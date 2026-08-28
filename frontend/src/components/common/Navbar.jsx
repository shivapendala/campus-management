import React from 'react';
import { useAuth } from '../../context/AuthContext';
import { Link, useNavigate } from 'react-router-dom';
import { ROLE_BADGE_CLASSES, ROLE_LABELS } from '../../utils/constants';

export const Navbar = () => {
  const { user, role, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const badgeClass = ROLE_BADGE_CLASSES[role] || 'bg-primary text-white';
  const roleLabel = ROLE_LABELS[role] || role || 'User';

  return (
    <header className="navbar navbar-expand bg-white border-bottom px-4 py-2 sticky-top shadow-sm">
      <div className="container-fluid p-0 d-flex justify-content-between align-items-center">
        {/* Left: Term Indicator & Search shortcut */}
        <div className="d-flex align-items-center gap-3">
          <span className="badge bg-light text-secondary border px-3 py-2 small fw-semibold">
            <i className="bi bi-calendar-event me-1 text-primary"></i> Academic Term: Fall 2026
          </span>
          <span className="badge bg-success-subtle text-success small fw-semibold d-none d-md-inline-block">
            <i className="bi bi-circle-fill me-1" style={{ fontSize: '8px' }}></i> System Online
          </span>
        </div>

        {/* Right: User Profile & Actions */}
        <div className="d-flex align-items-center gap-3">
          {/* Quick Notifications Button */}
          <div className="dropdown">
            <button
              className="btn btn-light rounded-circle position-relative p-2"
              type="button"
              id="notifDropdown"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              aria-label="Notifications"
            >
              <i className="bi bi-bell-fill text-secondary"></i>
              <span className="position-absolute top-0 start-100 translate-middle p-1 bg-danger border border-light rounded-circle"></span>
            </button>
            <ul className="dropdown-menu dropdown-menu-end shadow border-0 mt-2 p-2" style={{ width: '280px' }}>
              <li className="dropdown-header fw-bold text-dark">Notifications</li>
              <li>
                <a className="dropdown-item small p-2 rounded" href="#!">
                  <div className="fw-semibold">Midterm Schedule Ready</div>
                  <small className="text-muted">Exam schedule published for CS-101</small>
                </a>
              </li>
              <li>
                <a className="dropdown-item small p-2 rounded" href="#!">
                  <div className="fw-semibold">Fee Receipt Generated</div>
                  <small className="text-muted">Invoice TXN-982347 marked paid</small>
                </a>
              </li>
            </ul>
          </div>

          {/* User Account Info */}
          <div className="d-flex align-items-center gap-2 border-start ps-3">
            <div
              className="rounded-circle bg-gradient-primary text-white d-flex align-items-center justify-content-center fw-bold shadow-sm"
              style={{ width: '38px', height: '38px' }}
            >
              {user?.first_name?.[0] || user?.username?.[0] || 'U'}
            </div>
            <div className="d-none d-sm-block text-start">
              <div className="fw-bold text-dark small leading-none mb-1">
                {user?.first_name ? `${user.first_name} ${user.last_name || ''}` : user?.username || 'Authenticated User'}
              </div>
              <span className={`badge ${badgeClass} text-uppercase`} style={{ fontSize: '10px' }}>
                {roleLabel}
              </span>
            </div>
            <button
              onClick={handleLogout}
              className="btn btn-outline-danger btn-sm ms-2 py-1 px-2"
              title="Sign Out"
            >
              <i className="bi bi-box-arrow-right"></i>
            </button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
