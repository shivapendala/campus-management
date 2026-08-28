import React, { useState } from 'react';
import Modal from '../common/Modal';

const FineCalculatorModal = ({ isOpen, onClose }) => {
  const [daysOverdue, setDaysOverdue] = useState(12);

  const calculateFine = (days) => {
    if (days <= 0) return 0;
    let fine = 0;
    fine += Math.min(7, days) * 2;
    if (days > 7) fine += Math.min(14, days - 7) * 5;
    if (days > 21) fine += (days - 21) * 10;
    return fine;
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Overdue Fine Calculator" size="md">
      <div className="p-3">
        <div className="mb-3">
          <label className="form-label small fw-semibold">Days Overdue (Excluding Holidays)</label>
          <input
            type="number"
            className="form-control"
            value={daysOverdue}
            onChange={(e) => setDaysOverdue(parseInt(e.target.value) || 0)}
          />
        </div>

        <div className="p-3 bg-light rounded text-center mb-3">
          <span className="text-muted small d-block">Computed Library Fine</span>
          <strong className="h3 text-danger mb-0">Rs. {calculateFine(daysOverdue)}</strong>
        </div>

        <div className="text-end">
          <button className="btn btn-secondary" onClick={onClose}>Close</button>
        </div>
      </div>
    </Modal>
  );
};

export default FineCalculatorModal;
