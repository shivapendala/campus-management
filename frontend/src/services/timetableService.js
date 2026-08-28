import apiClient from './apiClient';

export const timetableService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/courses/timetable/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/courses/timetable/${id}/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/courses/timetable/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/courses/timetable/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/courses/timetable/${id}/`);
    return res.data;
  },
  checkConflicts: async (slotData) => {
    const res = await apiClient.post('/courses/timetable/check-conflicts/', slotData);
    return res.data;
  },
};

export default timetableService;
