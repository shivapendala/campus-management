import React from 'react';
import Modal from '../common/Modal';

export const FeeReceiptModal = ({ isOpen, onClose, receipt = null }) => {
  const data = receipt || {
    invoice_number: 'INV-2026-982347',
    transaction_id: 'TXN-CAMPUS-982347',
    payment_date: '2026-08-25T14:30:00Z',
    payment_method: 'Online Gateway (Stripe)',
    status: 'SUCCESS',
    student: {
      student_id: 'STU-2026-001',
      name: 'Alex Johnson',
      department: 'Computer Science & Engineering',
      year: 2,
      section: 'A',
    },
    fee_structure: {
      title: 'Fall 2026 CSE Tuition & Lab Assessment Fee',
      category: 'Semester Academic Tuition',
      semester: 4,
      total_billed: 4500.0,
    },
    amount_paid: 4500.0,
    balance_remaining: 0.0,
    issued_by: 'Campus Office of the Bursar & Accounts',
    tax_id: 'US-EDU-CAMPUS-948201',
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Official Institutional Fee Payment Receipt"
      size="lg"
    >
      {/* Institutional Receipt Sheet */}
      <div className="p-4 bg-white rounded-3 border mb-3" style={{ border: '2px solid #e2e8f0' }}>
        {/* Receipt Header */}
        <div className="d-flex justify-content-between align-items-start border-bottom pb-3 mb-3">
          <div>
            <span className="badge bg-primary px-3 py-1 mb-2 fw-bold">
              OFFICIAL ACADEMIC FEE RECEIPT
            </span>
            <h4 className="fw-bold text-dark mb-0">Campus Management University</h4>
            <small className="text-muted">Office of Financial Affairs & Bursar • Tax ID: {data.tax_id}</small>
          </div>
          <div className="text-end">
            <h6 className="fw-bold text-primary mb-0">{data.invoice_number}</h6>
            <small className="text-muted d-block">
              Date: {new Date(data.payment_date).toLocaleDateString()}
            </small>
            <span className="badge bg-success mt-1">PAID IN FULL</span>
          </div>
        </div>

        {/* Student & Payment Metadata */}
        <div className="row g-3 mb-3 small">
          <div className="col-12 col-md-6">
            <div className="p-2 bg-light rounded border">
              <strong className="text-secondary d-block">Student Details:</strong>
              <div className="fw-bold text-dark">{data.student?.name}</div>
              <div>ID: <strong className="text-primary">{data.student?.student_id}</strong></div>
              <div>Dept: {data.student?.department} (Yr {data.student?.year} Sec {data.student?.section})</div>
            </div>
          </div>
          <div className="col-12 col-md-6">
            <div className="p-2 bg-light rounded border">
              <strong className="text-secondary d-block">Transaction Details:</strong>
              <div>Ref ID: <strong className="text-dark">{data.transaction_id}</strong></div>
              <div>Method: {data.payment_method}</div>
              <div>Status: <span className="text-success fw-bold">Verified Success</span></div>
            </div>
          </div>
        </div>

        {/* Breakdown Table */}
        <div className="table-responsive mb-3">
          <table className="table table-bordered align-middle small mb-0">
            <thead className="table-light">
              <tr>
                <th>Description / Fee Item</th>
                <th>Category</th>
                <th className="text-end">Billed Amount</th>
                <th className="text-end">Paid Amount</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <strong>{data.fee_structure?.title}</strong>
                  <div className="text-muted small">Semester {data.fee_structure?.semester} Registration</div>
                </td>
                <td>{data.fee_structure?.category}</td>
                <td className="text-end">${Number(data.fee_structure?.total_billed).toLocaleString()}</td>
                <td className="text-end fw-bold text-success">${Number(data.amount_paid).toLocaleString()}</td>
              </tr>
            </tbody>
            <tfoot className="table-light">
              <tr>
                <th colSpan="3" className="text-end">Total Amount Paid:</th>
                <th className="text-end text-success fs-6">${Number(data.amount_paid).toLocaleString()}</th>
              </tr>
              <tr>
                <th colSpan="3" className="text-end">Outstanding Balance:</th>
                <th className="text-end text-muted">${Number(data.balance_remaining).toLocaleString()}</th>
              </tr>
            </tfoot>
          </table>
        </div>

        {/* Footer Seal & Stamps */}
        <div className="d-flex justify-content-between align-items-center pt-3 border-top small text-muted">
          <div>
            <i className="bi bi-shield-check text-success fs-5 me-1"></i>
            <span>Digitally certified by <strong>{data.issued_by}</strong>.</span>
          </div>
          <div className="text-end">
            <div className="text-dark fw-bold">[ Digitally Signed ]</div>
            <small>Chief Financial Officer</small>
          </div>
        </div>
      </div>

      {/* Action Buttons */}
      <div className="d-flex justify-content-end gap-2 pt-2">
        <button type="button" className="btn btn-outline-secondary btn-sm px-3" onClick={() => window.print()}>
          <i className="bi bi-printer-fill me-1"></i> Print / Download PDF
        </button>
        <button type="button" className="btn btn-primary btn-sm px-4 fw-semibold" onClick={onClose}>
          Close Receipt
        </button>
      </div>
    </Modal>
  );
};

export default FeeReceiptModal;
