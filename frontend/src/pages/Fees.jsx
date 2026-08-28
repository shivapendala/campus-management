import React, { useState, useEffect } from 'react';
import { feeService } from '../services';
import StatCard from '../components/StatCard';
import FeeStructureModal from '../components/Fees/FeeStructureModal';
import RecordPaymentModal from '../components/Fees/RecordPaymentModal';
import FeeReceiptModal from '../components/Fees/FeeReceiptModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Fees = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [activeTab, setActiveTab] = useState('student-dues'); // 'student-dues', 'structures', 'history'
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Financial KPIs
  const [summary, setSummary] = useState({
    total_fees: 11025000,
    collected_fees: 9580000,
    pending_fees: 1445000,
    overdue_fees: 320000,
    collection_rate_percentage: 86.9,
    pending_accounts_count: 320,
  });

  // Modals
  const structureModal = useModal();
  const paymentModal = useModal();
  const receiptModal = useModal();
  const deleteModal = useModal();

  // Filters & Search
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('ALL');

  // Fee Structures State
  const [structures, setStructures] = useState([
    { id: 1, title: 'Fall 2026 CSE Semester Tuition & Lab Fee', category_name: 'Semester Tuition Fee', department_code: 'CSE', semester: 4, amount: 4500, due_date: '2026-09-30' },
    { id: 2, title: 'Fall 2026 ECE Hardware & Silicon Lab Fee', category_name: 'Laboratory Fee', department_code: 'ECE', semester: 4, amount: 4200, due_date: '2026-09-30' },
    { id: 3, title: 'Fall 2026 EEE Embedded Microcontrollers Fee', category_name: 'Semester Tuition Fee', department_code: 'EEE', semester: 6, amount: 4100, due_date: '2026-09-30' },
    { id: 4, title: 'Fall 2026 MECH Thermal Workshop Assessment', category_name: 'Laboratory Fee', department_code: 'MECH', semester: 5, amount: 3900, due_date: '2026-09-30' },
    { id: 5, title: 'Fall 2026 Campus Technology & Library Access', category_name: 'Technology Fee', department_code: 'ALL', semester: 1, amount: 450, due_date: '2026-09-15' },
  ]);

  // Student Fees Ledger State
  const [studentFees, setStudentFees] = useState([
    { id: 1, student_id: 'STU-2026-001', student_name: 'Alex Johnson', department: 'CSE', year: 2, section: 'A', fee_title: 'Fall 2026 CSE Tuition & Lab Fee', total_billed: 4500, amount_paid: 4500, balance_remaining: 0, status: 'PAID', due_date: '2026-09-30', invoice_number: 'INV-2026-982347' },
    { id: 2, student_id: 'STU-2026-002', student_name: 'Maya Patel', department: 'CSE', year: 2, section: 'A', fee_title: 'Fall 2026 CSE Tuition & Lab Fee', total_billed: 4500, amount_paid: 2250, balance_remaining: 2250, status: 'PARTIAL', due_date: '2026-09-30', invoice_number: 'INV-2026-982348' },
    { id: 3, student_id: 'STU-2026-003', student_name: 'David Lee', department: 'EEE', year: 3, section: 'B', fee_title: 'Fall 2026 EEE Embedded Microcontrollers Fee', total_billed: 4100, amount_paid: 0, balance_remaining: 4100, status: 'PENDING', due_date: '2026-09-30', invoice_number: 'INV-2026-982349' },
    { id: 4, student_id: 'STU-2026-004', student_name: 'Sophia Martinez', department: 'ECE', year: 1, section: 'A', fee_title: 'Fall 2026 ECE Hardware & Silicon Lab Fee', total_billed: 4200, amount_paid: 0, balance_remaining: 4200, status: 'OVERDUE', due_date: '2026-08-15', invoice_number: 'INV-2026-982350' },
    { id: 5, student_id: 'STU-2026-005', student_name: 'Liam O\'Connor', department: 'MECH', year: 2, section: 'C', fee_title: 'Fall 2026 MECH Thermal Workshop Assessment', total_billed: 3900, amount_paid: 3900, balance_remaining: 0, status: 'PAID', due_date: '2026-09-30', invoice_number: 'INV-2026-982351' },
  ]);

  // Payment History State
  const [payments, setPayments] = useState([
    { id: 1, invoice_number: 'INV-2026-982347', student_id: 'STU-2026-001', student_name: 'Alex Johnson', amount_paid: 4500, payment_method: 'Online Gateway (Stripe)', transaction_id: 'TXN-CAMPUS-982347', payment_date: '2026-08-25T14:30:00Z', status: 'SUCCESS' },
    { id: 2, invoice_number: 'INV-2026-982348', student_id: 'STU-2026-002', student_name: 'Maya Patel', amount_paid: 2250, payment_method: 'Credit Card', transaction_id: 'TXN-CAMPUS-982348', payment_date: '2026-08-26T10:15:00Z', status: 'SUCCESS' },
    { id: 3, invoice_number: 'INV-2026-982351', student_id: 'STU-2026-005', student_name: 'Liam O\'Connor', amount_paid: 3900, payment_method: 'Net Banking', transaction_id: 'TXN-CAMPUS-982351', payment_date: '2026-08-27T16:45:00Z', status: 'SUCCESS' },
  ]);

  const fetchFeesData = async () => {
    setLoading(true);
    try {
      const summaryRes = await feeService.getFinancialSummary();
      if (summaryRes) setSummary(summaryRes);
    } catch (err) {
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchFeesData();
  }, []);

  // Filter Student Fees
  const filteredStudentFees = studentFees.filter((item) => {
    const matchesSearch =
      item.student_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.student_id.toLowerCase().includes(searchTerm.toLowerCase()) ||
      item.department.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = statusFilter === 'ALL' || item.status === statusFilter;
    return matchesSearch && matchesStatus;
  });

  // Handle Create/Edit Structure
  const handleStructureSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (structureModal.modalData?.isEdit) {
        setStructures((prev) =>
          prev.map((s) => (s.id === structureModal.modalData.structure.id ? { ...s, ...formData } : s))
        );
        showSuccess(`Fee structure "${formData.title}" updated.`);
      } else {
        const newS = { ...formData, id: Date.now() };
        setStructures([...structures, newS]);
        showSuccess(`Defined fee structure "${formData.title}".`);
      }
      structureModal.closeModal();
    } catch (err) {
      showError('Failed to save fee structure.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Process Payment
  const handlePaymentSubmit = async (paymentData) => {
    setActionLoading(true);
    try {
      const targetStudentFee = paymentModal.modalData?.studentFee;
      const newPaid = Number(paymentData.amount_paid);

      // Update student fee status
      setStudentFees((prev) =>
        prev.map((s) => {
          if (s.id === targetStudentFee.id) {
            const updatedPaid = s.amount_paid + newPaid;
            const updatedBal = Math.max(0, s.total_billed - updatedPaid);
            const updatedStatus = updatedBal === 0 ? 'PAID' : 'PARTIAL';
            return {
              ...s,
              amount_paid: updatedPaid,
              balance_remaining: updatedBal,
              status: updatedStatus,
            };
          }
          return s;
        })
      );

      // Add to payment history
      const newP = {
        id: Date.now(),
        invoice_number: paymentData.invoice_number,
        student_id: paymentData.student_id,
        student_name: paymentData.student_name,
        amount_paid: newPaid,
        payment_method: paymentData.payment_method,
        transaction_id: paymentData.transaction_id,
        payment_date: paymentData.payment_date,
        status: 'SUCCESS',
      };
      setPayments([newP, ...payments]);

      // Update summary KPI
      setSummary((prev) => ({
        ...prev,
        collected_fees: prev.collected_fees + newPaid,
        pending_fees: Math.max(0, prev.pending_fees - newPaid),
      }));

      paymentModal.closeModal();
      showSuccess(`Payment of $${newPaid.toLocaleString()} recorded for ${paymentData.student_name}!`);
    } catch (err) {
      showError('Failed to process payment.');
    } finally {
      setActionLoading(false);
    }
  };

  // Export CSV
  const handleExportCSV = () => {
    const headers = 'Invoice Number,Student ID,Student Name,Department,Fee Title,Billed Amount,Amount Paid,Balance Remaining,Status,Due Date\n';
    const rows = studentFees
      .map(
        (s) =>
          `"${s.invoice_number}","${s.student_id}","${s.student_name}","${s.department}","${s.fee_title}",${s.total_billed},${s.amount_paid},${s.balance_remaining},"${s.status}","${s.due_date}"`
      )
      .join('\n');
    const blob = new Blob([headers + rows], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.setAttribute('href', url);
    link.setAttribute('download', `Fee_Collection_Report_Fall_2026.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showSuccess('Exported Financial Fee Collection Report to CSV.');
  };

  const getStatusBadge = (status) => {
    switch (status) {
      case 'PAID':
        return <span className="badge bg-success px-3 py-1">Paid in Full</span>;
      case 'PARTIAL':
        return <span className="badge bg-info px-3 py-1">Partial Payment</span>;
      case 'PENDING':
        return <span className="badge bg-warning text-dark px-3 py-1">Pending Due</span>;
      case 'OVERDUE':
        return <span className="badge bg-danger px-3 py-1">⚠️ Overdue Notice</span>;
      default:
        return <span className="badge bg-secondary px-3 py-1">{status}</span>;
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Fees & Institutional Finance</h2>
          <p className="text-muted mb-0">
            Tuition structures, student accounts, payment transactions, pending dues, and official receipts
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={handleExportCSV}
            className="btn btn-outline-success btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-file-earmark-spreadsheet-fill"></i>
            <span>Export CSV</span>
          </button>
          <button
            onClick={() => structureModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-plus-circle-fill"></i>
            <span>Define Fee Structure</span>
          </button>
        </div>
      </div>

      {/* Financial Dashboard KPI Row */}
      <div className="row g-3 mb-4">
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Total Billed Fees"
            value={`$${(summary.total_fees / 1000000).toFixed(2)}M`}
            change="Fall 2026 Academic Term"
            isPositive={true}
            icon="bi-wallet2"
            gradientClass="bg-gradient-primary"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Collected Revenue"
            value={`$${(summary.collected_fees / 1000000).toFixed(2)}M`}
            change={`${summary.collection_rate_percentage}% Collection Rate`}
            isPositive={true}
            icon="bi-cash-coin"
            gradientClass="bg-gradient-emerald"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Pending Receivables"
            value={`$${(summary.pending_fees / 1000000).toFixed(2)}M`}
            change={`${summary.pending_accounts_count} Accounts Pending`}
            isPositive={false}
            icon="bi-hourglass-split"
            gradientClass="bg-gradient-amber"
          />
        </div>
        <div className="col-12 col-sm-6 col-xl-3">
          <StatCard
            title="Critical Overdue"
            value={`$${(summary.overdue_fees / 1000).toFixed(0)}K`}
            change="Notice Alerts Dispatched"
            isPositive={false}
            icon="bi-exclamation-triangle-fill"
            gradientClass="bg-gradient-rose"
          />
        </div>
      </div>

      {/* Navigation Tabs */}
      <ul className="nav nav-pills mb-4 gap-2">
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'student-dues' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('student-dues')}
          >
            <i className="bi bi-people-fill me-1"></i>
            Student Accounts & Dues ({filteredStudentFees.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'structures' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('structures')}
          >
            <i className="bi bi-layers-fill me-1"></i>
            Institutional Fee Structures ({structures.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'history' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('history')}
          >
            <i className="bi bi-receipt me-1"></i>
            Payment Transaction History ({payments.length})
          </button>
        </li>
      </ul>

      {/* TAB 1: STUDENT FEES & PENDING DUES */}
      {activeTab === 'student-dues' && (
        <div className="campus-card shadow-sm border-0 p-4">
          {/* Filter Bar */}
          <div className="d-flex flex-wrap align-items-center justify-content-between gap-3 mb-4">
            <div className="d-flex align-items-center gap-2 flex-grow-1" style={{ maxWidth: '400px' }}>
              <i className="bi bi-search text-muted"></i>
              <input
                type="text"
                className="form-control form-control-sm"
                placeholder="Search by student name, ID, or department..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>

            <div className="d-flex align-items-center gap-2">
              <select
                className="form-select form-select-sm"
                style={{ width: '180px' }}
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value)}
              >
                <option value="ALL">All Payment Statuses</option>
                <option value="PAID">Paid in Full</option>
                <option value="PARTIAL">Partial Payment</option>
                <option value="PENDING">Pending Dues</option>
                <option value="OVERDUE">Overdue Notices</option>
              </select>
            </div>
          </div>

          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Student Info</th>
                  <th>Fee Description</th>
                  <th>Billed Amount</th>
                  <th>Amount Paid</th>
                  <th>Balance Due</th>
                  <th>Due Date</th>
                  <th>Status</th>
                  <th className="text-end">Actions</th>
                </tr>
              </thead>
              <tbody>
                {filteredStudentFees.map((s) => (
                  <tr key={s.id}>
                    <td>
                      <strong className="text-primary">{s.student_id}</strong>
                      <div className="fw-semibold text-dark">{s.student_name}</div>
                      <small className="text-muted">{s.department} (Yr {s.year} Sec {s.section})</small>
                    </td>
                    <td>
                      <span className="fw-semibold text-dark d-block">{s.fee_title}</span>
                      <small className="text-muted">Inv: {s.invoice_number}</small>
                    </td>
                    <td><strong>${s.total_billed.toLocaleString()}</strong></td>
                    <td><strong className="text-success">${s.amount_paid.toLocaleString()}</strong></td>
                    <td>
                      <strong className={s.balance_remaining > 0 ? 'text-danger' : 'text-muted'}>
                        ${s.balance_remaining.toLocaleString()}
                      </strong>
                    </td>
                    <td>
                      <span className={s.status === 'OVERDUE' ? 'text-danger fw-bold' : 'text-muted'}>
                        {s.due_date}
                      </span>
                    </td>
                    <td>{getStatusBadge(s.status)}</td>
                    <td className="text-end">
                      <div className="d-flex justify-content-end gap-1">
                        {s.balance_remaining > 0 && (
                          <button
                            className="btn btn-success btn-sm fw-semibold"
                            onClick={() => paymentModal.openModal({ studentFee: s })}
                          >
                            <i className="bi bi-credit-card me-1"></i> Pay
                          </button>
                        )}
                        <button
                          className="btn btn-outline-primary btn-sm"
                          onClick={() => receiptModal.openModal()}
                          title="Print Receipt"
                        >
                          <i className="bi bi-receipt"></i> Receipt
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 2: FEE STRUCTURES */}
      {activeTab === 'structures' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Fee Structure Title</th>
                  <th>Category</th>
                  <th>Department & Semester</th>
                  <th>Billed Amount ($ USD)</th>
                  <th>Due Date</th>
                  <th className="text-end">Actions</th>
                </tr>
              </thead>
              <tbody>
                {structures.map((st) => (
                  <tr key={st.id}>
                    <td><strong className="text-dark">{st.title}</strong></td>
                    <td><span className="badge bg-light text-secondary border">{st.category_name}</span></td>
                    <td>
                      <span className="badge bg-primary me-1">{st.department_code}</span>
                      <span>Semester {st.semester}</span>
                    </td>
                    <td><strong className="text-success fs-6">${st.amount.toLocaleString()}</strong></td>
                    <td>{st.due_date}</td>
                    <td className="text-end">
                      <div className="d-flex justify-content-end gap-1">
                        <button
                          className="btn btn-outline-secondary btn-sm"
                          onClick={() => structureModal.openModal({ structure: st, isEdit: true })}
                        >
                          <i className="bi bi-pencil"></i>
                        </button>
                        <button
                          className="btn btn-outline-danger btn-sm"
                          onClick={() => deleteModal.openModal(st)}
                        >
                          <i className="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 3: PAYMENT TRANSACTION HISTORY */}
      {activeTab === 'history' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle small mb-0">
              <thead className="table-light">
                <tr>
                  <th>Invoice #</th>
                  <th>Student</th>
                  <th>Amount Paid</th>
                  <th>Payment Method</th>
                  <th>Transaction Reference</th>
                  <th>Date & Time</th>
                  <th>Status</th>
                  <th className="text-end">Receipt</th>
                </tr>
              </thead>
              <tbody>
                {payments.map((p) => (
                  <tr key={p.id}>
                    <td><strong className="text-primary">{p.invoice_number}</strong></td>
                    <td>
                      <div className="fw-semibold text-dark">{p.student_name}</div>
                      <small className="text-muted">{p.student_id}</small>
                    </td>
                    <td><strong className="text-success fs-6">${p.amount_paid.toLocaleString()}</strong></td>
                    <td><span className="badge bg-light text-dark border">{p.payment_method}</span></td>
                    <td><code>{p.transaction_id}</code></td>
                    <td>{new Date(p.payment_date).toLocaleString()}</td>
                    <td><span className="badge bg-success">Verified</span></td>
                    <td className="text-end">
                      <button
                        className="btn btn-outline-primary btn-sm"
                        onClick={() => receiptModal.openModal()}
                      >
                        <i className="bi bi-printer-fill me-1"></i> Receipt
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Modals */}
      <FeeStructureModal
        isOpen={structureModal.isOpen}
        onClose={structureModal.closeModal}
        onSubmit={handleStructureSubmit}
        initialData={structureModal.modalData?.structure}
        isEdit={structureModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <RecordPaymentModal
        isOpen={paymentModal.isOpen}
        onClose={paymentModal.closeModal}
        onSubmit={handlePaymentSubmit}
        studentFee={paymentModal.modalData?.studentFee}
        loading={actionLoading}
      />

      <FeeReceiptModal
        isOpen={receiptModal.isOpen}
        onClose={receiptModal.closeModal}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={() => {
          setStructures((prev) => prev.filter((s) => s.id !== deleteModal.modalData.id));
          deleteModal.closeModal();
          showSuccess('Fee structure removed.');
        }}
        title="Delete Fee Structure"
        message={`Are you sure you want to remove the fee structure "${deleteModal.modalData?.title}"?`}
        confirmText="Delete Structure"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Fees;
