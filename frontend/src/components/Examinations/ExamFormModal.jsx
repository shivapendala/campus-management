import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const ExamFormModal = ({
  isOpen,
  onClose,
  onSubmit,
  initialData = null,
  isEdit = false,
  loading = false,
}) => {
  const [formData, setFormData] = useState({
    name: 'Midterm Examination 2026',
    course_id: 1,
    course_code: 'CSE-101',
    exam_type: 'MIDTERM',
    date: new Date().toISOString().split('T')[0],
    start_time: '10:00',
    end_time: '12:00',
    semester: 'Fall 2026',
    max_internal_marks: 40,
    max_external_marks: 60,
    max_marks: 100,
    passing_marks: 40,
    venue: 'Main Examination Hall A',
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
        name: initialData.name || 'Midterm Examination 2026',
        course_id: initialData.course_id || initialData.course?.id || 1,
        course_code: initialData.course_code || initialData.course?.code || 'CSE-101',
        exam_type: initialData.exam_type || 'MIDTERM',
        date: initialData.date || new Date().toISOString().split('T')[0],
        start_time: initialData.start_time || '10:00',
        end_time: initialData.end_time || '12:00',
        semester: initialData.semester || 'Fall 2026',
        max_internal_marks: initialData.max_internal_marks || 40,
        max_external_marks: initialData.max_external_marks || 60,
        max_marks: initialData.max_marks || 100,
        passing_marks: initialData.passing_marks || 40,
        venue: initialData.venue || 'Main Examination Hall A',
      });
    }
  }, [initialData, isOpen]);

  const handleSubmit = (e) => {
    e.preventDefault();
    const totalMax = Number(formData.max_internal_marks) + Number(formData.max_external_marks);
    onSubmit({
      ...formData,
      max_marks: totalMax,
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={isEdit ? `Edit Examination — ${formData.name}` : 'Schedule New Examination'}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="row g-3 mb-3">
          <div className="col-12 col-md-8">
            <FormField
              label="Examination Title"
              name="name"
              placeholder="e.g. End-Semester Theoretical Assessment"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Exam Type"
              type="select"
              name="exam_type"
              value={formData.exam_type}
              options={[
                { value: 'MIDTERM', label: 'Midterm Examination' },
                { value: 'FINAL', label: 'End-Semester Final' },
                { value: 'PRACTICAL', label: 'Practical Lab Exam' },
                { value: 'QUIZ', label: 'Quiz / Continuous Assessment' },
              ]}
              onChange={(e) => setFormData({ ...formData, exam_type: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-6">
            <FormField
              label="Course / Subject"
              type="select"
              name="course_id"
              value={formData.course_id}
              options={availableCourses.map((c) => ({ value: c.id, label: c.label }))}
              onChange={(e) => {
                const cId = parseInt(e.target.value);
                const selectedC = availableCourses.find((c) => c.id === cId);
                setFormData({
                  ...formData,
                  course_id: cId,
                  course_code: selectedC?.code || '',
                });
              }}
            />
          </div>
          <div className="col-12 col-md-6">
            <FormField
              label="Academic Semester"
              name="semester"
              placeholder="Fall 2026"
              value={formData.semester}
              onChange={(e) => setFormData({ ...formData, semester: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Exam Date"
              type="date"
              name="date"
              value={formData.date}
              onChange={(e) => setFormData({ ...formData, date: e.target.value })}
              required
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Start Time"
              name="start_time"
              placeholder="10:00"
              value={formData.start_time}
              onChange={(e) => setFormData({ ...formData, start_time: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="End Time"
              name="end_time"
              placeholder="12:00"
              value={formData.end_time}
              onChange={(e) => setFormData({ ...formData, end_time: e.target.value })}
            />
          </div>
        </div>

        <div className="row g-3 mb-3">
          <div className="col-12 col-md-4">
            <FormField
              label="Max Internal Marks"
              type="number"
              name="max_internal_marks"
              value={formData.max_internal_marks}
              onChange={(e) => setFormData({ ...formData, max_internal_marks: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Max External Marks"
              type="number"
              name="max_external_marks"
              value={formData.max_external_marks}
              onChange={(e) => setFormData({ ...formData, max_external_marks: e.target.value })}
            />
          </div>
          <div className="col-12 col-md-4">
            <FormField
              label="Passing Threshold Marks"
              type="number"
              name="passing_marks"
              value={formData.passing_marks}
              onChange={(e) => setFormData({ ...formData, passing_marks: e.target.value })}
            />
          </div>
        </div>

        <div className="mb-4">
          <FormField
            label="Examination Venue / Hall"
            name="venue"
            placeholder="e.g. Main Examination Hall A, Lab 3"
            value={formData.venue}
            onChange={(e) => setFormData({ ...formData, venue: e.target.value })}
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-primary btn-sm px-4 fw-semibold">
            {loading ? 'Saving...' : isEdit ? 'Update Exam Schedule' : 'Schedule Examination'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default ExamFormModal;
