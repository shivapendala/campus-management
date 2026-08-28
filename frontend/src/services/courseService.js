import apiClient from './apiClient';

export const courseService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/courses/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/courses/${id}/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/courses/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/courses/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/courses/${id}/`);
    return res.data;
  },
};

export default courseService;
