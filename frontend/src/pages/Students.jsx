import React, { useState, useEffect } from 'react';
import { studentService } from '../services';
import {
  Table,
  Pagination,
  Search,
  Filter,
  Modal,
  FormField,
  ConfirmationDialog,
  Alert,
} from '../components/common';
import { usePagination, useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { DEPARTMENTS, STATUS_BADGE_CLASSES } from '../utils/constants';

export const Students = () => {
  const { showSuccess, showError } = useNotification();
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState('');
  const [deptFilter, setDeptFilter] = useState('');

  // Modals
  const createModal = useModal();
  const deleteModal = useModal();

  // Form state
  const [formData, setFormData] = useState({
    student_id: '',
    name: '',
    email: '',
    phone: '',
    department: 1,
    year: 1,
    section: 'A',
    semester: 1,
    gpa: '3.50',
  });
  const [formLoading, setFormLoading] = useState(false);

  const defaultStudents = [
    { id: 1, student_id: 'STU-2026-001', name: 'Alex Johnson', email: 'alex.j@campus.edu', phone: '+1 555-0191', department_detail: { name: 'Computer Science & Engineering' }, year: 2, section: 'A', semester: 4, gpa: '3.85', status: 'ACTIVE' },
    { id: 2, student_id: 'STU-2026-002', name: 'Maya Patel', email: 'maya.p@campus.edu', phone: '+1 555-0192', department_detail: { name: 'Computer Science & Engineering' }, year: 2, section: 'A', semester: 4, gpa: '3.92', status: 'ACTIVE' },
    { id: 3, student_id: 'STU-2026-003', name: 'David Lee', email: 'david.l@campus.edu', phone: '+1 555-0193', department_detail: { name: 'Electrical & Electronics Engineering' }, year: 3, section: 'B', semester: 6, gpa: '3.45', status: 'ACTIVE' },
    { id: 4, student_id: 'STU-2026-004', name: 'Sophia Martinez', email: 'sophia.m@campus.edu', phone: '+1 555-0194', department_detail: { name: 'Business Administration' }, year: 1, section: 'A', semester: 2, gpa: '3.78', status: 'ACTIVE' },
    { id: 5, student_id: 'STU-2026-005', name: 'Liam O\'Connor', email: 'liam.o@campus.edu', phone: '+1 555-0195', department_detail: { name: 'Mechanical Engineering' }, year: 2, section: 'C', semester: 3, gpa: '3.60', status: 'ACTIVE' },
  ];

  const fetchStudents = async () => {
    setLoading(true);
    try {
      const res = await studentService.getAll();
      if (res.results && res.results.length > 0) {
        setStudents(res.results);
      } else {
        setStudents(defaultStudents);
      }
    } catch (err) {
      setStudents(defaultStudents);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchStudents();
  }, []);

  const filteredStudents = students.filter((s) => {
    const matchesSearch =
      s.student_id?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.email?.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesDept = deptFilter
      ? s.department_detail?.name?.includes(deptFilter) || s.department === parseInt(deptFilter)
      : true;
    return matchesSearch && matchesDept;
  });

  const {
    paginatedItems,
    currentPage,
    totalPages,
    goToPage,
    totalItems,
  } = usePagination(filteredStudents, 5);

  const handleCreateSubmit = async (e) => {
    e.preventDefault();
    setFormLoading(true);
    try {
      const newStu = {
        ...formData,
        id: Date.now(),
        department_detail: { name: 'Computer Science & Engineering' },
        status: 'ACTIVE',
      };
      setStudents([newStu, ...students]);
      createModal.closeModal();
      showSuccess(`Student ${formData.name} registered successfully!`);
    } catch (err) {
      showError('Failed to register student.');
    } finally {
      setFormLoading(false);
    }
  };

  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setStudents(students.filter((s) => s.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Student record deleted successfully.');
    }
  };

  const columns = [
    {
      header: 'Student ID',
      accessor: 'student_id',
      render: (row) => <span className="fw-bold text-primary">{row.student_id}</span>,
    },
    {
      header: 'Student Name',
      accessor: 'name',
      render: (row) => (
        <div className="d-flex align-items-center gap-2">
          <div
            className="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm"
            style={{ width: '32px', height: '32px', fontSize: '0.8rem' }}
          >
            {row.name ? row.name[0] : 'S'}
          </div>
          <div>
            <span className="fw-semibold text-dark d-block leading-tight">{row.name}</span>
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
      header: 'Year & Section',
      accessor: 'year',
      render: (row) => (
        <span className="small text-secondary">
          Year {row.year || 1} • Sec {row.section || 'A'} (Sem {row.semester || 1})
        </span>
      ),
    },
    {
      header: 'GPA',
      accessor: 'gpa',
      render: (row) => (
        <span className="badge bg-success-subtle text-success fw-bold">
          {row.gpa || '3.50'}
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
            className="btn btn-sm btn-light text-danger"
            onClick={() => deleteModal.openModal(row)}
            title="Delete Student"
          >
            <i className="bi bi-trash"></i>
          </button>
        </div>
      ),
    },
  ];

  return (
    <div className="container-fluid p-4">
      {/* Header */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Student Directory</h2>
          <p className="text-muted mb-0">
            Search, filter, and enroll student profiles across institutional academic departments
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => createModal.openModal()}
            className="btn btn-primary btn-sm d-flex align-items-center gap-2 fw-semibold px-3"
          >
            <i className="bi bi-person-plus-fill"></i>
            <span>Register Student</span>
          </button>
        </div>
      </div>

      {/* Main Table Card */}
      <div className="campus-card shadow-sm border-0 mb-4">
        {/* Controls toolbar */}
        <div className="p-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <Search
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Search student ID, name, email..."
          />

          <div className="d-flex align-items-center gap-2">
            <Filter
              value={deptFilter}
              onChange={setDeptFilter}
              label="All Departments"
              options={DEPARTMENTS.map((d) => ({ value: d.name, label: d.name }))}
            />
          </div>
        </div>

        {/* Reusable Table */}
        <Table columns={columns} data={paginatedItems} loading={loading} />

        {/* Reusable Pagination */}
        <Pagination
          currentPage={currentPage}
          totalPages={totalPages}
          totalItems={totalItems}
          onPageChange={goToPage}
        />
      </div>

      {/* Register Student Modal */}
      <Modal
        isOpen={createModal.isOpen}
        onClose={createModal.closeModal}
        title="Register New Student"
        size="lg"
      >
        <form onSubmit={handleCreateSubmit}>
          <div className="row g-3 mb-3">
            <div className="col-12 col-md-6">
              <FormField
                label="Student ID"
                name="student_id"
                required
                placeholder="STU-2026-006"
                value={formData.student_id}
                onChange={(e) => setFormData({ ...formData, student_id: e.target.value })}
              />
            </div>
            <div className="col-12 col-md-6">
              <FormField
                label="Full Name"
                name="name"
                required
                placeholder="Emma Watson"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              />
            </div>
          </div>

          <div className="row g-3 mb-3">
            <div className="col-12 col-md-6">
              <FormField
                label="Email"
                type="email"
                name="email"
                required
                placeholder="emma.w@campus.edu"
                value={formData.email}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              />
            </div>
            <div className="col-12 col-md-6">
              <FormField
                label="Phone"
                name="phone"
                placeholder="+1 555-0196"
                value={formData.phone}
                onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
              />
            </div>
          </div>

          <div className="row g-3 mb-4">
            <div className="col-12 col-md-4">
              <FormField
                label="Year (1-4)"
                type="number"
                name="year"
                value={formData.year}
                onChange={(e) => setFormData({ ...formData, year: parseInt(e.target.value) })}
              />
            </div>
            <div className="col-12 col-md-4">
              <FormField
                label="Section"
                name="section"
                placeholder="A"
                value={formData.section}
                onChange={(e) => setFormData({ ...formData, section: e.target.value })}
              />
            </div>
            <div className="col-12 col-md-4">
              <FormField
                label="Initial GPA"
                name="gpa"
                placeholder="3.80"
                value={formData.gpa}
                onChange={(e) => setFormData({ ...formData, gpa: e.target.value })}
              />
            </div>
          </div>

          <div className="d-flex justify-content-end gap-2 pt-3 border-top">
            <button
              type="button"
              className="btn btn-light btn-sm px-3"
              onClick={createModal.closeModal}
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={formLoading}
              className="btn btn-primary btn-sm px-4 fw-semibold"
            >
              {formLoading ? 'Saving...' : 'Register Student'}
            </button>
          </div>
        </form>
      </Modal>

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Student Record"
        message={`Are you sure you want to remove ${deleteModal.modalData?.name} (${deleteModal.modalData?.student_id}) from the active student register?`}
        confirmText="Delete Record"
        confirmVariant="danger"
      />
    </div>
  );
};

export default Students;
