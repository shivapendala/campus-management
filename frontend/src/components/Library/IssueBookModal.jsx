import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const IssueBookModal = ({
  isOpen,
  onClose,
  onSubmit,
  selectedBook = null,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    book_id: 1,
    book_title: 'Introduction to Algorithms (CLRS)',
    student_id: 'STU-2026-001',
    student_name: 'Alex Johnson',
    issue_date: new Date().toISOString().split('T')[0],
    due_date: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
    fine_per_day: 1.0,
  });

  useEffect(() => {
    if (selectedBook) {
      setFormData((prev) => ({
        ...prev,
        book_id: selectedBook.id,
        book_title: selectedBook.title,
      }));
    }
  }, [selectedBook, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      ...formData,
      status: 'ISSUED',
      book_id: selectedBook?.id || 1,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Issue Book — ${selectedBook?.title || 'Library Circulation'}`}
      size="md"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-center mb-1">
            <strong className="text-dark">{selectedBook?.title}</strong>
            <span className="badge bg-success">{selectedBook?.available_copies || 8} Copies In Stock</span>
          </div>
          <small className="text-muted">ISBN: {selectedBook?.isbn || '978-0262046305'}</small>
        </div>

        <div className="mb-3">
          <FormField
            label="Student ID / Library Card #"
            name="student_id"
            placeholder="e.g. STU-2026-001"
            value={formData.student_id}
            onChange={(e) => setFormData({ ...formData, student_id: e.target.value })}
            required
          />
        </div>

        <div className="mb-3">
          <FormField
            label="Student Name"
            name="student_name"
            placeholder="e.g. Alex Johnson"
            value={formData.student_name}
            onChange={(e) => setFormData({ ...formData, student_name: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-4">
          <div className="col-6">
            <FormField
              label="Issue Date"
              type="date"
              name="issue_date"
              value={formData.issue_date}
              onChange={(e) => setFormData({ ...formData, issue_date: e.target.value })}
              required
            />
          </div>
          <div className="col-6">
            <FormField
              label="Due Date (14 Days)"
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
            {loading ? 'Processing...' : 'Confirm Book Checkout'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default IssueBookModal;
