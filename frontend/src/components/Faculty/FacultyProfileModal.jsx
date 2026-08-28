import React from 'react';
import Modal from '../common/Modal';
import { STATUS_BADGE_CLASSES } from '../../utils/constants';

export const FacultyProfileModal = ({ isOpen, onClose, faculty = null }) => {
  if (!faculty) return null;

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Faculty Dossier — ${faculty.name}`}
      size="lg"
    >
      <div className="p-3 mb-4 rounded-3 bg-light border d-flex align-items-center justify-content-between">
        <div className="d-flex align-items-center gap-3">
          <div
            className="rounded-circle bg-primary text-white d-flex align-items-center justify-content-center fw-bold fs-4 shadow-sm"
            style={{ width: '56px', height: '56px' }}
          >
            {faculty.name ? faculty.name[0] : 'F'}
          </div>
          <div>
            <h5 className="fw-bold text-dark mb-0">{faculty.name}</h5>
            <span className="text-muted small">
              {faculty.faculty_id} • {faculty.designation}
            </span>
          </div>
        </div>
        <span className={`badge ${STATUS_BADGE_CLASSES[faculty.status] || 'bg-success text-white'} px-3 py-2 fs-6`}>
          {faculty.status || 'ACTIVE'}
        </span>
      </div>

      <div className="row g-3 mb-4">
        <div className="col-12 col-md-6">
          <div className="p-3 bg-light rounded-3 border">
            <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Academic Profile</h6>
            <p className="small mb-2"><strong>Department:</strong> {faculty.department_detail?.name || 'Computer Science'}</p>
            <p className="small mb-2"><strong>Designation:</strong> {faculty.designation}</p>
            <p className="small mb-2"><strong>Qualification:</strong> {faculty.qualification || 'Ph.D. in Computer Science'}</p>
            <p className="small mb-0"><strong>Specialization:</strong> {faculty.specialization || 'Distributed Systems & AI'}</p>
          </div>
        </div>

        <div className="col-12 col-md-6">
          <div className="p-3 bg-light rounded-3 border">
            <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Office & Contact</h6>
            <p className="small mb-2"><strong>Email Address:</strong> {faculty.email}</p>
            <p className="small mb-2"><strong>Phone Number:</strong> {faculty.phone || '+1 (555) 019-2840'}</p>
            <p className="small mb-2"><strong>Office Room:</strong> {faculty.office_room || 'Turing Block 204'}</p>
            <p className="small mb-0"><strong>Office Hours:</strong> Mon/Wed 03:00 PM - 05:00 PM</p>
          </div>
        </div>
      </div>

      <div className="p-3 bg-light rounded-3 border">
        <h6 className="fw-bold text-dark mb-3 border-bottom pb-2">Allocated Teaching Workload</h6>
        <div className="table-responsive">
          <table className="table table-hover align-middle small mb-0 bg-white rounded">
            <thead className="table-light">
              <tr>
                <th>Course Code</th>
                <th>Course Title</th>
                <th>Assigned Batch</th>
                <th>Credits</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>CS-101</strong></td>
                <td>Data Structures & Algorithms</td>
                <td>Year 2 — Section A</td>
                <td>4 Credits</td>
                <td><span className="badge bg-success">Active</span></td>
              </tr>
              <tr>
                <td><strong>CS-204</strong></td>
                <td>Distributed Cloud Architectures</td>
                <td>Year 2 — Section B</td>
                <td>3 Credits</td>
                <td><span className="badge bg-success">Active</span></td>
              </tr>
              <tr>
                <td><strong>CS-305</strong></td>
                <td>Artificial Intelligence Foundations</td>
                <td>Year 3 — Section A</td>
                <td>4 Credits</td>
                <td><span className="badge bg-primary">Active</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </Modal>
  );
};

export default FacultyProfileModal;
