import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const SecurityAuditPortal = () => {
  const auditLogs = [
    { event_id: 'EVT-9801', timestamp: '2026-08-28 17:42:10 UTC', actor: 'admin', role: 'ADMIN', action: 'UPDATE', resource: 'FeeStructure', ip: '127.0.0.1', severity: 'HIGH' },
    { event_id: 'EVT-9802', timestamp: '2026-08-28 17:45:30 UTC', actor: 'hod_cse', role: 'HOD', action: 'APPROVE', resource: 'ExamMarks', ip: '192.168.1.45', severity: 'INFO' },
    { event_id: 'EVT-9803', timestamp: '2026-08-28 17:50:00 UTC', actor: 'faculty_math', role: 'FACULTY', action: 'MARK', resource: 'Attendance', ip: '192.168.1.88', severity: 'INFO' },
    { event_id: 'EVT-9804', timestamp: '2026-08-28 18:02:15 UTC', actor: 'accountant', role: 'ACCOUNTANT', action: 'CREATE', resource: 'FeeReceipt', ip: '192.168.1.12', severity: 'INFO' },
  ];

  const columns = [
    { key: 'event_id', label: 'Event ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'timestamp', label: 'Timestamp (UTC)' },
    { key: 'actor', label: 'Actor Username' },
    { key: 'role', label: 'Role Tier', render: (val) => <span className="badge bg-light text-dark">{val}</span> },
    { key: 'action', label: 'Action Type', render: (val) => <span className="badge bg-primary-subtle text-primary">{val}</span> },
    { key: 'resource', label: 'Resource' },
    { key: 'ip', label: 'IP Address' },
    { key: 'severity', label: 'Severity', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-shield-shaded me-2"></i>Institutional Security, RBAC & Audit Portal
          </h2>
          <p className="text-muted mb-0">
            Immutable system audit trails, role permission matrix explorer, password security policy enforcement, and JWT token revocation.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-danger">
            <i className="bi bi-slash-circle me-1"></i>Flush Blacklist Tokens
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-file-earmark-lock me-1"></i>Export Compliance Audit
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="System Security Health"
            value="100% Compliant"
            icon="bi-shield-check"
            variant="success"
            subtitle="FERPA & GDPR Aligned"
            delta="Secure"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Logged Sessions"
            value="342 Active"
            icon="bi-people"
            variant="primary"
            subtitle="JWT Stateless Tokens"
            delta="Normal Load"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Audit Events Recorded"
            value="18,450"
            icon="bi-journal-code"
            variant="info"
            subtitle="Immutable In-Memory Stream"
            delta="Live Stream"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Failed Auth Attempts (24h)"
            value="0 Flagged"
            icon="bi-shield-x"
            variant="warning"
            subtitle="Rate Limit Throttling Active"
            delta="Zero Breaches"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-clock-history me-2 text-primary"></i>Security & Operations Audit Trail
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={auditLogs}
          searchPlaceholder="Filter audit events by actor, action, or resource..."
        />
      </div>
    </div>
  );
};

export default SecurityAuditPortal;
