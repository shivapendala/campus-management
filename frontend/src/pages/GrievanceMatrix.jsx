import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const GrievanceMatrix = () => {
  const grievances = [
    { id: 'GRV-2026-081', category: 'HOSTEL_MESS', subject: 'Mess dining hall water filtration maintenance', filed_at: '2026-08-27', level: 'Level 1 (Warden)', sla_remaining: '28h remaining', status: 'ON_TRACK' },
    { id: 'GRV-2026-082', category: 'ACADEMIC', subject: 'Timetable lab period clash for ECE Section B', filed_at: '2026-08-26', level: 'Level 1 (Coordinator)', sla_remaining: '4h remaining', status: 'REVIEW_REQUIRED' },
    { id: 'GRV-2026-080', category: 'INFRASTRUCTURE', subject: 'Lab 3 central air conditioning repair', filed_at: '2026-08-24', level: 'Level 2 (HOD)', sla_remaining: 'Resolved', status: 'RESOLVED' },
  ];

  const columns = [
    { key: 'id', label: 'Ticket ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'category', label: 'Statutory Category', render: (val) => <span className="badge bg-light text-dark">{val}</span> },
    { key: 'subject', label: 'Grievance Description' },
    { key: 'filed_at', label: 'Date Filed' },
    { key: 'level', label: 'Resolution Tier' },
    { key: 'sla_remaining', label: 'SLA Timer' },
    { key: 'status', label: 'SLA Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-shield-lock-fill me-2"></i>Grievance Redressal & SLA Escalation Matrix
          </h2>
          <p className="text-muted mb-0">
            Statutory UGC Grievance Redressal (2023) SLA compliance, POSH Internal Complaints Committee, and confidential whistleblower channel.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-danger">
            <i className="bi bi-eye-slash-fill me-1"></i>File Whistleblower Report
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-plus-circle me-1"></i>Submit Grievance
          </button>
        </div>
      </div>

      {/* Metrics */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Avg Turnaround Time"
            value="32.4 Hours"
            icon="bi-stopwatch-fill"
            variant="success"
            subtitle="SLA Standard: < 48 Hours"
            delta="100% On-Time"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Resolution Rate"
            value="94.2%"
            icon="bi-check-circle-fill"
            variant="primary"
            subtitle="48 of 51 Resolved"
            delta="High Efficiency"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Student Satisfaction"
            value="4.7 / 5.0"
            icon="bi-star-fill"
            variant="warning"
            subtitle="Post-Resolution Rating"
            delta="Exemplary"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Escalated to L3 (Ombudsman)"
            value="0 Cases"
            icon="bi-shield-check"
            variant="info"
            subtitle="All Handled at L1 & L2"
            delta="Clean Record"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Table */}
      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-table me-2 text-primary"></i>Active Grievance Tickets & SLA Tracking
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={grievances}
          searchPlaceholder="Search tickets by ID, category, or keyword..."
        />
      </div>
    </div>
  );
};

export default GrievanceMatrix;
