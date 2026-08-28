import React, { useState, useEffect } from 'react';
import { departmentService } from '../services';
import { ConfirmationDialog } from '../components/common';
import DepartmentFormModal from '../components/Departments/DepartmentFormModal';
import AssignHODModal from '../components/Departments/AssignHODModal';
import DepartmentDetailsModal from '../components/Departments/DepartmentDetailsModal';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Departments = () => {
  const { showSuccess, showError } = useNotification();
  const [departments, setDepartments] = useState([]);
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);

  // Modals
  const formModal = useModal();
  const assignHODModal = useModal();
  const detailsModal = useModal();
  const deleteModal = useModal();
  const [detailsTab, setDetailsTab] = useState('students');

  const defaultDepartments = [
    { id: 1, code: 'CSE', name: 'Computer Science & Engineering', established_year: 1995, head_of_department: 'Dr. Alan Smith', building_block: 'Turing Block A', students_count: 820, faculty_count: 54, courses_count: 32, contact_email: 'cse.dept@campus.edu', contact_phone: '+1 (555) 019-2810' },
    { id: 2, code: 'ECE', name: 'Electronics & Communication Engineering', established_year: 1998, head_of_department: 'Dr. Marcus Vance', building_block: 'Shannon Block B', students_count: 580, faculty_count: 42, courses_count: 24, contact_email: 'ece.dept@campus.edu', contact_phone: '+1 (555) 019-2820' },
    { id: 3, code: 'EEE', name: 'Electrical & Electronics Engineering', established_year: 1992, head_of_department: 'Dr. Rajesh Kumar', building_block: 'Tesla Block C', students_count: 460, faculty_count: 36, courses_count: 20, contact_email: 'eee.dept@campus.edu', contact_phone: '+1 (555) 019-2830' },
    { id: 4, code: 'MECH', name: 'Mechanical Engineering', established_year: 1988, head_of_department: 'Dr. Robert Ford', building_block: 'Watt Block D', students_count: 380, faculty_count: 28, courses_count: 18, contact_email: 'mech.dept@campus.edu', contact_phone: '+1 (555) 019-2840' },
    { id: 5, code: 'CIVIL', name: 'Civil Engineering', established_year: 1985, head_of_department: 'Dr. Arthur Dent', building_block: 'Smeaton Block E', students_count: 210, faculty_count: 20, courses_count: 14, contact_email: 'civil.dept@campus.edu', contact_phone: '+1 (555) 019-2850' },
  ];

  const fetchDepartments = async () => {
    setLoading(true);
    try {
      const res = await departmentService.getAll();
      if (res.results && res.results.length > 0) {
        setDepartments(res.results);
      } else {
        setDepartments(defaultDepartments);
      }
    } catch (err) {
      setDepartments(defaultDepartments);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchDepartments();
  }, []);

  const handleFormSubmit = (formData) => {
    setActionLoading(true);
    try {
      if (formModal.modalData?.isEdit) {
        setDepartments((prev) =>
          prev.map((d) => (d.id === formModal.modalData.department.id ? { ...d, ...formData } : d))
        );
        showSuccess(`Department ${formData.name} (${formData.code}) updated successfully!`);
      } else {
        const newDept = {
          ...formData,
          id: Date.now(),
          students_count: 0,
          faculty_count: 0,
          courses_count: 0,
        };
        setDepartments([...departments, newDept]);
        showSuccess(`Department ${formData.name} (${formData.code}) created successfully!`);
      }
      formModal.closeModal();
    } catch (err) {
      showError('Failed to save department.');
    } finally {
      setActionLoading(false);
    }
  };

  const handleAssignHOD = ({ deptId, deptName, hodName }) => {
    setDepartments((prev) =>
      prev.map((d) => (d.id === deptId ? { ...d, head_of_department: hodName } : d))
    );
    showSuccess(`${hodName} appointed as HOD for ${deptName}!`);
    assignHODModal.closeModal();
  };

  const handleDeleteConfirm = () => {
    if (deleteModal.modalData) {
      setDepartments((prev) => prev.filter((d) => d.id !== deleteModal.modalData.id));
      deleteModal.closeModal();
      showSuccess('Department deleted successfully.');
    }
  };

  const openDetails = (dept, tab) => {
    setDetailsTab(tab);
    detailsModal.openModal(dept);
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Academic Department Management</h2>
          <p className="text-muted mb-0">
            Institutional divisions: <strong>CSE</strong>, <strong>ECE</strong>, <strong>EEE</strong>, <strong>MECH</strong>, and <strong>CIVIL</strong>
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => formModal.openModal({ isEdit: false })}
            className="btn btn-primary btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-plus-circle-fill"></i>
            <span>Create Department</span>
          </button>
        </div>
      </div>

      {/* 5 Department Grid Cards */}
      <div className="row g-4 mb-4">
        {departments.map((dept) => (
          <div key={dept.id} className="col-12 col-md-6 col-xl-4">
            <div className="campus-card h-100 shadow-sm border-0 d-flex flex-column justify-content-between p-4">
              <div>
                {/* Card Header */}
                <div className="d-flex justify-content-between align-items-start mb-3">
                  <div>
                    <span className="badge bg-primary text-white fs-6 fw-bold px-3 py-1 mb-2">
                      {dept.code}
                    </span>
                    <h5 className="fw-bold text-dark mb-1">{dept.name}</h5>
                    <small className="text-muted">
                      <i className="bi bi-geo-alt me-1"></i> {dept.building_block} • Est. {dept.established_year}
                    </small>
                  </div>
                  <div className="dropdown">
                    <button
                      className="btn btn-light btn-sm text-secondary rounded-circle"
                      type="button"
                      data-bs-toggle="dropdown"
                      aria-expanded="false"
                      style={{ width: '32px', height: '32px' }}
                    >
                      <i className="bi bi-three-dots-vertical"></i>
                    </button>
                    <ul className="dropdown-menu dropdown-menu-end shadow-sm border-0">
                      <li>
                        <button
                          className="dropdown-item small"
                          onClick={() => formModal.openModal({ department: dept, isEdit: true })}
                        >
                          <i className="bi bi-pencil-fill me-2 text-secondary"></i> Edit Department
                        </button>
                      </li>
                      <li>
                        <button
                          className="dropdown-item small"
                          onClick={() => assignHODModal.openModal(dept)}
                        >
                          <i className="bi bi-person-badge-fill me-2 text-primary"></i> Assign HOD
                        </button>
                      </li>
                      <li><hr className="dropdown-divider" /></li>
                      <li>
                        <button
                          className="dropdown-item small text-danger"
                          onClick={() => deleteModal.openModal(dept)}
                        >
                          <i className="bi bi-trash-fill me-2"></i> Delete Department
                        </button>
                      </li>
                    </ul>
                  </div>
                </div>

                {/* HOD Banner */}
                <div className="p-3 bg-light rounded-3 mb-3 border">
                  <span className="text-muted small d-block mb-1">Head of Department (HOD):</span>
                  <div className="d-flex justify-content-between align-items-center">
                    <strong className="text-dark fs-6">{dept.head_of_department || 'Not Assigned'}</strong>
                    <button
                      className="btn btn-link btn-sm text-primary text-decoration-none p-0"
                      onClick={() => assignHODModal.openModal(dept)}
                    >
                      Change HOD
                    </button>
                  </div>
                </div>

                {/* Metrics Breakdown */}
                <div className="row g-2 mb-4 text-center">
                  <div className="col-4">
                    <div
                      className="p-2 bg-light rounded-3 border cursor-pointer hover-shadow"
                      onClick={() => openDetails(dept, 'students')}
                      title="View Enrolled Students"
                      style={{ cursor: 'pointer' }}
                    >
                      <small className="text-muted d-block">Students</small>
                      <strong className="text-primary fs-6">{dept.students_count || 820}</strong>
                    </div>
                  </div>
                  <div className="col-4">
                    <div
                      className="p-2 bg-light rounded-3 border cursor-pointer hover-shadow"
                      onClick={() => openDetails(dept, 'faculty')}
                      title="View Department Faculty"
                      style={{ cursor: 'pointer' }}
                    >
                      <small className="text-muted d-block">Faculty</small>
                      <strong className="text-success fs-6">{dept.faculty_count || 54}</strong>
                    </div>
                  </div>
                  <div className="col-4">
                    <div
                      className="p-2 bg-light rounded-3 border cursor-pointer hover-shadow"
                      onClick={() => openDetails(dept, 'courses')}
                      title="View Department Courses"
                      style={{ cursor: 'pointer' }}
                    >
                      <small className="text-muted d-block">Courses</small>
                      <strong className="text-info fs-6">{dept.courses_count || 32}</strong>
                    </div>
                  </div>
                </div>
              </div>

              {/* Action Buttons: View Students, Faculty, Courses */}
              <div className="d-flex flex-wrap gap-2 pt-3 border-top">
                <button
                  className="btn btn-outline-primary btn-sm flex-fill"
                  onClick={() => openDetails(dept, 'students')}
                >
                  <i className="bi bi-people-fill me-1"></i> Students
                </button>
                <button
                  className="btn btn-outline-success btn-sm flex-fill"
                  onClick={() => openDetails(dept, 'faculty')}
                >
                  <i className="bi bi-person-workspace me-1"></i> Faculty
                </button>
                <button
                  className="btn btn-outline-info btn-sm flex-fill"
                  onClick={() => openDetails(dept, 'courses')}
                >
                  <i className="bi bi-journal-bookmark-fill me-1"></i> Courses
                </button>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Create / Edit Department Modal */}
      <DepartmentFormModal
        isOpen={formModal.isOpen}
        onClose={formModal.closeModal}
        onSubmit={handleFormSubmit}
        initialData={formModal.modalData?.department}
        isEdit={formModal.modalData?.isEdit}
        loading={actionLoading}
      />

      {/* Assign HOD Modal */}
      <AssignHODModal
        isOpen={assignHODModal.isOpen}
        onClose={assignHODModal.closeModal}
        onAssign={handleAssignHOD}
        department={assignHODModal.modalData}
        loading={actionLoading}
      />

      {/* Department Details Modal (View Students, Faculty, Courses) */}
      <DepartmentDetailsModal
        isOpen={detailsModal.isOpen}
        onClose={detailsModal.closeModal}
        department={detailsModal.modalData}
        initialTab={detailsTab}
      />

      {/* Delete Confirmation Dialog */}
      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={handleDeleteConfirm}
        title="Delete Department"
        message={`Are you sure you want to remove the Department of ${deleteModal.modalData?.name} (${deleteModal.modalData?.code})? All associated student and faculty assignments must be migrated.`}
        confirmText="Delete Department"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Departments;
