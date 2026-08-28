import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const DepartmentFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    code: '',
    name: '',
    established_year: 2000,
    head_of_department: '',
    building_block: 'Academic Block A',
    description: '',
    contact_email: '',
    contact_phone: '',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        code: initialData.code || '',
        name: initialData.name || '',
        established_year: initialData.established_year || 2000,
        head_of_department: initialData.head_of_department || '',
        building_block: initialData.building_block || 'Academic Block A',
        description: initialData.description || '',
        contact_email: initialData.contact_email || '',
        contact_phone: initialData.contact_phone || '',
      });
    } else {
      setFormData({
        code: '',
        name: '',
        established_year: 2026,
        head_of_department: 'Dr. New Faculty',
        building_block: 'Academic Block B',
        description: '',
        contact_email: 'dept@campus.edu',
        contact_phone: '+1 (555) 019-2800',
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
      title={isEdit ? `Edit Department — ${initialData?.name} (${initialData?.code})` : 'Create New Department'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Department Code"
              name="code"
              required
              disabled={isEdit}
              placeholder="e.g. CSE, ECE, EEE"
              value={formData.code}
              onChange={(e) => setFormData({ ...formData, code: e.target.value.toUpperCase() })}
            />
          </div>
          <div className="col-12 col-md-8">
            <FormField
              label="Department Name"
              name="name"
              required
              placeholder="e.g. Computer Science & Engineering"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Head of Department (HOD)"
              name="head_of_department"
              placeholder="e.g. Dr. Alan Smith"
              value={formData.head_of_department}
              onChange={(e) => setFormData({ ...formData, head_of_department: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Building / Block"
              name="building_block"
              placeholder="e.g. Turing Block A"
              value={formData.building_block}
              onChange={(e) => setFormData({ ...formData, building_block: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Established Year"
              type="number"
              name="established_year"
              value={formData.established_year}
              onChange={(e) => setFormData({ ...formData, established_year: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Contact Email"
              type="email"
              name="contact_email"
              placeholder="cse.dept@campus.edu"
              value={formData.contact_email}
              onChange={(e) => setFormData({ ...formData, contact_email: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Contact Phone"
              name="contact_phone"
              placeholder="+1 (555) 019-2801"
              value={formData.contact_phone}
              onChange={(e) => setFormData({ ...formData, contact_phone: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Department Description & Objectives"
            type="textarea"
            name="description"
            rows={3}
            placeholder="Brief overview of curriculum, research areas, and departmental facilities..."
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Create Department'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default DepartmentFormModal;
