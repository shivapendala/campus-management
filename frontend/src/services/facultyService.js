import apiClient from './apiClient';

export const facultyService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/faculty/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/faculty/${id}/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/faculty/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/faculty/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/faculty/${id}/`);
    return res.data;
  },
  assignSubject: async (facultyId, courseId) => {
    const res = await apiClient.post(`/faculty/${facultyId}/assign-subject/`, { course_id: courseId });
    return res.data;
  },
  assignClass: async (facultyId, year, section) => {
    const res = await apiClient.post(`/faculty/${facultyId}/assign-class/`, { year, section });
    return res.data;
  },
  getSchedule: async (facultyId) => {
    const res = await apiClient.get(`/faculty/${facultyId}/schedule/`);
    return res.data;
  },
  getDashboardStats: async () => {
    const res = await apiClient.get('/faculty/dashboard-stats/');
    return res.data;
  },
};

export default facultyService;
