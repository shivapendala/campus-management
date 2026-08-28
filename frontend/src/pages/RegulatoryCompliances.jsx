import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const RegulatoryCompliances = () => {
  const [activeChecklist, setActiveChecklist] = useState('ALL');

  const statutoryItems = [
    { id: 'REG-UGC-01', agency: 'UGC', criteria: '2(f) and 12(B) Status Maintenance', deadline: '2026-12-31', progress: 100, status: 'COMPLIANT', remarks: 'Statutory status verified; certified copy active on main portal.' },
    { id: 'REG-UGC-02', agency: 'UGC', criteria: 'POSH Statutory Committee Disclosures', deadline: '2026-10-15', progress: 100, status: 'COMPLIANT', remarks: 'Annual report submitted to state registrar.' },
    { id: 'REG-UGC-03', agency: 'UGC', criteria: 'Anti-Ragging Statutory Disclosures', deadline: '2026-09-01', progress: 100, status: 'COMPLIANT', remarks: 'Emergency student helpline active, proctorial circular published.' },
    { id: 'REG-AICTE-01', agency: 'AICTE', criteria: 'Extension of Approval (EoA) Annual Pack', deadline: '2027-04-30', progress: 45, status: 'IN_PROGRESS', remarks: 'Academic assets and land records verification pending review.' },
    { id: 'REG-AICTE-02', agency: 'AICTE', criteria: 'Faculty-to-Student Cadre Ratio 1:20 Compliance', deadline: '2026-11-30', progress: 100, status: 'COMPLIANT', remarks: 'FSR sits at 1:15 across engineering streams.' },
    { id: 'REG-NAAC-01', agency: 'NAAC', criteria: 'Annual Quality Assurance Report (AQAR) submission', deadline: '2026-12-15', progress: 75, status: 'IN_PROGRESS', remarks: 'Criterion 3 & 4 data structures require final IQAC director sign-off.' },
    { id: 'REG-NBA-01', agency: 'NBA', criteria: 'B.Tech CSE Tier-1 Re-Accreditation SAR Pack', deadline: '2027-03-15', progress: 60, status: 'IN_PROGRESS', remarks: 'Course files mapping with CO-PO attainment under review.' }
  ];

  const columns = [
    { key: 'id', label: 'Compliance ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'agency', label: 'Statutory Body', render: (val) => <span className="badge bg-secondary">{val}</span> },
    { key: 'criteria', label: 'Regulatory Criteria / Directive' },
    { key: 'deadline', label: 'Statutory Deadline' },
    { key: 'progress', label: 'Attainment Progress', render: (val) => (
      <div className="d-flex align-items-center gap-2" style={{ minWidth: '120px' }}>
        <div className="progress flex-grow-1" style={{ height: '6px' }}>
          <div className="progress-bar bg-primary" style={{ width: `${val}%` }}></div>
        </div>
        <span className="small fw-bold">{val}%</span>
      </div>
    )},
    { key: 'status', label: 'Audit Status', render: (val) => <StatusBadge status={val} size="small" /> },
    { key: 'remarks', label: 'Review Notes & Verification Logs' }
  ];

  const filteredData = activeChecklist === 'ALL' 
    ? statutoryItems 
    : statutoryItems.filter(item => item.agency === activeChecklist);

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-shield-check me-2"></i>Statutory Compliance & Regulatory Audits Portal
          </h2>
          <p className="text-muted mb-0">
            Real-time compliance checks against UGC, AICTE, NAAC, and NBA statutory standards to maintain accreditation standing.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-pdf-fill me-1"></i>Export Compliance Book
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-arrow-repeat me-1"></i>Run Automated Audit Checkers
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Directives Audited"
            value="18 Directives"
            icon="bi-journal-check"
            variant="primary"
            subtitle="UGC, AICTE, NBA, NAAC"
            delta="100% Monitored"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Overall Compliance Score"
            value="92.4 %"
            icon="bi-shield-check"
            variant="success"
            subtitle="Meets all statutory bars"
            delta="Excellent Standing"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Accreditation Risk Level"
            value="Zero Risk"
            icon="bi-shield-exclamation"
            variant="info"
            subtitle="No active warnings"
            delta="Safe Slabs"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Upcoming Audits"
            value="2 Site Visits"
            icon="bi-calendar-event-fill"
            variant="warning"
            subtitle="NBA Team & NAAC Peer Team"
            delta="Scheduled Q1"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <div className="d-flex justify-content-between align-items-center mb-3 flex-wrap gap-2">
          <h5 className="fw-bold mb-0"><i className="bi bi-list-task me-2 text-primary"></i>Statutory Compliance Checklists</h5>
          <div className="btn-group">
            <button className={`btn btn-sm ${activeChecklist === 'ALL' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setActiveChecklist('ALL')}>All Bodies</button>
            <button className={`btn btn-sm ${activeChecklist === 'UGC' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setActiveChecklist('UGC')}>UGC</button>
            <button className={`btn btn-sm ${activeChecklist === 'AICTE' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setActiveChecklist('AICTE')}>AICTE</button>
            <button className={`btn btn-sm ${activeChecklist === 'NAAC' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setActiveChecklist('NAAC')}>NAAC</button>
            <button className={`btn btn-sm ${activeChecklist === 'NBA' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => setActiveChecklist('NBA')}>NBA</button>
          </div>
        </div>

        <AdvancedDataTable columns={columns} data={filteredData} searchPlaceholder="Search regulatory compliance criteria..." />
      </div>
    </div>
  );
};

export default RegulatoryCompliances;
