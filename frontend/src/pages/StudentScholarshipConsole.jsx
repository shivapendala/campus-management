import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const StudentScholarshipConsole = () => {
  const [studentIncome, setStudentIncome] = useState('');
  const [socialCategory, setSocialCategory] = useState('GENERAL');
  const [cgpa, setCgpa] = useState('');
  const [calculationResult, setCalculationResult] = useState(null);

  const initialScholarships = [
    { id: 'SCH-2026-001', name: 'Post-Matric Scholarship Scheme', category: 'SC_ST', waiver: '100% Tuition', count: '320 Students', status: 'ACTIVE' },
    { id: 'SCH-2026-002', name: 'Merit-Cum-Means Scholarship', category: 'OBC_GEN', waiver: '50% Tuition', count: '145 Students', status: 'ACTIVE' },
    { id: 'SCH-2026-003', name: 'State Minority Special Scholarship', category: 'MINORITY', waiver: 'Rs. 25,000 Fixed', count: '98 Students', status: 'ACTIVE' },
    { id: 'SCH-2026-004', name: 'Dr. Ambedkar Scheme of Interest Subsidy', category: 'EWS', waiver: '100% Interest Subsidy', count: '64 Students', status: 'ACTIVE' },
    { id: 'SCH-2026-005', name: 'Institution Gold Medal Performance waiver', category: 'MERIT_ONLY', waiver: '100% Tuition & Hostel', count: '12 Students', status: 'ACTIVE' }
  ];

  const columns = [
    { key: 'id', label: 'Scheme ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'name', label: 'Scholarship Scheme' },
    { key: 'category', label: 'Target Category', render: (val) => <span className="badge bg-info text-dark">{val}</span> },
    { key: 'waiver', label: 'Concession / Waiver' },
    { key: 'count', label: 'Beneficiary Count' },
    { key: 'status', label: 'Scheme Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleCalculate = (e) => {
    e.preventDefault();
    const income = parseFloat(studentIncome) || 0;
    const gpa = parseFloat(cgpa) || 0;

    let incomeWaiver = 0.0;
    if (income <= 100000) {
      incomeWaiver = 1.00;
    } else if (income <= 250000) {
      incomeWaiver = 0.50;
    } else if (income <= 600000) {
      incomeWaiver = 0.25;
    } else if (income <= 800000) {
      incomeWaiver = 0.10;
    }

    let categoryWaiver = 0.0;
    if (socialCategory === 'SC' || socialCategory === 'ST') {
      categoryWaiver = 1.00;
    } else if (socialCategory === 'OBC_NCL' || socialCategory === 'EWS') {
      categoryWaiver = 0.50;
    }

    let meritWaiver = 0.0;
    if (gpa >= 9.5) {
      meritWaiver = 0.50;
    } else if (gpa >= 9.0) {
      meritWaiver = 0.25;
    } else if (gpa >= 8.5) {
      meritWaiver = 0.15;
    }

    const maxWaiver = Math.max(incomeWaiver, categoryWaiver, meritWaiver);
    const waiverPct = maxWaiver * 100;

    setCalculationResult({
      incomeWaiver: incomeWaiver * 100,
      categoryWaiver: categoryWaiver * 100,
      meritWaiver: meritWaiver * 100,
      finalWaiver: waiverPct,
      netPayable: 100 - waiverPct
    });
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-wallet2 me-2"></i>Statutory Scholarship & Concession Console
          </h2>
          <p className="text-muted mb-0">
            Verify student eligibility for governmental scholarships, state fee waivers, and calculate net payable tuition fees.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-calculator me-2"></i>Eligibility Simulator</h5>
            <form onSubmit={handleCalculate}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Annual Family Income (Rs.)</label>
                <input
                  type="number"
                  className="form-control"
                  value={studentIncome}
                  onChange={(e) => setStudentIncome(e.target.value)}
                  placeholder="e.g. 150000"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Social Category</label>
                <select className="form-select" value={socialCategory} onChange={(e) => setSocialCategory(e.target.value)}>
                  <option value="GENERAL">General</option>
                  <option value="OBC_NCL">OBC-NCL</option>
                  <option value="SC">SC</option>
                  <option value="ST">ST</option>
                  <option value="EWS">EWS</option>
                </select>
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Student Cumulative CGPA</label>
                <input
                  type="number"
                  step="0.01"
                  className="form-control"
                  value={cgpa}
                  onChange={(e) => setCgpa(e.target.value)}
                  placeholder="e.g. 8.75"
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-cpu-fill me-1"></i>Analyze Waiver Slab
              </button>
            </form>

            {calculationResult && (
              <div className="mt-4 p-3 bg-light rounded-3 border-start border-primary border-4">
                <h6 className="fw-bold mb-2">Simulated Concessions:</h6>
                <ul className="small mb-2 ps-3">
                  <li>Income-based waiver: {calculationResult.incomeWaiver}%</li>
                  <li>Category-based waiver: {calculationResult.categoryWaiver}%</li>
                  <li>Merit-based waiver: {calculationResult.meritWaiver}%</li>
                </ul>
                <div className="fw-bold text-success border-top pt-2 mt-2">
                  Final Approved Concession: {calculationResult.finalWaiver}%
                </div>
                <div className="small text-muted">
                  Net Tuition Payable: {calculationResult.netPayable}%
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-list-stars me-2"></i>Active Scholarship Schemes</h5>
            <AdvancedDataTable columns={columns} data={initialScholarships} searchPlaceholder="Search schemes..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default StudentScholarshipConsole;
