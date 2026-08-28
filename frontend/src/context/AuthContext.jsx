import React, { createContext, useContext, useState, useEffect } from 'react';
import { authAPI } from '../api/auth';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(authAPI.getCurrentUser());
  const [role, setRole] = useState(authAPI.getCurrentUser()?.role || null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      if (authAPI.isAuthenticated()) {
        try {
          const profile = await authAPI.getProfile();
          setUser(profile);
          setRole(profile.role);
          localStorage.setItem('user_info', JSON.stringify(profile));
        } catch (err) {
          console.error('Failed to restore session:', err);
          authAPI.logout();
          setUser(null);
          setRole(null);
        }
      }
      setLoading(false);
    };
    initAuth();
  }, []);

  const login = async (username, password) => {
    const data = await authAPI.login(username, password);
    setUser(data.user);
    setRole(data.user.role);
    return data;
  };

  const register = async (userData) => {
    return await authAPI.register(userData);
  };

  const logout = () => {
    authAPI.logout();
    setUser(null);
    setRole(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        role: user?.role || role,
        isAuthenticated: !!user,
        login,
        register,
        logout,
        loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
