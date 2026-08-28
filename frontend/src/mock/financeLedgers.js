/**
 * Standard Double-Entry Financial Accounting Ledger Mock Data Store
 */

export const mockFinancialLedgerStore = {
  chartOfAccounts: [
    { code: '1010', name: 'Cash on Hand', type: 'ASSET', balance: 450000.0 },
    { code: '1020', name: 'Bank Operating Account (SBI)', type: 'ASSET', balance: 18500000.0 },
    { code: '1030', name: 'Bank Endowment Corpus (HDFC)', type: 'ASSET', balance: 45000000.0 },
    { code: '2010', name: 'Student Accounts Receivable (Dues)', type: 'ASSET', balance: 3200000.0 },
    { code: '3010', name: 'Tuition Fee Revenue', type: 'INCOME', balance: 65000000.0 },
    { code: '3020', name: 'Hostel & Mess Fee Revenue', type: 'INCOME', balance: 18000000.0 },
    { code: '3030', name: 'Sponsored Research Grants (DST/SERB)', type: 'INCOME', balance: 15000000.0 },
    { code: '4010', name: 'Faculty & Staff Payroll Expense', type: 'EXPENSE', balance: 42000000.0 },
    { code: '4020', name: 'Laboratory Equipment CAPEX', type: 'EXPENSE', balance: 8500000.0 },
    { code: '4030', name: 'Campus Maintenance & Utilities', type: 'EXPENSE', balance: 6200000.0 },
  ],
  recentJournalVouchers: [
    {
      voucherNo: 'JV-2026-0801',
      date: '2026-08-28',
      description: 'Term 1 Tuition Fee Collection via Payment Gateway',
      debitAccount: '1020-Bank Operating (SBI)',
      debitAmount: 1850000.0,
      creditAccount: '2010-Student Dues AR',
      creditAmount: 1850000.0,
      status: 'POSTED_BALANCED',
    },
    {
      voucherNo: 'JV-2026-0802',
      date: '2026-08-28',
      description: 'Monthly Faculty & Non-Teaching Staff Salary Disbursement',
      debitAccount: '4010-Faculty & Staff Payroll Expense',
      debitAmount: 3800000.0,
      creditAccount: '1020-Bank Operating (SBI)',
      creditAmount: 3800000.0,
      status: 'POSTED_BALANCED',
    },
    {
      voucherNo: 'JV-2026-0803',
      date: '2026-08-27',
      description: 'DST Research Project 2nd Tranche Grant Fund Influx',
      debitAccount: '1020-Bank Operating (SBI)',
      debitAmount: 2500000.0,
      creditAccount: '3030-Sponsored Research Grants',
      creditAmount: 2500000.0,
      status: 'POSTED_BALANCED',
    },
  ],
};

export default mockFinancialLedgerStore;
