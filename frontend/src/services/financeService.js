import apiClient from './apiClient';

export const financeService = {
  getLedgerEntries: () => apiClient.get('/fees/ledger-entries/'),
  getInstallmentSchedule: (studentId) => apiClient.get(`/fees/installments/${studentId}/`),
  generateBankChallan: (studentId) => apiClient.get(`/fees/bank-challan/${studentId}/`),
  reconcileGatewayBatch: () => apiClient.post('/fees/reconcile-gateway/'),
};

export default financeService;
