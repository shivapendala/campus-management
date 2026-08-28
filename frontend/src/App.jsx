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
import Assignments from './pages/Assignments';
import Fees from './pages/Fees';
import Library from './pages/Library';
import Placements from './pages/Placements';
import Complaints from './pages/Complaints';
import Events from './pages/Events';
import Notifications from './pages/Notifications';
import Reports from './pages/Reports';

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

            {/* Authenticated Campus 15-Module Routes */}
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
              path="/faculty"
              element={
                <MainLayout>
                  <Faculty />
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
              path="/courses"
              element={
                <MainLayout>
                  <Courses />
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
              path="/attendance"
              element={
                <MainLayout>
                  <Attendance />
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
              path="/assignments"
              element={
                <MainLayout>
                  <Assignments />
                </MainLayout>
              }
            />
            <Route
              path="/fees"
              element={
                <MainLayout>
                  <Fees />
                </MainLayout>
              }
            />
            <Route
              path="/library"
              element={
                <MainLayout>
                  <Library />
                </MainLayout>
              }
            />
            <Route
              path="/placements"
              element={
                <MainLayout>
                  <Placements />
                </MainLayout>
              }
            />
            <Route
              path="/complaints"
              element={
                <MainLayout>
                  <Complaints />
                </MainLayout>
              }
            />
            <Route
              path="/events"
              element={
                <MainLayout>
                  <Events />
                </MainLayout>
              }
            />
            <Route
              path="/notifications"
              element={
                <MainLayout>
                  <Notifications />
                </MainLayout>
              }
            />
            <Route
              path="/reports"
              element={
                <MainLayout>
                  <Reports />
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
