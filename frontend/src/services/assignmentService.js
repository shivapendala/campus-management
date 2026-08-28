import apiClient from './apiClient';

export const assignmentService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/assignments/assignments/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/assignments/assignments/${id}/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/assignments/assignments/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/assignments/assignments/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/assignments/assignments/${id}/`);
    return res.data;
  },
  submitSolution: async (assignmentId, payload) => {
    const res = await apiClient.post(`/assignments/assignments/${assignmentId}/submit/`, payload);
    return res.data;
  },
  getSubmissions: async (params = {}) => {
    const res = await apiClient.get('/assignments/submissions/', { params });
    return res.data;
  },
  gradeSubmission: async (submissionId, payload) => {
    const res = await apiClient.post(`/assignments/submissions/${submissionId}/grade/`, payload);
    return res.data;
  },
};

export default assignmentService;
