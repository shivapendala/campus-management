import React from 'react';
import Modal from '../common/Modal';

const RolePermissionsModal = ({ isOpen, onClose, role = 'HOD' }) => {
  const permissions = [
    { code: 'student.view', name: 'View Student Roster', category: 'STUDENTS' },
    { code: 'faculty.assign_subject', name: 'Assign Teaching Subjects', category: 'FACULTY' },
    { code: 'exam.verify_results', name: 'Verify Semester Marks & Grade Cards', category: 'EXAMS' },
    { code: 'attendance.audit', name: 'Grant Attendance Medical Condonation', category: 'ATTENDANCE' },
    { code: 'report.generate', name: 'Export Department Accreditation Reports', category: 'REPORTS' },
  ];

  return (
    <Modal isOpen={isOpen} onClose={onClose} title={`RBAC Permission Matrix: ${role}`} size="lg">
      <div className="p-3">
        <p className="text-muted small mb-3">
          Institutional access control grants privileges according to statutory hierarchical role definitions.
        </p>

        <div className="table-responsive mb-3">
          <table className="table table-hover table-sm align-middle">
            <thead className="table-light">
              <tr>
                <th>Permission Code</th>
                <th>Privilege Name</th>
                <th>Category</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              {permissions.map((p, idx) => (
                <tr key={idx}>
                  <td><code>{p.code}</code></td>
                  <td>{p.name}</td>
                  <td><span className="badge bg-light text-dark">{p.category}</span></td>
                  <td><span className="badge bg-success-subtle text-success">Granted</span></td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <div className="text-end">
          <button className="btn btn-primary" onClick={onClose}>Close</button>
        </div>
      </div>
    </Modal>
  );
};

export default RolePermissionsModal;
