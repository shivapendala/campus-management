import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import Sidebar from './components/Sidebar';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Register from './pages/Register';
import ForgotPassword from './pages/ForgotPassword';
import ResetPassword from './pages/ResetPassword';
import Students from './pages/Students';
import Courses from './pages/Courses';
import Faculty from './pages/Faculty';

// Layout wrapper for dashboard pages
const MainLayout = ({ children }) => {
  return (
    <div className="d-flex" style={{ minHeight: '100vh', backgroundColor: '#f8fafc' }}>
      <Sidebar />
      <div className="d-flex flex-column flex-grow-1" style={{ minWidth: 0 }}>
        <Navbar />
        <main className="flex-grow-1">{children}</main>
      </div>
    </div>
  );
};

export const App = () => {
  return (
    <AuthProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/forgot-password" element={<ForgotPassword />} />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route
            path="/"
            element={
              <MainLayout>
                <Dashboard />
              </MainLayout>
            }
          />
          <Route
            path="/students"
            element={
              <MainLayout>
                <Students />
              </MainLayout>
            }
          />
          <Route
            path="/courses"
            element={
              <MainLayout>
                <Courses />
              </MainLayout>
            }
          />
          <Route
            path="/faculty"
            element={
              <MainLayout>
                <Faculty />
              </MainLayout>
            }
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </BrowserRouter>
    </AuthProvider>
  );
};

export default App;
