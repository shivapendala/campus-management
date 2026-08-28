import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const EventFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Annual International Hackathon 2026',
    event_type: 'HACKATHON',
    venue: 'Innovation & Incubation Arena',
    start_time: '2026-10-10T09:00',
    end_time: '2026-10-12T18:00',
    capacity: 250,
    description: '48-hour global student hackathon building AI agents and distributed cloud solutions.',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        event_type: initialData.event_type || 'HACKATHON',
        venue: initialData.venue || 'Innovation Arena',
        start_time: initialData.start_time ? initialData.start_time.slice(0, 16) : '2026-10-10T09:00',
        end_time: initialData.end_time ? initialData.end_time.slice(0, 16) : '2026-10-12T18:00',
        capacity: initialData.capacity || 250,
        description: initialData.description || '',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      capacity: Number(formData.capacity),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Event — ${formData.title}` : 'Organize New Campus Event'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-8">
            <FormField
              label="Event Title"
              name="title"
              placeholder="e.g. ACM Tech Symposium 2026"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Event Type"
              type="select"
              name="event_type"
              value={formData.event_type}
              options={[
                { value: 'HACKATHON', label: 'Hackathon / Codefest' },
                { value: 'SEMINAR', label: 'Technical Seminar / Keynote' },
                { value: 'WORKSHOP', label: 'Hands-on Workshop' },
                { value: 'CULTURAL', label: 'Cultural & Arts Festival' },
                { value: 'SPORTS', label: 'Inter-Department Sports Meet' },
              ]}
              onChange={(e) => setFormData({ ...formData, event_type: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Allocated Campus Venue"
              name="venue"
              value={formData.venue}
              onChange={(e) => setFormData({ ...formData, venue: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Start Date & Time"
              type="datetime-local"
              name="start_time"
              value={formData.start_time}
              onChange={(e) => setFormData({ ...formData, start_time: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="End Date & Time"
              type="datetime-local"
              name="end_time"
              value={formData.end_time}
              onChange={(e) => setFormData({ ...formData, end_time: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="row g-3 mb-4">
          <div className="col-12 col-md-4">
            <FormField
              label="Audience Capacity (Seats)"
              type="number"
              name="capacity"
              value={formData.capacity}
              onChange={(e) => setFormData({ ...formData, capacity: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-8">
            <FormField
              label="Event Description & Key Highlights"
              name="description"
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Publishing...' : isEdit ? 'Save Changes' : 'Publish Campus Event'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default EventFormModal;
