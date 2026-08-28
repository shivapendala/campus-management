import React from 'react';
import Modal from '../common/Modal';

const LedgerVoucherModal = ({ isOpen, onClose, voucher }) => {
  if (!voucher) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={`Accounting Journal Voucher: ${voucher.tx_id}`} size="md">
      <div className="p-3">
        <div className="border-bottom pb-2 mb-3">
          <div className="text-muted small">Description</div>
          <div className="fw-semibold">{voucher.description}</div>
        </div>

        <div className="table-responsive mb-3">
          <table className="table table-bordered table-sm align-middle">
            <thead className="table-light">
              <tr>
                <th>Account Head</th>
                <th className="text-end">Debit (Rs.)</th>
                <th className="text-end">Credit (Rs.)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{voucher.debit}</td>
                <td className="text-end text-success fw-bold">65,000.00</td>
                <td className="text-end">-</td>
              </tr>
              <tr>
                <td>{voucher.credit}</td>
                <td className="text-end">-</td>
                <td className="text-end text-primary fw-bold">65,000.00</td>
              </tr>
              <tr className="table-light fw-bold">
                <td>Total Balance</td>
                <td className="text-end">65,000.00</td>
                <td className="text-end">65,000.00</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div className="text-end">
          <button className="btn btn-secondary" onClick={onClose}>Close</button>
        </div>
      </div>
    </Modal>
  );
};

export default LedgerVoucherModal;
