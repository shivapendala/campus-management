import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const FeeStructureModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Fall 2026 CSE Semester Tuition Fee',
    category_id: 1,
    category_name: 'Semester Tuition Fee',
    department_id: 1,
    department_code: 'CSE',
    semester: 4,
    academic_year: '2026-2027',
    amount: 4500.0,
    due_date: new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
  });

  const availableDepts = [
    { id: 1, code: 'CSE', label: 'Computer Science & Engineering (CSE)' },
    { id: 2, code: 'ECE', label: 'Electronics & Communication (ECE)' },
    { id: 3, code: 'EEE', label: 'Electrical & Electronics (EEE)' },
    { id: 4, code: 'MECH', label: 'Mechanical Engineering (MECH)' },
    { id: 5, code: 'CIVIL', label: 'Civil Engineering (CIVIL)' },
  ];

  const availableCategories = [
    { id: 1, label: 'Semester Academic Tuition' },
    { id: 2, label: 'Laboratory & Infrastructure Fee' },
    { id: 3, label: 'Library & Technology Subscription' },
    { id: 4, label: 'Examination & Evaluation Fee' },
    { id: 5, label: 'Campus Hostel & Boarding' },
  ];

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        category_id: initialData.category_id || 1,
        category_name: initialData.category?.name || 'Semester Tuition Fee',
        department_id: initialData.department_id || 1,
        department_code: initialData.department?.code || 'CSE',
        semester: initialData.semester || 4,
        academic_year: initialData.academic_year || '2026-2027',
        amount: initialData.amount || 4500.0,
        due_date: initialData.due_date || new Date().toISOString().split('T')[0],
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      amount: Number(formData.amount),
      semester: Number(formData.semester),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Fee Structure — ${formData.title}` : 'Define New Institutional Fee Structure'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <FormField
            label="Fee Structure Title"
            name="title"
            placeholder="e.g. Fall 2026 CSE Tuition & Lab Assessment Fee"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Fee Category"
              type="select"
              name="category_id"
              value={formData.category_id}
              options={availableCategories.map((c) => ({ value: c.id, label: c.label }))}
              onChange={(e) => {
                const cId = parseInt(e.target.value);
                const cObj = availableCategories.find((c) => c.id === cId);
                setFormData({ ...formData, category_id: cId, category_name: cObj?.label });
              }}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Target Department"
              type="select"
              name="department_id"
              value={formData.department_id}
              options={availableDepts.map((d) => ({ value: d.id, label: d.label }))}
              onChange={(e) => {
                const dId = parseInt(e.target.value);
                const dObj = availableDepts.find((d) => d.id === dId);
                setFormData({ ...formData, department_id: dId, department_code: dObj?.code });
              }}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Semester (1–8)"
              type="number"
              name="semester"
              value={formData.semester}
              onChange={(e) => setFormData({ ...formData, semester: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Billed Amount ($ USD)"
              type="number"
              step="50"
              name="amount"
              value={formData.amount}
              onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Payment Due Date"
              type="date"
              name="due_date"
              value={formData.due_date}
              onChange={(e) => setFormData({ ...formData, due_date: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Create Fee Structure'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default FeeStructureModal;
