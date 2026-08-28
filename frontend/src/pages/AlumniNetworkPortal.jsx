import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const AlumniNetworkPortal = () => {
  const [showDonationModal, setShowDonationModal] = useState(false);
  const [alumniName, setAlumniName] = useState('');
  const [amount, setAmount] = useState('');
  const [projectAllocation, setProjectAllocation] = useState('SCHOLARSHIP_FUND');

  const alumniList = [
    { id: 1, name: 'Srinath Ravichandran', batch: '2012', degree: 'B.Tech (CSE)', company: 'Google Inc.', designation: 'Principal Staff Engineer', location: 'Mountain View, CA', status: 'ACTIVE_MENTOR' },
    { id: 2, name: 'Prerna Hegde', batch: '2015', degree: 'B.Tech (ECE)', company: 'NVIDIA Corp.', designation: 'Senior Hardware Architect', location: 'Santa Clara, CA', status: 'ACTIVE_MENTOR' },
    { id: 3, name: 'Vikram Malhotra', batch: '2008', degree: 'B.Tech (MECH)', company: 'Tesla Motors', designation: 'Director of PowerTrain Eng.', location: 'Austin, TX', status: 'DONOR' },
    { id: 4, name: 'Neha Deshmukh', batch: '2018', degree: 'B.Tech (AIML)', company: 'DeepMind', designation: 'Research Scientist', location: 'London, UK', status: 'ACTIVE_MENTOR' },
    { id: 5, name: 'Siddharth Rao', batch: '2010', degree: 'B.Tech (EEE)', company: 'Siemens Healthineers', designation: 'Lead Systems Architect', location: 'Erlangen, Germany', status: 'INACTIVE' }
  ];

  const columns = [
    { key: 'name', label: 'Alumnus Name', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'batch', label: 'Graduation Batch' },
    { key: 'degree', label: 'Degree Program' },
    { key: 'company', label: 'Employer Company' },
    { key: 'designation', label: 'Designation / Title' },
    { key: 'location', label: 'Current Location' },
    { key: 'status', label: 'Engagement Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-people-fill me-2"></i>Alumni Relations & Endowment Fund Studio
          </h2>
          <p className="text-muted mb-0">
            Longitudinal graduate tracking, mentorship connection pipelines, corporate references, and university endowment corpus allocations.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary" onClick={() => setShowDonationModal(true)}>
            <i className="bi bi-gift-fill me-1"></i>Record Endowment Donation
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-chat-left-text-fill me-1"></i>Launch Mentorship Matching
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Registered Alumni"
            value="4,820 Alumni"
            icon="bi-journal-check"
            variant="primary"
            subtitle="Batches 2002 - 2025"
            delta="+520 this year"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Endowment Corpus Fund"
            value="Rs. 2.45 Cr"
            icon="bi-cash-coin"
            variant="success"
            subtitle="Endowment Returns: 8.2% p.a."
            delta="100% Audited"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Industry Mentors"
            value="142 Mentors"
            icon="bi-person-badge-fill"
            variant="info"
            subtitle="Engaged in 1-on-1 Student Matching"
            delta="Active"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Referrals & Internships Secured"
            value="85 Placements"
            icon="bi-briefcase-fill"
            variant="warning"
            subtitle="Via Alumni Corporate Portals"
            delta="+28% YoY"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4 mb-4">
        <h5 className="fw-bold mb-3"><i className="bi bi-search me-2 text-primary"></i>Alumni Search & Interaction Grid</h5>
        <AdvancedDataTable columns={columns} data={alumniList} searchPlaceholder="Search alumni by name, batch, company, or location..." />
      </div>

      {showDonationModal && (
        <div className="modal show d-block" tabIndex="-1" style={{ backgroundColor: 'rgba(0,0,0,0.5)' }}>
          <div className="modal-dialog modal-dialog-centered">
            <div className="modal-content border-0 shadow rounded-3">
              <div className="modal-header border-0 bg-light p-3">
                <h5 className="modal-title fw-bold text-primary">Record Endowment Contribution</h5>
                <button type="button" className="btn-close" onClick={() => setShowDonationModal(false)}></button>
              </div>
              <div className="modal-body p-4">
                <div className="mb-3">
                  <label className="form-label small fw-bold">Donor Alumni Name</label>
                  <input type="text" className="form-control" value={alumniName} onChange={(e) => setAlumniName(e.target.value)} placeholder="Enter full name" />
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Contribution Amount (INR)</label>
                  <input type="number" className="form-control" value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount in Rs." />
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Project Allocation Fund</label>
                  <select className="form-select" value={projectAllocation} onChange={(e) => setProjectAllocation(e.target.value)}>
                    <option value="SCHOLARSHIP_FUND">Underprivileged Student Scholarship</option>
                    <option value="RESEARCH_LABS">Advanced AI/VLSI Laboratories Upgrade</option>
                    <option value="SPORTS_COMPLEX">Inter-Collegiate Indoor Sports Complex</option>
                    <option value="GENERAL_ENDOWMENT">General Institutional Endowment Corpus</option>
                  </select>
                </div>
                <div className="alert alert-info py-2 small mb-0">
                  <i className="bi bi-info-circle-fill me-2"></i>Contributions to the University Endowment Fund are tax exempted under Section 80G.
                </div>
              </div>
              <div className="modal-footer border-0 p-3 bg-light d-flex justify-content-end gap-2">
                <button className="btn btn-outline-secondary" onClick={() => setShowDonationModal(false)}>Cancel</button>
                <button className="btn btn-primary" onClick={() => setShowDonationModal(false)}>Post Donation Receipt</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default AlumniNetworkPortal;
