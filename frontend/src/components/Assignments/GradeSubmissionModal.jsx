import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const GradeSubmissionModal = ({
  isOpen,
  onClose,
  onSubmit,
  submission = null,
  maxScore = 50,
  loading = false,
}) => {
  const [score, setScore] = useState(48.5);
  const [feedback, setFeedback] = useState('Outstanding algorithm efficiency and clean C++ modular code structure. Edge cases handled perfectly.');

  useEffect(() => {
    if (submission) {
      setScore(submission.score !== null && submission.score !== undefined ? submission.score : 48.5);
      setFeedback(submission.feedback || 'Outstanding algorithm efficiency and clean C++ modular code structure. Edge cases handled perfectly.');
    }
  }, [submission, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      score: Number(score),
      feedback: feedback,
    });
  };

  const pct = Math.round((Number(score) / maxScore) * 100);

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Review & Grade Submission — ${submission?.student_name || submission?.student?.name || 'Student'}`}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        {/* Student Submission Preview */}
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-start mb-2">
            <div>
              <h6 className="fw-bold text-dark mb-0">
                {submission?.student_name || submission?.student?.name || 'Alex Johnson'} ({submission?.student_id || 'STU-2026-001'})
              </h6>
              <small className="text-muted">
                Submitted: {submission?.submitted_at ? new Date(submission.submitted_at).toLocaleString() : 'Recent'}
              </small>
            </div>
            <span className="badge bg-primary">
              {submission?.status || 'SUBMITTED'}
            </span>
          </div>

          {submission?.submission_file_url && (
            <div className="mb-2">
              <strong className="small text-secondary d-block">Submitted Link:</strong>
              <a
                href={submission.submission_file_url}
                target="_blank"
                rel="noreferrer"
                className="small text-primary text-decoration-underline"
              >
                <i className="bi bi-box-arrow-up-right me-1"></i>
                {submission.submission_file_url}
              </a>
            </div>
          )}

          <div>
            <strong className="small text-secondary d-block">Submission Content / Summary:</strong>
            <p className="small text-dark mb-0 bg-white p-2 rounded border">
              {submission?.submission_text || 'Submitted GitHub repository link with tests and documentation.'}
            </p>
          </div>
        </div>

        {/* Score & Feedback Inputs */}
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <label className="form-label small fw-semibold text-secondary">
              Award Score (Max: {maxScore} pts)
            </label>
            <div className="input-group input-group-sm">
              <input
                type="number"
                step="0.5"
                min="0"
                max={maxScore}
                className="form-control fw-bold fs-6 text-primary"
                value={score}
                onChange={(e) => setScore(e.target.value)}
                required
              />
              <span className="input-group-text">/ {maxScore} pts ({pct}%)</span>
            </div>
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Faculty Evaluative Feedback & Comments"
            type="textarea"
            rows={3}
            name="feedback"
            placeholder="Write constructive notes for the student..."
            value={feedback}
            onChange={(e) => setFeedback(e.target.value)}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : 'Commit Marks & Feedback'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default GradeSubmissionModal;
