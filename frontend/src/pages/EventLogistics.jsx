import React, { useState } from 'react';
import MetricCard from '../components/common/MetricCard';
import AdvancedDataTable from '../components/common/AdvancedDataTable';
import StatusBadge from '../components/common/StatusBadge';

const EventLogistics = () => {
  const events = [
    { code: 'EVT-2026-01', title: 'National Tech Symposium: INNOVA 2026', venue: 'Main Auditorium', dates: '2026-09-15 to 2026-09-17', attendees: '850 Registered', budget: 'Rs. 4.5L (Surplus)', status: 'CONFIRMED' },
    { code: 'EVT-2026-02', title: 'Annual Cultural Festival: RHYTHM 2026', venue: 'Open Air Theatre (OAT)', dates: '2026-10-02 to 2026-10-04', attendees: '2,200 Expected', budget: 'Rs. 12.0L (Sanctioned)', status: 'CONFIRMED' },
    { code: 'EVT-2026-03', title: 'IEEE International Conference on AI & IoT', venue: 'Seminar Hall A', dates: '2026-11-10 to 2026-11-12', attendees: '320 Delegates', budget: 'Rs. 6.0L (Grant)', status: 'ACTIVE' },
  ];

  const columns = [
    { key: 'code', label: 'Event ID', render: (val) => <strong className="text-primary">{val}</strong> },
    { key: 'title', label: 'Event Title' },
    { key: 'venue', label: 'Venue Booked' },
    { key: 'dates', label: 'Scheduled Dates' },
    { key: 'attendees', label: 'Delegates' },
    { key: 'budget', label: 'Fiscal Budget' },
    { key: 'status', label: 'Status', render: (val) => <StatusBadge status={val} size="small" /> },
  ];

  return (
    <div className="container-fluid py-4">
      <div className="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-2">
        <div>
          <h2 className="fw-bold mb-1 text-primary">
            <i className="bi bi-calendar-event-fill me-2"></i>Campus Events & Logistics Studio
          </h2>
          <p className="text-muted mb-0">
            Auditorium venue collision detector, delegate badge generation, sponsorship accounting, and attendee registrations.
          </p>
        </div>
        <div className="d-flex gap-2">
          <button className="btn btn-outline-primary">
            <i className="bi bi-qr-code me-1"></i>Delegate Pass Scanner
          </button>
          <button className="btn btn-primary">
            <i className="bi bi-plus-circle me-1"></i>Book Venue Slot
          </button>
        </div>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Scheduled Major Events"
            value="14 Events"
            icon="bi-calendar2-check-fill"
            variant="primary"
            subtitle="Academic Year 2026-27"
            delta="Calendar Finalized"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Total Registered Attendees"
            value="4,850"
            icon="bi-people-fill"
            variant="success"
            subtitle="Across Symposia & Conferences"
            delta="+22% YoY"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Venue Collision Risk"
            value="0 Collisions"
            icon="bi-shield-check"
            variant="info"
            subtitle="60-Minute Buffers Enforced"
            delta="Conflict-Free"
            deltaType="positive"
          />
        </div>
        <div className="col-md-3 col-sm-6">
          <MetricCard
            title="Sponsorship Raised"
            value="Rs. 18.5 Lakhs"
            icon="bi-cash-coin"
            variant="warning"
            subtitle="Corporate Event Grants"
            delta="Surplus"
            deltaType="positive"
          />
        </div>
      </div>

      <div className="card border-0 shadow-sm rounded-3 p-4">
        <h5 className="fw-bold mb-3">
          <i className="bi bi-calendar3 me-2 text-primary"></i>Scheduled Institutional Events & Symposia
        </h5>
        <AdvancedDataTable
          columns={columns}
          data={events}
          searchPlaceholder="Search event by name, venue, or code..."
        />
      </div>
    </div>
  );
};

export default EventLogistics;
