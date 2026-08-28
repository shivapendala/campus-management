import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { NotificationProvider } from './context/NotificationContext';
import MainLayout from './layouts/MainLayout';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Register from './pages/Register';
import ForgotPassword from './pages/ForgotPassword';
import ResetPassword from './pages/ResetPassword';
import Students from './pages/Students';
import Courses from './pages/Courses';
import Faculty from './pages/Faculty';
import Departments from './pages/Departments';
import Timetable from './pages/Timetable';
import Attendance from './pages/Attendance';
import Examinations from './pages/Examinations';

export const App = () => {
  return (
    <AuthProvider>
      <NotificationProvider>
        <BrowserRouter>
          <Routes>
            {/* Auth Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route path="/forgot-password" element={<ForgotPassword />} />
            <Route path="/reset-password" element={<ResetPassword />} />

            {/* Authenticated Campus Module Routes */}
            <Route
              path="/"
              element={
                <MainLayout>
                  <Dashboard />
                </MainLayout>
              }
            />
            <Route
              path="/examinations"
              element={
                <MainLayout>
                  <Examinations />
                </MainLayout>
              }
            />
            <Route
              path="/attendance"
              element={
                <MainLayout>
                  <Attendance />
                </MainLayout>
              }
            />
            <Route
              path="/timetable"
              element={
                <MainLayout>
                  <Timetable />
                </MainLayout>
              }
            />
            <Route
              path="/departments"
              element={
                <MainLayout>
                  <Departments />
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

            {/* Fallback */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </BrowserRouter>
      </NotificationProvider>
    </AuthProvider>
  );
};

export default App;
