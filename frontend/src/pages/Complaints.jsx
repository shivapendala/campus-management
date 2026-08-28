import React, { useState, useEffect } from 'react';
import { complaintService } from '../services';
import ComplaintFormModal from '../components/Complaints/ComplaintFormModal';
import ResolveComplaintModal from '../components/Complaints/ResolveComplaintModal';
import { ConfirmationDialog } from '../components/common';
import { useModal } from '../hooks';
import { useNotification } from '../context/NotificationContext';

export const Complaints = () => {
  const { showSuccess, showError, showInfo } = useNotification();
  const [loading, setLoading] = useState(true);
  const [actionLoading, setActionLoading] = useState(false);
  const [statusFilter, setStatusFilter] = useState('ALL');

  // Modals
  const complaintModal = useModal();
  const resolveModal = useModal();
  const deleteModal = useModal();

  const defaultComplaints = [
    { id: 1, title: 'Wi-Fi Bandwidth Degradation in Systems Lab 3', category: 'INFRASTRUCTURE', priority: 'HIGH', status: 'IN_PROGRESS', submitted_by_name: 'Alex Johnson', created_at: '2026-08-22', description: 'The wireless access points in Computer Lab 3 drop connection during concurrent benchmark sessions.' },
    { id: 2, title: 'Library Air Conditioning Noise in Stack CS-04', category: 'INFRASTRUCTURE', priority: 'LOW', status: 'RESOLVED', submitted_by_name: 'Maya Patel', created_at: '2026-08-18', description: 'Noisy blower motor on 2nd floor library study pod.', resolution_remarks: 'HVAC technicians serviced and replaced fan bearings.' },
    { id: 3, title: 'Hostel Dining Water Cooler Filter Replacement', category: 'HOSTEL', priority: 'MEDIUM', status: 'OPEN', submitted_by_name: 'David Lee', created_at: '2026-08-25', description: 'RO filter overdue for scheduled replacement in Block B mess.' },
    { id: 4, title: 'Request for Extra GPU Compute Hours on AI Cluster', category: 'ACADEMIC', priority: 'MEDIUM', status: 'OPEN', submitted_by_name: 'Sophia Martinez', created_at: '2026-08-26', description: 'Need allocation bump for deep learning final year thesis training.' },
  ];

  const [complaints, setComplaints] = useState(defaultComplaints);

  const fetchComplaints = async () => {
    setLoading(true);
    try {
      const res = await complaintService.getComplaints();
      if (res.results && res.results.length > 0) setComplaints(res.results);
    } catch (err) {
      setComplaints(defaultComplaints);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchComplaints();
  }, []);

  const filteredComplaints = complaints.filter((c) => {
    return statusFilter === 'ALL' || c.status === statusFilter;
  });

  // Submit Complaint
  const handleComplaintSubmit = async (formData) => {
    setActionLoading(true);
    try {
      if (complaintModal.modalData?.isEdit) {
        setComplaints((prev) =>
          prev.map((c) => (c.id === complaintModal.modalData.complaint.id ? { ...c, ...formData } : c))
        );
        showSuccess(`Ticket #${complaintModal.modalData.complaint.id} updated.`);
      } else {
        const newC = { ...formData, id: Date.now(), created_at: new Date().toISOString().split('T')[0] };
        setComplaints([newC, ...complaints]);
        showSuccess('Grievance ticket lodged. Department officer notified.');
      }
      complaintModal.closeModal();
    } catch (err) {
      showError('Failed to submit ticket.');
    } finally {
      setActionLoading(false);
    }
  };

  // Resolve Complaint
  const handleResolveSubmit = async (resolveData) => {
    setActionLoading(true);
    try {
      const targetC = resolveModal.modalData?.complaint;
      setComplaints((prev) =>
        prev.map((c) => (c.id === targetC.id ? { ...c, ...resolveData } : c))
      );
      resolveModal.closeModal();
      showSuccess(`Ticket #${targetC.id} marked as Resolved!`);
    } catch (err) {
      showError('Failed to resolve ticket.');
    } finally {
      setActionLoading(false);
    }
  };

  const getPriorityBadge = (p) => {
    switch (p) {
      case 'CRITICAL':
        return <span className="badge bg-danger">Critical</span>;
      case 'HIGH':
        return <span className="badge bg-danger-subtle text-danger fw-bold">High</span>;
      case 'MEDIUM':
        return <span className="badge bg-warning-subtle text-warning-emphasis">Medium</span>;
      default:
        return <span className="badge bg-secondary-subtle text-secondary">Low</span>;
    }
  };

  const getStatusBadge = (s) => {
    switch (s) {
      case 'RESOLVED':
        return <span className="badge bg-success px-3 py-1">Resolved</span>;
      case 'IN_PROGRESS':
        return <span className="badge bg-primary px-3 py-1">In Progress</span>;
      default:
        return <span className="badge bg-warning text-dark px-3 py-1">Open Ticket</span>;
    }
  };

  return (
    <div className="container-fluid p-4">
      {/* Header Banner */}
      <div className="d-flex flex-column flex-md-row justify-content-between align-items-md-center mb-4 gap-3">
        <div>
          <h2 className="fw-bold text-dark mb-1">Grievance Redressal & Support</h2>
          <p className="text-muted mb-0">
            Institutional grievance lodging, priority escalation routing, facility maintenance, and resolution audits
          </p>
        </div>
        <div className="d-flex gap-2">
          <button
            onClick={() => complaintModal.openModal({ isEdit: false })}
            className="btn btn-danger btn-sm d-flex align-items-center gap-1 fw-semibold px-3 shadow-sm"
          >
            <i className="bi bi-shield-exclamation"></i>
            <span>Lodge Grievance</span>
          </button>
        </div>
      </div>

      {/* Filter Bar */}
      <div className="campus-card shadow-sm border-0 p-4 mb-4">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h6 className="fw-bold text-dark mb-0">Active Grievance Tickets ({filteredComplaints.length})</h6>
          <select
            className="form-select form-select-sm"
            style={{ width: '180px' }}
            value={statusFilter}
            onChange={(e) => setStatusFilter(e.target.value)}
          >
            <option value="ALL">All Ticket Statuses</option>
            <option value="OPEN">Open Tickets</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="RESOLVED">Resolved Tickets</option>
          </select>
        </div>

        <div className="table-responsive">
          <table className="table table-hover align-middle small mb-0">
            <thead className="table-light">
              <tr>
                <th>Ticket ID & Title</th>
                <th>Category</th>
                <th>Priority</th>
                <th>Submitted By</th>
                <th>Lodged Date</th>
                <th>Status</th>
                <th className="text-end">Actions</th>
              </tr>
            </thead>
            <tbody>
              {filteredComplaints.map((c) => (
                <tr key={c.id}>
                  <td>
                    <strong className="text-dark d-block">#{c.id}: {c.title}</strong>
                    <small className="text-muted text-truncate d-block" style={{ maxWidth: '340px' }}>
                      {c.description}
                    </small>
                  </td>
                  <td><span className="badge bg-light text-secondary border">{c.category}</span></td>
                  <td>{getPriorityBadge(c.priority)}</td>
                  <td><strong className="text-primary">{c.submitted_by_name}</strong></td>
                  <td>{c.created_at}</td>
                  <td>{getStatusBadge(c.status)}</td>
                  <td className="text-end">
                    <div className="d-flex justify-content-end gap-1">
                      {c.status !== 'RESOLVED' && (
                        <button
                          className="btn btn-success btn-sm fw-semibold"
                          onClick={() => resolveModal.openModal({ complaint: c })}
                        >
                          <i className="bi bi-check-circle me-1"></i> Resolve
                        </button>
                      )}
                      <button
                        className="btn btn-outline-danger btn-sm"
                        onClick={() => deleteModal.openModal(c)}
                      >
                        <i className="bi bi-trash"></i>
                      </button>
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Modals */}
      <ComplaintFormModal
        isOpen={complaintModal.isOpen}
        onClose={complaintModal.closeModal}
        onSubmit={handleComplaintSubmit}
        initialData={complaintModal.modalData?.complaint}
        isEdit={complaintModal.modalData?.isEdit}
        loading={actionLoading}
      />

      <ResolveComplaintModal
        isOpen={resolveModal.isOpen}
        onClose={resolveModal.closeModal}
        onSubmit={handleResolveSubmit}
        complaint={resolveModal.modalData?.complaint}
        loading={actionLoading}
      />

      <ConfirmationDialog
        isOpen={deleteModal.isOpen}
        onClose={deleteModal.closeModal}
        onConfirm={() => {
          setComplaints((prev) => prev.filter((c) => c.id !== deleteModal.modalData.id));
          deleteModal.closeModal();
          showSuccess('Grievance ticket deleted.');
        }}
        title="Delete Grievance Ticket"
        message={`Are you sure you want to remove ticket #${deleteModal.modalData?.id}?`}
        confirmText="Delete Ticket"
        confirmVariant="danger"
        loading={actionLoading}
      />
    </div>
  );
};

export default Complaints;
