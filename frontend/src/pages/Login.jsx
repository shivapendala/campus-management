import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

export const Login = () => {
  const { login } = useAuth();
  const navigate = useNavigate();
  const [username, setUsername] = useState('admin');
  const [password, setPassword] = useState('admin123');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(username, password);
      navigate('/');
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          'Failed to sign in. Please check your username and password.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleDemoFill = (u, p) => {
    setUsername(u);
    setPassword(p);
  };

  return (
    <div
      className="d-flex align-items-center justify-content-center min-vh-100 px-3"
      style={{
        background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)',
      }}
    >
      <div className="campus-card p-4 p-md-5 shadow-lg" style={{ maxWidth: '440px', width: '100%', borderRadius: '16px' }}>
        <div className="text-center mb-4">
          <div
            className="bg-gradient-primary rounded-4 d-inline-flex align-items-center justify-content-center text-white mb-3"
            style={{ width: '56px', height: '56px' }}
          >
            <i className="bi bi-mortarboard-fill fs-3"></i>
          </div>
          <h4 className="fw-bold text-dark mb-1">Campus Management</h4>
          <p className="text-muted small">Sign in with your institutional credentials</p>
        </div>

        {error && (
          <div className="alert alert-danger py-2 px-3 small d-flex align-items-center gap-2" role="alert">
            <i className="bi bi-exclamation-triangle-fill"></i>
            <div>{error}</div>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label small fw-semibold text-secondary">Username or Email</label>
            <div className="input-group">
              <span className="input-group-text bg-light border-end-0 text-muted">
                <i className="bi bi-person"></i>
              </span>
              <input
                type="text"
                required
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                className="form-control border-start-0"
                placeholder="Enter username"
              />
            </div>
          </div>

          <div className="mb-4">
            <div className="d-flex justify-content-between align-items-center mb-1">
              <label className="form-label small fw-semibold text-secondary mb-0">Password</label>
              <a href="#forgot" className="small text-decoration-none text-primary" onClick={(e) => e.preventDefault()}>
                Forgot?
              </a>
            </div>
            <div className="input-group">
              <span className="input-group-text bg-light border-end-0 text-muted">
                <i className="bi bi-lock"></i>
              </span>
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="form-control border-start-0"
                placeholder="Enter password"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="btn btn-primary w-100 py-2 fw-semibold rounded-3 mb-3 d-flex align-items-center justify-content-center gap-2"
          >
            {loading ? (
              <>
                <span className="spinner-border spinner-border-sm" role="status"></span>
                <span>Authenticating...</span>
              </>
            ) : (
              <>
                <span>Sign In to Portal</span>
                <i className="bi bi-arrow-right"></i>
              </>
            )}
          </button>
        </form>

        <div className="p-3 bg-light rounded-3 mt-3 border">
          <small className="d-block fw-bold text-secondary mb-2">Quick Demo Accounts:</small>
          <div className="d-flex flex-wrap gap-2">
            <button
              type="button"
              className="btn btn-sm btn-outline-secondary py-1 px-2 text-nowrap"
              onClick={() => handleDemoFill('admin', 'admin123')}
            >
              Admin (admin / admin123)
            </button>
            <button
              type="button"
              className="btn btn-sm btn-outline-secondary py-1 px-2 text-nowrap"
              onClick={() => handleDemoFill('student', 'student123')}
            >
              Student (student / student123)
            </button>
            <button
              type="button"
              className="btn btn-sm btn-outline-secondary py-1 px-2 text-nowrap"
              onClick={() => handleDemoFill('prof_smith', 'faculty123')}
            >
              Faculty (prof_smith / faculty123)
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
