import apiClient from './apiClient';

export const departmentService = {
  getAll: async (params = {}) => {
    const res = await apiClient.get('/departments/', { params });
    return res.data;
  },
  getById: async (id) => {
    const res = await apiClient.get(`/departments/${id}/`);
    return res.data;
  },
  create: async (data) => {
    const res = await apiClient.post('/departments/', data);
    return res.data;
  },
  update: async (id, data) => {
    const res = await apiClient.put(`/departments/${id}/`, data);
    return res.data;
  },
  delete: async (id) => {
    const res = await apiClient.delete(`/departments/${id}/`);
    return res.data;
  },
  getStudents: async (id) => {
    const res = await apiClient.get(`/departments/${id}/students/`);
    return res.data;
  },
  getFaculty: async (id) => {
    const res = await apiClient.get(`/departments/${id}/faculty/`);
    return res.data;
  },
  getCourses: async (id) => {
    const res = await apiClient.get(`/departments/${id}/courses/`);
    return res.data;
  },
  assignHOD: async (id, hodName) => {
    const res = await apiClient.post(`/departments/${id}/assign-hod/`, { head_of_department: hodName });
    return res.data;
  },
};

export default departmentService;
