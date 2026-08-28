import apiClient from './apiClient';

export const studentService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/students/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/students/${id}/`);
    return res.data;
  },
  getProfileDetails: async (id) => {
    const res = await apiClient.get(`/students/${id}/profile-details/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/students/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/students/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/students/${id}/`);
    return res.data;
  },
  importCSV: async (csvText) => {
    const res = await apiClient.post('/students/import-csv/', { csv_text: csvText });
    return res.data;
  },
  exportCSV: async () => {
    const res = await apiClient.get('/students/export-csv/', { responseType: 'blob' });
    return res.data;
  },
};

export default studentService;
