import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';

export const MarksEntryModal = ({
  isOpen,
  onClose,
  onSubmit,
  exam = null,
  loading = false,
}) => {
  const [studentEntries, setStudentEntries] = useState([
    { id: 1, student_id: 'STU-2026-001', name: 'Alex Johnson', internal: 38, external: 56, remarks: 'Excellent project work' },
    { id: 2, student_id: 'STU-2026-002', name: 'Maya Patel', internal: 36, external: 54, remarks: 'Consistent performer' },
    { id: 3, student_id: 'STU-2026-003', name: 'David Lee', internal: 30, external: 45, remarks: 'Good analytical skills' },
    { id: 4, student_id: 'STU-2026-004', name: 'Sophia Martinez', internal: 34, external: 48, remarks: 'Active in class' },
    { id: 5, student_id: 'STU-2026-005', name: 'Liam O\'Connor', internal: 28, external: 42, remarks: 'Satisfactory' },
    { id: 6, student_id: 'STU-2026-006', name: 'Emma Watson', internal: 37, external: 55, remarks: 'Strong fundamentals' },
    { id: 7, student_id: 'STU-2026-007', name: 'Ethan Hunt', internal: 22, external: 28, remarks: 'Needs improvement' },
    { id: 8, student_id: 'STU-2026-008', name: 'Ava Gardner', internal: 35, external: 50, remarks: 'Good lab proficiency' },
  ]);

  const maxInternal = exam?.max_internal_marks || 40;
  const maxExternal = exam?.max_external_marks || 60;
  const totalMax = maxInternal + maxExternal;

  // Grade Derivation Algorithm
  const computeGrade = (total) => {
    const pct = (total / totalMax) * 100;
    if (pct >= 90) return { grade: 'A+', gp: 10.0, badge: 'bg-success', status: 'PASS' };
    if (pct >= 80) return { grade: 'A', gp: 9.0, badge: 'bg-success', status: 'PASS' };
    if (pct >= 70) return { grade: 'B+', gp: 8.0, badge: 'bg-primary', status: 'PASS' };
    if (pct >= 60) return { grade: 'B', gp: 7.0, badge: 'bg-primary', status: 'PASS' };
    if (pct >= 50) return { grade: 'C', gp: 6.0, badge: 'bg-warning text-dark', status: 'PASS' };
    if (pct >= 40) return { grade: 'P', gp: 5.0, badge: 'bg-secondary', status: 'PASS' };
    return { grade: 'F', gp: 0.0, badge: 'bg-danger', status: 'FAIL' };
  };

  const handleInternalChange = (id, val) => {
    const num = Math.min(maxInternal, Math.max(0, Number(val) || 0));
    setStudentEntries((prev) =>
      prev.map((s) => (s.id === id ? { ...s, internal: num } : s))
    );
  };

  const handleExternalChange = (id, val) => {
    const num = Math.min(maxExternal, Math.max(0, Number(val) || 0));
    setStudentEntries((prev) =>
      prev.map((s) => (s.id === id ? { ...s, external: num } : s))
    );
  };

  const handleRemarksChange = (id, val) => {
    setStudentEntries((prev) =>
      prev.map((s) => (s.id === id ? { ...s, remarks: val } : s))
    );
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const payload = studentEntries.map((s) => {
      const total = s.internal + s.external;
      const g = computeGrade(total);
      return {
        student_id: s.student_id,
        internal_marks: s.internal,
        external_marks: s.external,
        marks_obtained: total,
        grade: g.grade,
        grade_point: g.gp,
        remarks: s.remarks,
      };
    });
    onSubmit(payload);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Faculty Marks Entry & Automated Grade Calculation — ${exam?.name || 'Examination'}`}
      size="xl"
    >
      <form onSubmit={handleSubmit}>
        {/* Banner Info */}
        <div className="alert alert-primary p-3 mb-3 d-flex flex-wrap align-items-center justify-content-between gap-2">
          <div>
            <strong>Course:</strong> {exam?.course_code || exam?.course?.code || 'CSE-101'} • <strong>Semester:</strong> {exam?.semester || 'Fall 2026'}
          </div>
          <div className="d-flex gap-2 small">
            <span className="badge bg-white text-primary border">Internal Max: {maxInternal}</span>
            <span className="badge bg-white text-primary border">External Max: {maxExternal}</span>
            <span className="badge bg-white text-dark border fw-bold">Total Max: {totalMax}</span>
          </div>
        </div>

        {/* Ledger Table */}
        <div className="table-responsive mb-4" style={{ maxHeight: '420px', overflowY: 'auto' }}>
          <table className="table table-hover align-middle small mb-0">
            <thead className="table-light sticky-top">
              <tr>
                <th>Student ID & Name</th>
                <th style={{ width: '130px' }}>Internal Marks (/{maxInternal})</th>
                <th style={{ width: '130px' }}>External Marks (/{maxExternal})</th>
                <th style={{ width: '100px' }}>Total (/{totalMax})</th>
                <th style={{ width: '90px' }}>Calculated Grade</th>
                <th style={{ width: '80px' }}>Grade Point</th>
                <th>Instructor Remarks</th>
              </tr>
            </thead>
            <tbody>
              {studentEntries.map((stu) => {
                const total = stu.internal + stu.external;
                const g = computeGrade(total);
                return (
                  <tr key={stu.id}>
                    <td>
                      <strong className="text-primary d-block">{stu.student_id}</strong>
                      <span className="text-dark fw-semibold">{stu.name}</span>
                    </td>
                    <td>
                      <input
                        type="number"
                        min="0"
                        max={maxInternal}
                        className="form-control form-control-sm text-center fw-bold"
                        value={stu.internal}
                        onChange={(e) => handleInternalChange(stu.id, e.target.value)}
                        required
                      />
                    </td>
                    <td>
                      <input
                        type="number"
                        min="0"
                        max={maxExternal}
                        className="form-control form-control-sm text-center fw-bold"
                        value={stu.external}
                        onChange={(e) => handleExternalChange(stu.id, e.target.value)}
                        required
                      />
                    </td>
                    <td>
                      <strong className="fs-6 text-dark">{total}</strong>
                    </td>
                    <td>
                      <span className={`badge ${g.badge} fs-6 px-2 py-1`}>{g.grade}</span>
                    </td>
                    <td>
                      <span className="badge bg-light text-dark border fw-bold">{g.gp.toFixed(1)}</span>
                    </td>
                    <td>
                      <input
                        type="text"
                        className="form-control form-control-sm"
                        placeholder="Remarks..."
                        value={stu.remarks}
                        onChange={(e) => handleRemarksChange(stu.id, e.target.value)}
                      />
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>

        {/* Footer info & Submit */}
        <div className="d-flex justify-content-between align-items-center pt-3 border-top">
          <div className="small text-muted">
            <i className="bi bi-shield-lock-fill text-primary me-1"></i>
            Submitting marks routes the assessment to <strong>Department HOD</strong> for verification before results are declared.
          </div>
          <div className="d-flex gap-2">
            <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold shadow-sm">
              {loading ? 'Calculating & Saving...' : 'Submit Marks for HOD Verification'}
            </button>
          </div>
        </div>
      </form>
    </Modal>
  );
};

export default MarksEntryModal;
