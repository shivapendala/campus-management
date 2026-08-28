import React from 'react';
import Modal from '../common/Modal';

export const ConflictAlertModal = ({ isOpen, onClose, conflicts = [] }) => {
  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="⚠️ Timetable Scheduling Collision Detected"
      size="md"
    >
      <div className="alert alert-danger p-3 mb-3 d-flex align-items-center gap-2">
        <i className="bi bi-exclamation-triangle-fill fs-4 text-danger"></i>
        <div>
          <strong>Conflict Prevention Guard:</strong> The proposed schedule overlaps with existing academic bookings.
        </div>
      </div>

      <div className="d-flex flex-column gap-2 mb-4">
        {conflicts.map((c, i) => (
          <div key={i} className="p-3 bg-light rounded-3 border border-danger-subtle d-flex align-items-start gap-2">
            <span className="badge bg-danger mt-1">Conflict</span>
            <div className="small text-dark">
              <strong>{c.type?.replace('_', ' ')}:</strong> {c.message}
            </div>
          </div>
        ))}
      </div>

      <div className="d-flex justify-content-end pt-3 border-top">
        <button type="button" className="btn btn-primary btn-sm px-4 fw-semibold" onClick={onClose}>
          Adjust Slot Parameters
        </button>
      </div>
    </Modal>
  );
};

export default ConflictAlertModal;
