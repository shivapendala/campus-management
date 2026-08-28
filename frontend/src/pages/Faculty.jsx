import React, { useState, useEffect } from 'react';
import { facultyService } from '../services';
import {
  Table,
  Pagination,
  Search,
  Filter,
  ConfirmationDialog,
} from '../components/common';
import FacultyFormModal from '../components/Faculty/FacultyFormModal';
import FacultyProfileModal from '../components/Faculty/FacultyProfileModal';
import AssignSubjectModal from '../components/Faculty/AssignSubjectModal';
import FacultyScheduleModal from '../components/Faculty/FacultyScheduleModal';
import { usePagination, useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { DEPARTMENTS, STATUS_BADGE_CLASSES } from '../utils/constants';

export const Faculty = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [facultyList, setFacultyList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Search & Filters
  const [searchQuery, setSearchQuery] = useState('');
  const [deptFilter, setDeptFilter] = useState('');
  const [desigFilter, setDesigFilter] = useState('');

  // Modals
  const formModal = useModal();
  const profileModal = useModal();
  const assignModal = useModal();
  const scheduleModal = useModal();
  const deleteModal = useModal();

  const defaultFaculty = [
    { id: 1, faculty_id: 'FAC-CS-001', name: 'Dr. Alan Smith', email: 'alan.smith@campus.edu', phone: '+1 (555) 019-2841', designation: 'Professor & HOD', qualification: 'Ph.D. in AI', specialization: 'Artificial Intelligence & Neural Networks', office_room: 'Turing Block 101', department_detail: { name: 'Computer Science & Engineering' }, status: 'ACTIVE' },
    { id: 2, faculty_id: 'FAC-CS-002', name: 'Dr. Elena Rostova', email: 'elena.r@campus.edu', phone: '+1 (555) 019-2842', designation: 'Associate Professor', qualification: 'Ph.D. in Cloud Systems', specialization: 'Distributed Cloud Architectures', office_room: 'Turing Block 204', department_detail: { name: 'Computer Science & Engineering' }, status: 'ACTIVE' },
    { id: 3, faculty_id: 'FAC-EE-001', name: 'Dr. Rajesh Kumar', email: 'rajesh.k@campus.edu', phone: '+1 (555) 019-2843', designation: 'Professor & HOD', qualification: 'Ph.D. in VLSI', specialization: 'Embedded Microcontroller Systems', office_room: 'Tesla Block 102', department_detail: { name: 'Electrical & Electronics Engineering' }, status: 'ACTIVE' },
    { id: 4, faculty_id: 'FAC-BA-001', name: 'Dr. Sara Vance', email: 'sara.v@campus.edu', phone: '+1 (555) 019-2844', designation: 'Assistant Professor', qualification: 'Ph.D. in Finance', specialization: 'Corporate Finance & Valuation', office_room: 'Drucker Block 301', department_detail: { name: 'Business Administration' }, status: 'ACTIVE' },
    { id: 5, faculty_id: 'FAC-ME-001', name: 'Dr. Robert Ford', email: 'robert.f@campus.edu', phone: '+1 (555) 019-2845', designation: 'Professor & HOD', qualification: 'Ph.D. in Robotics', specialization: 'Thermodynamics & Robotics', office_room: 'Watt Block 105', department_detail: { name: 'Mechanical Engineering' }, status: 'ACTIVE' },
  ];

  const fetchFaculty = async () => {
    setLoading(true);
    try {
      const res = await facultyService.getAll();
      if (res.results && res.results.length > 0) {
        setFacultyList(res.results);
      } else {
        setFacultyList(defaultFaculty);
      }
    } catch (err) {
      setFacultyList(defaultFaculty);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchFaculty();
  }, []);

  const filteredFaculty = facultyList.filter((f) => {
    const matchesSearch =
      f.faculty_id?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.email?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      f.specialization?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesDept = deptFilter
      ? f.department_detail?.name?.includes(deptFilter) || f.department === parseInt(deptFilter)
      : true;

    const matchesDesig = desigFilter ? f.designation === desigFilter : true;

    return matchesSearch && matchesDept && matchesDesig;
  });

  const {
    paginatedItems,
    currentPage,
    totalPages,
    goToPage,
    totalItems,
  } = usePagination(filteredFaculty, 8);

  const handleFormSubmit = (formData) => {
    setActionLoading(true);
    try {
      if (formModal.modalData?.isEdit) {
        setFacultyList((prev) =>
          prev.map((f) => (f.id === formModal.modalData.faculty.id ? { ...f, ...formData } : f))
        );
        showSuccess(`Faculty member ${formData.name} updated successfully!`);
      } else {
        const newFac = {
          ...formData,
          id: Date.now(),
          department_detail: {
            name: DEPARTMENTS[(formData.department || 1) - 1]?.name || 'Computer Science & Engineering',
          },
        };
        setFacultyList([newFac, ...facultyList]);
        showSuccess(`Faculty member ${formData.name} added successfully!`);
      }
      formModal.closeModal();
    } catch (err) {
      showError('Failed to save faculty record.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setFacultyList((prev) => prev.filter((f) => f.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Faculty record deleted.');
    }
  };

  const handleAssignSubject = (assignmentData) => {
    showSuccess(
      `Course ${assignmentData.courseCode} and Year ${assignmentData.year} (Sec ${assignmentData.section}) allocated to ${assignmentData.facultyName}!`
    );
    assignModal.closeModal();
  };

  const columns = [
    {
      header: 'Faculty ID',
      accessor: 'faculty_id',
      render: (row) => (
        <span
          className="fw-bold text-primary cursor-pointer hover-underline"
          onClick={() => profileModal.openModal(row)}
          style={{ cursor: 'pointer' }}
          title="Click to view dossier"
        >
          {row.faculty_id}
        </span>
      ),
    },
    {
      header: 'Faculty Member',
      accessor: 'name',
      render: (row) => (
        <div className="d-flex align-items-center gap-2">
          <div
            className="bg-primary text-white rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm"
            style={{ width: '34px', height: '34px', fontSize: '0.85rem' }}
          >
            {row.name ? row.name[0] : 'F'}
          </div>
          <div>
            <span
              className="fw-semibold text-dark d-block leading-tight cursor-pointer"
              onClick={() => profileModal.openModal(row)}
              style={{ cursor: 'pointer' }}
            >
              {row.name}
            </span>
            <small className="text-muted">{row.email}</small>
          </div>
        </div>
      ),
    },
    {
      header: 'Department',
      accessor: 'department',
      render: (row) => (
        <span className="badge bg-light text-secondary border">
          {row.department_detail?.name || 'Computer Science'}
        </span>
      ),
    },
    {
      header: 'Designation',
      accessor: 'designation',
      render: (row) => (
        <span className="badge bg-primary-subtle text-primary fw-semibold">
          {row.designation || 'Assistant Professor'}
        </span>
      ),
    },
    {
      header: 'Specialization',
      accessor: 'specialization',
      render: (row) => (
        <span className="small text-secondary" style={{ maxWidth: '180px', display: 'inline-block' }}>
          {row.specialization || 'Academic Research'}
        </span>
      ),
    },
    {
      header: 'Status',
      accessor: 'status',
      render: (row) => (
        <span className={`badge ${STATUS_BADGE_CLASSES[row.status] || 'bg-success text-white'}`}>
          {row.status || 'ACTIVE'}
        </span>
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
            onClick={() => assignModal.openModal(row)}
            title="Assign Subject & Class"
          >
            <i className="bi bi-person-plus-fill me-1"></i> Assign
          </button>
          <button
            className="btn btn-sm btn-light text-info"
            onClick={() => scheduleModal.openModal(row)}
            title="View Weekly Schedule"
          >
            <i className="bi bi-calendar3 me-1"></i> Timetable
          </button>
          <button
            className="btn btn-sm btn-light text-secondary"
            onClick={() => formModal.openModal({ faculty: row, isEdit: true })}
            title="Edit Faculty"
          >
            <i className="bi bi-pencil-fill"></i>
          </button>
          <button
            className="btn btn-sm btn-light text-danger"
            onClick={() => deleteModal.openModal(row)}
            title="Delete Faculty"
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
          <h2 className="fw-bold text-dark mb-1">Faculty Management Directory</h2>
          <p className="text-muted mb-0">
            Allocate courses, manage department professors, assign sections, and view timetables
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => formModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-person-plus-fill"></i>
            <span>Add Faculty</span>
          </button>
        </div>
      </div>

      {/* Main Table Card */}
      <div className="campus-card shadow-sm border-0 mb-4">
        {/* Controls Toolbar: Search & Multi-Filters */}
        <div className="p-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <Search
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Search faculty name, ID, specialization..."
          />

          <div className="d-flex flex-wrap align-items-center gap-2">
            <Filter
              value={deptFilter}
              onChange={setDeptFilter}
              label="All Departments"
              options={DEPARTMENTS.map((d) => ({ value: d.name, label: d.name }))}
            />

            <Filter
              value={desigFilter}
              onChange={setDesigFilter}
              label="All Designations"
              options={[
                { value: 'Professor & HOD', label: 'Professor & HOD' },
                { value: 'Professor', label: 'Professor' },
                { value: 'Associate Professor', label: 'Associate Professor' },
                { value: 'Assistant Professor', label: 'Assistant Professor' },
              ]}
            />

            {(deptFilter || desigFilter || searchQuery) && (
              <button
                className="btn btn-sm btn-link text-danger text-decoration-none px-2"
                onClick={() => {
                  setDeptFilter('');
                  setDesigFilter('');
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

      {/* Faculty Profile Modal */}
      <FacultyProfileModal
        isOpen={profileModal.isOpen}
        onClose={profileModal.closeModal}
        faculty={profileModal.modalData}
      />

      {/* Add / Edit Faculty Form Modal */}
      <FacultyFormModal
        isOpen={formModal.isOpen}
        onClose={formModal.closeModal}
        onSubmit={handleFormSubmit}
        initialData={formModal.modalData?.faculty}
        isEdit={formModal.modalData?.isEdit}
        loading={actionLoading}
      />

      {/* Assign Subject & Class Modal */}
      <AssignSubjectModal
        isOpen={assignModal.isOpen}
        onClose={assignModal.closeModal}
        onAssign={handleAssignSubject}
        faculty={assignModal.modalData}
        loading={actionLoading}
      />

      {/* Weekly Timetable Schedule Modal */}
      <FacultyScheduleModal
        isOpen={scheduleModal.isOpen}
        onClose={scheduleModal.closeModal}
        faculty={scheduleModal.modalData}
      />

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Faculty Record"
        message={`Are you sure you want to remove ${deleteModal.modalData?.name} (${deleteModal.modalData?.faculty_id}) from active academic staff?`}
        confirmText="Delete Faculty"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Faculty;
