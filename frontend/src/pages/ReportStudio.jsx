import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';

const ReportStudio = () => {
  const [selectedReportType, setSelectedReportType] = useState('STUDENT_ROSTER');

  const reportPresets = [
    { code: 'STUDENT_ROSTER', title: 'Comprehensive Student Enrolment Roster', category: 'ACADEMIC', formats: ['CSV', 'PDF', 'EXCEL', 'JSON'] },
    { code: 'ATTENDANCE_SHORTAGE', title: 'Semester Attendance Shortage (<75%) & Condonation Audit', category: 'ATTENDANCE', formats: ['PDF', 'EXCEL'] },
    { code: 'NAAC_CRITERIA_SUMMARY', title: 'NAAC Institutional Self-Study Report (SSR) Data Pack', category: 'ACCREDITATION', formats: ['PDF', 'JSON'] },
    { code: 'FEE_COLLECTION_LEDGER', title: 'Departmental Fee Collection, Arrears & Waiver Ledger', category: 'FINANCE', formats: ['EXCEL', 'PDF'] },
    { code: 'PLACEMENT_CTC_ANALYSIS', title: 'Annual Placement Compensation & Tiered Hiring Report', category: 'PLACEMENTS', formats: ['PDF', 'EXCEL'] },
    { code: 'AISHE_STATUTORY_BUNDLE', title: 'AISHE (MHRD / UGC) Standardized Higher Education Dataset', category: 'COMPLIANCE', formats: ['XML', 'JSON'] },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-file-earmark-spreadsheet-fill me-2"></i>Institutional Report Studio & Data Exporter
          </h2>
          <p className="text-muted mb-0">
            Generate, customize, and stream regulatory compliance reports, statistical ledgers, and academic dossiers in CSV, PDF, XML, and Excel formats.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-gear me-1"></i>Report Builder
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-cloud-arrow-down-fill me-1"></i>Export Selected ({selectedReportType})
          </button>
        </div>
      </div>

      {/* Preset Cards Grid */}
      <div className="row g-3 mb-4">
        {reportPresets.map((preset, idx) => (
          <div key={idx} className="col-md-4 col-sm-6">
            <div
              className={`card border-0 shadow-sm rounded-3 p-3 h-100 cursor-pointer transition-all ${
                selectedReportType === preset.code ? 'border-primary ring bg-primary-subtle' : 'bg-white'
              }`}
              onClick={() => setSelectedReportType(preset.code)}
              style={{ borderLeft: '4px solid var(--bs-primary)' }}
            >
              <div className="d-flex justify-content-between align-items-start mb-2">
                <span className="badge bg-secondary-subtle text-secondary small">{preset.category}</span>
                <i className="bi bi-file-earmark-text fs-4 text-primary"></i>
              </div>
              <h6 className="fw-bold text-dark mb-2">{preset.title}</h6>
              <div className="d-flex gap-1 mt-auto">
                {preset.formats.map((f, fIdx) => (
                  <span key={fIdx} className="badge bg-light text-dark border small">{f}</span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ReportStudio;
