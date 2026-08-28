import apiClient from './apiClient';

export const feeService = {
  getStructures: async (params = {}) => {
    const res = await apiClient.get('/fees/structures/', { params });
    return res.data;
  },
  createStructure: async (data) => {
    const res = await apiClient.post('/fees/structures/', data);
    return res.data;
  },
  updateStructure: async (id, data) => {
    const res = await apiClient.put(`/fees/structures/${id}/`, data);
    return res.data;
  },
  deleteStructure: async (id) => {
    const res = await apiClient.delete(`/fees/structures/${id}/`);
    return res.data;
  },
  getPayments: async (params = {}) => {
    const res = await apiClient.get('/fees/payments/', { params });
    return res.data;
  },
  recordPayment: async (data) => {
    const res = await apiClient.post('/fees/payments/', data);
    return res.data;
  },
  getFinancialSummary: async () => {
    const res = await apiClient.get('/fees/payments/financial-summary/');
    return res.data;
  },
  getReceipt: async (paymentId) => {
    const res = await apiClient.get(`/fees/payments/${paymentId}/receipt/`);
    return res.data;
  },
};

export default feeService;
