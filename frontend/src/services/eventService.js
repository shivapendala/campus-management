import apiClient from './apiClient';

export const eventService = {
  getEvents: async (params = {}) => {
    const res = await apiClient.get('/events/events/', { params });
    return res.data;
  },
  createEvent: async (data) => {
    const res = await apiClient.post('/events/events/', data);
    return res.data;
  },
  registerForEvent: async (data) => {
    const res = await apiClient.post('/events/registrations/', data);
    return res.data;
  },
};

export default eventService;
