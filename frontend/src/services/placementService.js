import apiClient from './apiClient';

export const placementService = {
  getCompanies: async (params = {}) => {
    const res = await apiClient.get('/placements/companies/', { params });
    return res.data;
  },
  createCompany: async (data) => {
    const res = await apiClient.post('/placements/companies/', data);
    return res.data;
  },
  getDrives: async (params = {}) => {
    const res = await apiClient.get('/placements/drives/', { params });
    return res.data;
  },
  createDrive: async (data) => {
    const res = await apiClient.post('/placements/drives/', data);
    return res.data;
  },
  getApplications: async (params = {}) => {
    const res = await apiClient.get('/placements/applications/', { params });
    return res.data;
  },
  applyForDrive: async (data) => {
    const res = await apiClient.post('/placements/applications/', data);
    return res.data;
  },
};

export default placementService;
