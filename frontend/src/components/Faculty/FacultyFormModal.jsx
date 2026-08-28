import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';
import { DEPARTMENTS } from '../../utils/constants';

export const FacultyFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    faculty_id: '',
    name: '',
    email: '',
    phone: '',
    department: 1,
    designation: 'Assistant Professor',
    qualification: 'Ph.D. in Computer Science',
    specialization: 'Artificial Intelligence & Machine Learning',
    office_room: 'Turing Block Room 204',
    status: 'ACTIVE',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        faculty_id: initialData.faculty_id || '',
        name: initialData.name || '',
        email: initialData.email || '',
        phone: initialData.phone || '',
        department: initialData.department || 1,
        designation: initialData.designation || 'Assistant Professor',
        qualification: initialData.qualification || 'Ph.D.',
        specialization: initialData.specialization || '',
        office_room: initialData.office_room || '',
        status: initialData.status || 'ACTIVE',
      });
    } else {
      setFormData({
        faculty_id: `FAC-CS-00${Math.floor(10 + Math.random() * 90)}`,
        name: '',
        email: '',
        phone: '',
        department: 1,
        designation: 'Assistant Professor',
        qualification: 'Ph.D. in Computer Science',
        specialization: 'Artificial Intelligence',
        office_room: 'Turing Block 204',
        status: 'ACTIVE',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Faculty — ${initialData?.name || initialData?.faculty_id}` : 'Add Faculty Member'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Faculty ID"
              name="faculty_id"
              required
              disabled={isEdit}
              placeholder="FAC-CS-009"
              value={formData.faculty_id}
              onChange={(e) => setFormData({ ...formData, faculty_id: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Full Name"
              name="name"
              required
              placeholder="Dr. Katherine Johnson"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Email Address"
              type="email"
              name="email"
              required
              placeholder="katherine.j@campus.edu"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Contact Phone"
              name="phone"
              placeholder="+1 (555) 019-2840"
              value={formData.phone}
              onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Department"
              type="select"
              name="department"
              value={formData.department}
              options={DEPARTMENTS.map((d, i) => ({ value: i + 1, label: d.name }))}
              onChange={(e) => setFormData({ ...formData, department: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Academic Designation"
              type="select"
              name="designation"
              value={formData.designation}
              options={[
                { value: 'Professor & HOD', label: 'Professor & HOD' },
                { value: 'Professor', label: 'Professor' },
                { value: 'Associate Professor', label: 'Associate Professor' },
                { value: 'Assistant Professor', label: 'Assistant Professor' },
                { value: 'Lecturer / Adjunct', label: 'Lecturer / Adjunct' },
              ]}
              onChange={(e) => setFormData({ ...formData, designation: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-4">
          <div className="col-12 col-md-4">
            <FormField
              label="Highest Qualification"
              name="qualification"
              placeholder="Ph.D., M.Tech"
              value={formData.qualification}
              onChange={(e) => setFormData({ ...formData, qualification: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Area of Specialization"
              name="specialization"
              placeholder="Cloud & Distributed Systems"
              value={formData.specialization}
              onChange={(e) => setFormData({ ...formData, specialization: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Office Room"
              name="office_room"
              placeholder="Room Turing-204"
              value={formData.office_room}
              onChange={(e) => setFormData({ ...formData, office_room: e.target.value })}
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Add Faculty'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default FacultyFormModal;
