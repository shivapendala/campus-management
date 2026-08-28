import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const TimetableFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    day: 'Monday',
    start_time: '09:00',
    end_time: '10:00',
    title: 'DBMS',
    course_code: 'CSE-202',
    faculty_id: 2,
    faculty_name: 'Dr. Elena Rostova',
    room: 'Turing-204',
    year: 3,
    section: 'A',
    entry_type: 'LECTURE',
  });

  const availableSubjects = [
    { value: 'DBMS', code: 'CSE-202', label: 'CSE-202: Database Management Systems (DBMS)' },
    { value: 'OS', code: 'CSE-301', label: 'CSE-301: Operating Systems' },
    { value: 'Networks', code: 'CSE-302', label: 'CSE-302: Computer Networks' },
    { value: 'ML', code: 'CSE-401', label: 'CSE-401: Machine Learning & Neural Networks' },
    { value: 'Data Structures', code: 'CSE-101', label: 'CSE-101: Data Structures & Algorithms' },
    { value: 'Break / Recess', code: 'BREAK', label: '☕ Institutional Break / Recess' },
  ];

  const availableRooms = [
    { value: 'Turing-101', label: 'Turing-101 (Lecture Hall, Cap: 80)' },
    { value: 'Turing-204', label: 'Turing-204 (Smart Classroom, Cap: 60)' },
    { value: 'Tesla-204', label: 'Tesla-204 (Electronics Lab Hall, Cap: 50)' },
    { value: 'Curie-301', label: 'Curie-301 (Auditorium, Cap: 120)' },
    { value: 'Lab-3', label: 'Computer Lab 3 (Systems & Database, Cap: 45)' },
    { value: 'Cloud Lab 2', label: 'Cloud Lab 2 (Kubernetes & DevOps, Cap: 45)' },
    { value: 'Campus Lounge', label: 'Campus Lounge / Cafeteria' },
  ];

  const availableProfessors = [
    { id: 1, name: 'Dr. Alan Smith', label: 'Dr. Alan Smith (Professor, CS & AI)' },
    { id: 2, name: 'Dr. Elena Rostova', label: 'Dr. Elena Rostova (Associate Professor, Cloud/DB)' },
    { id: 3, name: 'Dr. Marcus Vance', label: 'Dr. Marcus Vance (Professor, Networks/DSP)' },
    { id: 4, name: 'Dr. Rajesh Kumar', label: 'Dr. Rajesh Kumar (Professor, EEE)' },
    { id: 0, name: 'None / Recess', label: 'None (Break or Free Period)' },
  ];

  useEffect(() => {
    if (initialData) {
      setFormData({
        day: initialData.day || 'Monday',
        start_time: initialData.start_time || '09:00',
        end_time: initialData.end_time || '10:00',
        title: initialData.title || 'DBMS',
        course_code: initialData.course_code || 'CSE-202',
        faculty_id: initialData.faculty_id || 2,
        faculty_name: initialData.faculty_name || 'Dr. Elena Rostova',
        room: initialData.room || 'Turing-204',
        year: initialData.year || 3,
        section: initialData.section || 'A',
        entry_type: initialData.entry_type || 'LECTURE',
      });
    } else {
      setFormData({
        day: 'Monday',
        start_time: '09:00',
        end_time: '10:00',
        title: 'DBMS',
        course_code: 'CSE-202',
        faculty_id: 2,
        faculty_name: 'Dr. Elena Rostova',
        room: 'Turing-204',
        year: 3,
        section: 'A',
        entry_type: 'LECTURE',
      });
    }
  }, [initialData, isOpen]);

  const handleSubjectChange = (e) => {
    const selectedTitle = e.target.value;
    const sub = availableSubjects.find((s) => s.value === selectedTitle);
    setFormData((prev) => ({
      ...prev,
      title: selectedTitle,
      course_code: sub?.code || '',
      entry_type: selectedTitle.includes('Break') ? 'BREAK' : prev.entry_type,
    }));
  };

  const handleFacultyChange = (e) => {
    const fId = parseInt(e.target.value);
    const prof = availableProfessors.find((p) => p.id === fId);
    setFormData((prev) => ({
      ...prev,
      faculty_id: fId,
      faculty_name: prof?.name || '',
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Timetable Slot — ${initialData?.day} ${initialData?.start_time}` : 'Schedule New Timetable Slot'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Day of Week"
              type="select"
              name="day"
              value={formData.day}
              options={[
                { value: 'Monday', label: 'Monday' },
                { value: 'Tuesday', label: 'Tuesday' },
                { value: 'Wednesday', label: 'Wednesday' },
                { value: 'Thursday', label: 'Thursday' },
                { value: 'Friday', label: 'Friday' },
              ]}
              onChange={(e) => setFormData({ ...formData, day: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Start Time"
              name="start_time"
              placeholder="09:00"
              value={formData.start_time}
              onChange={(e) => setFormData({ ...formData, start_time: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="End Time"
              name="end_time"
              placeholder="10:00"
              value={formData.end_time}
              onChange={(e) => setFormData({ ...formData, end_time: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Subject / Academic Activity"
              type="select"
              name="title"
              value={formData.title}
              options={availableSubjects.map((s) => ({ value: s.value, label: s.label }))}
              onChange={handleSubjectChange}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Assigned Faculty Instructor"
              type="select"
              name="faculty_id"
              value={formData.faculty_id}
              options={availableProfessors.map((p) => ({ value: p.id, label: p.label }))}
              onChange={handleFacultyChange}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Allocated Room / Laboratory"
              type="select"
              name="room"
              value={formData.room}
              options={availableRooms}
              onChange={(e) => setFormData({ ...formData, room: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-3">
            <FormField
              label="Academic Year"
              type="select"
              name="year"
              value={formData.year}
              options={[
                { value: 1, label: 'Year 1' },
                { value: 2, label: 'Year 2' },
                { value: 3, label: 'Year 3' },
                { value: 4, label: 'Year 4' },
              ]}
              onChange={(e) => setFormData({ ...formData, year: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-3">
            <FormField
              label="Section"
              type="select"
              name="section"
              value={formData.section}
              options={[
                { value: 'A', label: 'Section A' },
                { value: 'B', label: 'Section B' },
                { value: 'C', label: 'Section C' },
              ]}
              onChange={(e) => setFormData({ ...formData, section: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Slot Period Type"
            type="select"
            name="entry_type"
            value={formData.entry_type}
            options={[
              { value: 'LECTURE', label: 'Classroom Lecture' },
              { value: 'LAB', label: 'Practical Laboratory' },
              { value: 'BREAK', label: 'Recess / Break' },
              { value: 'TUTORIAL', label: 'Tutorial & Problem Solving' },
            ]}
            onChange={(e) => setFormData({ ...formData, entry_type: e.target.value })}
          />
        </div>

        <div className="alert alert-info py-2 px-3 small d-flex align-items-center gap-2 mb-4">
          <i className="bi bi-shield-check fs-5"></i>
          <div>Automated conflict verification will validate room, faculty, and student availability before scheduling.</div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Validating...' : isEdit ? 'Save Changes' : 'Schedule Slot'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default TimetableFormModal;
