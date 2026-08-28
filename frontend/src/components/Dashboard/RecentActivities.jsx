import React, { useEffect, useState } from 'react';
import api from '../../api/axios';

export const RecentActivities = () => {
  const [activities, setActivities] = useState([
    {
      id: 1,
      title: 'Placement Offer Extended',
      description: 'Google Cloud extended 8 software engineering offers for B.Tech CS students.',
      category: 'PLACEMENT',
      badge_class: 'bg-success text-white',
      time_ago: '12 mins ago',
      icon: 'bi-briefcase-fill',
    },
    {
      id: 2,
      title: 'Tuition Fee Payment Received',
      description: 'Online fee receipt #TXN-982347 verified for Student Alex Johnson ($4,500.00).',
      category: 'FINANCE',
      badge_class: 'bg-primary text-white',
      time_ago: '34 mins ago',
      icon: 'bi-cash-coin',
    },
    {
      id: 3,
      title: 'Attendance Session Recorded',
      description: 'Dr. Alan Smith submitted lecture attendance for CS-101 (58 Present, 2 Absent).',
      category: 'ATTENDANCE',
      badge_class: 'bg-info text-dark',
      time_ago: '1 hour ago',
      icon: 'bi-calendar-check-fill',
    },
    {
      id: 4,
      title: 'Grievance Ticket Resolved',
      description: 'Ticket #INF-2026-44 (Wi-Fi Signal in Computer Lab 3) marked as RESOLVED.',
      category: 'COMPLAINT',
      badge_class: 'bg-warning text-dark',
      time_ago: '2 hours ago',
      icon: 'bi-check-circle-fill',
    },
    {
      id: 5,
      title: 'Midterm Examination Schedule Published',
      description: 'Fall 2026 assessment dates uploaded for all 95 active catalog courses.',
      category: 'EXAM',
      badge_class: 'bg-secondary text-white',
      time_ago: '4 hours ago',
      icon: 'bi-mortarboard-fill',
    },
  ]);

  useEffect(() => {
    const fetchActivities = async () => {
      try {
        const res = await api.get('/reports/activities/');
        if (res.data && res.data.length > 0) {
          setActivities(res.data);
        }
      } catch (err) {
        // use fallback activities
      }
    };
    fetchActivities();
  }, []);

  return (
    <div className="campus-card p-4 h-100 shadow-sm border-0">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <div>
          <h5 className="fw-bold text-dark mb-1">
            <i className="bi bi-activity text-primary me-2"></i>
            Live Recent Activities
          </h5>
          <p className="text-muted small mb-0">System audit log of academic and administrative actions</p>
        </div>
        <span className="badge bg-light text-secondary border">Real-Time</span>
      </div>

      <div className="timeline">
        {activities.map((item) => (
          <div key={item.id} className="d-flex gap-3 mb-3 pb-3 border-bottom last-border-0">
            <div
              className={`rounded-circle d-flex align-items-center justify-content-center flex-shrink-0 shadow-sm ${item.badge_class}`}
              style={{ width: '38px', height: '38px' }}
            >
              <i className={`bi ${item.icon} fs-6`}></i>
            </div>
            <div className="flex-grow-1">
              <div className="d-flex justify-content-between align-items-start">
                <strong className="text-dark small">{item.title}</strong>
                <span className="text-muted" style={{ fontSize: '11px' }}>
                  {item.time_ago}
                </span>
              </div>
              <p className="text-muted small mb-0 mt-1">{item.description}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default RecentActivities;
