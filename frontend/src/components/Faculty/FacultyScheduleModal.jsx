import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import { facultyService } from '../../services';

export const FacultyScheduleModal = ({ isOpen, onClose, faculty = null }) => {
  const [schedule, setSchedule] = useState([
    {
      day: 'Monday',
      slots: [
        { time: '09:00 AM - 10:30 AM', course: 'CS-101', title: 'Data Structures & Algorithms', type: 'Lecture', room: 'Turing-101', section: 'Sec A' },
        { time: '11:00 AM - 12:30 PM', course: 'CS-204', title: 'Distributed Cloud Architectures', type: 'Lecture', room: 'Tesla-204', section: 'Sec B' },
      ],
    },
    {
      day: 'Tuesday',
      slots: [
        { time: '10:00 AM - 11:30 AM', course: 'CS-305', title: 'Artificial Intelligence Foundations', type: 'Lecture', room: 'Curie-301', section: 'Sec A' },
        { time: '02:00 PM - 04:30 PM', course: 'CS-101', title: 'Data Structures Laboratory', type: 'Lab', room: 'Lab-3', section: 'Sec A' },
      ],
    },
    {
      day: 'Wednesday',
      slots: [
        { time: '09:00 AM - 10:30 AM', course: 'CS-101', title: 'Data Structures & Algorithms', type: 'Lecture', room: 'Turing-101', section: 'Sec A' },
        { time: '02:00 PM - 03:30 PM', course: 'CS-204', title: 'Distributed Cloud Architectures', type: 'Lecture', room: 'Tesla-204', section: 'Sec B' },
      ],
    },
    {
      day: 'Thursday',
      slots: [
        { time: '11:00 AM - 12:30 PM', course: 'CS-305', title: 'Artificial Intelligence Foundations', type: 'Lecture', room: 'Curie-301', section: 'Sec A' },
        { time: '03:30 PM - 05:00 PM', course: 'OFFICE', title: 'Student Mentoring & Advising', type: 'Office Hours', room: faculty?.office_room || 'Room 204', section: 'All Batches' },
      ],
    },
    {
      day: 'Friday',
      slots: [
        { time: '09:00 AM - 10:30 AM', course: 'CS-101', title: 'Data Structures Problem Solving', type: 'Tutorial', room: 'Turing-101', section: 'Sec A' },
        { time: '02:00 PM - 04:30 PM', course: 'CS-204', title: 'Cloud Container Kubernetes Lab', type: 'Lab', room: 'Cloud Lab 2', section: 'Sec B' },
      ],
    },
  ]);

  useEffect(() => {
    if (isOpen && faculty?.id) {
      facultyService
        .getSchedule(faculty.id)
        .then((res) => {
          if (res.schedule && res.schedule.length > 0) setSchedule(res.schedule);
        })
        .catch(() => {});
    }
  }, [isOpen, faculty]);

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Weekly Timetable & Schedule — ${faculty?.name || 'Faculty Member'}`}
      size="lg"
    >
      <div className="d-flex flex-column gap-3">
        {schedule.map((dayItem, idx) => (
          <div key={idx} className="p-3 bg-light rounded-3 border">
            <div className="d-flex justify-content-between align-items-center mb-2 pb-1 border-bottom">
              <strong className="text-primary">{dayItem.day}</strong>
              <span className="badge bg-white text-secondary border small">{dayItem.slots?.length || 0} Periods</span>
            </div>
            <div className="d-flex flex-column gap-2">
              {dayItem.slots?.map((slot, sIdx) => (
                <div key={sIdx} className="p-2 bg-white rounded border d-flex flex-wrap justify-content-between align-items-center gap-2 small">
                  <div>
                    <span className="fw-bold text-dark me-2">{slot.time}</span>
                    <span className="badge bg-primary-subtle text-primary me-2">{slot.course}</span>
                    <span className="text-secondary">{slot.title} ({slot.section})</span>
                  </div>
                  <div className="d-flex align-items-center gap-2">
                    <span className="badge bg-light text-muted border">{slot.room}</span>
                    <span className={`badge ${slot.type === 'Lab' ? 'bg-info text-dark' : slot.type === 'Lecture' ? 'bg-success text-white' : 'bg-secondary text-white'}`}>
                      {slot.type}
                    </span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>
    </Modal>
  );
};

export default FacultyScheduleModal;
