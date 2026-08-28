import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const RecordPaymentModal = ({
  isOpen,
  onClose,
  onSubmit,
  studentFee = null,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    student_id: 'STU-2026-001',
    student_name: 'Alex Johnson',
    fee_structure_id: 1,
    fee_title: 'Fall 2026 CSE Tuition & Lab Fee',
    amount_paid: 4500.0,
    payment_method: 'ONLINE',
    transaction_id: `TXN-PAY-${Math.floor(100000 + Math.random() * 900000)}`,
    remarks: 'Paid in full via Stripe online gateway',
  });

  useEffect(() => {
    if (studentFee) {
      setFormData({
        student_id: studentFee.student_id || 'STU-2026-001',
        student_name: studentFee.student_name || 'Alex Johnson',
        fee_structure_id: studentFee.fee_structure_id || 1,
        fee_title: studentFee.fee_title || 'Fall 2026 CSE Tuition & Lab Fee',
        amount_paid: studentFee.balance_remaining || studentFee.total_billed || 4500.0,
        payment_method: 'ONLINE',
        transaction_id: `TXN-CAMPUS-${Math.floor(100000 + Math.random() * 900000)}`,
        remarks: 'Payment processed successfully.',
      });
    }
  }, [studentFee, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      amount_paid: Number(formData.amount_paid),
      invoice_number: `INV-${Date.now().toString().slice(-8)}`,
      payment_date: new Date().toISOString(),
      status: 'SUCCESS',
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Process Fee Payment — ${formData.student_name} (${formData.student_id})`}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-center mb-1">
            <strong className="text-dark">{formData.student_name} ({formData.student_id})</strong>
            <span className="badge bg-primary">Account Dues</span>
          </div>
          <div className="small text-muted">{formData.fee_title}</div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Payment Amount ($ USD)"
              type="number"
              step="50"
              name="amount_paid"
              value={formData.amount_paid}
              onChange={(e) => setFormData({ ...formData, amount_paid: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Payment Method / Channel"
              type="select"
              name="payment_method"
              value={formData.payment_method}
              options={[
                { value: 'ONLINE', label: 'Online Payment Gateway (Stripe/Cards)' },
                { value: 'CREDIT_CARD', label: 'Credit Card (POS Terminal)' },
                { value: 'DEBIT_CARD', label: 'Debit Card' },
                { value: 'NET_BANKING', label: 'Direct Net Banking Transfer' },
                { value: 'CHEQUE', label: 'Cheque / Demand Draft' },
                { value: 'CASH', label: 'Cash at Bursar Desk' },
              ]}
              onChange={(e) => setFormData({ ...formData, payment_method: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Transaction Reference / Cheque #"
              name="transaction_id"
              placeholder="e.g. TXN-CAMPUS-982347"
              value={formData.transaction_id}
              onChange={(e) => setFormData({ ...formData, transaction_id: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Bursar Notes / Remarks"
              name="remarks"
              placeholder="e.g. Paid in full"
              value={formData.remarks}
              onChange={(e) => setFormData({ ...formData, remarks: e.target.value })}
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-success btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Processing...' : 'Confirm & Generate Receipt'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default RecordPaymentModal;
