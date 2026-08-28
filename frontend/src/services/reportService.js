import apiClient from './apiClient';

export const reportService = {
  getOverview: async () => {
    const res = await apiClient.get('/reports/overview/');
    return res.data;
  },
  getDepartments: async () => {
    const res = await apiClient.get('/reports/departments/');
    return res.data;
  },
  getFinances: async () => {
    const res = await apiClient.get('/reports/finances/');
    return res.data;
  },
  getPlacements: async () => {
    const res = await apiClient.get('/reports/placements/');
    return res.data;
  },
};

export default reportService;
