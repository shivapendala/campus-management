import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const DisciplinaryTribunalConsole = () => {
  const [selectedCase, setSelectedCase] = useState(null);
  const [findings, setFindings] = useState('');
  const [severity, setSeverity] = useState('CAT_A_MINOR');

  const initialCases = [
    { id: 'DISC-CASE-001', student: 'Amit Kumar', roll: '2024CS08', infraction: 'Smartwatch in Examination Hall', date: '2026-08-20', status: 'SCHEDULED' },
    { id: 'DISC-CASE-002', student: 'Rohan Sharma', roll: '2023ME45', infraction: 'Hostel Curfew Violation', date: '2026-08-22', status: 'DECIDED', findings: 'Imposed Rs. 500 fine and strict warning.', severity: 'CAT_A_MINOR' },
    { id: 'DISC-CASE-003', student: 'Sneha Reddy', roll: '2025EC12', infraction: 'Proxy Attendance Swiping', date: '2026-08-25', status: 'SCHEDULED' },
    { id: 'DISC-CASE-004', student: 'Vikram Singh', roll: '2023CE19', infraction: 'Laboratory Equipment Damage', date: '2026-08-26', status: 'DECIDED', findings: 'Suspended for 3 days and parents notified.', severity: 'CAT_B_MEDIUM' }
  ];

  const columns = [
    { key: 'id', label: 'Case Reference', render: (val) => <strong className="text-danger">{val}</strong> },
    { key: 'student', label: 'Student Name' },
    { key: 'roll', label: 'Roll Number' },
    { key: 'infraction', label: 'Infraction Details' },
    { key: 'date', label: 'Hearing Date' },
    { key: 'status', label: 'Case Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleResolveCase = (e) => {
    e.preventDefault();
    if (!selectedCase) return;
    
    // Simulate updating case details
    selectedCase.status = 'DECIDED';
    selectedCase.findings = findings;
    selectedCase.severity = severity;
    
    setSelectedCase(null);
    setFindings('');
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-shield-slash-fill me-2"></i>Disciplinary Board & Tribunal Console
          </h2>
          <p className="text-muted mb-0">
            Schedule hearings, audit student conduct records, and verify statutory compliance protocols.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-journal-text me-2"></i>Disciplinary Blotter Registry</h5>
            <AdvancedDataTable
              columns={columns}
              data={initialCases}
              searchPlaceholder="Search cases..."
              onRowClick={(row) => setSelectedCase(row)}
            />
          </div>
        </div>

        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-shield-fill-check me-2"></i>Hearing Action Form</h5>
            {selectedCase ? (
              <form onSubmit={handleResolveCase}>
                <div className="mb-3 p-3 bg-light rounded-3">
                  <div className="small fw-bold text-danger">Selected Case: {selectedCase.id}</div>
                  <div className="small text-muted">{selectedCase.student} ({selectedCase.roll})</div>
                  <div className="small text-dark mt-1"><strong>Violation:</strong> {selectedCase.infraction}</div>
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Hearing Findings / Summary</label>
                  <textarea
                    className="form-control"
                    rows="3"
                    value={findings}
                    onChange={(e) => setFindings(e.target.value)}
                    placeholder="Provide details of the defense, witnesses, and findings..."
                    required
                  ></textarea>
                </div>
                <div className="mb-3">
                  <label className="form-label small fw-bold">Penalty Severity Slab</label>
                  <select className="form-select" value={severity} onChange={(e) => setSeverity(e.target.value)}>
                    <option value="CAT_A_MINOR">Category A: Minor Fine (Rs. 500)</option>
                    <option value="CAT_B_MEDIUM">Category B: Medium Suspension (3 Days) + Parent Call</option>
                    <option value="CAT_C_SEVERE">Category C: Severe Suspension (15 Days)</option>
                    <option value="CAT_D_EXPULSION">Category D: Expulsion</option>
                  </select>
                </div>
                <button type="submit" className="btn btn-danger w-100 mt-2">
                  <i className="bi bi-check-circle-fill me-1"></i>Resolve Case & Issue Order
                </button>
              </form>
            ) : (
              <div className="text-center py-5 text-muted">
                <i className="bi bi-info-circle fs-3 mb-2 d-block"></i>
                Select a case from the blotter registry to log hearings and finalize decisions.
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default DisciplinaryTribunalConsole;
