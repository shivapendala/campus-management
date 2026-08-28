import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';
import { DEPARTMENTS } from '../../utils/constants';

export const StudentFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    student_id: '',
    name: '',
    email: '',
    phone: '',
    department: 1,
    year: 1,
    section: 'A',
    semester: 1,
    gpa: '3.50',
    guardian_name: '',
    guardian_phone: '',
    gender: 'Male',
    status: 'ACTIVE',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        student_id: initialData.student_id || '',
        name: initialData.name || '',
        email: initialData.email || '',
        phone: initialData.phone || '',
        department: initialData.department || 1,
        year: initialData.year || 1,
        section: initialData.section || 'A',
        semester: initialData.semester || 1,
        gpa: initialData.gpa || '3.50',
        guardian_name: initialData.guardian_name || '',
        guardian_phone: initialData.guardian_phone || '',
        gender: initialData.gender || 'Male',
        status: initialData.status || 'ACTIVE',
      });
    } else {
      setFormData({
        student_id: `STU-2026-${Math.floor(100 + Math.random() * 900)}`,
        name: '',
        email: '',
        phone: '',
        department: 1,
        year: 1,
        section: 'A',
        semester: 1,
        gpa: '3.50',
        guardian_name: '',
        guardian_phone: '',
        gender: 'Male',
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
      title={isEdit ? `Edit Student — ${initialData?.name || initialData?.student_id}` : 'Enroll New Student'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Student ID"
              name="student_id"
              required
              disabled={isEdit}
              placeholder="e.g. STU-2026-009"
              value={formData.student_id}
              onChange={(e) => setFormData({ ...formData, student_id: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Full Name"
              name="name"
              required
              placeholder="e.g. Michael Chang"
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
              placeholder="e.g. m.chang@campus.edu"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Contact Phone"
              name="phone"
              placeholder="+1 (555) 019-2839"
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
          <div className="col-12 col-md-2">
            <FormField
              label="Year"
              type="number"
              name="year"
              value={formData.year}
              onChange={(e) => setFormData({ ...formData, year: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-2">
            <FormField
              label="Section"
              name="section"
              value={formData.section}
              onChange={(e) => setFormData({ ...formData, section: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-2">
            <FormField
              label="Semester"
              type="number"
              name="semester"
              value={formData.semester}
              onChange={(e) => setFormData({ ...formData, semester: parseInt(e.target.value) })}
            />
          </div>
        </div>

        <div className="row g-3 mb-4">
          <div className="col-12 col-md-4">
            <FormField
              label="GPA"
              name="gpa"
              placeholder="3.75"
              value={formData.gpa}
              onChange={(e) => setFormData({ ...formData, gpa: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Guardian Name"
              name="guardian_name"
              placeholder="Parent/Guardian"
              value={formData.guardian_name}
              onChange={(e) => setFormData({ ...formData, guardian_name: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Guardian Phone"
              name="guardian_phone"
              placeholder="+1 555-0199"
              value={formData.guardian_phone}
              onChange={(e) => setFormData({ ...formData, guardian_phone: e.target.value })}
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Enroll Student'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default StudentFormModal;
