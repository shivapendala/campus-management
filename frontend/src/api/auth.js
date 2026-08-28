import api from './axios';

export const authAPI = {
  // Login with username and password
  login: async (username, password) => {
    const response = await api.post('/auth/token/', { username, password });
    const { access, refresh, user } = response.data;
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    localStorage.setItem('user_info', JSON.stringify(user));
    return response.data;
  },

  // Register a new user
  register: async (userData) => {
    const response = await api.post('/auth/register/', userData);
    return response.data;
  },

  // Fetch current user profile
  getProfile: async () => {
    const response = await api.get('/auth/profile/');
    return response.data;
  },

  // Logout by clearing tokens
  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_info');
  },

  // Check if user is currently authenticated
  isAuthenticated: () => {
    return !!localStorage.getItem('access_token');
  },

  // Get cached user info
  getCurrentUser: () => {
    const stored = localStorage.getItem('user_info');
    return stored ? JSON.parse(stored) : null;
  },
};
