import React from 'react';
import { NavLink } from 'react-router-dom';

export const Sidebar = () => {
  return (
    <aside
      className="d-flex flex-column flex-shrink-0 p-3 text-white"
      style={{
        width: '260px',
        minHeight: '100vh',
        backgroundColor: '#0f172a',
        borderRight: '1px solid rgba(255, 255, 255, 0.08)',
      }}
    >
      <div className="d-flex align-items-center mb-4 px-2 pt-2">
        <div
          className="bg-gradient-primary rounded-3 d-flex align-items-center justify-content-center text-white me-3"
          style={{ width: '40px', height: '40px' }}
        >
          <i className="bi bi-mortarboard-fill fs-5"></i>
        </div>
        <div>
          <h5 className="mb-0 fw-bold tracking-tight text-white">EduCore</h5>
          <small className="text-muted" style={{ fontSize: '0.75rem' }}>
            Campus Management
          </small>
        </div>
      </div>

      <hr style={{ borderColor: 'rgba(255, 255, 255, 0.1)' }} />

      <div className="text-uppercase text-muted fw-bold px-3 my-2" style={{ fontSize: '0.7rem', letterSpacing: '0.08em' }}>
        Main Menu
      </div>

      <ul className="nav nav-pills flex-column mb-auto gap-1">
        <li className="nav-item">
          <NavLink
            to="/"
            end
            className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}
          >
            <i className="bi bi-grid-1x2-fill"></i>
            <span>Dashboard</span>
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink
            to="/students"
            className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}
          >
            <i className="bi bi-people-fill"></i>
            <span>Students</span>
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink
            to="/courses"
            className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}
          >
            <i className="bi bi-journal-bookmark-fill"></i>
            <span>Courses</span>
          </NavLink>
        </li>
        <li className="nav-item">
          <NavLink
            to="/faculty"
            className={({ isActive }) => `sidebar-link ${isActive ? 'active' : ''}`}
          >
            <i className="bi bi-person-workspace"></i>
            <span>Faculty</span>
          </NavLink>
        </li>
      </ul>

      <hr style={{ borderColor: 'rgba(255, 255, 255, 0.1)' }} />

      <div className="p-2 rounded-3" style={{ background: 'rgba(255, 255, 255, 0.04)' }}>
        <div className="d-flex align-items-center">
          <span className="badge bg-success me-2 p-1 px-2">v1.0</span>
          <span className="text-muted small">System Status: Active</span>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
