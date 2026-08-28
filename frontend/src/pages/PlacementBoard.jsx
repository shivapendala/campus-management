import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const PlacementBoard = () => {
  const drives = [
    { company: 'Google India', role: 'Software Engineer', ctc: '32.5 LPA', tier: 'SUPER_DREAM', date: '2026-09-05', eligible_count: 145, shortlisted_count: 18, status: 'SLOTTED_DAY_0' },
    { company: 'Microsoft IDC', role: 'Software Development Engineer', ctc: '28.0 LPA', tier: 'SUPER_DREAM', date: '2026-09-08', eligible_count: 180, shortlisted_count: 24, status: 'SLOTTED_DAY_0' },
    { company: 'Oracle Cloud', role: 'Member of Technical Staff', ctc: '18.5 LPA', tier: 'SUPER_DREAM', date: '2026-09-12', eligible_count: 240, shortlisted_count: 35, status: 'SLOTTED_DAY_1' },
    { company: 'TCS Digital', role: 'System Architect', ctc: '7.5 LPA', tier: 'DREAM', date: '2026-09-20', eligible_count: 450, shortlisted_count: 110, status: 'ACTIVE' },
  ];

  const columns = [
    { key: 'company', label: 'Company Name', render: (val) => <strong className="text-dark">{val}</strong> },
    { key: 'role', label: 'Job Role' },
    { key: 'ctc', label: 'Package (CTC)', render: (val) => <span className="fw-bold text-success">{val}</span> },
    { key: 'tier', label: 'Tier', render: (val) => <span className="badge bg-primary-subtle text-primary">{val}</span> },
    { key: 'date', label: 'Drive Date' },
    { key: 'eligible_count', label: 'Eligible Pool', render: (val) => `${val} Candidates` },
    { key: 'shortlisted_count', label: 'Shortlisted', render: (val) => <span className="badge bg-success">{val}</span> },
    { key: 'status', label: 'Stage', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-briefcase-fill me-2"></i>Corporate Placement & Career Board
          </h2>
          <p className="text-muted mb-0">
            Day-0/Day-1 drive slotting, eligibility criteria rule engine, candidate pipeline, and CTC compensation analytics.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-plus-circle me-1"></i>Schedule New Drive
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-file-earmark-bar-graph me-1"></i>Export Placement Report
          </button>
        </div>
      </div>

      {/* Quick Metrics */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Highest CTC Offered"
            value="42.0 LPA"
            icon="bi-trophy-fill"
            variant="success"
            subtitle="Atlassian International"
            delta="+15% YoY"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Average CTC Package"
            value="10.8 LPA"
            icon="bi-graph-up-arrow"
            variant="primary"
            subtitle="Across All Engineering Branches"
            delta="Benchmark: 9.5L"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Job Offers"
            value="145 Offers"
            icon="bi-envelope-check-fill"
            variant="info"
            subtitle="82.5% Outgoing Batch Placed"
            delta="Season Active"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Company Drives"
            value="38 Companies"
            icon="bi-buildings-fill"
            variant="warning"
            subtitle="14 Super Dream (> 12 LPA)"
            delta="Ongoing"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Recruitment Pipeline Table */}
      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-kanban me-2 text-primary"></i>Placement Drive Pipeline (Day-0 to Day-3)
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={drives}
          searchPlaceholder="Search company, job role, or tier..."
        />
      </div>
    </div>
  );
};

export default PlacementBoard;
