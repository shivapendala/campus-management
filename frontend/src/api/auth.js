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

  // Verify role permissions
  verifyRole: async () => {
    const response = await api.get('/auth/verify-role/');
    return response.data;
  },

  // Forgot password request
  forgotPassword: async (email) => {
    const response = await api.post('/auth/forgot-password/', { email });
    return response.data;
  },

  // Reset password confirm
  resetPassword: async (token, new_password, confirm_password) => {
    const response = await api.post('/auth/reset-password/', {
      token,
      new_password,
      confirm_password,
    });
    return response.data;
  },

  // Change password
  changePassword: async (old_password, new_password) => {
    const response = await api.post('/auth/change-password/', {
      old_password,
      new_password,
    });
    return response.data;
  },

  // Logout by clearing tokens
  logout: () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user_info');
  },

  // Check if token exists
  isAuthenticated: () => {
    return !!localStorage.getItem('access_token');
  },

  // Get cached user info
  getCurrentUser: () => {
    const stored = localStorage.getItem('user_info');
    return stored ? JSON.parse(stored) : null;
  },
};
