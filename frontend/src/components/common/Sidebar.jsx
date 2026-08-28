import React from 'react';
import { NavLink } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';

export const Sidebar = () => {
  const { role } = useAuth();

  const navItems = [
    { to: '/', icon: 'bi-grid-1x2-fill', label: 'Dashboard' },
    { to: '/departments', icon: 'bi-buildings-fill', label: 'Departments' },
    { to: '/students', icon: 'bi-people-fill', label: 'Students' },
    { to: '/courses', icon: 'bi-journal-bookmark-fill', label: 'Courses & Catalog' },
    { to: '/faculty', icon: 'bi-person-workspace', label: 'Faculty Directory' },
  ];

  return (
    <aside
      className="d-flex flex-column flex-shrink-0 p-3 text-white border-end shadow-sm"
      style={{
        width: '260px',
        backgroundColor: '#0f172a',
        minHeight: '100vh',
      }}
    >
      {/* Brand Header */}
      <div className="d-flex align-items-center gap-2 mb-4 px-2 py-1">
        <div
          className="bg-primary rounded-3 d-flex align-items-center justify-content-center text-white shadow"
          style={{ width: '40px', height: '40px' }}
        >
          <i className="bi bi-mortarboard-fill fs-5"></i>
        </div>
        <div>
          <h5 className="fw-bold mb-0 text-white leading-tight">EduCore</h5>
          <small className="text-secondary" style={{ fontSize: '11px' }}>Campus Management</small>
        </div>
      </div>

      {/* Navigation Links */}
      <ul className="nav nav-pills flex-column mb-auto gap-1">
        <li className="nav-item">
          <small className="text-uppercase text-secondary fw-bold px-3 py-1 d-block" style={{ fontSize: '10px' }}>
            Main Menu
          </small>
        </li>
        {navItems.map((item) => (
          <li key={item.to} className="nav-item">
            <NavLink
              to={item.to}
              end={item.to === '/'}
              className={({ isActive }) =>
                `nav-link d-flex align-items-center gap-3 py-2 px-3 rounded-3 text-decoration-none fw-medium transition-all ${
                  isActive
                    ? 'bg-primary text-white shadow-sm'
                    : 'text-light opacity-75 hover-opacity-100 hover-bg-slate'
                }`
              }
            >
              <i className={`bi ${item.icon} fs-5`}></i>
              <span>{item.label}</span>
            </NavLink>
          </li>
        ))}

        <li className="nav-item mt-3">
          <small className="text-uppercase text-secondary fw-bold px-3 py-1 d-block" style={{ fontSize: '10px' }}>
            Campus Modules
          </small>
        </li>
        <li className="nav-item">
          <span className="nav-link text-light opacity-50 d-flex align-items-center gap-3 py-2 px-3">
            <i className="bi bi-calendar-check fs-5"></i>
            <span>Attendance (Live)</span>
          </span>
        </li>
        <li className="nav-item">
          <span className="nav-link text-light opacity-50 d-flex align-items-center gap-3 py-2 px-3">
            <i className="bi bi-cash-stack fs-5"></i>
            <span>Fee Collections</span>
          </span>
        </li>
        <li className="nav-item">
          <span className="nav-link text-light opacity-50 d-flex align-items-center gap-3 py-2 px-3">
            <i className="bi bi-book-half fs-5"></i>
            <span>Library System</span>
          </span>
        </li>
        <li className="nav-item">
          <span className="nav-link text-light opacity-50 d-flex align-items-center gap-3 py-2 px-3">
            <i className="bi bi-briefcase-fill fs-5"></i>
            <span>Placements</span>
          </span>
        </li>
      </ul>

      {/* Footer / Version Badge */}
      <div className="mt-auto pt-3 border-top border-secondary border-opacity-25 px-2">
        <div className="d-flex justify-content-between align-items-center text-secondary small">
          <span>EduCore Portal</span>
          <span className="badge bg-secondary bg-opacity-25 text-light">v2.0.0</span>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
