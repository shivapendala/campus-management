import React from 'react';

export const AuthLayout = ({ children }) => {
  return (
    <div
      className="d-flex align-items-center justify-content-center min-vh-100 px-3 py-4"
      style={{
        background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)',
      }}
    >
      {children}
    </div>
  );
};

export default AuthLayout;
