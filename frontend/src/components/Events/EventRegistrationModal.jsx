import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const EventRegistrationModal = ({
  isOpen,
  onClose,
  onSubmit,
  selectedEvent = null,
  loading = false,
}) => {
  const [studentId, setStudentId] = useState('STU-2026-001');
  const [studentName, setStudentName] = useState('Alex Johnson');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      event_id: selectedEvent?.id,
      student_id: studentId,
      student_name: studentName,
      registered_at: new Date().toISOString(),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Register Pass — ${selectedEvent?.title || 'Campus Event'}`}
      size="md"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-center mb-1">
            <strong className="text-dark">{selectedEvent?.title}</strong>
            <span className="badge bg-primary">{selectedEvent?.event_type}</span>
          </div>
          <small className="text-muted d-block">Venue: {selectedEvent?.venue}</small>
          <small className="text-muted d-block">Time: {selectedEvent?.start_time ? new Date(selectedEvent.start_time).toLocaleString() : 'TBD'}</small>
        </div>

        <div className="mb-3">
          <FormField
            label="Student ID"
            name="student_id"
            value={studentId}
            onChange={(e) => setStudentId(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <FormField
            label="Full Name"
            name="student_name"
            value={studentName}
            onChange={(e) => setStudentName(e.target.value)}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-success btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Confirming...' : 'Claim Registration Pass'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default EventRegistrationModal;
