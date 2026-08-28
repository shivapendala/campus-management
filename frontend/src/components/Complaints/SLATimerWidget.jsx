import React from 'react';

const SLATimerWidget = ({ hoursRemaining = 28, maxHours = 48 }) => {
  const pct = Math.max(0, Math.min(100, (hoursRemaining / maxHours) * 100));

  return (
    <div className="card border-0 shadow-sm p-3">
      <div className="d-flex justify-content-between align-items-center mb-2">
        <span className="small text-muted fw-semibold">UGC Grievance SLA Clock</span>
        <span className="badge bg-success-subtle text-success">{hoursRemaining}h remaining</span>
      </div>
      <div className="progress" style={{ height: '8px' }}>
        <div className="progress-bar bg-success" style={{ width: `${pct}%` }}></div>
      </div>
      <small className="text-muted mt-2 d-block" style={{ fontSize: '11px' }}>
        Auto-escalation to Level 2 (HOD) in {hoursRemaining} hours if unresolved.
      </small>
    </div>
  );
};

export default SLATimerWidget;
