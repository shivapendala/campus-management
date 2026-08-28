import React from 'react';
import Modal from '../common/Modal';
import StatusBadge from '../common/StatusBadge';

const StudentDossierModal = ({ isOpen, onClose, student }) => {
  if (!student) return null;

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Official Dossier: ${student.name} (${student.roll_number})`}
      size="lg"
    >
      <div className="p-3">
        <div className="d-flex align-items-center gap-3 mb-4 pb-3 border-bottom">
          <div
            className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center fw-bold fs-4"
            style={{ width: '64px', height: '64px' }}
          >
            {student.name?.[0]}
          </div>
          <div>
            <h5 className="fw-bold mb-1">{student.name}</h5>
            <span className="text-muted small me-3">Roll: {student.roll_number}</span>
            <span className="text-muted small me-3">Department: {student.department}</span>
            <StatusBadge status={student.status || 'ACTIVE'} size="small" />
          </div>
        </div>

        <div className="row g-3 mb-4">
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Cumulative CGPA</span>
              <strong className="h4 text-primary mb-0">{student.cgpa || '8.42'}</strong>
            </div>
          </div>
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Attendance %</span>
              <strong className="h4 text-success mb-0">{student.attendance_pct || '87.5'}%</strong>
            </div>
          </div>
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Backlogs</span>
              <strong className="h4 text-dark mb-0">{student.backlogs_count || '0'}</strong>
            </div>
          </div>
        </div>

        <div className="text-end">
          <button className="btn btn-outline-secondary me-2" onClick={onClose}>Close</button>
          <button className="btn btn-primary" onClick={() => window.print()}>
            <i className="bi bi-printer me-1"></i>Print Dossier
          </button>
        </div>
      </div>
    </Modal>
  );
};

export default StudentDossierModal;
