import React from 'react';
import Modal from '../common/Modal';
import StatusBadge from '../common/StatusBadge';

const FacultyWorkloadModal = ({ isOpen, onClose, faculty }) => {
  if (!faculty) return null;

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="AICTE Teaching Workload Compliance" size="lg">
      <div className="p-3">
        <div className="row g-3 mb-4">
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Target Weekly Hours</span>
              <strong className="h4 text-dark mb-0">14.0 hrs</strong>
            </div>
          </div>
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Actual Effective Load</span>
              <strong className="h4 text-primary mb-0">14.5 hrs</strong>
            </div>
          </div>
          <div className="col-4">
            <div className="p-3 bg-light rounded text-center">
              <span className="text-muted small d-block">Workload Status</span>
              <div className="mt-1"><StatusBadge status="OPTIMAL" size="small" /></div>
            </div>
          </div>
        </div>

        <h6 className="fw-bold mb-2">Assigned Theory & Practical Courses</h6>
        <div className="table-responsive mb-4">
          <table className="table table-sm table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>Course</th>
                <th>Type</th>
                <th>Batches</th>
                <th>Lecture Hrs</th>
                <th>Lab Hrs</th>
                <th>Effective Load</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>CS301: DBMS</td>
                <td>Theory</td>
                <td>2 Batches</td>
                <td>6 hrs</td>
                <td>0 hrs</td>
                <td className="fw-bold">6.0 hrs</td>
              </tr>
              <tr>
                <td>CS302: DBMS Lab</td>
                <td>Practical</td>
                <td>3 Batches</td>
                <td>0 hrs</td>
                <td>6 hrs</td>
                <td className="fw-bold">4.5 hrs</td>
              </tr>
              <tr>
                <td>CS701: Cloud Computing</td>
                <td>Elective</td>
                <td>1 Batch</td>
                <td>4 hrs</td>
                <td>0 hrs</td>
                <td className="fw-bold">4.0 hrs</td>
              </tr>
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

export default FacultyWorkloadModal;
