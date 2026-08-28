import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';
import { DEPARTMENTS } from '../../utils/constants';

export const CourseFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    code: '',
    title: '',
    department: 1,
    semester: 3,
    credits: 4,
    course_type: 'THEORY',
    capacity: 60,
    description: '',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        code: initialData.code || '',
        title: initialData.title || '',
        department: initialData.department || 1,
        semester: initialData.semester || 3,
        credits: initialData.credits || 4,
        course_type: initialData.course_type || 'THEORY',
        capacity: initialData.capacity || 60,
        description: initialData.description || '',
      });
    } else {
      setFormData({
        code: '',
        title: '',
        department: 1,
        semester: 3,
        credits: 4,
        course_type: 'THEORY',
        capacity: 60,
        description: '',
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
      title={isEdit ? `Edit Subject — ${initialData?.code} (${initialData?.title})` : 'Create Catalog Course / Subject'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Course Code"
              name="code"
              required
              disabled={isEdit}
              placeholder="e.g. CSE-101, CSE-202"
              value={formData.code}
              onChange={(e) => setFormData({ ...formData, code: e.target.value.toUpperCase() })}
            />
          </div>
          <div className="col-12 col-md-8">
            <FormField
              label="Course / Subject Title"
              name="title"
              required
              placeholder="e.g. Data Structures & Algorithms"
              value={formData.title}
              onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Academic Department"
              type="select"
              name="department"
              value={formData.department}
              options={DEPARTMENTS.map((d, i) => ({ value: i + 1, label: `${d.code} — ${d.name}` }))}
              onChange={(e) => setFormData({ ...formData, department: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-2">
            <FormField
              label="Semester"
              type="select"
              name="semester"
              value={formData.semester}
              options={[
                { value: 1, label: 'Sem 1' },
                { value: 2, label: 'Sem 2' },
                { value: 3, label: 'Sem 3' },
                { value: 4, label: 'Sem 4' },
                { value: 5, label: 'Sem 5' },
                { value: 6, label: 'Sem 6' },
                { value: 7, label: 'Sem 7' },
                { value: 8, label: 'Sem 8' },
              ]}
              onChange={(e) => setFormData({ ...formData, semester: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-2">
            <FormField
              label="Credits"
              type="select"
              name="credits"
              value={formData.credits}
              options={[
                { value: 1, label: '1 Credit' },
                { value: 2, label: '2 Credits' },
                { value: 3, label: '3 Credits' },
                { value: 4, label: '4 Credits' },
              ]}
              onChange={(e) => setFormData({ ...formData, credits: parseInt(e.target.value) })}
            />
          </div>
          <div className="col-12 col-md-2">
            <FormField
              label="Course Type"
              type="select"
              name="course_type"
              value={formData.course_type}
              options={[
                { value: 'THEORY', label: 'Theory' },
                { value: 'LAB', label: 'Lab' },
                { value: 'ELECTIVE', label: 'Elective' },
                { value: 'PROJECT', label: 'Project' },
              ]}
              onChange={(e) => setFormData({ ...formData, course_type: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Course Syllabus Summary & Prerequisites"
            type="textarea"
            name="description"
            rows={3}
            placeholder="Outline course learning objectives, covered topics across modules, and laboratory prerequisites..."
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Save Changes' : 'Create Course'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default CourseFormModal;
