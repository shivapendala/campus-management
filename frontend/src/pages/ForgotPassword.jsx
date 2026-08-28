import React, { useState } from 'react';
import { authAPI } from '../api/auth';
import { Link, useNavigate } from 'react-router-dom';

export const ForgotPassword = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [info, setInfo] = useState('');
  const [resetToken, setResetToken] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setInfo('');
    try {
      const res = await authAPI.forgotPassword(email);
      setInfo(res.detail || 'Reset instructions generated.');
      if (res.reset_token) {
        setResetToken(res.reset_token);
      }
    } catch (err) {
      setInfo('An error occurred. Please try again.');
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
            <i className="bi bi-key-fill fs-3"></i>
          </div>
          <h4 className="fw-bold text-dark mb-1">Reset Password</h4>
          <p className="text-muted small">Enter your email to receive recovery instructions</p>
        </div>

        {info && (
          <div className="alert alert-info py-2 px-3 small mb-3" role="alert">
            <i className="bi bi-info-circle-fill me-2"></i>
            {info}
          </div>
        )}

        {resetToken ? (
          <div className="p-3 bg-light rounded-3 border mb-4 text-center">
            <span className="badge bg-success mb-2">Token Generated</span>
            <p className="small text-muted mb-2">Use the token below or continue to the reset page:</p>
            <code className="d-block p-2 bg-white rounded border small text-break mb-3 font-monospace">
              {resetToken}
            </code>
            <Link
              to={`/reset-password?token=${encodeURIComponent(resetToken)}`}
              className="btn btn-primary btn-sm w-100 py-2 fw-semibold"
            >
              Proceed to Reset Password Form
            </Link>
          </div>
        ) : (
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label className="form-label small fw-semibold text-secondary">Registered Email Address</label>
              <div className="input-group">
                <span className="input-group-text bg-light border-end-0 text-muted">
                  <i className="bi bi-envelope"></i>
                </span>
                <input
                  type="email"
                  required
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="form-control border-start-0"
                  placeholder="name@campus.edu"
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
                  <span>Generating Instructions...</span>
                </>
              ) : (
                <>
                  <span>Send Recovery Token</span>
                  <i className="bi bi-arrow-right"></i>
                </>
              )}
            </button>
          </form>
        )}

        <div className="text-center">
          <Link to="/login" className="small text-muted text-decoration-none">
            <i className="bi bi-arrow-left me-1"></i> Back to Login
          </Link>
        </div>
      </div>
    </div>
  );
};

export default ForgotPassword;
