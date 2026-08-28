import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const VenueConflictDashboard = () => {
  const [venueCapacity, setVenueCapacity] = useState('');
  const [expectedAttendees, setExpectedAttendees] = useState('');
  const [conflictAlert, setConflictAlert] = useState(null);

  const initialBookings = [
    { id: 'BKG-001', title: 'CSE Department Research Seminar', room: 'Seminar Hall 1', time: '10:00 AM - 12:00 PM', capacity: '150 Pax', status: 'CONFIRMED' },
    { id: 'BKG-002', title: 'Placement Drive pre-talk - Robert Bosch', room: 'Seminar Hall 3', time: '11:00 AM - 01:00 PM', capacity: '200 Pax', status: 'CONFIRMED' },
    { id: 'BKG-003', title: 'VLSI lab workshop', room: 'VLSI Design Center Lab', time: '02:00 PM - 05:00 PM', capacity: '40 Pax', status: 'CONFIRMED' },
    { id: 'BKG-004', title: 'AICTE Compliance inspection briefing', room: 'Board Room', time: '03:00 PM - 04:30 PM', capacity: '30 Pax', status: 'CONFIRMED' }
  ];

  const columns = [
    { key: 'id', label: 'Booking Code', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'title', label: 'Event Title' },
    { key: 'room', label: 'Venue / Room' },
    { key: 'time', label: 'Booked Slot' },
    { key: 'capacity', label: 'Capacity limit' },
    { key: 'status', label: 'Booking Status', render: (val) => <StatusBadge status={val} size="small" /> }
  ];

  const handleBookingCheck = (e) => {
    e.preventDefault();
    const cap = parseInt(venueCapacity) || 0;
    const att = parseInt(expectedAttendees) || 0;

    if (att > cap) {
      setConflictAlert({
        success: False,
        message: `Capacity constraint violated: Attendees (${att}) exceed venue capacity (${cap}).`
      });
    } else {
      setConflictAlert({
        success: True,
        message: "No capacity issues detected. Booking can be safely processed."
      });
    }
  };

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-calendar-event-fill me-2"></i>Venue Booking & Conflict Console
          </h2>
          <p className="text-muted mb-0">
            Real-time schedule audits, room double-booking detection, and capacity constraint verification.
          </p>
        </div>
      </div>

      <div className="row g-4 mb-4">
        <div className="col-lg-4">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-clock me-2"></i>Conflict & Capacity Check</h5>
            <form onSubmit={handleBookingCheck}>
              <div className="mb-3">
                <label className="form-label small fw-bold">Venue Capacity Limit</label>
                <input
                  type="number"
                  className="form-control"
                  value={venueCapacity}
                  onChange={(e) => setVenueCapacity(e.target.value)}
                  placeholder="e.g. 100"
                  required
                />
              </div>
              <div className="mb-3">
                <label className="form-label small fw-bold">Expected Attendees</label>
                <input
                  type="number"
                  className="form-control"
                  value={expectedAttendees}
                  onChange={(e) => setExpectedAttendees(e.target.value)}
                  placeholder="e.g. 120"
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary w-100 mt-2">
                <i className="bi bi-calendar-check me-1"></i>Check Allocation Availability
              </button>
            </form>

            {conflictAlert && (
              <div className={`mt-4 p-3 rounded-3 border-start border-4 ${conflictAlert.success ? 'bg-success-subtle border-success' : 'bg-danger-subtle border-danger'}`}>
                <h6 className="fw-bold mb-1">{conflictAlert.success ? 'Approval OK' : 'Conflict Alert'}</h6>
                <div className="small">{conflictAlert.message}</div>
              </div>
            )}
          </div>
        </div>

        <div className="col-lg-8">
          <div className="card border-0 shadow-sm rounded-3 p-4 h-100">
            <h5 className="fw-bold mb-3 text-primary"><i className="bi bi-list-stars me-2"></i>Venue Bookings Schedule</h5>
            <AdvancedDataTable columns={columns} data={initialBookings} searchPlaceholder="Search bookings..." />
          </div>
        </div>
      </div>
    </div>
  );
};

export default VenueConflictDashboard;
