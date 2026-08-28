import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const DriveFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Google Cloud Campus Recruitment Drive 2026',
    company_name: 'Google Cloud',
    job_role: 'Associate Cloud Solutions Architect',
    package_lpa: 24.5,
    eligibility_gpa: 3.5,
    drive_date: '2026-10-15',
    application_deadline: '2026-10-01',
    description: 'Recruitment drive for graduating B.Tech CSE/ECE seniors with strong systems and distributed cloud fundamentals.',
  });

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        company_name: initialData.company_name || initialData.company?.name || 'Google Cloud',
        job_role: initialData.job_role || '',
        package_lpa: initialData.package_lpa || 24.5,
        eligibility_gpa: initialData.eligibility_gpa || 3.5,
        drive_date: initialData.drive_date || '2026-10-15',
        application_deadline: initialData.application_deadline || '2026-10-01',
        description: initialData.description || '',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      package_lpa: Number(formData.package_lpa),
      eligibility_gpa: Number(formData.eligibility_gpa),
      status: 'UPCOMING',
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Recruitment Drive — ${formData.title}` : 'Schedule Campus Placement Drive'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <FormField
            label="Placement Drive Title"
            name="title"
            placeholder="e.g. Microsoft AI & Systems Campus Hiring 2026"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Hiring Company"
              name="company_name"
              placeholder="e.g. Google Cloud, Amazon AWS, Microsoft"
              value={formData.company_name}
              onChange={(e) => setFormData({ ...formData, company_name: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Job Role / Designation"
              name="job_role"
              placeholder="e.g. Member of Technical Staff, Cloud Engineer"
              value={formData.job_role}
              onChange={(e) => setFormData({ ...formData, job_role: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-3">
            <FormField
              label="CTC Package ($ / LPA)"
              type="number"
              step="0.5"
              name="package_lpa"
              value={formData.package_lpa}
              onChange={(e) => setFormData({ ...formData, package_lpa: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-3">
            <FormField
              label="Minimum GPA Cutoff"
              type="number"
              step="0.1"
              name="eligibility_gpa"
              value={formData.eligibility_gpa}
              onChange={(e) => setFormData({ ...formData, eligibility_gpa: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-3">
            <FormField
              label="Application Deadline"
              type="date"
              name="application_deadline"
              value={formData.application_deadline}
              onChange={(e) => setFormData({ ...formData, application_deadline: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-3">
            <FormField
              label="Drive Date"
              type="date"
              name="drive_date"
              value={formData.drive_date}
              onChange={(e) => setFormData({ ...formData, drive_date: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Job Description, Skillsets & Eligibility Criteria"
            type="textarea"
            rows={3}
            name="description"
            value={formData.description}
            onChange={(e) => setFormData({ ...formData, description: e.target.value })}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Scheduling...' : isEdit ? 'Save Changes' : 'Announce Drive'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default DriveFormModal;
