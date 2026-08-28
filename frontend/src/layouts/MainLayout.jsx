import React from 'react';
import Navbar from '../components/common/Navbar';
import Sidebar from '../components/common/Sidebar';
import Footer from '../components/common/Footer';

export const MainLayout = ({ children }) => {
  return (
    <div className="d-flex" style={{ minHeight: '100vh', backgroundColor: '#f8fafc' }}>
      <Sidebar />
      <div className="d-flex flex-column flex-grow-1" style={{ minWidth: 0 }}>
        <Navbar />
        <main className="flex-grow-1 p-0">{children}</main>
        <Footer />
      </div>
    </div>
  );
};

export default MainLayout;
