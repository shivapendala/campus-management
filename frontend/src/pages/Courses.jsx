import React, { useState, useEffect } from 'react';
import { courseService } from '../services';
import {
  Table,
  Pagination,
  Search,
  Filter,
  ConfirmationDialog,
} from '../components/common';
import CourseFormModal from '../components/Courses/CourseFormModal';
import AssignFacultyModal from '../components/Courses/AssignFacultyModal';
import CourseSyllabusModal from '../components/Courses/CourseSyllabusModal';
import { usePagination, useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { DEPARTMENTS } from '../utils/constants';

export const Courses = () => {
  const { showSuccess, showError } = useNotification();
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Search & Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [deptFilter, setDeptFilter] = useState('');
  const [semFilter, setSemFilter] = useState('');
  const [typeFilter, setTypeFilter] = useState('');

  // Modals
  const formModal = useModal();
  const assignModal = useModal();
  const syllabusModal = useModal();
  const deleteModal = useModal();

  const defaultCourses = [
    { id: 1, code: 'CSE-101', title: 'Data Structures & Algorithms', department_detail: { name: 'Computer Science & Engineering', code: 'CSE' }, credits: 4, semester: 3, course_type: 'THEORY', instructor_detail: { name: 'Dr. Alan Smith' }, capacity: 60 },
    { id: 2, code: 'CSE-202', title: 'Database Management Systems (DBMS)', department_detail: { name: 'Computer Science & Engineering', code: 'CSE' }, credits: 4, semester: 4, course_type: 'THEORY', instructor_detail: { name: 'Dr. Elena Rostova' }, capacity: 60 },
    { id: 3, code: 'CSE-301', title: 'Operating Systems', department_detail: { name: 'Computer Science & Engineering', code: 'CSE' }, credits: 4, semester: 5, course_type: 'THEORY', instructor_detail: { name: 'Dr. Alan Smith' }, capacity: 60 },
    { id: 4, code: 'CSE-302', title: 'Computer Networks', department_detail: { name: 'Computer Science & Engineering', code: 'CSE' }, credits: 3, semester: 6, course_type: 'THEORY', instructor_detail: { name: 'Dr. Elena Rostova' }, capacity: 60 },
    { id: 5, code: 'CSE-401', title: 'Machine Learning & Neural Networks', department_detail: { name: 'Computer Science & Engineering', code: 'CSE' }, credits: 4, semester: 7, course_type: 'ELECTIVE', instructor_detail: { name: 'Dr. Alan Smith' }, capacity: 45 },
    { id: 6, code: 'ECE-201', title: 'Digital Signal Processing', department_detail: { name: 'Electronics & Communication Engineering', code: 'ECE' }, credits: 4, semester: 4, course_type: 'THEORY', instructor_detail: { name: 'Dr. Marcus Vance' }, capacity: 50 },
    { id: 7, code: 'EEE-201', title: 'Embedded Microcontroller Systems', department_detail: { name: 'Electrical & Electronics Engineering', code: 'EEE' }, credits: 4, semester: 4, course_type: 'THEORY', instructor_detail: { name: 'Dr. Rajesh Kumar' }, capacity: 45 },
    { id: 8, code: 'MECH-301', title: 'Thermodynamics & Heat Transfer', department_detail: { name: 'Mechanical Engineering', code: 'MECH' }, credits: 4, semester: 5, course_type: 'THEORY', instructor_detail: { name: 'Dr. Robert Ford' }, capacity: 40 },
    { id: 9, code: 'CIVIL-201', title: 'Structural Analysis & Mechanics', department_detail: { name: 'Civil Engineering', code: 'CIVIL' }, credits: 4, semester: 4, course_type: 'THEORY', instructor_detail: { name: 'Dr. Arthur Dent' }, capacity: 40 },
  ];

  const fetchCourses = async () => {
    setLoading(true);
    try {
      const res = await courseService.getAll();
      if (res.results && res.results.length > 0) {
        setCourses(res.results);
      } else {
        setCourses(defaultCourses);
      }
    } catch (err) {
      setCourses(defaultCourses);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCourses();
  }, []);

  const filteredCourses = courses.filter((c) => {
    const matchesSearch =
      c.code?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.title?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      c.instructor_detail?.name?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesDept = deptFilter
      ? c.department_detail?.code === deptFilter || c.department_detail?.name?.includes(deptFilter)
      : true;

    const matchesSem = semFilter ? String(c.semester) === String(semFilter) : true;
    const matchesType = typeFilter ? c.course_type === typeFilter : true;

    return matchesSearch && matchesDept && matchesSem && matchesType;
  });

  const {
    paginatedItems,
    currentPage,
    totalPages,
    goToPage,
    totalItems,
  } = usePagination(filteredCourses, 8);

  const handleFormSubmit = (formData) => {
    setActionLoading(true);
    try {
      if (formModal.modalData?.isEdit) {
        setCourses((prev) =>
          prev.map((c) => (c.id === formModal.modalData.course.id ? { ...c, ...formData } : c))
        );
        showSuccess(`Subject ${formData.code} (${formData.title}) updated!`);
      } else {
        const dept = DEPARTMENTS[(formData.department || 1) - 1] || DEPARTMENTS[0];
        const newCourse = {
          ...formData,
          id: Date.now(),
          department_detail: { name: dept.name, code: dept.code },
          instructor_detail: { name: 'Not Assigned' },
        };
        setCourses([newCourse, ...courses]);
        showSuccess(`Subject ${formData.code} (${formData.title}) added to catalog!`);
      }
      formModal.closeModal();
    } catch (err) {
      showError('Failed to save course.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleAssignFaculty = ({ courseId, courseCode, facultyName }) => {
    setCourses((prev) =>
      prev.map((c) => (c.id === courseId ? { ...c, instructor_detail: { name: facultyName } } : c))
    );
    showSuccess(`${facultyName} assigned as lead instructor for ${courseCode}!`);
    assignModal.closeModal();
  };

  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setCourses((prev) => prev.filter((c) => c.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Subject deleted from active catalog.');
    }
  };

  const columns = [
    {
      header: 'Course Code',
      accessor: 'code',
      render: (row) => (
        <span
          className="fw-bold text-primary cursor-pointer hover-underline"
          onClick={() => syllabusModal.openModal(row)}
          title="Click to view 5-Unit Syllabus"
          style={{ cursor: 'pointer' }}
        >
          {row.code}
        </span>
      ),
    },
    {
      header: 'Subject Title',
      accessor: 'title',
      render: (row) => (
        <div>
          <span
            className="fw-semibold text-dark d-block leading-tight cursor-pointer"
            onClick={() => syllabusModal.openModal(row)}
            style={{ cursor: 'pointer' }}
          >
            {row.title}
          </span>
          <small className="text-muted">{row.department_detail?.name || 'Computer Science'}</small>
        </div>
      ),
    },
    {
      header: 'Semester',
      accessor: 'semester',
      render: (row) => (
        <span className="badge bg-light text-secondary border">
          Semester {row.semester}
        </span>
      ),
    },
    {
      header: 'Credits & Type',
      accessor: 'credits',
      render: (row) => (
        <div className="d-flex align-items-center gap-1">
          <span className="badge bg-primary-subtle text-primary fw-bold">
            {row.credits} Credits
          </span>
          <span className={`badge ${row.course_type === 'LAB' ? 'bg-info text-dark' : row.course_type === 'ELECTIVE' ? 'bg-warning text-dark' : 'bg-secondary text-white'}`}>
            {row.course_type}
          </span>
        </div>
      ),
    },
    {
      header: 'Assigned Faculty',
      accessor: 'instructor',
      render: (row) => (
        <div className="d-flex align-items-center gap-2">
          <div
            className="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm"
            style={{ width: '28px', height: '28px', fontSize: '0.75rem' }}
          >
            {row.instructor_detail?.name ? row.instructor_detail.name[0] : 'P'}
          </div>
          <span className="small text-dark fw-medium">
            {row.instructor_detail?.name || 'Unassigned'}
          </span>
        </div>
      ),
    },
    {
      header: 'Actions',
      className: 'text-end',
      cellClassName: 'text-end',
      render: (row) => (
        <div className="d-inline-flex gap-1">
          <button
            className="btn btn-sm btn-light text-primary"
            onClick={() => syllabusModal.openModal(row)}
            title="View 5-Unit Syllabus"
          >
            <i className="bi bi-book-half me-1"></i> Syllabus
          </button>
          <button
            className="btn btn-sm btn-light text-success"
            onClick={() => assignModal.openModal(row)}
            title="Allocate Faculty"
          >
            <i className="bi bi-person-check-fill me-1"></i> Assign
          </button>
          <button
            className="btn btn-sm btn-light text-secondary"
            onClick={() => formModal.openModal({ course: row, isEdit: true })}
            title="Edit Subject"
          >
            <i className="bi bi-pencil-fill"></i>
          </button>
          <button
            className="btn btn-sm btn-light text-danger"
            onClick={() => deleteModal.openModal(row)}
            title="Delete Subject"
          >
            <i className="bi bi-trash-fill"></i>
          </button>
        </div>
      ),
    },
  ];

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Course & Subject Catalog</h2>
          <p className="text-muted mb-0">
            Curriculum management, 5-Unit syllabi, semester mappings, and faculty allocations
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => formModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-journal-plus"></i>
            <span>Add Course</span>
          </button>
        </div>
      </div>

      {/* Main Table Card */}
      <div className="campus-card shadow-sm border-0 mb-4">
        {/* Controls Toolbar */}
        <div className="p-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <Search
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Search code, title, professor..."
          />

          <div className="d-flex flex-wrap align-items-center gap-2">
            <Filter
              value={deptFilter}
              onChange={setDeptFilter}
              label="All Departments"
              options={DEPARTMENTS.map((d) => ({ value: d.code, label: `${d.code} — ${d.name}` }))}
            />

            <Filter
              value={semFilter}
              onChange={setSemFilter}
              label="All Semesters"
              options={[
                { value: '1', label: 'Semester 1' },
                { value: '2', label: 'Semester 2' },
                { value: '3', label: 'Semester 3' },
                { value: '4', label: 'Semester 4' },
                { value: '5', label: 'Semester 5' },
                { value: '6', label: 'Semester 6' },
                { value: '7', label: 'Semester 7' },
                { value: '8', label: 'Semester 8' },
              ]}
            />

            <Filter
              value={typeFilter}
              onChange={setTypeFilter}
              label="All Types"
              options={[
                { value: 'THEORY', label: 'Theory' },
                { value: 'LAB', label: 'Lab' },
                { value: 'ELECTIVE', label: 'Elective' },
                { value: 'PROJECT', label: 'Project' },
              ]}
            />

            {(deptFilter || semFilter || typeFilter || searchQuery) && (
              <button
                className="btn btn-sm btn-link text-danger text-decoration-none px-2"
                onClick={() => {
                  setDeptFilter('');
                  setSemFilter('');
                  setTypeFilter('');
                  setSearchQuery('');
                }}
              >
                Reset Filters
              </button>
            )}
          </div>
        </div>

        {/* Table View */}
        <Table columns={columns} data={paginatedItems} loading={loading} />

        {/* Pagination */}
        <Pagination
          currentPage={currentPage}
          totalPages={totalPages}
          totalItems={totalItems}
          onPageChange={goToPage}
        />
      </div>

      {/* Course Form Modal */}
      <CourseFormModal
        isOpen={formModal.isOpen}
        onClose={formModal.closeModal}
        onSubmit={handleFormSubmit}
        initialData={formModal.modalData?.course}
        isEdit={formModal.modalData?.isEdit}
        loading={actionLoading}
      />

      {/* Assign Faculty Modal */}
      <AssignFacultyModal
        isOpen={assignModal.isOpen}
        onClose={assignModal.closeModal}
        onAssign={handleAssignFaculty}
        course={assignModal.modalData}
        loading={actionLoading}
      />

      {/* 5-Unit Syllabus Modal */}
      <CourseSyllabusModal
        isOpen={syllabusModal.isOpen}
        onClose={syllabusModal.closeModal}
        course={syllabusModal.modalData}
      />

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Course Record"
        message={`Are you sure you want to remove ${deleteModal.modalData?.code}: ${deleteModal.modalData?.title} from the active catalog?`}
        confirmText="Delete Subject"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Courses;
