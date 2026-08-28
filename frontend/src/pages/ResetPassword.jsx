import React, { useState, useEffect } from 'react';
import { authAPI } from '../api/auth';
import { useNavigate, useSearchParams, Link } from 'react-router-dom';

export const ResetPassword = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [token, setToken] = useState(searchParams.get('token') || '');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const urlToken = searchParams.get('token');
    if (urlToken) {
      setToken(urlToken);
    }
  }, [searchParams]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    if (newPassword !== confirmPassword) {
      setError('Passwords do not match.');
      return;
    }
    setLoading(true);
    try {
      const res = await authAPI.resetPassword(token, newPassword, confirmPassword);
      setSuccess(res.detail || 'Password updated successfully!');
      setTimeout(() => navigate('/login'), 2500);
    } catch (err) {
      setError(err.response?.data?.token?.[0] || 'Failed to reset password. Please ensure the token is valid.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="d-flex align-items-center justify-content-center min-vh-100 px-3 py-4"
      style={{
        background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)',
      }}
    >
      <div className="campus-card p-4 p-md-5 shadow-lg" style={{ maxWidth: '460px', width: '100%', borderRadius: '16px' }}>
        <div className="text-center mb-4">
          <div
            className="bg-gradient-primary rounded-4 d-inline-flex align-items-center justify-content-center text-white mb-3 shadow"
            style={{ width: '56px', height: '56px' }}
          >
            <i className="bi bi-shield-lock-fill fs-3"></i>
          </div>
          <h4 className="fw-bold text-dark mb-1">Set New Password</h4>
          <p className="text-muted small">Enter your reset token and new credentials</p>
        </div>

        {error && (
          <div className="alert alert-danger py-2 px-3 small d-flex align-items-center gap-2" role="alert">
            <i className="bi bi-exclamation-triangle-fill"></i>
            <div>{error}</div>
          </div>
        )}

        {success && (
          <div className="alert alert-success py-2 px-3 small d-flex align-items-center gap-2" role="alert">
            <i className="bi bi-check-circle-fill"></i>
            <div>{success} Redirecting to login...</div>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label small fw-semibold text-secondary">Reset Token or Code</label>
            <input
              type="text"
              required
              value={token}
              onChange={(e) => setToken(e.target.value)}
              className="form-control font-monospace"
              placeholder="Paste token or enter 6-digit code"
            />
          </div>

          <div className="mb-3">
            <label className="form-label small fw-semibold text-secondary">New Password</label>
            <input
              type="password"
              required
              minLength={6}
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
              className="form-control"
              placeholder="Min 6 characters"
            />
          </div>

          <div className="mb-4">
            <label className="form-label small fw-semibold text-secondary">Confirm New Password</label>
            <input
              type="password"
              required
              minLength={6}
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              className="form-control"
              placeholder="Repeat new password"
            />
          </div>

          <button
            type="submit"
            disabled={loading || !!success}
            className="btn btn-primary w-100 py-2 fw-semibold rounded-3 mb-3 d-flex align-items-center justify-content-center gap-2"
          >
            {loading ? (
              <>
                <span className="spinner-border spinner-border-sm" role="status"></span>
                <span>Updating Password...</span>
              </>
            ) : (
              <>
                <span>Update Password</span>
                <i className="bi bi-check-lg"></i>
              </>
            )}
          </button>
        </form>

        <div className="text-center">
          <Link to="/login" className="small text-muted text-decoration-none">
            <i className="bi bi-arrow-left me-1"></i> Back to Login
          </Link>
        </div>
      </div>
    </div>
  );
};

export default ResetPassword;
