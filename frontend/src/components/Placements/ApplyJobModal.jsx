import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const ApplyJobModal = ({
  isOpen,
  onClose,
  onSubmit,
  selectedDrive = null,
  loading = false,
}) => {
  const [resumeUrl, setResumeUrl] = useState('https://linkedin.com/in/alex-johnson-dev');
  const [coverNote, setCoverNote] = useState('Senior B.Tech CSE student specializing in distributed cloud infrastructure, operating systems, and ML neural networks. Cumulative GPA: 3.85.');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      drive_id: selectedDrive?.id,
      resume_url: resumeUrl,
      cover_note: coverNote,
      student_id: 'STU-2026-001',
      student_name: 'Alex Johnson',
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Apply for Campus Recruitment — ${selectedDrive?.company_name || 'Placement Drive'}`}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-start mb-2">
            <div>
              <h5 className="fw-bold text-dark mb-0">{selectedDrive?.title}</h5>
              <div className="text-muted small">Role: <strong>{selectedDrive?.job_role}</strong></div>
            </div>
            <span className="badge bg-success fs-6 fw-bold">
              ${selectedDrive?.package_lpa} LPA / Year
            </span>
          </div>
          <div className="small text-secondary">
            Eligibility Cutoff: <strong>GPA {selectedDrive?.eligibility_gpa}+</strong> • Drive Date: <strong>{selectedDrive?.drive_date}</strong>
          </div>
        </div>

        <div className="mb-3">
          <FormField
            label="Resume / Portfolio / LinkedIn Profile Link"
            name="resume_url"
            placeholder="https://..."
            value={resumeUrl}
            onChange={(e) => setResumeUrl(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <FormField
            label="Statement of Purpose / Candidate Profile Summary"
            type="textarea"
            rows={3}
            name="cover_note"
            value={coverNote}
            onChange={(e) => setCoverNote(e.target.value)}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-success btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Submitting Application...' : 'Submit Job Application'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default ApplyJobModal;
