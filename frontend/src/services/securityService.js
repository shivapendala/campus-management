import apiClient from './apiClient';

export const securityService = {
  getAuditLogs: (params) => apiClient.get('/core/audit-logs/', { params }),
  getRBACMatrix: () => apiClient.get('/core/rbac-matrix/'),
  getSystemHealthProbes: () => apiClient.get('/core/health/'),
  flushRevokedTokens: () => apiClient.post('/core/flush-revoked-tokens/'),
};

export default securityService;
