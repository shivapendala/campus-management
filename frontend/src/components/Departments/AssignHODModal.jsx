import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const AssignHODModal = ({ isOpen, onClose, onAssign, department = null, loading = false }) => {
  const [hodName, setHodName] = useState('');

  const availableProfessors = [
    { value: 'Dr. Alan Smith', label: 'Dr. Alan Smith (Professor, CS & AI)' },
    { value: 'Dr. Elena Rostova', label: 'Dr. Elena Rostova (Associate Professor, Cloud Systems)' },
    { value: 'Dr. Marcus Vance', label: 'Dr. Marcus Vance (Professor, Communications & DSP)' },
    { value: 'Dr. Rajesh Kumar', label: 'Dr. Rajesh Kumar (Professor, Power Systems & VLSI)' },
    { value: 'Dr. Robert Ford', label: 'Dr. Robert Ford (Professor, Robotics & Automation)' },
    { value: 'Dr. Arthur Dent', label: 'Dr. Arthur Dent (Professor, Structural Engineering)' },
  ];

  useEffect(() => {
    if (department) {
      setHodName(department.head_of_department || 'Dr. Alan Smith');
    }
  }, [department, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onAssign({
      deptId: department?.id,
      deptName: department?.name,
      hodName,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Assign Head of Department (HOD) — ${department?.code}`}
      size="md"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 mb-3 bg-light rounded-3 border">
          <span className="small text-muted d-block mb-1">Target Academic Department:</span>
          <strong className="text-dark d-block fs-6">{department?.name} ({department?.code})</strong>
          <small className="text-secondary">Current HOD: {department?.head_of_department || 'Not Appointed'}</small>
        </div>

        <FormField
          label="Select Senior Professor as HOD"
          type="select"
          name="hodName"
          value={hodName}
          options={availableProfessors}
          onChange={(e) => setHodName(e.target.value)}
        />

        <div className="d-flex justify-content-end gap-2 pt-3 border-top mt-4">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Assigning...' : 'Confirm HOD Appointment'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default AssignHODModal;
