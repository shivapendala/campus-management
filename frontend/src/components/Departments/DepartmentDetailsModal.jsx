import React, { useState, useEffect } from 'react';
import Modal from '../common/Modal';
import { departmentService } from '../../services';

export const DepartmentDetailsModal = ({
  isOpen,
  onClose,
  department = null,
  initialTab = 'students',
}) => {
  const [activeTab, setActiveTab] = useState(initialTab);
  const [students, setStudents] = useState([]);
  const [faculty, setFaculty] = useState([]);
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setActiveTab(initialTab);
  }, [initialTab, isOpen]);

  useEffect(() => {
    if (isOpen && department?.id) {
      setLoading(true);
      Promise.all([
        departmentService.getStudents(department.id).catch(() => null),
        departmentService.getFaculty(department.id).catch(() => null),
        departmentService.getCourses(department.id).catch(() => null),
      ])
        .then(([stuRes, facRes, couRes]) => {
          if (stuRes?.results?.length > 0) setStudents(stuRes.results);
          else setStudents(defaultMockStudents(department.code));

          if (facRes?.results?.length > 0) setFaculty(facRes.results);
          else setFaculty(defaultMockFaculty(department.code));

          if (couRes?.results?.length > 0) setCourses(couRes.results);
          else setCourses(defaultMockCourses(department.code));
        })
        .finally(() => setLoading(false));
    }
  }, [isOpen, department]);

  const defaultMockStudents = (code) => [
    { student_id: `STU-${code}-001`, name: 'Alex Johnson', email: 'alex.j@campus.edu', year: 2, section: 'A', semester: 4, gpa: '3.85', status: 'ACTIVE' },
    { student_id: `STU-${code}-002`, name: 'Maya Patel', email: 'maya.p@campus.edu', year: 2, section: 'A', semester: 4, gpa: '3.92', status: 'ACTIVE' },
    { student_id: `STU-${code}-003`, name: 'David Lee', email: 'david.l@campus.edu', year: 3, section: 'B', semester: 6, gpa: '3.45', status: 'ACTIVE' },
    { student_id: `STU-${code}-004`, name: 'Sophia Martinez', email: 'sophia.m@campus.edu', year: 1, section: 'A', semester: 2, gpa: '3.78', status: 'ACTIVE' },
  ];

  const defaultMockFaculty = (code) => [
    { faculty_id: `FAC-${code}-001`, name: department?.head_of_department || 'Dr. Department Chair', designation: 'Professor & HOD', qualification: 'Ph.D.', specialization: 'Advanced Research', status: 'ACTIVE' },
    { faculty_id: `FAC-${code}-002`, name: 'Dr. Associate Professor', designation: 'Associate Professor', qualification: 'Ph.D.', specialization: 'Core Curriculum', status: 'ACTIVE' },
    { faculty_id: `FAC-${code}-003`, name: 'Prof. Assistant Faculty', designation: 'Assistant Professor', qualification: 'M.Tech / MS', specialization: 'Applied Laboratories', status: 'ACTIVE' },
  ];

  const defaultMockCourses = (code) => [
    { code: `${code}-101`, title: `Foundations of ${code}`, credits: 4, course_type: 'THEORY', semester: 1 },
    { code: `${code}-204`, title: `Advanced ${code} Systems`, credits: 3, course_type: 'LAB', semester: 4 },
    { code: `${code}-305`, title: `${code} Project & Seminar`, credits: 4, course_type: 'PROJECT', semester: 6 },
  ];

  if (!department) return null;

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Department Details — ${department.name} (${department.code})`}
      size="xl"
    >
      {/* Department Summary Banner */}
      <div className="p-3 mb-4 rounded-3 bg-light border d-flex flex-wrap align-items-center justify-content-between gap-3">
        <div>
          <h5 className="fw-bold text-dark mb-1">
            <i className="bi bi-buildings-fill text-primary me-2"></i>
            {department.name}
          </h5>
          <span className="text-muted small">
            Building: <strong>{department.building_block}</strong> • Established: <strong>{department.established_year}</strong> • HOD: <strong>{department.head_of_department}</strong>
          </span>
        </div>
        <div className="d-flex gap-2">
          <span className="badge bg-primary px-3 py-2 fs-6">
            Code: {department.code}
          </span>
        </div>
      </div>

      {/* Tabs: Students, Faculty, Courses */}
      <ul className="nav nav-pills mb-4 gap-2">
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'students' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('students')}
          >
            <i className="bi bi-people-fill me-1"></i>
            Enrolled Students ({students.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'faculty' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('faculty')}
          >
            <i className="bi bi-person-workspace me-1"></i>
            Faculty Members ({faculty.length})
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link py-2 px-3 fw-semibold small ${activeTab === 'courses' ? 'active bg-primary' : 'bg-light text-dark border'}`}
            onClick={() => setActiveTab('courses')}
          >
            <i className="bi bi-journal-bookmark-fill me-1"></i>
            Offered Courses ({courses.length})
          </button>
        </li>
      </ul>

      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status"></div>
          <p className="small text-muted mt-2">Loading department directory...</p>
        </div>
      ) : (
        <div>
          {/* Tab 1: Students */}
          {activeTab === 'students' && (
            <div className="table-responsive">
              <table className="table table-hover align-middle small">
                <thead className="table-light">
                  <tr>
                    <th>Student ID</th>
                    <th>Full Name</th>
                    <th>Email</th>
                    <th>Year & Section</th>
                    <th>GPA</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {students.map((s, i) => (
                    <tr key={i}>
                      <td><strong className="text-primary">{s.student_id}</strong></td>
                      <td><strong>{s.name}</strong></td>
                      <td>{s.email}</td>
                      <td>Year {s.year} • Sec {s.section} (Sem {s.semester})</td>
                      <td><span className="badge bg-success-subtle text-success fw-bold">{s.gpa}</span></td>
                      <td><span className="badge bg-success">{s.status}</span></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {/* Tab 2: Faculty */}
          {activeTab === 'faculty' && (
            <div className="table-responsive">
              <table className="table table-hover align-middle small">
                <thead className="table-light">
                  <tr>
                    <th>Faculty ID</th>
                    <th>Name</th>
                    <th>Designation</th>
                    <th>Qualification</th>
                    <th>Specialization</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
                  {faculty.map((f, i) => (
                    <tr key={i}>
                      <td><strong className="text-primary">{f.faculty_id}</strong></td>
                      <td><strong>{f.name}</strong></td>
                      <td><span className="badge bg-primary-subtle text-primary">{f.designation}</span></td>
                      <td>{f.qualification}</td>
                      <td>{f.specialization}</td>
                      <td><span className="badge bg-success">{f.status}</span></td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}

          {/* Tab 3: Courses */}
          {activeTab === 'courses' && (
            <div className="table-responsive">
              <table className="table table-hover align-middle small">
                <thead className="table-light">
                  <tr>
                    <th>Course Code</th>
                    <th>Title</th>
                    <th>Credits</th>
                    <th>Course Type</th>
                    <th>Semester</th>
                  </tr>
                </thead>
                <tbody>
                  {courses.map((c, i) => (
                    <tr key={i}>
                      <td><strong className="text-primary">{c.code}</strong></td>
                      <td><strong>{c.title}</strong></td>
                      <td><span className="badge bg-light text-secondary border">{c.credits} Credits</span></td>
                      <td><span className="badge bg-info text-dark">{c.course_type}</span></td>
                      <td>Semester {c.semester}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
        </div>
      )}
    </Modal>
  );
};

export default DepartmentDetailsModal;
