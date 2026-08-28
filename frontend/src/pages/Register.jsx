import React, { useState } from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate, Link } from 'react-router-dom';

export const Register = () => {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    role: 'STUDENT',
    department_name: 'Computer Science & Engineering',
    phone: '',
    password: '',
    password_confirm: '',
  });
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    if (formData.password !== formData.password_confirm) {
      setError('Passwords do not match.');
      return;
    }
    setLoading(true);
    try {
      await register(formData);
      setSuccess(true);
      setTimeout(() => navigate('/login'), 2000);
    } catch (err) {
      const msg = err.response?.data?.username?.[0] ||
        err.response?.data?.email?.[0] ||
        err.response?.data?.password?.[0] ||
        'Registration failed. Please verify your details.';
      setError(msg);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className="d-flex align-items-center justify-content-center min-vh-100 px-3 py-5"
      style={{
        background: 'linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%)',
      }}
    >
      <div className="campus-card p-4 p-md-5 shadow-lg" style={{ maxWidth: '560px', width: '100%', borderRadius: '16px' }}>
        <div className="text-center mb-4">
          <div
            className="bg-gradient-primary rounded-4 d-inline-flex align-items-center justify-content-center text-white mb-3 shadow"
            style={{ width: '52px', height: '52px' }}
          >
            <i className="bi bi-person-plus-fill fs-4"></i>
          </div>
          <h4 className="fw-bold text-dark mb-1">Create Institutional Account</h4>
          <p className="text-muted small">Join EduCore Campus Management Platform</p>
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
            <div>Registration successful! Redirecting to login portal...</div>
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="row g-3 mb-3">
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">First Name</label>
              <input
                type="text"
                name="first_name"
                required
                className="form-control"
                placeholder="John"
                value={formData.first_name}
                onChange={handleChange}
              />
            </div>
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Last Name</label>
              <input
                type="text"
                name="last_name"
                required
                className="form-control"
                placeholder="Doe"
                value={formData.last_name}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="row g-3 mb-3">
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Username</label>
              <input
                type="text"
                name="username"
                required
                className="form-control"
                placeholder="johndoe"
                value={formData.username}
                onChange={handleChange}
              />
            </div>
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Institutional Email</label>
              <input
                type="email"
                name="email"
                required
                className="form-control"
                placeholder="john.doe@campus.edu"
                value={formData.email}
                onChange={handleChange}
              />
            </div>
          </div>

          <div className="row g-3 mb-3">
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Campus Role</label>
              <select
                name="role"
                className="form-select"
                value={formData.role}
                onChange={handleChange}
              >
                <option value="STUDENT">🎓 Student</option>
                <option value="FACULTY">👨‍🏫 Faculty / Professor</option>
                <option value="HOD">🏛️ Head of Department (HOD)</option>
                <option value="PLACEMENT_OFFICER">💼 Placement Officer</option>
                <option value="ACCOUNTANT">💳 Finance / Accountant</option>
                <option value="LIBRARIAN">📖 Librarian</option>
              </select>
            </div>
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Department</label>
              <select
                name="department_name"
                className="form-select"
                value={formData.department_name}
                onChange={handleChange}
              >
                <option value="Computer Science & Engineering">Computer Science & Eng.</option>
                <option value="Electrical & Electronics Engineering">Electrical & Electronics</option>
                <option value="Mechanical Engineering">Mechanical Engineering</option>
                <option value="Business Administration">Business Administration</option>
                <option value="Biotechnology & Bioinformatics">Biotechnology</option>
              </select>
            </div>
          </div>

          <div className="mb-3">
            <label className="form-label small fw-semibold text-secondary">Phone Number</label>
            <input
              type="text"
              name="phone"
              className="form-control"
              placeholder="+1 (555) 000-0000"
              value={formData.phone}
              onChange={handleChange}
            />
          </div>

          <div className="row g-3 mb-4">
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Password</label>
              <input
                type="password"
                name="password"
                required
                minLength={6}
                className="form-control"
                placeholder="Min 6 characters"
                value={formData.password}
                onChange={handleChange}
              />
            </div>
            <div className="col-12 col-sm-6">
              <label className="form-label small fw-semibold text-secondary">Confirm Password</label>
              <input
                type="password"
                name="password_confirm"
                required
                minLength={6}
                className="form-control"
                placeholder="Repeat password"
                value={formData.password_confirm}
                onChange={handleChange}
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading || success}
            className="btn btn-primary w-100 py-2 fw-semibold rounded-3 mb-3 d-flex align-items-center justify-content-center gap-2"
          >
            {loading ? (
              <>
                <span className="spinner-border spinner-border-sm" role="status"></span>
                <span>Creating Account...</span>
              </>
            ) : (
              <>
                <span>Complete Registration</span>
                <i className="bi bi-arrow-right"></i>
              </>
            )}
          </button>
        </form>

        <div className="text-center">
          <span className="small text-muted">
            Already have an account?{' '}
            <Link to="/login" className="text-primary fw-semibold text-decoration-none">
              Sign in
            </Link>
          </span>
        </div>
      </div>
    </div>
  );
};

export default Register;
