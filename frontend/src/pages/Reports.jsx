import React, { useState } from 'react';
import StatCard from '../components/StatCard';
import { useNotification } from '../context/NotificationContext';

export const Reports = () => {
  const { showSuccess } = useNotification();
  const [selectedReportType, setSelectedReportType] = useState('ALL');

  const reportPillars = [
    {
      id: 'academic',
      title: 'Institutional Academic & GPA Audit',
      description: 'Course pass rates, semester SGPA distribution across CSE/ECE/EEE/MECH/CIVIL, and faculty performance indexes.',
      recordCount: '2,450 Students',
      lastGenerated: '2026-08-28',
      format: 'PDF & CSV',
    },
    {
      id: 'attendance',
      title: 'Campus Attendance Compliance & Shortage Report',
      description: 'Section-wise attendance compliance, student condonation rosters (<75%), and faculty attendance velocity.',
      recordCount: '95 Sections',
      lastGenerated: '2026-08-28',
      format: 'PDF & CSV',
    },
    {
      id: 'finance',
      title: 'Fiscal Revenue & Fee Collection Ledger',
      description: 'Total billed vs collected revenue ($9.58M / $11.02M • 86.9%), pending receivables, and department budget allocations.',
      recordCount: '320 Accounts Pending',
      lastGenerated: '2026-08-28',
      format: 'CSV & Audit Sheet',
    },
    {
      id: 'placement',
      title: 'Corporate Placements & CTC Package Intelligence',
      description: 'Hiring drive conversion ratios, average package CTC ($18.5 LPA), company visit logs, and offer letter distributions.',
      recordCount: '145 Placed Students',
      lastGenerated: '2026-08-27',
      format: 'Executive Dossier',
    },
    {
      id: 'grievance',
      title: 'Grievance Redressal & SLA Resolution Audit',
      description: 'Infrastructure, Academic, Hostel, and Safety tickets breakdown, resolution timelines, and student satisfaction ratings.',
      recordCount: '25 Active Tickets',
      lastGenerated: '2026-08-28',
      format: 'Compliance PDF',
    },
  ];

  const handleExport = (reportTitle) => {
    const csvContent = `Report: ${reportTitle}\nGenerated: ${new Date().toISOString()}\nStatus: Verified\nUniversity: Campus Management System\n`;
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `${reportTitle.replace(/\s+/g, '_')}_2026.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showSuccess(`Generated and exported "${reportTitle}"!`);
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Institutional Analytics & Audit Reports</h2>
          <p className="text-muted mb-0">
            Executive intelligence dossiers, academic pass ratios, fiscal audits, and multi-format report exports
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => window.print()}
            className="btn btn-outline-secondary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-printer-fill"></i>
            <span>Print Executive Audit</span>
          </button>
        </div>
      </div>

      {/* KPI Metrics */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Institutional Retention"
            value="98.4%"
            change="+1.2% YoY Improvement"
            isPositive={true}
            icon="bi-trophy-fill"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Avg Campus Attendance"
            value="89.2%"
            change="Across 95 Course Sections"
            isPositive={true}
            icon="bi-calendar-check-fill"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Placement Conversion"
            value="78.5%"
            change="Avg Package $18.5 LPA"
            isPositive={true}
            icon="bi-briefcase-fill"
            gradientClass="bg-gradient-amber"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Fee Realization"
            value="86.9%"
            change="$9.58M Collected"
            isPositive={true}
            icon="bi-cash-coin"
            gradientClass="bg-gradient-rose"
          />
        </div>
      </div>

      {/* Reports Catalog */}
      <div className="campus-card shadow-sm border-0 p-4">
        <h5 className="fw-bold text-dark mb-4">Official Institutional Report Packages</h5>

        <div className="d-flex flex-column gap-3">
          {reportPillars.map((rep) => (
            <div key={rep.id} className="p-3 bg-light rounded-3 border d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3">
              <div>
                <div className="d-flex align-items-center gap-2 mb-1">
                  <h6 className="fw-bold text-dark mb-0">{rep.title}</h6>
                  <span className="badge bg-primary">{rep.format}</span>
                  <small className="text-muted">• Generated {rep.lastGenerated}</small>
                </div>
                <p className="small text-secondary mb-0">{rep.description}</p>
                <small className="text-primary fw-semibold">Data Scope: {rep.recordCount}</small>
              </div>

              <div className="d-flex gap-2">
                <button
                  className="btn btn-outline-primary btn-sm fw-semibold"
                  onClick={() => handleExport(rep.title)}
                >
                  <i className="bi bi-file-earmark-spreadsheet me-1"></i> Export CSV
                </button>
                <button
                  className="btn btn-primary btn-sm fw-semibold"
                  onClick={() => window.print()}
                >
                  <i className="bi bi-file-earmark-pdf-fill me-1"></i> Download PDF
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Reports;
