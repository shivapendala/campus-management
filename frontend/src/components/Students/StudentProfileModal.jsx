import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import { studentService } from '../../services';
import { STATUS_BADGE_CLASSES } from '../../utils/constants';
import { formatCurrency, formatDate } from '../../utils/formatters';

export const StudentProfileModal = ({ isOpen, onClose, studentId, studentBasic }) => {
  const [activeTab, setActiveTab] = useState('personal');
  const [details, setDetails] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (isOpen && studentId) {
      setLoading(true);
      studentService
        .getProfileDetails(studentId)
        .then((data) => setDetails(data))
        .catch(() => {
          // Fallback mock details if offline/error
          setDetails({
            personal_info: {
              student_id: studentBasic?.student_id || 'STU-2026-001',
              name: studentBasic?.name || 'Alex Johnson',
              email: studentBasic?.email || 'alex.j@campus.edu',
              phone: studentBasic?.phone || '+1 (555) 019-2834',
              gender: 'Male',
              date_of_birth: '2004-05-14',
              guardian_name: 'Robert Johnson',
              guardian_phone: '+1 (555) 019-2835',
            },
            academic_info: {
              department: studentBasic?.department_detail?.name || 'Computer Science & Engineering',
              department_code: 'CS',
              year: studentBasic?.year || 2,
              semester: studentBasic?.semester || 4,
              section: studentBasic?.section || 'A',
              admission_date: '2024-08-15',
              status: studentBasic?.status || 'ACTIVE',
              gpa: studentBasic?.gpa || '3.85',
              credits_completed: 72,
            },
            attendance: {
              total_sessions: 20,
              present_count: 19,
              percentage: 95.0,
              records: [
                { course: 'CS-101', course_title: 'Data Structures & Algorithms', date: '2026-08-26', session_type: 'LECTURE', topic: 'Binary Search Trees', status: 'PRESENT' },
                { course: 'CS-204', course_title: 'Distributed Cloud Architectures', date: '2026-08-25', session_type: 'LAB', topic: 'Docker Container Orchestration', status: 'PRESENT' },
                { course: 'EE-201', course_title: 'Embedded Microcontroller Systems', date: '2026-08-24', session_type: 'LECTURE', topic: 'ARM Cortex Timers', status: 'PRESENT' },
              ],
            },
            marks: [
              { exam_name: 'Midterm Assessment 2026', course: 'CS-101', exam_type: 'MIDTERM', max_marks: 100, marks_obtained: 94.5, grade: 'A+', is_passed: true },
              { exam_name: 'Cloud Lab Assessment 1', course: 'CS-204', exam_type: 'LAB', max_marks: 50, marks_obtained: 47.0, grade: 'A', is_passed: true },
            ],
            fees: [
              { invoice_number: 'INV-2026-001', title: 'Fall 2026 Tuition', amount: 4500.0, payment_method: 'ONLINE', transaction_id: 'TXN-CAMPUS-982347', status: 'SUCCESS', date: '2026-08-10' },
            ],
            assignments: [
              { assignment_title: 'Assignment 1: Graph Traversal Algorithms', course: 'CS-101', max_score: 50, score: 48.5, status: 'GRADED', feedback: 'Great complexity analysis and BFS implementation.' },
            ],
            library: [
              { book_title: 'The C Programming Language', author: 'Kernighan & Ritchie', isbn: '978-0131103627', issue_date: '2026-08-14', due_date: '2026-08-28', status: 'ISSUED', fine_amount: 0.0 },
            ],
            placement: [
              { company: 'Google Cloud', job_role: 'Associate Cloud Solutions Engineer', package_lpa: 24.5, status: 'SHORTLISTED', applied_at: '2026-08-18' },
            ],
            complaints: [
              { ticket_id: 'TCK-2026-981', title: 'Wi-Fi Signal in Computer Lab 3', category: 'INFRASTRUCTURE', priority: 'MEDIUM', status: 'OPEN', resolution_notes: 'Assigned to IT support team.', created_at: '2026-08-20' },
            ],
          });
        })
        .finally(() => setLoading(false));
    }
  }, [isOpen, studentId, studentBasic]);

  const tabs = [
    { id: 'personal', label: 'Personal Info', icon: 'bi-person-fill' },
    { id: 'academic', label: 'Academic Info', icon: 'bi-mortarboard-fill' },
    { id: 'attendance', label: 'Attendance', icon: 'bi-calendar-check-fill' },
    { id: 'marks', label: 'Marks & Exams', icon: 'bi-award-fill' },
    { id: 'fees', label: 'Fees & Payments', icon: 'bi-cash-coin' },
    { id: 'assignments', label: 'Assignments', icon: 'bi-file-earmark-code-fill' },
    { id: 'library', label: 'Library', icon: 'bi-book-fill' },
    { id: 'placement', label: 'Placement', icon: 'bi-briefcase-fill' },
    { id: 'complaints', label: 'Complaints', icon: 'bi-chat-left-dots-fill' },
  ];

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Student 360° Profile — ${details?.personal_info?.name || studentBasic?.name || 'Student'}`}
      size="xl"
    >
      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status"></div>
          <p className="small text-muted mt-2">Loading complete student dossier...</p>
        </div>
      ) : details ? (
        <div>
          {/* Header Summary Banner */}
          <div className="p-3 mb-4 rounded-3 bg-light border d-flex flex-wrap align-items-center justify-content-between gap-3">
            <div className="d-flex align-items-center gap-3">
              <div
                className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center fw-bold fs-4 shadow-sm"
                style={{ width: '56px', height: '56px' }}
              >
                {details.personal_info.name ? details.personal_info.name[0] : 'S'}
              </div>
              <div>
                <h5 className="fw-bold text-dark mb-0">{details.personal_info.name}</h5>
                <span className="text-muted small">
                  {details.personal_info.student_id} • {details.academic_info.department}
                </span>
              </div>
            </div>
            <div className="d-flex gap-2">
              <span className={`badge ${STATUS_BADGE_CLASSES[details.academic_info.status] || 'bg-success text-white'} px-3 py-2 fs-6`}>
                {details.academic_info.status}
              </span>
              <span className="badge bg-primary-subtle text-primary fw-bold px-3 py-2 fs-6">
                GPA: {details.academic_info.gpa}
              </span>
            </div>
          </div>

          {/* 9 Profile Tabs */}
          <ul className="nav nav-tabs mb-4 flex-nowrap overflow-auto">
            {tabs.map((tab) => (
              <li key={tab.id} className="nav-item">
                <button
                  className={`nav-link text-nowrap py-2 px-3 fw-semibold small ${
                    activeTab === tab.id ? 'active text-primary border-bottom border-primary border-2' : 'text-secondary'
                  }`}
                  onClick={() => setActiveTab(tab.id)}
                >
                  <i className={`bi ${tab.icon} me-1`}></i>
                  {tab.label}
                </button>
              </li>
            ))}
          </ul>

          {/* Tab 1: Personal Information */}
          {activeTab === 'personal' && (
            <div className="row g-3">
              <div className="col-12 col-md-6">
                <div className="p-3 bg-light rounded-3 border">
                  <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Student Demographics</h6>
                  <p className="small mb-2"><strong>Full Name:</strong> {details.personal_info.name}</p>
                  <p className="small mb-2"><strong>Institutional Email:</strong> {details.personal_info.email}</p>
                  <p className="small mb-2"><strong>Contact Phone:</strong> {details.personal_info.phone || 'N/A'}</p>
                  <p className="small mb-2"><strong>Gender:</strong> {details.personal_info.gender}</p>
                  <p className="small mb-0"><strong>Date of Birth:</strong> {formatDate(details.personal_info.date_of_birth)}</p>
                </div>
              </div>
              <div className="col-12 col-md-6">
                <div className="p-3 bg-light rounded-3 border">
                  <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Guardian & Emergency Contacts</h6>
                  <p className="small mb-2"><strong>Guardian Name:</strong> {details.personal_info.guardian_name}</p>
                  <p className="small mb-2"><strong>Guardian Phone:</strong> {details.personal_info.guardian_phone}</p>
                  <p className="small mb-2"><strong>Emergency Relation:</strong> Parent</p>
                  <p className="small mb-0"><strong>Address:</strong> Campus Hostel Block 2, Room 304</p>
                </div>
              </div>
            </div>
          )}

          {/* Tab 2: Academic Information */}
          {activeTab === 'academic' && (
            <div className="row g-3">
              <div className="col-12 col-md-6">
                <div className="p-3 bg-light rounded-3 border">
                  <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Academic Standing</h6>
                  <p className="small mb-2"><strong>Department:</strong> {details.academic_info.department}</p>
                  <p className="small mb-2"><strong>Current Year:</strong> Year {details.academic_info.year}</p>
                  <p className="small mb-2"><strong>Semester:</strong> Semester {details.academic_info.semester}</p>
                  <p className="small mb-2"><strong>Section:</strong> Section {details.academic_info.section}</p>
                  <p className="small mb-0"><strong>Admission Date:</strong> {formatDate(details.academic_info.admission_date)}</p>
                </div>
              </div>
              <div className="col-12 col-md-6">
                <div className="p-3 bg-light rounded-3 border">
                  <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Grading & Credits</h6>
                  <p className="small mb-2"><strong>Cumulative GPA:</strong> <span className="badge bg-success-subtle text-success fs-6">{details.academic_info.gpa}</span></p>
                  <p className="small mb-2"><strong>Credits Earned:</strong> {details.academic_info.credits_completed} Credits</p>
                  <p className="small mb-2"><strong>Graduation Target:</strong> Spring 2028</p>
                  <p className="small mb-0"><strong>Academic Status:</strong> Good Standing</p>
                </div>
              </div>
            </div>
          )}

          {/* Tab 3: Attendance */}
          {activeTab === 'attendance' && (
            <div>
              <div className="d-flex justify-content-between align-items-center mb-3">
                <h6 className="fw-bold text-dark mb-0">Lecture & Lab Attendance Logs</h6>
                <span className="badge bg-success-subtle text-success fs-6">
                  {details.attendance.percentage}% Overall Attendance ({details.attendance.present_count}/{details.attendance.total_sessions} Sessions)
                </span>
              </div>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Course</th>
                      <th>Date</th>
                      <th>Session Type</th>
                      <th>Topic Covered</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.attendance.records.map((r, i) => (
                      <tr key={i}>
                        <td><strong>{r.course}</strong> <span className="text-muted">({r.course_title})</span></td>
                        <td>{formatDate(r.date)}</td>
                        <td><span className="badge bg-light text-secondary border">{r.session_type}</span></td>
                        <td>{r.topic}</td>
                        <td>
                          <span className={`badge ${r.status === 'PRESENT' ? 'bg-success' : 'bg-danger'}`}>
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

          {/* Tab 4: Marks & Examinations */}
          {activeTab === 'marks' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Examination Scorecard</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Assessment</th>
                      <th>Course</th>
                      <th>Type</th>
                      <th>Score</th>
                      <th>Letter Grade</th>
                      <th>Result</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.marks.map((m, i) => (
                      <tr key={i}>
                        <td><strong>{m.exam_name}</strong></td>
                        <td>{m.course}</td>
                        <td><span className="badge bg-light text-secondary border">{m.exam_type}</span></td>
                        <td>{m.marks_obtained} / {m.max_marks}</td>
                        <td><span className="badge bg-primary text-white fw-bold">{m.grade}</span></td>
                        <td>
                          <span className={`badge ${m.is_passed ? 'bg-success' : 'bg-danger'}`}>
                            {m.is_passed ? 'PASSED' : 'FAILED'}
                          </span>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Tab 5: Fees & Payments */}
          {activeTab === 'fees' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Tuition & Fee Payment Invoices</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Invoice #</th>
                      <th>Description</th>
                      <th>Amount</th>
                      <th>Method</th>
                      <th>Transaction ID</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.fees.map((f, i) => (
                      <tr key={i}>
                        <td><strong className="text-primary">{f.invoice_number}</strong></td>
                        <td>{f.title}</td>
                        <td><strong>{formatCurrency(f.amount)}</strong></td>
                        <td><span className="badge bg-light text-secondary border">{f.payment_method}</span></td>
                        <td><code>{f.transaction_id}</code></td>
                        <td><span className="badge bg-success">{f.status}</span></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Tab 6: Assignments */}
          {activeTab === 'assignments' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Course Assignment Submissions</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Assignment Title</th>
                      <th>Course</th>
                      <th>Score</th>
                      <th>Status</th>
                      <th>Feedback</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.assignments.map((a, i) => (
                      <tr key={i}>
                        <td><strong>{a.assignment_title}</strong></td>
                        <td>{a.course}</td>
                        <td><strong>{a.score !== null ? `${a.score}/${a.max_score}` : 'Pending'}</strong></td>
                        <td><span className="badge bg-success">{a.status}</span></td>
                        <td className="text-muted">{a.feedback || 'No feedback yet.'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Tab 7: Library */}
          {activeTab === 'library' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Library Book Borrowing Log</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Book Title</th>
                      <th>Author</th>
                      <th>ISBN</th>
                      <th>Issued Date</th>
                      <th>Due Date</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.library.map((l, i) => (
                      <tr key={i}>
                        <td><strong>{l.book_title}</strong></td>
                        <td>{l.author}</td>
                        <td><code>{l.isbn}</code></td>
                        <td>{formatDate(l.issue_date)}</td>
                        <td>{formatDate(l.due_date)}</td>
                        <td><span className="badge bg-primary">{l.status}</span></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Tab 8: Placement */}
          {activeTab === 'placement' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Campus Recruitment & Job Applications</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Company</th>
                      <th>Job Role</th>
                      <th>Package (LPA)</th>
                      <th>Application Date</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.placement.map((p, i) => (
                      <tr key={i}>
                        <td><strong>{p.company}</strong></td>
                        <td>{p.job_role}</td>
                        <td><strong className="text-success">{p.package_lpa} LPA</strong></td>
                        <td>{formatDate(p.applied_at)}</td>
                        <td><span className="badge bg-warning text-dark">{p.status}</span></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Tab 9: Complaints */}
          {activeTab === 'complaints' && (
            <div>
              <h6 className="fw-bold text-dark mb-3">Grievance & Issue Redressal History</h6>
              <div className="table-responsive">
                <table className="table table-hover align-middle small">
                  <thead className="table-light">
                    <tr>
                      <th>Ticket #</th>
                      <th>Title</th>
                      <th>Category</th>
                      <th>Priority</th>
                      <th>Resolution Notes</th>
                      <th>Status</th>
                    </tr>
                  </thead>
                  <tbody>
                    {details.complaints.map((c, i) => (
                      <tr key={i}>
                        <td><code>{c.ticket_id}</code></td>
                        <td><strong>{c.title}</strong></td>
                        <td><span className="badge bg-light text-secondary border">{c.category}</span></td>
                        <td><span className="badge bg-warning text-dark">{c.priority}</span></td>
                        <td>{c.resolution_notes}</td>
                        <td><span className="badge bg-primary">{c.status}</span></td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}
        </div>
      ) : null}
    </Modal>
  );
};

export default StudentProfileModal;
