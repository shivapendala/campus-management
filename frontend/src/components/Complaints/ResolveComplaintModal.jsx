import React, { useState } from 'react';
import Modal from '../common/Modal';
import FormField from '../common/FormField';

export const ResolveComplaintModal = ({
  isOpen,
  onClose,
  onSubmit,
  complaint = null,
  loading = false,
}) => {
  const [resolutionRemarks, setResolutionRemarks] = useState('Campus IT upgraded the dual Cisco Wi-Fi 6 access points in Lab 3. Bandwidth tested at 1 Gbps with 60 active nodes.');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      resolution_remarks: resolutionRemarks,
      status: 'RESOLVED',
      resolved_at: new Date().toISOString(),
    });
  };

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={`Resolve Grievance Ticket #${complaint?.id} — ${complaint?.title || 'Complaint'}`}
      size="lg"
    >
      <form onSubmit={handleSubmit}>
        <div className="p-3 bg-light rounded-3 border mb-3">
          <div className="d-flex justify-content-between align-items-center mb-1">
            <strong className="text-dark">{complaint?.title}</strong>
            <span className="badge bg-warning text-dark">{complaint?.status}</span>
          </div>
          <p className="small text-secondary mb-0">{complaint?.description}</p>
        </div>

        <div className="mb-4">
          <FormField
            label="Resolution Actions & Official Remarks"
            type="textarea"
            rows={4}
            name="resolution_remarks"
            value={resolutionRemarks}
            onChange={(e) => setResolutionRemarks(e.target.value)}
            required
          />
        </div>

        <div className="d-flex justify-content-end gap-2 pt-3 border-top">
          <button type="button" className="btn btn-light btn-sm px-3" onClick={onClose}>
            Cancel
          </button>
          <button type="submit" disabled={loading} className="btn btn-success btn-sm px-4 fw-semibold shadow-sm">
            {loading ? 'Resolving...' : 'Mark Ticket as Resolved'}
          </button>
        </div>
      </form>
    </Modal>
  );
};

export default ResolveComplaintModal;
