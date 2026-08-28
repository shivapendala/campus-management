import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const AssignFacultyModal = ({ isOpen, onClose, onAssign, course = null, loading = false }) => {
  const [facultyId, setFacultyId] = useState(1);

  const availableProfessors = [
    { value: 1, label: 'Dr. Alan Smith (Professor, CS & AI — Turing 101)' },
    { value: 2, label: 'Dr. Elena Rostova (Associate Professor, Cloud & Distributed Systems — Turing 204)' },
    { value: 3, label: 'Dr. Marcus Vance (Professor, Communications & DSP — Shannon 102)' },
    { value: 4, label: 'Dr. Rajesh Kumar (Professor, Power Systems & VLSI — Tesla 102)' },
    { value: 5, label: 'Dr. Robert Ford (Professor, Robotics & Automation — Watt 105)' },
    { value: 6, label: 'Dr. Arthur Dent (Professor, Structural Mechanics — Smeaton 201)' },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    const chosen = availableProfessors.find((p) => p.value === parseInt(facultyId));
    onAssign({
      courseId: course?.id,
      courseCode: course?.code,
      facultyId: parseInt(facultyId),
      facultyName: chosen?.label.split('(')[0].trim() || 'Assigned Faculty',
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Allocate Faculty Instructor — ${course?.code}`}
      size="md"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 mb-3 bg-light rounded-3 border">
          <span className="small text-muted d-block mb-1">Target Subject:</span>
          <strong className="text-dark d-block fs-6">{course?.code}: {course?.title}</strong>
          <small className="text-secondary">Semester {course?.semester} • {course?.credits} Credits</small>
        </div>

        <FormField
          label="Select Lead Faculty Instructor"
          type="select"
          name="facultyId"
          value={facultyId}
          options={availableProfessors}
          onChange={(e) => setFacultyId(parseInt(e.target.value))}
        />

        <div className="d-flex justify-content-end gap-2 pt-3 border-top mt-4">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Assigning...' : 'Confirm Faculty Allocation'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default AssignFacultyModal;
