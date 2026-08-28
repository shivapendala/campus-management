import React, { useState, useEffect } from 'react';
import { assignmentService } from '../services';
import AssignmentFormModal from '../components/Assignments/AssignmentFormModal';
import SubmitAssignmentModal from '../components/Assignments/SubmitAssignmentModal';
import GradeSubmissionModal from '../components/Assignments/GradeSubmissionModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { useAuth } from '../context/AuthContext';

export const Assignments = () => {
  const { user, role } = useAuth();
  const { showSuccess, showError, showInfo } = useNotification();

  const [assignments, setAssignments] = useState([]);
  const [submissions, setSubmissions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [viewMode, setViewMode] = useState('faculty'); // 'faculty', 'student'
  const [selectedAssignment, setSelectedAssignment] = useState(null);

  // Modals
  const createModal = useModal();
  const submitModal = useModal();
  const gradeModal = useModal();
  const deleteModal = useModal();

  const defaultAssignments = [
    {
      id: 1,
      title: 'Assignment 1: Graph Traversal Algorithms & Dijkstra Optimization',
      course_code: 'CSE-101',
      course_title: 'Data Structures & Algorithms',
      description: 'Implement BFS, DFS, and Dijkstra shortest path algorithm in C++ or Python with benchmark dataset test runs and runtime complexity analysis.',
      max_score: 50,
      deadline: '2026-09-10T23:59:00',
      attachment_url: 'https://github.com/campus-benchmarks/cs101-lab-specs',
      faculty_name: 'Dr. Alan Smith',
      submissions_count: 8,
    },
    {
      id: 2,
      title: 'Lab 2: B+ Tree Indexing & SQL Query Optimizer',
      course_code: 'CSE-202',
      course_title: 'Database Management Systems (DBMS)',
      description: 'Construct a disk-based B+ Tree index supporting point lookups, range scans, and explain output comparison with PostgreSQL query plans.',
      max_score: 50,
      deadline: '2026-09-18T23:59:00',
      attachment_url: 'https://github.com/campus-benchmarks/dbms-bplus-trees',
      faculty_name: 'Dr. Elena Rostova',
      submissions_count: 7,
    },
    {
      id: 3,
      title: 'Project: Kernel Process Scheduler & Concurrency Locks',
      course_code: 'CSE-301',
      course_title: 'Operating Systems',
      description: 'Design a priority preemptive scheduler in xv6/Linux with spinlock and mutex implementations avoiding deadlocks.',
      max_score: 100,
      deadline: '2026-09-25T23:59:00',
      attachment_url: 'https://github.com/campus-benchmarks/os-kernel-sched',
      faculty_name: 'Dr. Alan Smith',
      submissions_count: 6,
    },
    {
      id: 4,
      title: 'Assignment 2: Sliding Window Protocol & TCP Congestion Control',
      course_code: 'CSE-302',
      course_title: 'Computer Networks',
      description: 'Simulate Go-Back-N and Selective Repeat protocols under simulated packet drop and latency conditions.',
      max_score: 50,
      deadline: '2026-10-02T23:59:00',
      attachment_url: 'https://github.com/campus-benchmarks/networks-tcp-sim',
      faculty_name: 'Dr. Elena Rostova',
      submissions_count: 5,
    },
    {
      id: 5,
      title: 'Capstone: Convolutional Neural Network for Medical Imaging',
      course_code: 'CSE-401',
      course_title: 'Machine Learning & Neural Networks',
      description: 'Train a ResNet-50 transfer learning architecture on CT scan datasets with ROC-AUC evaluation and confusion matrix reporting.',
      max_score: 100,
      deadline: '2026-10-15T23:59:00',
      attachment_url: 'https://github.com/campus-benchmarks/ml-resnet-medical',
      faculty_name: 'Dr. Alan Smith',
      submissions_count: 6,
    },
  ];

  const defaultSubmissions = [
    { id: 101, assignment_id: 1, student_id: 'STU-2026-001', student_name: 'Alex Johnson', submitted_at: '2026-08-25T14:20:00', score: 48.5, feedback: 'Outstanding algorithm efficiency and clean C++ modular code structure. Edge cases handled perfectly.', status: 'GRADED', submission_file_url: 'https://github.com/alex-johnson/cse101-graphs', submission_text: 'Implemented Dijkstra with min-heap priority queue (O((V+E)logV)). Passed all 15 benchmark test suites.' },
    { id: 102, assignment_id: 1, student_id: 'STU-2026-002', student_name: 'Maya Patel', submitted_at: '2026-08-25T16:10:00', score: 47.0, feedback: 'Great BFS/DFS visualizer. Good comments.', status: 'GRADED', submission_file_url: 'https://github.com/maya-patel/dijkstra-py', submission_text: 'Python 3.12 implementation with matplotlib graph visualization.' },
    { id: 103, assignment_id: 1, student_id: 'STU-2026-003', student_name: 'David Lee', submitted_at: '2026-08-26T11:05:00', score: 42.0, feedback: 'Good logic, but memory leaks detected in node deletion.', status: 'GRADED', submission_file_url: 'https://github.com/david-lee/cs101-paths', submission_text: 'C++ solution with benchmark time logs.' },
    { id: 104, assignment_id: 1, student_id: 'STU-2026-004', student_name: 'Sophia Martinez', submitted_at: '2026-08-26T18:40:00', score: null, feedback: '', status: 'SUBMITTED', submission_file_url: 'https://github.com/sophia-m/graphs-repo', submission_text: 'All algorithms implemented with documentation and test cases.' },
    { id: 105, assignment_id: 1, student_id: 'STU-2026-005', student_name: 'Liam O\'Connor', submitted_at: '2026-08-27T09:30:00', score: null, feedback: '', status: 'SUBMITTED', submission_file_url: 'https://github.com/liam-o/graph-traversal', submission_text: 'Completed in Go with goroutine parallelism benchmarks.' },
  ];

  const fetchAssignments = async () => {
    setLoading(true);
    try {
      const res = await assignmentService.getAll();
      if (res.results && res.results.length > 0) {
        setAssignments(
          res.results.map((a) => ({
            ...a,
            course_code: a.course_detail?.code || a.course_code || 'CSE-101',
            course_title: a.course_detail?.title || a.course_title || 'Core Subject',
          }))
        );
      } else {
        setAssignments(defaultAssignments);
      }
      setSubmissions(defaultSubmissions);
    } catch (err) {
      setAssignments(defaultAssignments);
      setSubmissions(defaultSubmissions);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAssignments();
  }, []);

  // Faculty: Create / Edit Assignment
  const handleAssignmentSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (createModal.modalData?.isEdit) {
        setAssignments((prev) =>
          prev.map((a) => (a.id === createModal.modalData.assignment.id ? { ...a, ...formData } : a))
        );
        showSuccess(`Assignment "${formData.title}" updated.`);
      } else {
        const newA = {
          ...formData,
          id: Date.now(),
          faculty_name: 'Dr. Alan Smith',
          submissions_count: 0,
        };
        setAssignments([...assignments, newA]);
        showSuccess(`Published assignment "${formData.title}" for ${formData.course_code}!`);
      }
      createModal.closeModal();
    } catch (err) {
      showError('Failed to save assignment.');
    } finally {
      setActionLoading(false);
    }
  };

  // Student: Upload Submission
  const handleStudentSubmit = async (submissionPayload) => {
    setActionLoading(true);
    try {
      const targetA = submitModal.modalData?.assignment;
      const newSub = {
        id: Date.now(),
        assignment_id: targetA.id,
        student_id: 'STU-2026-001',
        student_name: 'Alex Johnson',
        submitted_at: new Date().toISOString(),
        score: null,
        feedback: '',
        status: 'SUBMITTED',
        submission_file_url: submissionPayload.submission_file_url,
        submission_text: submissionPayload.submission_text,
      };
      setSubmissions([newSub, ...submissions]);
      submitModal.closeModal();
      showSuccess(`Solution for "${targetA.title}" successfully uploaded!`);
    } catch (err) {
      showError('Failed to submit work.');
    } finally {
      setActionLoading(false);
    }
  };

  // Faculty: Grade Submission
  const handleGradeSubmit = async (gradePayload) => {
    setActionLoading(true);
    try {
      const subId = gradeModal.modalData?.submission?.id;
      setSubmissions((prev) =>
        prev.map((s) =>
          s.id === subId
            ? { ...s, score: gradePayload.score, feedback: gradePayload.feedback, status: 'GRADED' }
            : s
        )
      );
      gradeModal.closeModal();
      showSuccess(`Awarded ${gradePayload.score} pts. Feedback sent to student!`);
    } catch (err) {
      showError('Failed to grade submission.');
    } finally {
      setActionLoading(false);
    }
  };

  // Delete Assignment
  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setAssignments((prev) => prev.filter((a) => a.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Assignment removed.');
    }
  };

  const getSubmissionsForAssignment = (aId) => {
    return submissions.filter((s) => s.assignment_id === aId);
  };

  // Student personal submission status for an assignment
  const getStudentSubmission = (aId) => {
    return submissions.find((s) => s.assignment_id === aId && s.student_id === 'STU-2026-001');
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Course Assignments & Submissions</h2>
          <p className="text-muted mb-0">
            Publish coursework, set deadlines, collect code/file submissions, and deliver evaluative marks & feedback
          </p>
        </div>
        <div className="d-flex gap-2">
          {/* Perspective Switcher */}
          <div className="btn-group shadow-sm" role="group">
            <button
              type="button"
              className={`btn btn-sm px-3 fw-semibold ${viewMode === 'faculty' ? 'btn-primary' : 'btn-outline-secondary'}`}
              onClick={() => setViewMode('faculty')}
            >
              <i className="bi bi-person-workspace me-1"></i> Faculty Mode
            </button>
            <button
              type="button"
              className={`btn btn-sm px-3 fw-semibold ${viewMode === 'student' ? 'btn-primary' : 'btn-outline-secondary'}`}
              onClick={() => setViewMode('student')}
            >
              <i className="bi bi-mortarboard-fill me-1"></i> Student Mode
            </button>
          </div>

          <button
            onClick={() => createModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-plus-circle-fill"></i>
            <span>Create Assignment</span>
          </button>
        </div>
      </div>

      {/* FACULTY VIEW */}
      {viewMode === 'faculty' && (
        <div className="d-flex flex-column gap-4">
          {assignments.map((assignment) => {
            const assignmentSubs = getSubmissionsForAssignment(assignment.id);
            const isExpanded = selectedAssignment?.id === assignment.id;
            return (
              <div key={assignment.id} className="campus-card shadow-sm border-0 p-4">
                <div className="d-flex flex-column flex-md-row justify-content-between align-items-start gap-3 border-bottom pb-3 mb-3">
                  <div>
                    <div className="d-flex align-items-center gap-2 mb-1">
                      <span className="badge bg-primary fs-6 fw-bold">{assignment.course_code}</span>
                      <span className="badge bg-light text-secondary border">Max Score: {assignment.max_score} pts</span>
                      <span className="badge bg-warning-subtle text-warning-emphasis">
                        <i className="bi bi-clock me-1"></i>
                        Due: {new Date(assignment.deadline).toLocaleDateString()}
                      </span>
                    </div>
                    <h5 className="fw-bold text-dark mb-1">{assignment.title}</h5>
                    <p className="text-secondary small mb-2">{assignment.description}</p>
                    {assignment.attachment_url && (
                      <a
                        href={assignment.attachment_url}
                        target="_blank"
                        rel="noreferrer"
                        className="small text-primary text-decoration-underline d-inline-flex align-items-center gap-1"
                      >
                        <i className="bi bi-paperclip"></i>
                        Specifications / Repository Specs
                      </a>
                    )}
                  </div>

                  <div className="d-flex align-items-center gap-2">
                    <button
                      className="btn btn-outline-primary btn-sm fw-semibold"
                      onClick={() =>
                        setSelectedAssignment(isExpanded ? null : assignment)
                      }
                    >
                      <i className="bi bi-folder2-open me-1"></i>
                      {isExpanded ? 'Hide Submissions' : `View Submissions (${assignmentSubs.length})`}
                    </button>
                    <button
                      className="btn btn-outline-secondary btn-sm"
                      onClick={() => createModal.openModal({ assignment, isEdit: true })}
                      title="Edit Assignment"
                    >
                      <i className="bi bi-pencil"></i>
                    </button>
                    <button
                      className="btn btn-outline-danger btn-sm"
                      onClick={() => deleteModal.openModal(assignment)}
                      title="Delete Assignment"
                    >
                      <i className="bi bi-trash"></i>
                    </button>
                  </div>
                </div>

                {/* Submissions Drawer */}
                {isExpanded && (
                  <div className="bg-light p-3 rounded-3 border">
                    <h6 className="fw-bold text-dark mb-3">
                      <i className="bi bi-card-checklist text-primary me-2"></i>
                      Student Submissions Ledger ({assignmentSubs.length} Received)
                    </h6>

                    {assignmentSubs.length === 0 ? (
                      <div className="text-muted small py-3 text-center">
                        No submissions received yet for this assignment.
                      </div>
                    ) : (
                      <div className="table-responsive">
                        <table className="table table-hover align-middle small bg-white mb-0 rounded border">
                          <thead className="table-light">
                            <tr>
                              <th>Student</th>
                              <th>Submission Work / Link</th>
                              <th>Timestamp</th>
                              <th>Score</th>
                              <th>Status</th>
                              <th className="text-end">Evaluation</th>
                            </tr>
                          </thead>
                          <tbody>
                            {assignmentSubs.map((sub) => (
                              <tr key={sub.id}>
                                <td>
                                  <strong className="text-primary d-block">{sub.student_id}</strong>
                                  <span className="text-dark fw-semibold">{sub.student_name}</span>
                                </td>
                                <td>
                                  <div className="small text-truncate" style={{ maxWidth: '280px' }}>
                                    {sub.submission_text}
                                  </div>
                                  {sub.submission_file_url && (
                                    <a
                                      href={sub.submission_file_url}
                                      target="_blank"
                                      rel="noreferrer"
                                      className="small text-primary text-decoration-underline"
                                    >
                                      <i className="bi bi-box-arrow-up-right me-1"></i>
                                      Repository Link
                                    </a>
                                  )}
                                </td>
                                <td>
                                  <span className="text-muted">
                                    {new Date(sub.submitted_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })},{' '}
                                    {new Date(sub.submitted_at).toLocaleDateString()}
                                  </span>
                                </td>
                                <td>
                                  {sub.score !== null ? (
                                    <strong className="text-success fs-6">
                                      {sub.score} / {assignment.max_score}
                                    </strong>
                                  ) : (
                                    <span className="badge bg-secondary">Ungraded</span>
                                  )}
                                </td>
                                <td>
                                  <span
                                    className={`badge ${sub.status === 'GRADED' ? 'bg-success' : 'bg-primary'}`}
                                  >
                                    {sub.status}
                                  </span>
                                </td>
                                <td className="text-end">
                                  <button
                                    className="btn btn-primary btn-sm fw-semibold"
                                    onClick={() =>
                                      gradeModal.openModal({
                                        submission: sub,
                                        maxScore: assignment.max_score,
                                      })
                                    }
                                  >
                                    <i className="bi bi-pencil-square me-1"></i>
                                    {sub.status === 'GRADED' ? 'Edit Marks' : 'Grade & Feedback'}
                                  </button>
                                </td>
                              </tr>
                            ))}
                          </tbody>
                        </table>
                      </div>
                    )}
                  </div>
                )}
              </div>
            );
          })}
        </div>
      )}

      {/* STUDENT VIEW */}
      {viewMode === 'student' && (
        <div className="d-flex flex-column gap-4">
          <div className="alert alert-info d-flex align-items-center gap-2 p-3 shadow-sm border-0">
            <i className="bi bi-info-circle-fill fs-5 text-info"></i>
            <div>
              You are viewing the <strong>Student Assignment Portal</strong> for <strong>Alex Johnson (STU-2026-001)</strong>. Review your coursework, submit deliverables, and inspect graded marks.
            </div>
          </div>

          <div className="row g-4">
            {assignments.map((assignment) => {
              const mySub = getStudentSubmission(assignment.id);
              return (
                <div key={assignment.id} className="col-12 col-lg-6">
                  <div className="campus-card shadow-sm border-0 p-4 h-100 d-flex flex-column justify-content-between">
                    <div>
                      <div className="d-flex justify-content-between align-items-start mb-2">
                        <span className="badge bg-primary text-white">{assignment.course_code}</span>
                        {mySub ? (
                          <span className={`badge ${mySub.status === 'GRADED' ? 'bg-success' : 'bg-info'} px-3 py-1`}>
                            {mySub.status === 'GRADED' ? 'Graded' : 'Submitted'}
                          </span>
                        ) : (
                          <span className="badge bg-warning text-dark px-3 py-1">Pending Submission</span>
                        )}
                      </div>

                      <h5 className="fw-bold text-dark mb-1">{assignment.title}</h5>
                      <p className="text-muted small mb-2">{assignment.course_title}</p>
                      <p className="small text-secondary mb-3">{assignment.description}</p>

                      <div className="d-flex justify-content-between small text-muted p-2 bg-light rounded border mb-3">
                        <span>Max Score: <strong>{assignment.max_score} pts</strong></span>
                        <span>
                          <i className="bi bi-clock me-1"></i>
                          Due: {new Date(assignment.deadline).toLocaleDateString()}
                        </span>
                      </div>

                      {/* Graded Feedback Dossier */}
                      {mySub && mySub.status === 'GRADED' && (
                        <div className="p-3 bg-success-subtle rounded-3 border border-success-subtle mb-3">
                          <div className="d-flex justify-content-between align-items-center mb-1">
                            <strong className="text-success">Awarded Score:</strong>
                            <span className="badge bg-success fs-6 fw-bold">
                              {mySub.score} / {assignment.max_score} pts ({Math.round((mySub.score / assignment.max_score) * 100)}%)
                            </span>
                          </div>
                          <div className="small text-dark mt-2">
                            <strong>Faculty Feedback:</strong> "{mySub.feedback}"
                          </div>
                        </div>
                      )}
                    </div>

                    <div className="pt-3 border-top d-flex justify-content-between align-items-center">
                      {assignment.attachment_url && (
                        <a
                          href={assignment.attachment_url}
                          target="_blank"
                          rel="noreferrer"
                          className="small text-primary"
                        >
                          <i className="bi bi-download me-1"></i> Instructions Spec
                        </a>
                      )}

                      <button
                        className={`btn btn-sm fw-semibold px-4 ${mySub ? 'btn-outline-primary' : 'btn-primary shadow-sm'}`}
                        onClick={() => submitModal.openModal({ assignment })}
                      >
                        <i className="bi bi-cloud-arrow-up me-1"></i>
                        {mySub ? 'Resubmit Work' : 'Upload Submission'}
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* Modals */}
      <AssignmentFormModal
        isOpen={createModal.isOpen}
        onClose={createModal.closeModal}
        onSubmit={handleAssignmentSubmit}
        initialData={createModal.modalData?.assignment}
        isEdit={createModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <SubmitAssignmentModal
        isOpen={submitModal.isOpen}
        onClose={submitModal.closeModal}
        onSubmit={handleStudentSubmit}
        assignment={submitModal.modalData?.assignment}
        loading={actionLoading}
      />

      <GradeSubmissionModal
        isOpen={gradeModal.isOpen}
        onClose={gradeModal.closeModal}
        onSubmit={handleGradeSubmit}
        submission={gradeModal.modalData?.submission}
        maxScore={gradeModal.modalData?.maxScore}
        loading={actionLoading}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Assignment"
        message={`Are you sure you want to remove the assignment "${deleteModal.modalData?.title}"?`}
        confirmText="Delete Assignment"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Assignments;
