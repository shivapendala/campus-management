import apiClient from './apiClient';

export const analyticsService = {
  getKpiOverview: () => apiClient.get('/analytics/kpi-overview/'),
  getStudentAcademicRisk: () => apiClient.get('/analytics/student-risk/'),
  getNaacAccreditation: () => apiClient.get('/analytics/accreditation-naac/'),
  getCampusUtilization: () => apiClient.get('/analytics/utilization/'),
};

export default analyticsService;
