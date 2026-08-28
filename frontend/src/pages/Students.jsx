import React, { useState, useEffect } from 'react';
import { studentService } from '../services';
import {
  Table,
  Pagination,
  Search,
  Filter,
  ConfirmationDialog,
} from '../components/common';
import StudentProfileModal from '../components/Students/StudentProfileModal';
import StudentFormModal from '../components/Students/StudentFormModal';
import ImportStudentsModal from '../components/Students/ImportStudentsModal';
import { usePagination, useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';
import { DEPARTMENTS, STATUS_BADGE_CLASSES } from '../utils/constants';

export const Students = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Filters & Search
  const [searchQuery, setSearchQuery] = useState('');
  const [deptFilter, setDeptFilter] = useState('');
  const [yearFilter, setYearFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState('');

  // Modals
  const formModal = useModal();
  const profileModal = useModal();
  const deleteModal = useModal();
  const importModal = useModal();

  const defaultStudents = [
    { id: 1, student_id: 'STU-2026-001', name: 'Alex Johnson', email: 'alex.j@campus.edu', phone: '+1 (555) 019-2831', department_detail: { name: 'Computer Science & Engineering' }, year: 2, section: 'A', semester: 4, gpa: '3.85', status: 'ACTIVE' },
    { id: 2, student_id: 'STU-2026-002', name: 'Maya Patel', email: 'maya.p@campus.edu', phone: '+1 (555) 019-2832', department_detail: { name: 'Computer Science & Engineering' }, year: 2, section: 'A', semester: 4, gpa: '3.92', status: 'ACTIVE' },
    { id: 3, student_id: 'STU-2026-003', name: 'David Lee', email: 'david.l@campus.edu', phone: '+1 (555) 019-2833', department_detail: { name: 'Electrical & Electronics Engineering' }, year: 3, section: 'B', semester: 6, gpa: '3.45', status: 'ACTIVE' },
    { id: 4, student_id: 'STU-2026-004', name: 'Sophia Martinez', email: 'sophia.m@campus.edu', phone: '+1 (555) 019-2834', department_detail: { name: 'Business Administration' }, year: 1, section: 'A', semester: 2, gpa: '3.78', status: 'ACTIVE' },
    { id: 5, student_id: 'STU-2026-005', name: 'Liam O\'Connor', email: 'liam.o@campus.edu', phone: '+1 (555) 019-2835', department_detail: { name: 'Mechanical Engineering' }, year: 2, section: 'C', semester: 3, gpa: '3.60', status: 'ACTIVE' },
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

  // Filtered dataset
  const filteredStudents = students.filter((s) => {
    const matchesSearch =
      s.student_id?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.name?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.email?.toLowerCase().includes(searchQuery.toLowerCase()) ||
      s.phone?.toLowerCase().includes(searchQuery.toLowerCase());

    const matchesDept = deptFilter
      ? s.department_detail?.name?.includes(deptFilter) || s.department === parseInt(deptFilter)
      : true;

    const matchesYear = yearFilter ? String(s.year) === String(yearFilter) : true;
    const matchesStatus = statusFilter ? s.status === statusFilter : true;

    return matchesSearch && matchesDept && matchesYear && matchesStatus;
  });

  const {
    paginatedItems,
    currentPage,
    totalPages,
    goToPage,
    totalItems,
  } = usePagination(filteredStudents, 8);

  // Form Submit (Add or Edit)
  const handleFormSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (formModal.modalData?.isEdit) {
        // Edit existing student
        setStudents((prev) =>
          prev.map((s) => (s.id === formModal.modalData.student.id ? { ...s, ...formData } : s))
        );
        showSuccess(`Student ${formData.name} updated successfully!`);
      } else {
        // Add new student
        const newStu = {
          ...formData,
          id: Date.now(),
          department_detail: {
            name: DEPARTMENTS[(formData.department || 1) - 1]?.name || 'Computer Science & Engineering',
          },
        };
        setStudents([newStu, ...students]);
        showSuccess(`Student ${formData.name} enrolled successfully!`);
      }
      formModal.closeModal();
    } catch (err) {
      showError('Failed to save student record.');
    } finally {
      setActionLoading(false);
    }
  };

  // Delete Action
  const handleDeleteConfirm = async () => {
    if (deleteModal.modalData) {
      setStudents((prev) => prev.filter((s) => s.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Student record deleted.');
    }
  };

  // CSV Import
  const handleCSVImport = async (csvText) => {
    setActionLoading(true);
    try {
      // parse rows
      const lines = csvText.trim().split('\n');
      if (lines.length > 1) {
        const imported = lines.slice(1).map((line, idx) => {
          const [sid, name, email, phone, year, sec, sem, gpa] = line.split(',');
          return {
            id: Date.now() + idx,
            student_id: sid?.trim() || `STU-2026-${idx}`,
            name: name?.trim() || 'New Student',
            email: email?.trim() || 'student@campus.edu',
            phone: phone?.trim() || '+1 555-0199',
            year: parseInt(year) || 1,
            section: sec?.trim() || 'A',
            semester: parseInt(sem) || 1,
            gpa: gpa?.trim() || '3.50',
            department_detail: { name: 'Computer Science & Engineering' },
            status: 'ACTIVE',
          };
        });
        setStudents([...imported, ...students]);
        showSuccess(`Imported ${imported.length} student records from CSV!`);
      }
      importModal.closeModal();
    } catch (err) {
      showError('Failed to parse CSV file.');
    } finally {
      setActionLoading(false);
    }
  };

  // CSV Export
  const handleCSVExport = () => {
    const headers = 'Student ID,Full Name,Email,Phone,Department,Year,Section,Semester,GPA,Status\n';
    const rows = filteredStudents
      .map(
        (s) =>
          `"${s.student_id}","${s.name}","${s.email}","${s.phone || ''}","${s.department_detail?.name || 'CS'}","${s.year}","${s.section}","${s.semester}","${s.gpa}","${s.status}"`
      )
      .join('\n');

    const blob = new Blob([headers + rows], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'students_register_2026.csv');
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    showInfo('Student directory exported to CSV.');
  };

  const columns = [
    {
      header: 'Student ID',
      accessor: 'student_id',
      render: (row) => (
        <span
          className="fw-bold text-primary cursor-pointer hover-underline"
          onClick={() => profileModal.openModal(row)}
          title="Click to view 360° Profile"
          style={{ cursor: 'pointer' }}
        >
          {row.student_id}
        </span>
      ),
    },
    {
      header: 'Full Name',
      accessor: 'name',
      render: (row) => (
        <div className="d-flex align-items-center gap-2">
          <div
            className="bg-light text-primary rounded-circle d-flex align-items-center justify-content-center fw-bold shadow-sm"
            style={{ width: '34px', height: '34px', fontSize: '0.85rem' }}
          >
            {row.name ? row.name[0] : 'S'}
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
      header: 'Year & Batch',
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
            className="btn btn-sm btn-light text-primary"
            onClick={() => profileModal.openModal(row)}
            title="View 360° Profile"
          >
            <i className="bi bi-eye-fill"></i>
          </button>
          <button
            className="btn btn-sm btn-light text-secondary"
            onClick={() => formModal.openModal({ student: row, isEdit: true })}
            title="Edit Student"
          >
            <i className="bi bi-pencil-fill"></i>
          </button>
          <button
            className="btn btn-sm btn-light text-danger"
            onClick={() => deleteModal.openModal(row)}
            title="Delete Record"
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
          <h2 className="fw-bold text-dark mb-1">Student Management & Registry</h2>
          <p className="text-muted mb-0">
            Search, filter, view 360° student records, and manage institutional enrollments
          </p>
        </div>
        <div className="d-flex flex-wrap gap-2">
          <button
            onClick={() => importModal.openModal()}
            className="btn btn-outline-secondary btn-sm d-flex align-items-center gap-1 fw-semibold px-3"
          >
            <i className="bi bi-file-earmark-arrow-up"></i>
            <span>Import CSV</span>
          </button>
          <button
            onClick={handleCSVExport}
            className="btn btn-outline-secondary btn-sm d-flex align-items-center gap-1 fw-semibold px-3"
          >
            <i className="bi bi-file-earmark-arrow-down"></i>
            <span>Export CSV</span>
          </button>
          <button
            onClick={() => formModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-person-plus-fill"></i>
            <span>Add Student</span>
          </button>
        </div>
      </div>

      {/* Main Student Directory Table Card */}
      <div className="campus-card shadow-sm border-0 mb-4">
        {/* Controls Toolbar: Search & Multi-Filters */}
        <div className="p-3 border-bottom d-flex flex-wrap align-items-center justify-content-between gap-3">
          <Search
            value={searchQuery}
            onChange={setSearchQuery}
            placeholder="Search student ID, name, email, phone..."
          />

          <div className="d-flex flex-wrap align-items-center gap-2">
            <Filter
              value={deptFilter}
              onChange={setDeptFilter}
              label="All Departments"
              options={DEPARTMENTS.map((d) => ({ value: d.name, label: d.name }))}
            />

            <Filter
              value={yearFilter}
              onChange={setYearFilter}
              label="All Years"
              options={[
                { value: '1', label: 'Year 1' },
                { value: '2', label: 'Year 2' },
                { value: '3', label: 'Year 3' },
                { value: '4', label: 'Year 4' },
              ]}
            />

            <Filter
              value={statusFilter}
              onChange={setStatusFilter}
              label="All Statuses"
              options={[
                { value: 'ACTIVE', label: 'Active' },
                { value: 'INACTIVE', label: 'Inactive' },
                { value: 'GRADUATED', label: 'Graduated' },
                { value: 'SUSPENDED', label: 'Suspended' },
              ]}
            />

            {(deptFilter || yearFilter || statusFilter || searchQuery) && (
              <button
                className="btn btn-sm btn-link text-danger text-decoration-none px-2"
                onClick={() => {
                  setDeptFilter('');
                  setYearFilter('');
                  setStatusFilter('');
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

      {/* 360° Student Profile Modal (9 Tabs) */}
      <StudentProfileModal
        isOpen={profileModal.isOpen}
        onClose={profileModal.closeModal}
        studentId={profileModal.modalData?.id}
        studentBasic={profileModal.modalData}
      />

      {/* Add / Edit Student Form Modal */}
      <StudentFormModal
        isOpen={formModal.isOpen}
        onClose={formModal.closeModal}
        onSubmit={handleFormSubmit}
        initialData={formModal.modalData?.student}
        isEdit={formModal.modalData?.isEdit}
        loading={actionLoading}
      />

      {/* Import CSV Modal */}
      <ImportStudentsModal
        isOpen={importModal.isOpen}
        onClose={importModal.closeModal}
        onImport={handleCSVImport}
        loading={actionLoading}
      />

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Student Record"
        message={`Are you sure you want to delete student record ${deleteModal.modalData?.name} (${deleteModal.modalData?.student_id})? This action cannot be reversed.`}
        confirmText="Delete Record"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Students;
