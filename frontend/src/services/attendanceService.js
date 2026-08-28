import apiClient from './apiClient';

export const attendanceService = {
  getSessions: async (params = {}) => {
    const res = await apiClient.get('/attendance/sessions/', { params });
    return res.data;
  },
  getRecords: async (params = {}) => {
    const res = await apiClient.get('/attendance/records/', { params });
    return res.data;
  },
  bulkRecord: async (payload) => {
    const res = await apiClient.post('/attendance/sessions/bulk-record/', payload);
    return res.data;
  },
  getMonthlyReport: async (params = {}) => {
    const res = await apiClient.get('/attendance/sessions/monthly-report/', { params });
    return res.data;
  },
  getSemesterReport: async (params = {}) => {
    const res = await apiClient.get('/attendance/sessions/semester-report/', { params });
    return res.data;
  },
};

export default attendanceService;
