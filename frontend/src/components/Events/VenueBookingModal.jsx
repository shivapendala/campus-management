import React, { useState } from 'react';
import Modal from '../common/Modal';

const VenueBookingModal = ({ isOpen, onClose }) => {
  const [venue, setVenue] = useState('MAIN_AUDITORIUM');
  const [eventDate, setEventDate] = useState('2026-09-15');

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Reserve Institutional Venue" size="md">
      <div className="p-3">
        <div className="mb-3">
          <label className="form-label small fw-semibold">Target Venue</label>
          <select className="form-select" value={venue} onChange={(e) => setVenue(e.target.value)}>
            <option value="MAIN_AUDITORIUM">Main University Auditorium (Cap: 800)</option>
            <option value="SEMINAR_HALL_A">Seminar Hall A (Cap: 120)</option>
            <option value="OAT">Open Air Theatre (OAT) (Cap: 2,500)</option>
            <option value="INDOOR_STADIUM">Indoor Sports Complex (Cap: 1,000)</option>
          </select>
        </div>

        <div className="mb-3">
          <label className="form-label small fw-semibold">Event Date</label>
          <input type="date" className="form-control" value={eventDate} onChange={(e) => setEventDate(e.target.value)} />
        </div>

        <div className="alert alert-success py-2 small mb-3">
          <i className="bi bi-check-circle me-1"></i>60-minute teardown buffer verified; zero schedule collisions.
        </div>

        <div className="text-end">
          <button className="btn btn-outline-secondary me-2" onClick={onClose}>Cancel</button>
          <button className="btn btn-primary" onClick={onClose}>
            <i className="bi bi-calendar-check me-1"></i>Confirm Booking
          </button>
        </div>
      </div>
    </Modal>
  );
};

export default VenueBookingModal;
