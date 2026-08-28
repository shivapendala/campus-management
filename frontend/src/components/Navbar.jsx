import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

export const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <header className="top-navbar d-flex align-items-center justify-content-between px-4 sticky-top">
      <div className="d-flex align-items-center gap-3">
        <div className="input-group" style={{ maxWidth: '320px' }}>
          <span className="input-group-text bg-light border-end-0 text-muted">
            <i className="bi bi-search"></i>
          </span>
          <input
            type="text"
            className="form-control bg-light border-start-0"
            placeholder="Search students, courses, faculty..."
            style={{ fontSize: '0.875rem' }}
          />
        </div>
      </div>

      <div className="d-flex align-items-center gap-3">
        <div className="d-flex align-items-center gap-2">
          <button className="btn btn-light rounded-circle position-relative p-2" title="Notifications">
            <i className="bi bi-bell text-secondary"></i>
            <span className="position-absolute top-0 start-100 translate-middle p-1 bg-danger border border-light rounded-circle">
              <span className="visually-hidden">New alerts</span>
            </span>
          </button>
        </div>

        <div className="vr h-50 mx-2 text-muted"></div>

        {user ? (
          <div className="dropdown">
            <button
              className="btn d-flex align-items-center gap-2 p-1 border-0"
              type="button"
              id="userMenuDropdown"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <div
                className="bg-gradient-primary rounded-circle d-flex align-items-center justify-content-center text-white fw-bold"
                style={{ width: '36px', height: '36px', fontSize: '0.85rem' }}
              >
                {user.first_name ? user.first_name[0] : (user.username ? user.username[0].toUpperCase() : 'U')}
              </div>
              <div className="text-start d-none d-md-block">
                <span className="d-block fw-semibold small text-dark leading-tight">
                  {user.first_name ? `${user.first_name} ${user.last_name}` : user.username}
                </span>
                <span className="badge bg-light text-primary border" style={{ fontSize: '0.68rem' }}>
                  {user.role || 'Admin'}
                </span>
              </div>
            </button>
            <ul className="dropdown-menu dropdown-menu-end shadow border-0 mt-2" aria-labelledby="userMenuDropdown">
              <li>
                <h6 className="dropdown-header">Signed in as {user.email || user.username}</h6>
              </li>
              <li><hr className="dropdown-divider" /></li>
              <li>
                <button className="dropdown-item text-danger d-flex align-items-center gap-2" onClick={handleLogout}>
                  <i className="bi bi-box-arrow-right"></i> Sign Out
                </button>
              </li>
            </ul>
          </div>
        ) : (
          <button className="btn btn-primary btn-sm px-3" onClick={() => navigate('/login')}>
            Sign In
          </button>
        )}
      </div>
    </header>
  );
};

export default Navbar;
