import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const SubmitAssignmentModal = ({
  isOpen,
  onClose,
  onSubmit,
  assignment = null,
  loading = false,
}) => {
  const [submissionFileUrl, setSubmissionFileUrl] = useState('https://github.com/alex-johnson/cse101-graph-traversals');
  const [submissionText, setSubmissionText] = useState('Completed all BFS, DFS, and Dijkstra implementations in C++20 with benchmarks and README documentation.');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      submission_file_url: submissionFileUrl,
      submission_text: submissionText,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Upload Solution — ${assignment?.title || 'Assignment'}`}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        {/* Assignment Brief */}
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-center mb-1">
            <span className="badge bg-primary">{assignment?.course_code || 'CSE-101'}</span>
            <small className="text-danger fw-bold">
              <i className="bi bi-clock-history me-1"></i>
              Deadline: {assignment?.deadline ? new Date(assignment.deadline).toLocaleString() : 'Soon'}
            </small>
          </div>
          <h6 className="fw-bold text-dark mb-1">{assignment?.title}</h6>
          <p className="small text-secondary mb-0">{assignment?.description}</p>
        </div>

        <div className="mb-3">
          <FormField
            label="Solution Repository / Drive / File URL"
            name="submission_file_url"
            placeholder="https://github.com/... or Google Drive URL"
            value={submissionFileUrl}
            onChange={(e) => setSubmissionFileUrl(e.target.value)}
            required
          />
        </div>

        <div className="mb-4">
          <FormField
            label="Submission Summary / Notes / Code Snippet"
            type="textarea"
            rows={4}
            name="submission_text"
            placeholder="Describe your solution, methodology, test results, or paste code..."
            value={submissionText}
            onChange={(e) => setSubmissionText(e.target.value)}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-success btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Submitting...' : 'Upload & Submit Work'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default SubmitAssignmentModal;
