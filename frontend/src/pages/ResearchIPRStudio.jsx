import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const ResearchIPRStudio = () => {
  const patents = [
    { app_no: '202541029841', title: 'Edge AI Vision Sensor for Defect Detection in High-Speed Manufacturing', inventors: 'Dr. Rajesh Raman, Dr. Sunita Murthy', filing_date: '2025-06-15', stage: 'GRANTED', royalty: 'Rs. 2,50,000' },
    { app_no: '202541031022', title: 'Smart Grid Bidirectional Power Inverter with Adaptive MPPT', inventors: 'Dr. Meenakshi Sundaram, Gautam Menon', filing_date: '2025-08-20', stage: 'PUBLISHED', royalty: '-' },
    { app_no: '202641004128', title: 'Biodegradable Polymer Composite for Agricultural Mulch Films', inventors: 'Dr. Ramesh Chandra', filing_date: '2026-02-10', stage: 'UNDER_EXAMINATION', royalty: '-' },
  ];

  const columns = [
    { key: 'app_no', label: 'Application No.', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'title', label: 'Invention Title' },
    { key: 'inventors', label: 'Faculty Inventors' },
    { key: 'filing_date', label: 'Filing Date' },
    { key: 'royalty', label: 'Commercial Royalty' },
    { key: 'stage', label: 'Patent Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-lightbulb-fill me-2"></i>Intellectual Property (IPR), Patents & Sponsored Research
          </h2>
          <p className="text-muted mb-0">
            Patent prosecution lifecycle, Indian Patent Office (IPO) filings, seed grants, and sponsored DST/SERB funding projects.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-plus me-1"></i>Apply for Seed Grant
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-shield-plus me-1"></i>Submit IPR Invention Disclosure
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Patents Filed"
            value="24 Patents"
            icon="bi-award-fill"
            variant="primary"
            subtitle="6 Granted by IPO"
            delta="+8 this year"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Sponsored Grants Received"
            value="Rs. 4.50 Cr"
            icon="bi-cash-coin"
            variant="success"
            subtitle="DST, SERB, AICTE, ISRO"
            delta="100% Disbursed"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Active Seed Grants"
            value="12 Projects"
            icon="bi-rocket-takeoff-fill"
            variant="info"
            subtitle="Internal Institutional Corpus"
            delta="Ongoing"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Scopus Research Papers"
            value="420 Papers"
            icon="bi-journal-richtext"
            variant="warning"
            subtitle="2,150 Total Citations"
            delta="h-index: 22"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3"><i className="bi bi-file-earmark-lock me-2 text-primary"></i>Institutional Patent & Innovation Ledger</h5>
        <AdvancedDataTable columns={columns} data={patents} searchPlaceholder="Search patent by title, inventor, or application number..." />
      </div>
    </div>
  );
};

export default ResearchIPRStudio;
