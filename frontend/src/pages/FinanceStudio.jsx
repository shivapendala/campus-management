import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const FinanceStudio = () => {
  const [activeTab, setActiveTab] = useState('ledger');

  const journalEntries = [
    { tx_id: 'TX-98421', date: '2026-08-28', description: 'Tuition fee received for Rahul Sharma (23CSE01042)', debit: '1020-Bank Operating (Rs. 65,000)', credit: '2010-Student Dues AR (Rs. 65,000)', mode: 'RAZORPAY', status: 'BALANCED' },
    { tx_id: 'TX-98422', date: '2026-08-28', description: 'Hostel & Mess fee received for Priya Verma (23CSE01088)', debit: '1020-Bank Operating (Rs. 42,000)', credit: '2010-Student Dues AR (Rs. 42,000)', mode: 'BANK_NEFT', status: 'BALANCED' },
    { tx_id: 'TX-98423', date: '2026-08-27', description: 'DST Research Grant tranche received (PI: Dr. Rajesh Raman)', debit: '1020-Bank Operating (Rs. 15,00,000)', credit: '3010-Sponsored Research Fund (Rs. 15,00,000)', mode: 'GOVT_RTGS', status: 'BALANCED' },
  ];

  const columns = [
    { key: 'tx_id', label: 'Voucher No.', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'date', label: 'Date' },
    { key: 'description', label: 'Description' },
    { key: 'debit', label: 'Debit Account' },
    { key: 'credit', label: 'Credit Account' },
    { key: 'mode', label: 'Payment Mode', render: (val) => <span className="badge bg-light text-dark">{val}</span> },
    { key: 'status', label: 'Ledger Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-bank2 me-2"></i>Finance & Accounting Ledger Studio
          </h2>
          <p className="text-muted mb-0">
            Double-entry institutional accounting vouchers, installment schedule builder, UGC fee refunds, and bank settlement reconciliation.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-file-earmark-spreadsheet me-1"></i>Export Ledger (CSV)
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-receipt me-1"></i>Issue Manual Receipt
          </button>
        </div>
      </div>

      {/* Financial KPIs */}
      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Revenue Collected"
            value="Rs. 1.85 Cr"
            icon="bi-cash-stack"
            variant="success"
            subtitle="Academic Year 2026-27"
            delta="+12.4% YoY"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Outstanding Student Dues"
            value="Rs. 32.0 Lakhs"
            icon="bi-hourglass-split"
            variant="warning"
            subtitle="Overdue Past Grace Period: Rs. 8.5L"
            delta="Collection in Progress"
            deltaType="neutral"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Scholarships Disbursed"
            value="Rs. 24.5 Lakhs"
            icon="bi-gift-fill"
            variant="info"
            subtitle="Benefiting 180 Students"
            delta="100% Disbursed"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Gateway Reconciliation"
            value="99.8% Matched"
            icon="bi-check2-all"
            variant="primary"
            subtitle="Zero Unsettled Chargebacks"
            delta="Balanced"
            deltaType="positive"
          />
        </div>
      </div>

      {/* Double-Entry Journal Table */}
      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-journal-text me-2 text-primary"></i>Double-Entry Journal & Ledger Entries
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={journalEntries}
          searchPlaceholder="Search vouchers by ID, student, or account..."
        />
      </div>
    </div>
  );
};

export default FinanceStudio;
