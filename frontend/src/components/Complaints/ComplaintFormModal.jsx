import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const ComplaintFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Wi-Fi Bandwidth Degradation in Systems Lab 3',
    category: 'INFRASTRUCTURE',
    priority: 'HIGH',
    description: 'The wireless access points in Computer Lab 3 drop connection when 30+ workstations run network benchmark experiments.',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        category: initialData.category || 'INFRASTRUCTURE',
        priority: initialData.priority || 'MEDIUM',
        description: initialData.description || '',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      status: 'OPEN',
      submitted_by_name: 'Alex Johnson',
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Grievance Ticket — #${initialData?.id}` : 'Lodge Grievance or Institutional Complaint'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <FormField
            label="Grievance Title / Subject"
            name="title"
            placeholder="e.g. Broken AC unit in Curie-301, Lab network latency"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Grievance Category"
              type="select"
              name="category"
              value={formData.category}
              options={[
                { value: 'INFRASTRUCTURE', label: 'Campus Infrastructure & Labs' },
                { value: 'ACADEMIC', label: 'Academic & Curriculum Feedback' },
                { value: 'HOSTEL', label: 'Hostel & Residential Dining' },
                { value: 'RAGGING', label: 'Anti-Ragging & Campus Safety (Urgent)' },
                { value: 'ADMINISTRATIVE', label: 'Administrative & Bursar Support' },
              ]}
              onChange={(e) => setFormData({ ...formData, category: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Urgency & Priority Matrix"
              type="select"
              name="priority"
              value={formData.priority}
              options={[
                { value: 'LOW', label: 'Low — Routine Suggestion' },
                { value: 'MEDIUM', label: 'Medium — Standard Resolution' },
                { value: 'HIGH', label: 'High — Immediate Attention' },
                { value: 'CRITICAL', label: 'Critical — Safety / Escalation' },
              ]}
              onChange={(e) => setFormData({ ...formData, priority: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Detailed Statement of Problem & Location Specifics"
            type="textarea"
            rows={4}
            name="description"
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-danger btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Submitting...' : 'Submit Grievance Ticket'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default ComplaintFormModal;
