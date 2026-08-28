import apiClient from './apiClient';

export const reportService = {
  getExecutiveSummary: async () => {
    const res = await apiClient.get('/reports/reports/executive_summary/');
    return res.data;
  },
  getAttendanceAnalytics: async () => {
    const res = await apiClient.get('/reports/reports/attendance_analytics/');
    return res.data;
  },
  getAcademicAnalytics: async () => {
    const res = await apiClient.get('/reports/reports/academic_analytics/');
    return res.data;
  },
  getPlacementAnalytics: async () => {
    const res = await apiClient.get('/reports/reports/placement_analytics/');
    return res.data;
  },
  getFinancialAudit: async () => {
    const res = await apiClient.get('/reports/reports/financial_audit/');
    return res.data;
  },
};

export default reportService;
