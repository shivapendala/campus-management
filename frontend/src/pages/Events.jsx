import React, { useState, useEffect } from 'react';
import { eventService } from '../services';
import EventFormModal from '../components/Events/EventFormModal';
import EventRegistrationModal from '../components/Events/EventRegistrationModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Events = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Modals
  const eventModal = useModal();
  const regModal = useModal();
  const deleteModal = useModal();

  const defaultEvents = [
    { id: 1, title: 'Annual International Hackathon 2026', event_type: 'HACKATHON', venue: 'Innovation Arena', start_time: '2026-10-10T09:00:00', end_time: '2026-10-12T18:00:00', capacity: 250, registered_count: 184, description: '48-hour global student hackathon building AI agents and cloud systems with industry mentorship.' },
    { id: 2, title: 'IEEE Keynote: Quantum Computing & Distributed State', event_type: 'SEMINAR', venue: 'Curie-301 Auditorium', start_time: '2026-10-18T14:00:00', end_time: '2026-10-18T17:00:00', capacity: 180, registered_count: 120, description: 'Guest keynote by visiting MIT and Stanford research fellows on qubit fault tolerance.' },
    { id: 3, title: 'Autumn Cultural & Performing Arts Festival', event_type: 'CULTURAL', venue: 'Open Amphitheatre', start_time: '2026-11-01T17:00:00', end_time: '2026-11-03T22:00:00', capacity: 600, registered_count: 450, description: 'Campus musical performances, drama club productions, and culinary showcases.' },
    { id: 4, title: 'Kubernetes & Production Cloud Workshop', event_type: 'WORKSHOP', venue: 'Cloud Systems Lab 2', start_time: '2026-11-10T10:00:00', end_time: '2026-11-10T16:00:00', capacity: 60, registered_count: 58, description: 'Hands-on cluster deployments, microservices orchestration, and Helm charts.' },
  ];

  const [events, setEvents] = useState(defaultEvents);

  const fetchEvents = async () => {
    setLoading(true);
    try {
      const res = await eventService.getEvents();
      if (res.results && res.results.length > 0) setEvents(res.results);
    } catch (err) {
      setEvents(defaultEvents);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  // Handle Event CRUD
  const handleEventSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (eventModal.modalData?.isEdit) {
        setEvents((prev) =>
          prev.map((e) => (e.id === eventModal.modalData.event.id ? { ...e, ...formData } : e))
        );
        showSuccess(`Event "${formData.title}" updated.`);
      } else {
        const newE = { ...formData, id: Date.now(), registered_count: 0 };
        setEvents([...events, newE]);
        showSuccess(`Published event "${formData.title}"!`);
      }
      eventModal.closeModal();
    } catch (err) {
      showError('Failed to save event.');
    } finally {
      setActionLoading(false);
    }
  };

  // Handle Register
  const handleRegisterSubmit = async (regData) => {
    setActionLoading(true);
    try {
      const targetEvent = regModal.modalData?.event;
      setEvents((prev) =>
        prev.map((e) => (e.id === targetEvent.id ? { ...e, registered_count: e.registered_count + 1 } : e))
      );
      regModal.closeModal();
      showSuccess(`Pass registered for "${targetEvent.title}"!`);
    } catch (err) {
      showError('Failed to register.');
    } finally {
      setActionLoading(false);
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Campus Events & Co-Curricular Life</h2>
          <p className="text-muted mb-0">
            Hackathons, technical symposiums, research keynotes, cultural festivals, and registration passes
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => eventModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-calendar-event-fill"></i>
            <span>Create Campus Event</span>
          </button>
        </div>
      </div>

      {/* Events Grid */}
      <div className="row g-4">
        {events.map((ev) => (
          <div key={ev.id} className="col-12 col-lg-6">
            <div className="campus-card shadow-sm border-0 p-4 h-100 d-flex flex-column justify-content-between">
              <div>
                <div className="d-flex justify-content-between align-items-start mb-2">
                  <span className="badge bg-primary px-3 py-1">{ev.event_type}</span>
                  <span className="badge bg-light text-secondary border">
                    {ev.registered_count} / {ev.capacity} Registered
                  </span>
                </div>

                <h5 className="fw-bold text-dark mb-1">{ev.title}</h5>
                <p className="small text-secondary mb-3">{ev.description}</p>

                <div className="p-2 bg-light rounded border small mb-3">
                  <div className="row g-2">
                    <div className="col-6">
                      <span className="text-secondary d-block">Venue:</span>
                      <strong><i className="bi bi-geo-alt-fill text-danger me-1"></i>{ev.venue}</strong>
                    </div>
                    <div className="col-6">
                      <span className="text-secondary d-block">Starts:</span>
                      <strong>{new Date(ev.start_time).toLocaleString()}</strong>
                    </div>
                  </div>
                </div>

                {/* Capacity Progress */}
                <div className="mb-2">
                  <div className="d-flex justify-content-between small text-muted mb-1">
                    <span>Registration Capacity</span>
                    <span>{Math.round((ev.registered_count / ev.capacity) * 100)}% Claimed</span>
                  </div>
                  <div className="progress" style={{ height: '6px' }}>
                    <div
                      className="progress-bar bg-primary"
                      style={{ width: `${(ev.registered_count / ev.capacity) * 100}%` }}
                    ></div>
                  </div>
                </div>
              </div>

              <div className="pt-3 border-top d-flex justify-content-between align-items-center">
                <div className="d-flex gap-1">
                  <button
                    className="btn btn-outline-secondary btn-sm"
                    onClick={() => eventModal.openModal({ event: ev, isEdit: true })}
                    title="Edit Event"
                  >
                    <i className="bi bi-pencil"></i>
                  </button>
                  <button
                    className="btn btn-outline-danger btn-sm"
                    onClick={() => deleteModal.openModal(ev)}
                    title="Delete Event"
                  >
                    <i className="bi bi-trash"></i>
                  </button>
                </div>

                <button
                  disabled={ev.registered_count >= ev.capacity}
                  className="btn btn-success btn-sm px-4 fw-semibold shadow-sm"
                  onClick={() => regModal.openModal({ event: ev })}
                >
                  <i className="bi bi-ticket-perforated-fill me-1"></i> Register Pass
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Modals */}
      <EventFormModal
        isOpen={eventModal.isOpen}
        onClose={eventModal.closeModal}
        onSubmit={handleEventSubmit}
        initialData={eventModal.modalData?.event}
        isEdit={eventModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <EventRegistrationModal
        isOpen={regModal.isOpen}
        onClose={regModal.closeModal}
        onSubmit={handleRegisterSubmit}
        selectedEvent={regModal.modalData?.event}
        loading={actionLoading}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={() => {
          setEvents((prev) => prev.filter((e) => e.id !== deleteModal.modalData.id));
          deleteModal.closeModal();
          showSuccess('Event deleted.');
        }}
        title="Cancel Campus Event"
        message={`Are you sure you want to cancel "${deleteModal.modalData?.title}"?`}
        confirmText="Cancel Event"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Events;
