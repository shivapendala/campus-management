import apiClient from './apiClient';

export const notificationService = {
  getNotifications: async (params = {}) => {
    const res = await apiClient.get('/notifications/notifications/', { params });
    return res.data;
  },
  broadcastNotice: async (data) => {
    const res = await apiClient.post('/notifications/notifications/', data);
    return res.data;
  },
  markAsRead: async (id) => {
    const res = await apiClient.post(`/notifications/notifications/${id}/mark_read/`);
    return res.data;
  },
};

export default notificationService;
