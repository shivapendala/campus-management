import React from 'react';
import Modal from '../common/Modal';

export const StudentGradeCardModal = ({ isOpen, onClose, gradeCard = null }) => {
  const data = gradeCard || {
    student_id: 'STU-2026-001',
    student_name: 'Alex Johnson',
    department: 'Computer Science & Engineering',
    semester: 'Semester 4 (Fall 2026)',
    total_credits: 19,
    sgpa: 9.68,
    academic_standing: 'FIRST CLASS WITH DISTINCTION',
    is_published: true,
    verified_by: 'Dr. Alan Smith (HOD & Dean)',
    results: [
      { code: 'CSE-101', title: 'Data Structures & Algorithms', credits: 4, internal: 38, external: 56, total: 94, max: 100, grade: 'A+', grade_point: 10.0, status: 'PASS' },
      { code: 'CSE-202', title: 'Database Management Systems (DBMS)', credits: 4, internal: 36, external: 54, total: 90, max: 100, grade: 'A+', grade_point: 10.0, status: 'PASS' },
      { code: 'CSE-301', title: 'Operating Systems', credits: 4, internal: 35, external: 51, total: 86, max: 100, grade: 'A', grade_point: 9.0, status: 'PASS' },
      { code: 'CSE-302', title: 'Computer Networks', credits: 3, internal: 33, external: 48, total: 81, max: 100, grade: 'A', grade_point: 9.0, status: 'PASS' },
      { code: 'CSE-401', title: 'Machine Learning & Neural Networks', credits: 4, internal: 39, external: 56, total: 95, max: 100, grade: 'A+', grade_point: 10.0, status: 'PASS' },
    ],
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Official Grade Card & Examination Results Dossier"
      size="lg"
    >
      {/* Institutional Grade Sheet Header */}
      <div className="p-3 bg-light rounded-3 border mb-3">
        <div className="d-flex justify-content-between align-items-start border-bottom pb-2 mb-2">
          <div>
            <h5 className="fw-bold text-dark mb-0">{data.student_name}</h5>
            <div className="small text-muted">
              Student ID: <strong className="text-primary">{data.student_id}</strong> • {data.department}
            </div>
          </div>
          <div className="text-end">
            <span className="badge bg-success px-3 py-1 fw-bold fs-6">
              SGPA: {data.sgpa}
            </span>
            <small className="d-block text-muted mt-1">{data.semester}</small>
          </div>
        </div>

        <div className="d-flex flex-wrap justify-content-between small text-secondary">
          <span>Total Credits Registered: <strong>{data.total_credits} Credits</strong></span>
          <span>Standing: <strong className="text-success">{data.academic_standing}</strong></span>
          <span>Verified By: <strong>{data.verified_by}</strong></span>
        </div>
      </div>

      {/* Results Table */}
      <div className="table-responsive mb-3">
        <table className="table table-bordered align-middle small mb-0">
          <thead className="table-light">
            <tr>
              <th>Course Code & Title</th>
              <th className="text-center">Credits</th>
              <th className="text-center">Internal (40)</th>
              <th className="text-center">External (60)</th>
              <th className="text-center">Total (100)</th>
              <th className="text-center">Grade</th>
              <th className="text-center">Grade Point</th>
              <th className="text-center">Result</th>
            </tr>
          </thead>
          <tbody>
            {data.results?.map((r, i) => (
              <tr key={i}>
                <td>
                  <strong className="text-primary">{r.code}</strong>
                  <div className="text-dark">{r.title}</div>
                </td>
                <td className="text-center">{r.credits}</td>
                <td className="text-center">{r.internal}</td>
                <td className="text-center">{r.external}</td>
                <td className="text-center fw-bold">{r.total}</td>
                <td className="text-center">
                  <span className={`badge ${r.grade === 'A+' || r.grade === 'A' ? 'bg-success' : 'bg-primary'}`}>
                    {r.grade}
                  </span>
                </td>
                <td className="text-center fw-bold">{r.grade_point}</td>
                <td className="text-center">
                  <span className="badge bg-success-subtle text-success border border-success-subtle px-2 py-1">
                    {r.status}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Official Stamp & Actions */}
      <div className="d-flex justify-content-between align-items-center pt-3 border-top">
        <div className="small text-muted d-flex align-items-center gap-2">
          <i className="bi bi-patch-check-fill text-success fs-5"></i>
          <span>Digitally Verified & Signed by Controller of Examinations.</span>
        </div>
        <div className="d-flex gap-2">
          <button type="button" className="btn btn-outline-secondary btn-sm" onClick={() => window.print()}>
            <i className="bi bi-printer me-1"></i> Print Grade Sheet
          </button>
          <button type="button" className="btn btn-primary btn-sm px-4 fw-semibold" onClick={onClose}>
            Close Dossier
          </button>
        </div>
      </div>
    </Modal>
  );
};

export default StudentGradeCardModal;
