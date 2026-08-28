import React from 'react';
import Modal from '../common/Modal';

const IDCardPreviewModal = ({ isOpen, onClose, student }) => {
  if (!student) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Smart PVC Student ID Card Preview" size="md">
      <div className="p-3 text-center">
        <div
          className="id-card-pvc card border shadow mx-auto p-3 text-start bg-white rounded-4"
          style={{ width: '320px', minHeight: '460px', borderTop: '8px solid #0d6efd' }}
        >
          <div className="text-center mb-3">
            <h6 className="fw-bold text-primary mb-0">EDUCORE UNIVERSITY</h6>
            <small className="text-muted" style={{ fontSize: '10px' }}>CAMPUS OF ADVANCED TECHNOLOGY</small>
          </div>

          <div className="text-center mb-3">
            <div
              className="rounded-circle bg-light border mx-auto d-flex align-items-center justify-content-center fw-bold fs-3 text-primary shadow-xs"
              style={{ width: '90px', height: '90px' }}
            >
              {student.name?.[0]}
            </div>
          </div>

          <div className="text-center mb-3">
            <h5 className="fw-bold mb-1">{student.name}</h5>
            <span className="badge bg-primary px-3 py-1 mb-1">STUDENT</span>
            <div className="small text-muted">Roll: <strong>{student.roll_number}</strong></div>
          </div>

          <div className="small border-top pt-2 mb-3">
            <div className="d-flex justify-content-between py-1">
              <span className="text-muted">Branch:</span>
              <strong className="text-end">{student.department || 'CSE'}</strong>
            </div>
            <div className="d-flex justify-content-between py-1">
              <span className="text-muted">Valid Till:</span>
              <strong>2027</strong>
            </div>
            <div className="d-flex justify-content-between py-1">
              <span className="text-muted">Blood Group:</span>
              <strong className="text-danger">O+</strong>
            </div>
          </div>

          <div className="text-center mt-auto border-top pt-2">
            <div className="bg-light p-1 rounded font-monospace small text-muted">
              ||| ||||| || |||||| ||| ||||
            </div>
            <small style={{ fontSize: '9px' }} className="text-muted">RFID CHIP EMBEDDED • CRYPTOGRAPHIC SEAL</small>
          </div>
        </div>

        <div className="mt-4">
          <button className="btn btn-outline-secondary me-2" onClick={onClose}>Close</button>
          <button className="btn btn-primary" onClick={() => window.print()}>
            <i className="bi bi-printer me-1"></i>Print ID Card
          </button>
        </div>
      </div>
    </Modal>
  );
};

export default IDCardPreviewModal;
