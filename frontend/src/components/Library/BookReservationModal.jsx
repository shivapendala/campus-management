import React from 'react';
import Modal from '../common/Modal';

const BookReservationModal = ({ isOpen, onClose, bookTitle = 'Database System Concepts' }) => {
  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Hold & Reserve Book Copy" size="md">
      <div className="p-3">
        <p className="text-muted small">
          All circulating copies of <strong>{bookTitle}</strong> are currently checked out. Place a priority hold to be notified upon return.
        </p>

        <div className="p-3 bg-light rounded mb-3">
          <div className="d-flex justify-content-between py-1 small">
            <span className="text-muted">Queue Position:</span>
            <strong>#2 in Line</strong>
          </div>
          <div className="d-flex justify-content-between py-1 small">
            <span className="text-muted">Estimated Availability:</span>
            <strong>3-5 Days</strong>
          </div>
          <div className="d-flex justify-content-between py-1 small">
            <span className="text-muted">Pickup Window:</span>
            <strong>48 Hours from notification</strong>
          </div>
        </div>

        <div className="text-end">
          <button className="btn btn-outline-secondary me-2" onClick={onClose}>Cancel</button>
          <button className="btn btn-primary" onClick={onClose}>
            <i className="bi bi-bookmark-check me-1"></i>Confirm Reservation
          </button>
        </div>
      </div>
    </Modal>
  );
};

export default BookReservationModal;
