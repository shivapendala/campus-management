import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const UgcCasAppraisalConsole = () => {
  const [teachingWorkload, setTeachingWorkload] = useState('');
  const [researchPapers, setResearchPapers] = useState('');
  const [adminCharges, setAdminCharges] = useState('');
  const [scoreSummary, setScoreSummary] = useState(null);

  const initialAppraisals = [
    { id: 'FAC-101', name: 'Dr. Sunita Murthy', dept: 'CSE', score: 142.5, recommendation: 'ELIGIBLE_STAGE_3', status: 'VERIFIED' },
    { id: 'FAC-102', name: 'Dr. Meenakshi Sundaram', dept: 'ECE', score: 165.0, recommendation: 'ELIGIBLE_STAGE_4', status: 'VERIFIED' },
    { id: 'FAC-103', name: 'Mr. P. Murugan', dept: 'EEE', score: 92.0, recommendation: 'INELIGIBLE_STAGE_2', status: 'PENDING_REVIEW' }
  ];

  const columns = [
    { key: 'id', label: 'Faculty ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'name', label: 'Faculty Name' },
    { key: 'dept', label: 'Department' },
    { key: 'score', label: 'Total PBAS Score' },
    { key: 'recommendation', label: 'Promotion Stage Advice', render: (val) => <span className="badge bg-secondary">{val}</span> },
    { key: 'status', label: 'Verification Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleAppraisalCalculate = (e) => {
    e.preventDefault();
    const teaching = parseFloat(teachingWorkload) || 0;
    const papers = parseInt(researchPapers) || 0;
    const admin = parseFloat(adminCharges) || 0;

    // Normalize teaching score capping at 50
    const cat1 = Math.min((teaching / 16) * 50.0, 50.0);
    // Base 15 points per Scopus paper + scaling
    const cat3 = papers * 15.0;
    // Capping category 2 administrative workload at 45
    const cat2 = Math.min(admin * 5.0, 45.0);

    const total = cat1 + cat2 + cat3;

    setScoreSummary({
      teachingScore: roundScore(cat1),
      adminScore: roundScore(cat2),
      researchScore: roundScore(cat3),
      totalScore: roundScore(total),
      advice: total >= 120.0 ? 'STAGE_PROMOTION_RECOMMENDED' : 'STAGE_PROMOTION_DEFERRED'
    });
  };

  const roundScore = (num) => Math.round((num + Number.EPSILON) * 100) / 100;

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-person-badge-fill me-2"></i>UGC CAS Faculty Appraisal Console
          </h2>
          <p className="text-muted mb-0">
            Performance Based Appraisal System (PBAS) score compiling, academic performance index (API) audits, and Career Advancement Scheme eligibility checks.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-sliders me-2"></i>API Score Calculator</h5>
            <form onSubmit={handleAppraisalCalculate}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Actual Weekly Teaching Hours</label>
                <input
                  type="number"
                  className="form-control"
                  value={teachingWorkload}
                  onChange={(e) => setTeachingWorkload(e.target.value)}
                  placeholder="e.g. 14"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Scopus / UGC Care Research Papers</label>
                <input
                  type="number"
                  className="form-control"
                  value={researchPapers}
                  onChange={(e) => setResearchPapers(e.target.value)}
                  placeholder="e.g. 4"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Admin Hours / Week (HOD/Dean/Committees)</label>
                <input
                  type="number"
                  className="form-control"
                  value={adminCharges}
                  onChange={(e) => setAdminCharges(e.target.value)}
                  placeholder="e.g. 6"
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-calculator-fill me-1"></i>Compile PBAS Scorecard
              </button>
            </form>

            {scoreSummary && (
              <div className="mt-4 p-3 bg-light rounded-3 border-start border-primary border-4">
                <h6 className="fw-bold mb-2">Compiled PBAS API Slabs:</h6>
                <ul className="small mb-2 ps-3">
                  <li>Category I (Teaching): {scoreSummary.teachingScore} Points</li>
                  <li>Category II (Co-curricular/Admin): {scoreSummary.adminScore} Points</li>
                  <li>Category III (Research): {scoreSummary.researchScore} Points</li>
                </ul>
                <div className="fw-bold text-success border-top pt-2 mt-2">
                  Total Compiled score: {scoreSummary.totalScore} Points
                </div>
                <div className="small text-muted">
                  Advice: {scoreSummary.advice}
                </div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-award-fill me-2"></i>CAS Verification Register</h5>
            <AdvancedDataTable columns={columns} data={initialAppraisals} searchPlaceholder="Search appraisal records..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default UgcCasAppraisalConsole;
