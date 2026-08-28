import React, { useState, useEffect } from 'react';
import { timetableService } from '../services';
import TimetableGrid from '../components/Timetable/TimetableGrid';
import TimetableFormModal from '../components/Timetable/TimetableFormModal';
import ConflictAlertModal from '../components/Timetable/ConflictAlertModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Timetable = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [slots, setSlots] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // View Perspective: 'student', 'faculty', 'room'
  const [viewPerspective, setViewPerspective] = useState('student');
  const [selectedSection, setSelectedSection] = useState('A');
  const [selectedYear, setSelectedYear] = useState('3');
  const [selectedFaculty, setSelectedFaculty] = useState('ALL');
  const [selectedRoom, setSelectedRoom] = useState('ALL');

  // Modals
  const formModal = useModal();
  const conflictModal = useModal();
  const deleteModal = useModal();
  const [detectedConflicts, setDetectedConflicts] = useState([]);

  const defaultMondaySlots = [
    { id: 1, day: 'Monday', start_time: '09:00', end_time: '10:00', title: 'DBMS', course_code: 'CSE-202', faculty_id: 2, faculty_name: 'Dr. Elena Rostova', room: 'Turing-204', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 2, day: 'Monday', start_time: '10:00', end_time: '11:00', title: 'OS', course_code: 'CSE-301', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 3, day: 'Monday', start_time: '11:00', end_time: '11:30', title: 'Break / Recess', course_code: 'BREAK', faculty_id: 0, faculty_name: 'None', room: 'Campus Lounge', year: 3, section: 'A', entry_type: 'BREAK' },
    { id: 4, day: 'Monday', start_time: '11:30', end_time: '12:30', title: 'Networks', course_code: 'CSE-302', faculty_id: 2, faculty_name: 'Dr. Elena Rostova', room: 'Tesla-204', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 5, day: 'Monday', start_time: '01:30', end_time: '02:30', title: 'ML', course_code: 'CSE-401', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'LECTURE' },
    // Tuesday
    { id: 6, day: 'Tuesday', start_time: '09:00', end_time: '10:00', title: 'Data Structures', course_code: 'CSE-101', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 7, day: 'Tuesday', start_time: '10:00', end_time: '12:30', title: 'DBMS SQL Laboratory', course_code: 'CSE-202', faculty_id: 2, faculty_name: 'Dr. Elena Rostova', room: 'Lab-3', year: 3, section: 'A', entry_type: 'LAB' },
    // Wednesday
    { id: 8, day: 'Wednesday', start_time: '09:00', end_time: '10:00', title: 'Operating Systems', course_code: 'CSE-301', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 9, day: 'Wednesday', start_time: '10:00', end_time: '11:00', title: 'Computer Networks', course_code: 'CSE-302', faculty_id: 2, faculty_name: 'Dr. Elena Rostova', room: 'Tesla-204', year: 3, section: 'A', entry_type: 'LECTURE' },
    // Thursday
    { id: 10, day: 'Thursday', start_time: '09:00', end_time: '10:00', title: 'Machine Learning', course_code: 'CSE-401', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'LECTURE' },
    { id: 11, day: 'Thursday', start_time: '02:00', end_time: '04:30', title: 'OS Kernel Lab', course_code: 'CSE-301', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Cloud Lab 2', year: 3, section: 'A', entry_type: 'LAB' },
    // Friday
    { id: 12, day: 'Friday', start_time: '09:00', end_time: '10:00', title: 'Data Structures Tutorial', course_code: 'CSE-101', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Turing-101', year: 3, section: 'A', entry_type: 'TUTORIAL' },
    { id: 13, day: 'Friday', start_time: '11:00', end_time: '12:30', title: 'AI Project Mentoring', course_code: 'CSE-401', faculty_id: 1, faculty_name: 'Dr. Alan Smith', room: 'Curie-301', year: 3, section: 'A', entry_type: 'LECTURE' },
  ];

  const fetchTimetable = async () => {
    setLoading(true);
    try {
      const res = await timetableService.getAll();
      if (res.results && res.results.length > 0) {
        setSlots(res.results);
      } else {
        setSlots(defaultMondaySlots);
      }
    } catch (err) {
      setSlots(defaultMondaySlots);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTimetable();
  }, []);

  // Filter slots by active perspective
  const filteredSlots = slots.filter((slot) => {
    if (viewPerspective === 'student') {
      const matchesYear = selectedYear === 'ALL' || String(slot.year) === String(selectedYear);
      const matchesSec = selectedSection === 'ALL' || slot.section === selectedSection;
      return matchesYear && matchesSec;
    } else if (viewPerspective === 'faculty') {
      if (selectedFaculty === 'ALL') return true;
      return String(slot.faculty_id) === String(selectedFaculty) || slot.faculty_name?.includes(selectedFaculty);
    } else if (viewPerspective === 'room') {
      if (selectedRoom === 'ALL') return true;
      return slot.room === selectedRoom;
    }
    return true;
  });

  // Form Submit with Conflict Verification
  const handleFormSubmit = async (formData) => {
    setActionLoading(true);

    // Client-side conflict detection guard
    const conflicts = [];
    const excludeId = formModal.modalData?.slot?.id;

    const roomClash = slots.find(
      (s) =>
        s.id !== excludeId &&
        s.day === formData.day &&
        s.room === formData.room &&
        s.start_time === formData.start_time
    );
    if (roomClash) {
      conflicts.push({
        type: 'ROOM_COLLISION',
        message: `Room ${formData.room} is already allocated on ${formData.day} at ${formData.start_time} for ${roomClash.title} (${roomClash.section}).`,
      });
    }

    if (formData.faculty_id && formData.faculty_id > 0) {
      const facClash = slots.find(
        (s) =>
          s.id !== excludeId &&
          s.day === formData.day &&
          s.faculty_id === formData.faculty_id &&
          s.start_time === formData.start_time
      );
      if (facClash) {
        conflicts.push({
          type: 'FACULTY_DOUBLE_BOOKING',
          message: `${formData.faculty_name || 'Professor'} is already scheduled to teach ${facClash.title} in ${facClash.room} on ${formData.day} at ${formData.start_time}.`,
        });
      }
    }

    if (conflicts.length > 0) {
      setActionLoading(false);
      setDetectedConflicts(conflicts);
      conflictModal.openModal();
      return;
    }

    // Save
    try {
      if (formModal.modalData?.isEdit) {
        setSlots((prev) =>
          prev.map((s) => (s.id === formModal.modalData.slot.id ? { ...s, ...formData } : s))
        );
        showSuccess(`Timetable period for ${formData.title} updated!`);
      } else {
        const newSlot = { ...formData, id: Date.now() };
        setSlots([...slots, newSlot]);
        showSuccess(`Scheduled ${formData.title} (${formData.start_time} - ${formData.end_time})!`);
      }
      formModal.closeModal();
    } catch (err) {
      showError('Failed to schedule slot.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setSlots((prev) => prev.filter((s) => s.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Timetable slot removed.');
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Academic Timetable Management</h2>
          <p className="text-muted mb-0">
            Automated conflict resolution, room allocations, student batch schedules, and faculty timetables
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => formModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-calendar-plus-fill"></i>
            <span>Schedule Slot</span>
          </button>
        </div>
      </div>

      {/* Perspective Filter Bar */}
      <div className="campus-card shadow-sm border-0 p-3 mb-4">
        <div className="d-flex flex-wrap align-items-center justify-content-between gap-3">
          {/* View Mode Buttons */}
          <div className="btn-group shadow-sm" role="group">
            <button
              type="button"
              className={`btn btn-sm px-3 fw-semibold ${viewPerspective === 'student' ? 'btn-primary' : 'btn-outline-secondary'}`}
              onClick={() => setViewPerspective('student')}
            >
              <i className="bi bi-people-fill me-1"></i> Student View
            </button>
            <button
              type="button"
              className={`btn btn-sm px-3 fw-semibold ${viewPerspective === 'faculty' ? 'btn-primary' : 'btn-outline-secondary'}`}
              onClick={() => setViewPerspective('faculty')}
            >
              <i className="bi bi-person-workspace me-1"></i> Faculty View
            </button>
            <button
              type="button"
              className={`btn btn-sm px-3 fw-semibold ${viewPerspective === 'room' ? 'btn-primary' : 'btn-outline-secondary'}`}
              onClick={() => setViewPerspective('room')}
            >
              <i className="bi bi-geo-alt-fill me-1"></i> Room Allocation
            </button>
          </div>

          {/* Perspective-Specific Filters */}
          <div className="d-flex flex-wrap align-items-center gap-2">
            {viewPerspective === 'student' && (
              <>
                <select
                  className="form-select form-select-sm"
                  style={{ width: '160px' }}
                  value={selectedYear}
                  onChange={(e) => setSelectedYear(e.target.value)}
                >
                  <option value="ALL">All Academic Years</option>
                  <option value="1">Year 1 (Freshmen)</option>
                  <option value="2">Year 2 (Sophomores)</option>
                  <option value="3">Year 3 (Juniors - CSE)</option>
                  <option value="4">Year 4 (Seniors)</option>
                </select>

                <select
                  className="form-select form-select-sm"
                  style={{ width: '130px' }}
                  value={selectedSection}
                  onChange={(e) => setSelectedSection(e.target.value)}
                >
                  <option value="ALL">All Sections</option>
                  <option value="A">Section A</option>
                  <option value="B">Section B</option>
                  <option value="C">Section C</option>
                </select>
              </>
            )}

            {viewPerspective === 'faculty' && (
              <select
                className="form-select form-select-sm"
                style={{ width: '220px' }}
                value={selectedFaculty}
                onChange={(e) => setSelectedFaculty(e.target.value)}
              >
                <option value="ALL">All Professors</option>
                <option value="Dr. Alan Smith">Dr. Alan Smith (OS / ML)</option>
                <option value="Dr. Elena Rostova">Dr. Elena Rostova (DBMS / Networks)</option>
                <option value="Dr. Marcus Vance">Dr. Marcus Vance (DSP)</option>
                <option value="Dr. Rajesh Kumar">Dr. Rajesh Kumar (Microcontrollers)</option>
              </select>
            )}

            {viewPerspective === 'room' && (
              <select
                className="form-select form-select-sm"
                style={{ width: '220px' }}
                value={selectedRoom}
                onChange={(e) => setSelectedRoom(e.target.value)}
              >
                <option value="ALL">All Classrooms & Labs</option>
                <option value="Turing-101">Turing-101 (Lecture Hall)</option>
                <option value="Turing-204">Turing-204 (Smart Classroom)</option>
                <option value="Tesla-204">Tesla-204 (Hall)</option>
                <option value="Lab-3">Computer Lab 3</option>
                <option value="Cloud Lab 2">Cloud Lab 2</option>
                <option value="Curie-301">Curie-301 (Auditorium)</option>
              </select>
            )}
          </div>
        </div>
      </div>

      {/* Benchmark Banner for Monday */}
      <div className="alert alert-primary p-3 mb-4 shadow-sm border-0 d-flex align-items-center justify-content-between">
        <div className="d-flex align-items-center gap-2">
          <i className="bi bi-calendar2-week-fill fs-4 text-primary"></i>
          <div>
            <strong>Monday Benchmark Schedule:</strong> 09:00 → <strong>DBMS</strong> | 10:00 → <strong>OS</strong> | 11:00 → ☕ <strong>Break</strong> | 11:30 → <strong>Networks</strong> | 01:30 → <strong>ML</strong>
          </div>
        </div>
        <span className="badge bg-primary text-white">Active Curriculum</span>
      </div>

      {/* Weekly Matrix Grid */}
      <TimetableGrid
        slots={filteredSlots}
        onEditSlot={(slot) => formModal.openModal({ slot, isEdit: true })}
        onDeleteSlot={(slot) => deleteModal.openModal(slot)}
        viewPerspective={viewPerspective}
      />

      {/* Schedule / Edit Form Modal */}
      <TimetableFormModal
        isOpen={formModal.isOpen}
        onClose={formModal.closeModal}
        onSubmit={handleFormSubmit}
        initialData={formModal.modalData?.slot}
        isEdit={formModal.modalData?.isEdit}
        loading={actionLoading}
      />

      {/* Conflict Alert Modal */}
      <ConflictAlertModal
        isOpen={conflictModal.isOpen}
        onClose={conflictModal.closeModal}
        conflicts={detectedConflicts}
      />

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Cancel Timetable Slot"
        message={`Are you sure you want to remove ${deleteModal.modalData?.title} on ${deleteModal.modalData?.day} at ${deleteModal.modalData?.start_time}?`}
        confirmText="Remove Slot"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Timetable;
