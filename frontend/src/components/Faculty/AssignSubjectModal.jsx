import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const AssignSubjectModal = ({ isOpen, onClose, onAssign, faculty = null, loading = false }) => {
  const [courseCode, setCourseCode] = useState('CS-101');
  const [year, setYear] = useState(2);
  const [section, setSection] = useState('A');

  const availableCourses = [
    { value: 'CS-101', label: 'CS-101: Data Structures & Algorithms (4 Credits)' },
    { value: 'CS-204', label: 'CS-204: Distributed Cloud Architectures (3 Credits)' },
    { value: 'CS-305', label: 'CS-305: Artificial Intelligence Foundations (4 Credits)' },
    { value: 'CS-302', label: 'CS-302: Database Management Systems (4 Credits)' },
    { value: 'EE-201', label: 'EE-201: Embedded Microcontroller Systems (4 Credits)' },
    { value: 'BA-102', label: 'BA-102: Corporate Finance & Valuation (3 Credits)' },
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    onAssign({
      facultyId: faculty?.id,
      facultyName: faculty?.name,
      courseCode,
      year,
      section,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Assign Subject & Class — ${faculty?.name || 'Faculty Member'}`}
      size="md"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 mb-3 bg-light rounded-3 border">
          <span className="small text-muted d-block mb-1">Target Faculty:</span>
          <strong className="text-dark d-block">{faculty?.name} ({faculty?.faculty_id})</strong>
          <small className="text-secondary">{faculty?.department_detail?.name || 'Computer Science'}</small>
        </div>

        <FormField
          label="Select Subject / Course"
          type="select"
          name="courseCode"
          value={courseCode}
          options={availableCourses}
          onChange={(e) => setCourseCode(e.target.value)}
        />

        <div className="row g-3 mb-4">
          <div className="col-6">
            <FormField
              label="Assign Academic Year"
              type="select"
              name="year"
              value={year}
              options={[
                { value: 1, label: 'Year 1 (Freshman)' },
                { value: 2, label: 'Year 2 (Sophomore)' },
                { value: 3, label: 'Year 3 (Junior)' },
                { value: 4, label: 'Year 4 (Senior)' },
              ]}
              onChange={(e) => setYear(parseInt(e.target.value))}
            />
          </div>
          <div className="col-6">
            <FormField
              label="Assign Section"
              type="select"
              name="section"
              value={section}
              options={[
                { value: 'A', label: 'Section A' },
                { value: 'B', label: 'Section B' },
                { value: 'C', label: 'Section C' },
              ]}
              onChange={(e) => setSection(e.target.value)}
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Assigning...' : 'Confirm Assignment'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default AssignSubjectModal;
