import React from 'react';
import Modal from '../common/Modal';
import StatusBadge from '../common/StatusBadge';

const FeeInstallmentModal = ({ isOpen, onClose, totalFee = 120000 }) => {
  const tranches = [
    { no: 1, dueDate: '2026-09-01', amount: totalFee / 3, status: 'PAID' },
    { no: 2, dueDate: '2026-12-01', amount: totalFee / 3, status: 'PENDING' },
    { no: 3, dueDate: '2027-03-01', amount: totalFee / 3, status: 'PENDING' },
  ];

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Tuition Fee Installment Schedule" size="md">
      <div className="p-3">
        <div className="alert alert-info py-2 small mb-3">
          Annual fee partitioned into 3 equal tranches (every 90 days). Grace period of 7 days applies.
        </div>

        <div className="table-responsive mb-4">
          <table className="table table-sm table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>Tranche</th>
                <th>Due Date</th>
                <th>Amount</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {tranches.map((t, idx) => (
                <tr key={idx}>
                  <td className="fw-bold">Installment #{t.no}</td>
                  <td>{t.dueDate}</td>
                  <td className="fw-semibold">Rs. {t.amount.toLocaleString()}</td>
                  <td><StatusBadge status={t.status} size="small" /></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="text-end">
          <button className="btn btn-primary" onClick={onClose}>Close</button>
        </div>
      </div>
    </Modal>
  );
};

export default FeeInstallmentModal;
