import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const AssignmentFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    title: 'Assignment 1: Graph Traversal Algorithms & Dijkstra Optimization',
    course_id: 1,
    course_code: 'CSE-101',
    description: 'Implement BFS, DFS, and Dijkstra shortest path algorithm in C++ or Python with benchmark dataset test runs.',
    max_score: 50,
    deadline: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 16),
    attachment_url: 'https://github.com/campus-benchmarks/cs101-lab-specs',
    is_published: true,
  });

  const availableCourses = [
    { id: 1, code: 'CSE-101', label: 'CSE-101: Data Structures & Algorithms' },
    { id: 2, code: 'CSE-202', label: 'CSE-202: Database Management Systems (DBMS)' },
    { id: 3, code: 'CSE-301', label: 'CSE-301: Operating Systems' },
    { id: 4, code: 'CSE-302', label: 'CSE-302: Computer Networks' },
    { id: 5, code: 'CSE-401', label: 'CSE-401: Machine Learning & Neural Networks' },
  ];

  useEffect(() => {
    if (initialData) {
      setFormData({
        title: initialData.title || '',
        course_id: initialData.course_id || initialData.course?.id || 1,
        course_code: initialData.course_code || initialData.course?.code || 'CSE-101',
        description: initialData.description || '',
        max_score: initialData.max_score || 50,
        deadline: initialData.deadline ? initialData.deadline.slice(0, 16) : new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString().slice(0, 16),
        attachment_url: initialData.attachment_url || '',
        is_published: initialData.is_published !== undefined ? initialData.is_published : true,
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
      title={isEdit ? `Edit Assignment — ${formData.title}` : 'Create New Course Assignment'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="mb-3">
          <FormField
            label="Assignment Title"
            name="title"
            placeholder="e.g. Laboratory 3: Multi-Threaded Kernel Synchronization"
            value={formData.title}
            onChange={(e) => setFormData({ ...formData, title: e.target.value })}
            required
          />
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Subject / Course"
              type="select"
              name="course_id"
              value={formData.course_id}
              options={availableCourses.map((c) => ({ value: c.id, label: c.label }))}
              onChange={(e) => {
                const cId = parseInt(e.target.value);
                const cObj = availableCourses.find((c) => c.id === cId);
                setFormData({
                  ...formData,
                  course_id: cId,
                  course_code: cObj?.code || '',
                });
              }}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Max Possible Score / Marks"
              type="number"
              name="max_score"
              value={formData.max_score}
              onChange={(e) => setFormData({ ...formData, max_score: e.target.value })}
              required
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Submission Deadline"
              type="datetime-local"
              name="deadline"
              value={formData.deadline}
              onChange={(e) => setFormData({ ...formData, deadline: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Attachment / Reference Specification URL"
              name="attachment_url"
              placeholder="https://..."
              value={formData.attachment_url}
              onChange={(e) => setFormData({ ...formData, attachment_url: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Detailed Assignment Instructions & Rubrics"
            type="textarea"
            rows={4}
            name="description"
            placeholder="Enter instructions, requirements, deliverables, and format guidelines..."
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
            {loading ? 'Publishing...' : isEdit ? 'Save Changes' : 'Publish Assignment'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default AssignmentFormModal;
