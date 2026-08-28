import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const NepCreditAnalyzer = () => {
  const [studentId, setStudentId] = useState('');
  const [courseCode, setCourseCode] = useState('');
  const [courseName, setCourseName] = useState('');
  const [credits, setCredits] = useState('4');
  const [category, setCategory] = useState('CORE');
  const [gradePoints, setGradePoints] = useState('10');
  const [ledgers, setLedgers] = useState([
    { id: '1', course: 'CS101 Programming Basics', category: 'CORE', credits: 4, grade: 9, points: 36 },
    { id: '2', course: 'MA102 Linear Algebra', category: 'MULTIDISCIPLINARY', credits: 3, grade: 8, points: 24 },
    { id: '3', course: 'HS103 Communication Skills', category: 'ABILITY_ENHANCEMENT', credits: 2, grade: 10, points: 20 },
    { id: '4', course: 'CE104 Environmental Science', category: 'VALUE_ADDED', credits: 2, grade: 9, points: 18 }
  ]);

  const columns = [
    { key: 'course', label: 'Course Code & Description' },
    { key: 'category', label: 'NEP Category', render: (val) => <span className="badge bg-secondary">{val}</span> },
    { key: 'credits', label: 'Credits Allocated' },
    { key: 'grade', label: 'Grade Points Obtained' },
    { key: 'points', label: 'Weighted Points', render: (val) => <strong>{val}</strong> }
  ];

  const handleAddCredit = (e) => {
    e.preventDefault();
    if (!courseCode || !courseName) return;

    const credVal = parseInt(credits) || 0;
    const gradeVal = parseInt(gradePoints) || 0;
    const wPoints = credVal * gradeVal;

    const newLedger = {
      id: String(ledgers.length + 1),
      course: `${courseCode} ${courseName}`,
      category: category,
      credits: credVal,
      grade: gradeVal,
      points: wPoints
    };

    setLedgers((prev) => [...prev, newLedger]);
    setCourseCode('');
    setCourseName('');
  };

  const totalCredits = ledgers.reduce((acc, curr) => acc + curr.credits, 0);
  const totalPoints = ledgers.reduce((acc, curr) => acc + curr.points, 0);
  const sgpa = totalCredits > 0 ? (totalPoints / totalCredits).toFixed(2) : '0.00';

  const getExitAward = () => {
    if (totalCredits >= 160) return { title: 'B.Tech (Honours/Research)', color: 'text-success' };
    if (totalCredits >= 120) return { title: 'Bachelor of Technology', color: 'text-info' };
    if (totalCredits >= 80) return { title: 'Undergraduate Diploma', color: 'text-warning' };
    if (totalCredits >= 40) return { title: 'Undergraduate Certificate', color: 'text-primary' };
    return { title: 'No Award (Minimum 40 Credits required)', color: 'text-danger' };
  };

  const award = getExitAward();

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-bank2 me-2"></i>NEP Credit & SGPA Analyzer
          </h2>
          <p className="text-muted mb-0">
            Monitor student credit accumulation in Academic Bank of Credits (ABC) and evaluate multiple entry-exit options.
          </p>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-4">
          <div className="p-3 bg-white shadow-sm rounded-3 border-start border-primary border-4 d-flex justify-content-between align-items-center">
            <div>
              <div className="small text-muted fw-bold">Total Accumulated Credits</div>
              <h3 className="fw-bold text-primary mb-0">{totalCredits} Credits</h3>
            </div>
            <i className="bi bi-award fs-2 text-primary"></i>
          </div>
        </div>
        <div className="col-md-4">
          <div className="p-3 bg-white shadow-sm rounded-3 border-start border-success border-4 d-flex justify-content-between align-items-center">
            <div>
              <div className="small text-muted fw-bold">Calculated SGPA</div>
              <h3 className="fw-bold text-success mb-0">{sgpa} / 10.00</h3>
            </div>
            <i className="bi bi-calculator fs-2 text-success"></i>
          </div>
        </div>
        <div className="col-md-4">
          <div className="p-3 bg-white shadow-sm rounded-3 border-start border-info border-4 d-flex justify-content-between align-items-center">
            <div>
              <div className="small text-muted fw-bold">Eligible Exit Award</div>
              <h5 className={`fw-bold mb-0 ${award.color}`}>{award.title}</h5>
            </div>
            <i className="bi bi-box-arrow-right fs-2 text-info"></i>
          </div>
        </div>
      </div>

      <div className="row g-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-plus-circle me-2"></i>Record Academic Credit</h5>
            <form onSubmit={handleAddCredit}>
              <div className="row g-2 mb-3">
                <div className="col-md-4">
                  <label className="form-label small fw-bold">Code</label>
                  <input
                    type="text"
                    className="form-control"
                    value={courseCode}
                    onChange={(e) => setCourseCode(e.target.value.toUpperCase())}
                    placeholder="e.g. EC301"
                    required
                  />
                </div>
                <div className="col-md-8">
                  <label className="form-label small fw-bold">Course Title</label>
                  <input
                    type="text"
                    className="form-control"
                    value={courseName}
                    onChange={(e) => setCourseName(e.target.value)}
                    placeholder="e.g. Microprocessors"
                    required
                  />
                </div>
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">NEP Category</label>
                <select className="form-select" value={category} onChange={(e) => setCategory(e.target.value)}>
                  <option value="CORE">Major Core</option>
                  <option value="ELECTIVE">Minor Elective</option>
                  <option value="MULTIDISCIPLINARY">Multidisciplinary</option>
                  <option value="ABILITY_ENHANCEMENT">Ability Enhancement (AEC)</option>
                  <option value="SKILL_ENHANCEMENT">Skill Enhancement (SEC)</option>
                  <option value="VALUE_ADDED">Value Added Course (VAC)</option>
                </select>
              </div>
              <div className="row g-2 mb-3">
                <div className="col-md-6">
                  <label className="form-label small fw-bold">Credits</label>
                  <select className="form-select" value={credits} onChange={(e) => setCredits(e.target.value)}>
                    <option value="1">1 Credit</option>
                    <option value="2">2 Credits</option>
                    <option value="3">3 Credits</option>
                    <option value="4">4 Credits</option>
                  </select>
                </div>
                <div className="col-md-6">
                  <label className="form-label small fw-bold">Grade Points</label>
                  <select className="form-select" value={gradePoints} onChange={(e) => setGradePoints(e.target.value)}>
                    <option value="10">O (10 Points)</option>
                    <option value="9">A+ (9 Points)</option>
                    <option value="8">A (8 Points)</option>
                    <option value="7">B+ (7 Points)</option>
                    <option value="6">B (6 Points)</option>
                    <option value="5">C (5 Points)</option>
                  </select>
                </div>
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-cloud-arrow-up-fill me-1"></i>Deposit Credits in Ledger
              </button>
            </form>
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-journal-text me-2"></i>Academic Bank of Credits Ledger</h5>
            <AdvancedDataTable columns={columns} data={ledgers} searchPlaceholder="Search deposited credits..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default NepCreditAnalyzer;
