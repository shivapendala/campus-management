import React from 'react';

export const TimetableGrid = ({
  slots = [],
  onEditSlot,
  onDeleteSlot,
  viewPerspective = 'student', // 'student', 'faculty', 'room'
}) => {
  const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];

  const getDaySlots = (day) => {
    return slots
      .filter((s) => s.day === day)
      .sort((a, b) => (a.start_time > b.start_time ? 1 : -1));
  };

  const getSlotColorClass = (entryType, title) => {
    if (entryType === 'BREAK' || title.toLowerCase().includes('break')) return 'border-warning bg-warning-subtle text-warning-emphasis';
    if (entryType === 'LAB') return 'border-info bg-info-subtle text-info-emphasis';
    if (entryType === 'TUTORIAL') return 'border-success bg-success-subtle text-success-emphasis';
    return 'border-primary bg-primary-subtle text-primary-emphasis';
  };

  return (
    <div className="d-flex flex-column gap-4">
      {days.map((day) => {
        const daySlots = getDaySlots(day);
        return (
          <div key={day} className="campus-card p-3 shadow-sm border-0">
            <div className="d-flex justify-content-between align-items-center mb-3 pb-2 border-bottom">
              <div className="d-flex align-items-center gap-2">
                <span className="badge bg-primary text-white fs-6 px-3 py-1 fw-bold">
                  {day}
                </span>
                <span className="text-muted small">
                  {daySlots.length} Scheduled Periods
                </span>
              </div>
            </div>

            {daySlots.length === 0 ? (
              <div className="text-center py-4 text-muted small">
                <i className="bi bi-calendar-x d-block fs-3 mb-1"></i>
                No classes scheduled for {day} in this view.
              </div>
            ) : (
              <div className="row g-3">
                {daySlots.map((slot) => {
                  const isBreak = slot.entry_type === 'BREAK' || slot.title.toLowerCase().includes('break');
                  return (
                    <div key={slot.id} className="col-12 col-md-6 col-xl-4">
                      <div
                        className={`p-3 rounded-3 border-start border-4 h-100 shadow-sm transition-all hover-shadow ${getSlotColorClass(
                          slot.entry_type,
                          slot.title
                        )}`}
                        style={{ backgroundColor: '#ffffff' }}
                      >
                        <div className="d-flex justify-content-between align-items-start mb-2">
                          <span className="badge bg-dark text-white fw-bold">
                            <i className="bi bi-clock me-1"></i>
                            {slot.start_time} - {slot.end_time}
                          </span>
                          <div className="d-flex gap-1">
                            <button
                              className="btn btn-sm btn-link text-secondary p-0"
                              onClick={() => onEditSlot(slot)}
                              title="Edit Slot"
                            >
                              <i className="bi bi-pencil"></i>
                            </button>
                            <button
                              className="btn btn-sm btn-link text-danger p-0 ms-1"
                              onClick={() => onDeleteSlot(slot)}
                              title="Delete Slot"
                            >
                              <i className="bi bi-trash"></i>
                            </button>
                          </div>
                        </div>

                        <div className="mb-2">
                          <h6 className="fw-bold text-dark mb-0">{slot.title}</h6>
                          {slot.course_code && (
                            <span className="badge bg-light text-secondary border small mt-1">
                              {slot.course_code}
                            </span>
                          )}
                        </div>

                        {!isBreak && (
                          <div className="d-flex flex-column gap-1 small text-secondary mt-2 pt-2 border-top">
                            <div>
                              <i className="bi bi-person-fill text-primary me-1"></i>
                              <strong>Faculty:</strong> {slot.faculty_name || slot.faculty_detail?.name || 'Dr. Alan Smith'}
                            </div>
                            <div className="d-flex justify-content-between">
                              <span>
                                <i className="bi bi-geo-alt-fill text-danger me-1"></i>
                                <strong>Room:</strong> {slot.room}
                              </span>
                              <span>
                                <i className="bi bi-people-fill text-info me-1"></i>
                                Sec {slot.section} (Yr {slot.year})
                              </span>
                            </div>
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
};

export default TimetableGrid;
