import React from 'react';
import Modal from './Modal';

export const ConfirmationDialog = ({
  isOpen,
  onClose,
  onConfirm,
  title = 'Confirm Action',
  message = 'Are you sure you want to proceed with this action? This operation cannot be undone.',
  confirmText = 'Confirm',
  cancelText = 'Cancel',
  confirmVariant = 'danger', // danger, primary, warning
  loading = false,
}) => {
  const footer = (
    <div className="d-flex justify-content-end gap-2 w-100">
      <button
        type="button"
        disabled={loading}
        className="btn btn-light btn-sm px-3"
        onClick={onClose}
      >
        {cancelText}
      </button>
      <button
        type="button"
        disabled={loading}
        className={`btn btn-${confirmVariant} btn-sm px-3 d-flex align-items-center gap-2`}
        onClick={onConfirm}
      >
        {loading && <span className="spinner-border spinner-border-sm" role="status"></span>}
        <span>{confirmText}</span>
      </button>
    </div>
  );

  return (
    <Modal
      isOpen={isOpen}
      onClose={onClose}
      title={title}
      size="sm"
      footer={footer}
    >
      <div className="text-secondary small">{message}</div>
    </Modal>
  );
};

export default ConfirmationDialog;
