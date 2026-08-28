import React, { useState, useEffect } from 'react';
import { notificationService } from '../services';
import BroadcastNoticeModal from '../components/Notifications/BroadcastNoticeModal';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Notifications = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [filterType, setFilterType] = useState('ALL');

  const broadcastModal = useModal();

  const defaultNotifications = [
    { id: 1, title: 'Mid-Term Examination Timetable Released', message: 'The official semester examination matrix for CSE/ECE/EEE/MECH/CIVIL has been published. Check Examinations tab.', notification_type: 'EXAMINATION', target_role: 'ALL', is_read: false, created_at: '2026-08-28T10:30:00' },
    { id: 2, title: 'Fall 2026 Tuition Fee Payment Due Date Approaching', message: 'Tuition fees must be cleared by September 30th to avoid late registration holds. Receipts can be generated online.', notification_type: 'FEE', target_role: 'STUDENT', is_read: false, created_at: '2026-08-27T15:00:00' },
    { id: 3, title: 'Google Cloud Campus Recruitment Drive Registrations Open', message: 'Senior CSE/ECE students with GPA 3.5+ can apply for the Associate Cloud Solutions Engineer role.', notification_type: 'EVENT', target_role: 'STUDENT', is_read: true, created_at: '2026-08-26T09:15:00' },
    { id: 4, title: 'Annual International Hackathon 2026 Registration Passes', message: 'Claim your 48-hour hackathon participant pass. Mentors and compute clusters allocated in Innovation Arena.', notification_type: 'EVENT', target_role: 'ALL', is_read: true, created_at: '2026-08-25T11:45:00' },
  ];

  const [notifications, setNotifications] = useState(defaultNotifications);

  const fetchNotifications = async () => {
    setLoading(true);
    try {
      const res = await notificationService.getNotifications();
      if (res.results && res.results.length > 0) setNotifications(res.results);
    } catch (err) {
      setNotifications(defaultNotifications);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNotifications();
  }, []);

  const filtered = notifications.filter((n) => {
    return filterType === 'ALL' || n.notification_type === filterType;
  });

  const handleBroadcastSubmit = async (formData) => {
    setActionLoading(true);
    try {
      const newN = { ...formData, id: Date.now() };
      setNotifications([newN, ...notifications]);
      broadcastModal.closeModal();
      showSuccess(`Broadcasted notice: "${formData.title}"!`);
    } catch (err) {
      showError('Failed to broadcast notice.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleToggleRead = (id) => {
    setNotifications((prev) =>
      prev.map((n) => (n.id === id ? { ...n, is_read: !n.is_read } : n))
    );
  };

  const handleMarkAllRead = () => {
    setNotifications((prev) => prev.map((n) => ({ ...n, is_read: true })));
    showSuccess('Marked all notices as read.');
  };

  const getTypeBadge = (type) => {
    switch (type) {
      case 'EXAMINATION':
        return <span className="badge bg-danger px-3 py-1">Examination</span>;
      case 'FEE':
        return <span className="badge bg-warning text-dark px-3 py-1">Finance & Dues</span>;
      case 'EVENT':
        return <span className="badge bg-info px-3 py-1">Campus Event</span>;
      default:
        return <span className="badge bg-primary px-3 py-1">Academic</span>;
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Campus Announcements & Alerts</h2>
          <p className="text-muted mb-0">
            Targeted notifications, academic circulars, fee reminders, and real-time campus broadcasts
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={handleMarkAllRead}
            className="btn btn-outline-secondary btn-sm fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-check2-all me-1"></i> Mark All Read
          </button>
          <button
            onClick={() => broadcastModal.openModal()}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-megaphone-fill"></i>
            <span>Broadcast Notice</span>
          </button>
        </div>
      </div>

      {/* Filter Tabs */}
      <div className="d-flex gap-2 mb-4">
        {['ALL', 'EXAMINATION', 'FEE', 'EVENT', 'ACADEMIC'].map((cat) => (
          <button
            key={cat}
            className={`btn btn-sm px-3 fw-semibold ${filterType === cat ? 'btn-primary' : 'btn-light border'}`}
            onClick={() => setFilterType(cat)}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Notices Feed */}
      <div className="d-flex flex-column gap-3">
        {filtered.map((n) => (
          <div
            key={n.id}
            className={`campus-card shadow-sm border-0 p-4 ${n.is_read ? 'opacity-75 bg-light' : 'border-start border-primary border-4'}`}
          >
            <div className="d-flex justify-content-between align-items-start mb-2">
              <div className="d-flex align-items-center gap-2">
                {getTypeBadge(n.notification_type)}
                <span className="badge bg-light text-secondary border">Audience: {n.target_role}</span>
                <small className="text-muted">
                  <i className="bi bi-clock me-1"></i>
                  {new Date(n.created_at).toLocaleString()}
                </small>
              </div>
              <button
                className="btn btn-sm btn-link text-decoration-none p-0 text-muted"
                onClick={() => handleToggleRead(n.id)}
              >
                <i className={`bi ${n.is_read ? 'bi-envelope-open' : 'bi-envelope-fill text-primary'}`}></i>
              </button>
            </div>

            <h5 className="fw-bold text-dark mb-2">{n.title}</h5>
            <p className="text-secondary small mb-0">{n.message}</p>
          </div>
        ))}
      </div>

      {/* Broadcast Modal */}
      <BroadcastNoticeModal
        isOpen={broadcastModal.isOpen}
        onClose={broadcastModal.closeModal}
        onSubmit={handleBroadcastSubmit}
        loading={actionLoading}
      />
    </div>
  );
};

export default Notifications;
