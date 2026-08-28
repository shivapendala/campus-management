import apiClient from './apiClient';

export const complaintService = {
  getComplaints: async (params = {}) => {
    const res = await apiClient.get('/complaints/complaints/', { params });
    return res.data;
  },
  createComplaint: async (data) => {
    const res = await apiClient.post('/complaints/complaints/', data);
    return res.data;
  },
  updateComplaint: async (id, data) => {
    const res = await apiClient.put(`/complaints/complaints/${id}/`, data);
    return res.data;
  },
  resolveComplaint: async (id, payload) => {
    const res = await apiClient.post(`/complaints/complaints/${id}/resolve/`, payload);
    return res.data;
  },
};

export default complaintService;
