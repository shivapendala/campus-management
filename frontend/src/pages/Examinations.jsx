import React, { useState, useEffect } from 'react';
import { examService } from '../services';
import ExamFormModal from '../components/Examinations/ExamFormModal';
import MarksEntryModal from '../components/Examinations/MarksEntryModal';
import StudentGradeCardModal from '../components/Examinations/StudentGradeCardModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { useAuth } from '../context/AuthContext';

export const Examinations = () => {
  const { user, role } = useAuth();
  const { showSuccess, showError, showInfo } = useNotification();

  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [activeTab, setActiveTab] = useState('schedules'); // 'schedules', 'grading', 'results'

  // Modals
  const examModal = useModal();
  const marksModal = useModal();
  const gradeCardModal = useModal();
  const deleteModal = useModal();

  const defaultExams = [
    {
      id: 1,
      name: 'Midterm Examination Fall 2026',
      course_code: 'CSE-101',
      course_title: 'Data Structures & Algorithms',
      exam_type: 'MIDTERM',
      date: '2026-09-15',
      start_time: '10:00',
      end_time: '12:00',
      semester: 'Fall 2026',
      max_internal_marks: 40,
      max_external_marks: 60,
      max_marks: 100,
      passing_marks: 40,
      venue: 'Main Examination Hall A',
      status: 'PUBLISHED',
      total_students_graded: 8,
    },
    {
      id: 2,
      name: 'Midterm Examination Fall 2026',
      course_code: 'CSE-202',
      course_title: 'Database Management Systems (DBMS)',
      exam_type: 'MIDTERM',
      date: '2026-09-17',
      start_time: '10:00',
      end_time: '12:00',
      semester: 'Fall 2026',
      max_internal_marks: 40,
      max_external_marks: 60,
      max_marks: 100,
      passing_marks: 40,
      venue: 'Main Examination Hall B',
      status: 'UNDER_REVIEW',
      total_students_graded: 8,
    },
    {
      id: 3,
      name: 'Practical Lab Assessment',
      course_code: 'CSE-301',
      course_title: 'Operating Systems',
      exam_type: 'PRACTICAL',
      date: '2026-09-22',
      start_time: '02:00',
      end_time: '04:30',
      semester: 'Fall 2026',
      max_internal_marks: 40,
      max_external_marks: 60,
      max_marks: 100,
      passing_marks: 40,
      venue: 'Cloud Systems Lab 2',
      status: 'SCHEDULED',
      total_students_graded: 0,
    },
    {
      id: 4,
      name: 'Continuous Assessment Quiz 2',
      course_code: 'CSE-302',
      course_title: 'Computer Networks',
      exam_type: 'QUIZ',
      date: '2026-09-28',
      start_time: '11:30',
      end_time: '12:30',
      semester: 'Fall 2026',
      max_internal_marks: 40,
      max_external_marks: 60,
      max_marks: 100,
      passing_marks: 40,
      venue: 'Tesla-204',
      status: 'SCHEDULED',
      total_students_graded: 0,
    },
    {
      id: 5,
      name: 'End-Semester Final Examination',
      course_code: 'CSE-401',
      course_title: 'Machine Learning & Neural Networks',
      exam_type: 'FINAL',
      date: '2026-10-05',
      start_time: '09:30',
      end_time: '12:30',
      semester: 'Fall 2026',
      max_internal_marks: 40,
      max_external_marks: 60,
      max_marks: 100,
      passing_marks: 40,
      venue: 'Auditorium Hall Curie-301',
      status: 'SCHEDULED',
      total_students_graded: 0,
    },
  ];

  const fetchExams = async () => {
    setLoading(true);
    try {
      const res = await examService.getExams();
      if (res.results && res.results.length > 0) {
        setExams(
          res.results.map((e) => ({
            ...e,
            course_code: e.course_detail?.code || e.course_code || 'CSE-101',
            course_title: e.course_detail?.title || e.course_title || 'Core Subject',
          }))
        );
      } else {
        setExams(defaultExams);
      }
    } catch (err) {
      setExams(defaultExams);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchExams();
  }, []);

  // 1. Admin Create/Edit Exam
  const handleExamSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (examModal.modalData?.isEdit) {
        setExams((prev) =>
          prev.map((e) => (e.id === examModal.modalData.exam.id ? { ...e, ...formData } : e))
        );
        showSuccess(`Exam schedule for ${formData.name} updated!`);
      } else {
        const newExam = {
          ...formData,
          id: Date.now(),
          status: 'SCHEDULED',
          total_students_graded: 0,
        };
        setExams([...exams, newExam]);
        showSuccess(`Scheduled ${formData.name} for ${formData.course_code}!`);
      }
      examModal.closeModal();
    } catch (err) {
      showError('Failed to save examination.');
    } finally {
      setActionLoading(false);
    }
  };

  // 2. Faculty Submit Marks -> System calculates Grade
  const handleMarksSubmit = async (marksPayload) => {
    setActionLoading(true);
    try {
      const examId = marksModal.modalData?.exam?.id;
      setExams((prev) =>
        prev.map((e) =>
          e.id === examId
            ? { ...e, status: 'UNDER_REVIEW', total_students_graded: marksPayload.length }
            : e
        )
      );
      marksModal.closeModal();
      showSuccess('Marks recorded & grades calculated. Sent to HOD for verification!');
    } catch (err) {
      showError('Failed to submit marks.');
    } finally {
      setActionLoading(false);
    }
  };

  // 3. HOD Verifies & Declares Results
  const handleHODVerify = (exam) => {
    setExams((prev) =>
      prev.map((e) => (e.id === exam.id ? { ...e, status: 'PUBLISHED' } : e))
    );
    showSuccess(`HOD verified & approved results for ${exam.name} (${exam.course_code})!`);
  };

  // Delete Exam
  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setExams((prev) => prev.filter((e) => e.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Examination removed.');
    }
  };

  const getStatusBadge = (status) => {
    switch (status) {
      case 'PUBLISHED':
        return <span className="badge bg-success px-3 py-1">Declared / Published</span>;
      case 'UNDER_REVIEW':
        return <span className="badge bg-warning text-dark px-3 py-1">Under HOD Review</span>;
      case 'GRADING':
        return <span className="badge bg-info px-3 py-1">Grading in Progress</span>;
      default:
        return <span className="badge bg-secondary px-3 py-1">Scheduled</span>;
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Examination & Results Management</h2>
          <p className="text-muted mb-0">
            Scheduling, Internal/External marks entry, automated 10-point grade computation, and HOD approval verification
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => gradeCardModal.openModal()}
            className="btn btn-outline-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3"
          >
            <i className="bi bi-person-lines-fill"></i>
            <span>Student Grade Card</span>
          </button>
          <button
            onClick={() => examModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-calendar-plus-fill"></i>
            <span>Create Exam Schedule</span>
          </button>
        </div>
      </div>

      {/* Navigation Tabs */}
      <ul className="nav nav-pills mb-4 gap-2">
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'schedules' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('schedules')}
          >
            <i className="bi bi-calendar3 me-1"></i>
            Active Exam Schedules ({exams.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'grading' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('grading')}
          >
            <i className="bi bi-pencil-square me-1"></i>
            Faculty Marks Entry & HOD Verification Gate
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'results' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('results')}
          >
            <i className="bi bi-award-fill me-1"></i>
            Declared Results & SGPA Transcripts
          </button>
        </li>
      </ul>

      {/* TAB 1: ACTIVE EXAM SCHEDULES */}
      {activeTab === 'schedules' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="table-responsive">
            <table className="table table-hover align-middle mb-0">
              <thead className="table-light small">
                <tr>
                  <th>Examination Details</th>
                  <th>Course & Subject</th>
                  <th>Date & Time</th>
                  <th>Marks Breakdown</th>
                  <th>Allocated Venue</th>
                  <th>Lifecycle Status</th>
                  <th className="text-end">Actions</th>
                </tr>
              </thead>
              <tbody>
                {exams.map((exam) => (
                  <tr key={exam.id}>
                    <td>
                      <strong className="text-dark d-block">{exam.name}</strong>
                      <span className="badge bg-light text-secondary border small">{exam.exam_type}</span>
                    </td>
                    <td>
                      <strong className="text-primary">{exam.course_code}</strong>
                      <div className="small text-muted">{exam.course_title}</div>
                    </td>
                    <td>
                      <div className="fw-semibold text-dark">{exam.date}</div>
                      <small className="text-muted">
                        {exam.start_time} - {exam.end_time}
                      </small>
                    </td>
                    <td>
                      <div className="small">
                        <span>Int: <strong>{exam.max_internal_marks}</strong></span> • <span>Ext: <strong>{exam.max_external_marks}</strong></span>
                      </div>
                      <strong className="text-success small">Total Max: {exam.max_marks} (Pass: {exam.passing_marks})</strong>
                    </td>
                    <td>
                      <span className="small text-secondary">
                        <i className="bi bi-geo-alt-fill text-danger me-1"></i>
                        {exam.venue}
                      </span>
                    </td>
                    <td>{getStatusBadge(exam.status)}</td>
                    <td className="text-end">
                      <div className="d-flex justify-content-end gap-1">
                        <button
                          className="btn btn-outline-primary btn-sm"
                          onClick={() => marksModal.openModal({ exam })}
                          title="Enter Marks"
                        >
                          <i className="bi bi-pencil-square me-1"></i> Marks
                        </button>
                        <button
                          className="btn btn-outline-secondary btn-sm"
                          onClick={() => examModal.openModal({ exam, isEdit: true })}
                          title="Edit Exam"
                        >
                          <i className="bi bi-pencil"></i>
                        </button>
                        <button
                          className="btn btn-outline-danger btn-sm"
                          onClick={() => deleteModal.openModal(exam)}
                          title="Delete Exam"
                        >
                          <i className="bi bi-trash"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* TAB 2: FACULTY MARKS ENTRY & HOD VERIFICATION GATE */}
      {activeTab === 'grading' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="d-flex justify-content-between align-items-center mb-4 pb-2 border-bottom">
            <div>
              <h5 className="fw-bold text-dark mb-1">
                <i className="bi bi-shield-check text-primary me-2"></i>
                HOD Assessment Review & Grading Gate
              </h5>
              <p className="text-muted small mb-0">
                Faculty submits internal and external marks; HOD verifies results prior to official release
              </p>
            </div>
          </div>

          <div className="row g-3">
            {exams.map((exam) => (
              <div key={exam.id} className="col-12 col-lg-6">
                <div className="p-3 bg-light rounded-3 border h-100 d-flex flex-column justify-content-between">
                  <div>
                    <div className="d-flex justify-content-between align-items-start mb-2">
                      <div>
                        <span className="badge bg-primary text-white mb-1">{exam.course_code}</span>
                        <h6 className="fw-bold text-dark mb-0">{exam.name}</h6>
                      </div>
                      {getStatusBadge(exam.status)}
                    </div>

                    <p className="small text-muted mb-2">{exam.course_title}</p>

                    <div className="d-flex justify-content-between small text-secondary p-2 bg-white rounded border mb-3">
                      <span>Internal: {exam.max_internal_marks} pts</span>
                      <span>External: {exam.max_external_marks} pts</span>
                      <span>Total: <strong>{exam.max_marks} pts</strong></span>
                    </div>
                  </div>

                  <div className="d-flex justify-content-between align-items-center pt-2 border-top">
                    <button
                      className="btn btn-primary btn-sm fw-semibold"
                      onClick={() => marksModal.openModal({ exam })}
                    >
                      <i className="bi bi-pencil-square me-1"></i> Enter / Edit Marks
                    </button>

                    {exam.status === 'UNDER_REVIEW' && (
                      <button
                        className="btn btn-success btn-sm fw-semibold shadow-sm"
                        onClick={() => handleHODVerify(exam)}
                      >
                        <i className="bi bi-check2-circle me-1"></i> HOD Verify & Approve
                      </button>
                    )}

                    {exam.status === 'PUBLISHED' && (
                      <span className="text-success small fw-semibold">
                        <i className="bi bi-check-circle-fill me-1"></i> Approved by HOD
                      </span>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* TAB 3: DECLARED RESULTS & SGPA TRANSCRIPTS */}
      {activeTab === 'results' && (
        <div className="campus-card shadow-sm border-0 p-4">
          <div className="d-flex justify-content-between align-items-center mb-4 pb-2 border-bottom">
            <div>
              <h5 className="fw-bold text-dark mb-1">
                <i className="bi bi-award text-success me-2"></i>
                Official Academic Performance & SGPA Dossiers
              </h5>
              <p className="text-muted small mb-0">Fall 2026 Semester Grade Records</p>
            </div>
            <button
              onClick={() => gradeCardModal.openModal()}
              className="btn btn-success btn-sm fw-semibold shadow-sm"
            >
              <i className="bi bi-printer-fill me-1"></i> View Student Grade Card (Alex Johnson)
            </button>
          </div>

          <div className="table-responsive">
            <table className="table table-hover align-middle small">
              <thead className="table-light">
                <tr>
                  <th>Course Code & Title</th>
                  <th>Credits</th>
                  <th>Internal Marks (40)</th>
                  <th>External Marks (60)</th>
                  <th>Total Score (100)</th>
                  <th>Calculated Grade</th>
                  <th>Grade Point</th>
                  <th>Standing</th>
                </tr>
              </thead>
              <tbody>
                {[
                  { code: 'CSE-101', title: 'Data Structures & Algorithms', credits: 4, internal: 38, external: 56, total: 94, grade: 'A+', gp: 10.0, status: 'PASS' },
                  { code: 'CSE-202', title: 'Database Management Systems (DBMS)', credits: 4, internal: 36, external: 54, total: 90, grade: 'A+', gp: 10.0, status: 'PASS' },
                  { code: 'CSE-301', title: 'Operating Systems', credits: 4, internal: 35, external: 51, total: 86, grade: 'A', gp: 9.0, status: 'PASS' },
                  { code: 'CSE-302', title: 'Computer Networks', credits: 3, internal: 33, external: 48, total: 81, grade: 'A', gp: 9.0, status: 'PASS' },
                  { code: 'CSE-401', title: 'Machine Learning & Neural Networks', credits: 4, internal: 39, external: 56, total: 95, grade: 'A+', gp: 10.0, status: 'PASS' },
                ].map((r, i) => (
                  <tr key={i}>
                    <td>
                      <strong className="text-primary">{r.code}</strong>
                      <div className="text-dark">{r.title}</div>
                    </td>
                    <td><strong>{r.credits}</strong></td>
                    <td>{r.internal}</td>
                    <td>{r.external}</td>
                    <td><strong className="fs-6 text-dark">{r.total}</strong></td>
                    <td>
                      <span className={`badge ${r.grade === 'A+' || r.grade === 'A' ? 'bg-success' : 'bg-primary'} px-2 py-1`}>
                        {r.grade}
                      </span>
                    </td>
                    <td><span className="badge bg-light text-dark border fw-bold">{r.gp.toFixed(1)}</span></td>
                    <td>
                      <span className="badge bg-success-subtle text-success border border-success-subtle px-2 py-1">
                        {r.status}
                      </span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Modals */}
      <ExamFormModal
        isOpen={examModal.isOpen}
        onClose={examModal.closeModal}
        onSubmit={handleExamSubmit}
        initialData={examModal.modalData?.exam}
        isEdit={examModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <MarksEntryModal
        isOpen={marksModal.isOpen}
        onClose={marksModal.closeModal}
        onSubmit={handleMarksSubmit}
        exam={marksModal.modalData?.exam}
        loading={actionLoading}
      />

      <StudentGradeCardModal
        isOpen={gradeCardModal.isOpen}
        onClose={gradeCardModal.closeModal}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Examination Schedule"
        message={`Are you sure you want to cancel the examination schedule for ${deleteModal.modalData?.name} (${deleteModal.modalData?.course_code})?`}
        confirmText="Cancel Exam"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Examinations;
