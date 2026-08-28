import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const BroadcastNoticeModal = ({
  isOpen,
  onClose,
  onSubmit,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Mid-Term Examination Schedule & Hall Ticket Issuance',
    message: 'Official mid-term examination timetable has been published. All students must download hall tickets by September 15th.',
    notification_type: 'ACADEMIC',
    target_role: 'ALL',
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      is_read: false,
      created_at: new Date().toISOString(),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title="Broadcast Campus Notice / Announcement"
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <FormField
            label="Announcement Headline / Title"
            name="title"
            placeholder="e.g. Campus Holiday Notice, Examination Schedule"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Notification Category"
              type="select"
              name="notification_type"
              value={formData.notification_type}
              options={[
                { value: 'ACADEMIC', label: 'Academic & Curriculum' },
                { value: 'EXAMINATION', label: 'Examination & Hall Tickets' },
                { value: 'FEE', label: 'Finance & Tuition Due Reminder' },
                { value: 'EVENT', label: 'Campus Event & Seminar' },
                { value: 'GENERAL', label: 'General Administrative Notice' },
              ]}
              onChange={(e) => setFormData({ ...formData, notification_type: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Target Audience"
              type="select"
              name="target_role"
              value={formData.target_role}
              options={[
                { value: 'ALL', label: 'All Campus (Students, Faculty, Staff)' },
                { value: 'STUDENT', label: 'Students Only' },
                { value: 'FACULTY', label: 'Faculty Members Only' },
                { value: 'ADMIN', label: 'Administrative Staff' },
              ]}
              onChange={(e) => setFormData({ ...formData, target_role: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Announcement Message Content"
            type="textarea"
            rows={4}
            name="message"
            value={formData.message}
            onChange={(e) => setFormData({ ...formData, message: e.target.value })}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Broadcasting...' : 'Broadcast Notice'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default BroadcastNoticeModal;
