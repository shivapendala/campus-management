import React from 'react';
import AttendanceBarChart from '../Charts/AttendanceBarChart';

export const AttendanceStatsPanel = () => {
  return (
    <div className="campus-card p-4 h-100 shadow-sm border-0">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <h5 className="fw-bold text-dark mb-1">
            <i className="bi bi-calendar-check-fill text-primary me-2"></i>
            Campus Attendance Statistics
          </h5>
          <p className="text-muted small mb-0">Live daily session attendance by academic department</p>
        </div>
        <div className="text-end">
          <span className="badge bg-success-subtle text-success fs-6 fw-bold px-3 py-1">
            94.2% Avg
          </span>
          <small className="text-muted d-block" style={{ fontSize: '11px' }}>Institutional Rate</small>
        </div>
      </div>

      <AttendanceBarChart />

      <div className="row g-2 mt-3 pt-3 border-top text-center">
        <div className="col-4">
          <span className="text-muted small d-block">Today's Lectures</span>
          <strong className="text-dark fs-6">142 Sessions</strong>
        </div>
        <div className="col-4">
          <span className="text-muted small d-block">Present Count</span>
          <strong className="text-success fs-6">2,308 Students</strong>
        </div>
        <div className="col-4">
          <span className="text-muted small d-block">At-Risk (&lt;75%)</span>
          <strong className="text-danger fs-6">18 Students</strong>
        </div>
      </div>
    </div>
  );
};

export default AttendanceStatsPanel;
