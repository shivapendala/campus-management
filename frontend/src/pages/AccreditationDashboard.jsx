import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import StatusBadge from '../components/common/StatusBadge';

const AccreditationDashboard = () => {
  const [accreditationType, setAccreditationType] = useState('NBA');

  const nbaCriteria = [
    { no: 1, title: 'Vision, Mission & PEOs', max: 50, score: 48, status: 'COMPLIANT' },
    { no: 2, title: 'Program Curriculum & Teaching-Learning', max: 100, score: 92, status: 'COMPLIANT' },
    { no: 3, title: 'Course Outcomes & Program Outcomes (CO-PO)', max: 175, score: 158, status: 'COMPLIANT' },
    { no: 4, title: 'Students Performance & Success Rate', max: 100, score: 86, status: 'COMPLIANT' },
    { no: 5, title: 'Faculty Contributions & Research', max: 200, score: 176, status: 'COMPLIANT' },
    { no: 6, title: 'Facilities & Technical Support', max: 80, score: 74, status: 'COMPLIANT' },
    { no: 7, title: 'Continuous Improvement (IQAC)', max: 75, score: 68, status: 'COMPLIANT' },
    { no: 8, title: 'First Year Academics', max: 50, score: 46, status: 'COMPLIANT' },
    { no: 9, title: 'Student Support Systems', max: 50, score: 48, status: 'COMPLIANT' },
    { no: 10, title: 'Governance & Institutional Support', max: 120, score: 108, status: 'COMPLIANT' },
  ];

  const totalNBAScore = nbaCriteria.reduce((acc, c) => acc + c.score, 0);

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-patch-check-fill me-2"></i>Accreditation Dashboard: NAAC & NBA Tier-1 Studio
          </h2>
          <p className="text-muted mb-0">
            Real-time compliance audit for National Board of Accreditation (NBA 1000-Point Scale) and NAAC Institutional SSR Dossier.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-arrow-down me-1"></i>Download SAR (Self Assessment Report)
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-cloud-check-fill me-1"></i>Run Automated Compliance Audit
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="NBA Tier-1 Attainment"
            value={`${totalNBAScore} / 1000`}
            icon="bi-trophy-fill"
            variant="success"
            subtitle="Accredited for 6 Full Years (>= 750)"
            delta="Tier-1 Pass"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="NAAC CGPA Forecast"
            value="3.68 / 4.00"
            icon="bi-star-fill"
            variant="primary"
            subtitle="Grade A++ (Highest Statutory Tier)"
            delta="A++"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="NBA CO-PO Attainment"
            value="90.3%"
            icon="bi-bullseye"
            variant="info"
            subtitle="Across All 48 Theory & Practical Courses"
            delta="High Attainment"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Faculty Cadre Ratio"
            value="1 : 2.1 : 5.8"
            icon="bi-people-fill"
            variant="warning"
            subtitle="Prof : Assoc : Asst (AICTE Norm Compliant)"
            delta="Optimal"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h5 className="fw-bold mb-0"><i className="bi bi-check2-all me-2 text-primary"></i>NBA 10-Criteria Evaluation Matrix</h5>
          <span className="badge bg-success fs-6">Total Score: {totalNBAScore} / 1000 Marks (90.8%)</span>
        </div>

        <div className="table-responsive">
          <table className="table table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>Criterion #</th>
                <th>Title</th>
                <th>Max Marks</th>
                <th>Attained Marks</th>
                <th>Attainment %</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {nbaCriteria.map((c, idx) => {
                const pct = ((c.score / c.max) * 100).toFixed(1);
                return (
                  <tr key={idx}>
                    <td className="fw-bold text-primary">Criterion {c.no}</td>
                    <td>{c.title}</td>
                    <td>{c.max}</td>
                    <td className="fw-bold">{c.score}</td>
                    <td>
                      <div className="d-flex align-items-center gap-2">
                        <div className="progress flex-grow-1" style={{ height: '8px' }}>
                          <div className="progress-bar bg-success" style={{ width: `${pct}%` }}></div>
                        </div>
                        <span className="small">{pct}%</span>
                      </div>
                    </td>
                    <td><StatusBadge status={c.status} size="small" /></td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};

export default AccreditationDashboard;
