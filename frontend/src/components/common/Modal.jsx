import React from 'react';

export const Modal = ({
  isOpen,
  onClose,
  title,
  children,
  size = 'md', // sm, md, lg, xl
  footer = null,
}) => {
  if (!isOpen) return null;

  return (
    <>
      <div className="modal show d-block" tabIndex="-1" role="dialog" style={{ backgroundColor: 'rgba(15, 23, 42, 0.6)' }}>
        <div className={`modal-dialog modal-dialog-centered modal-${size}`} role="document">
          <div className="modal-content border-0 shadow-lg" style={{ borderRadius: '16px', overflow: 'hidden' }}>
            {/* Header */}
            <div className="modal-header border-bottom px-4 py-3 bg-light">
              <h5 className="modal-title fw-bold text-dark">{title}</h5>
              <button
                type="button"
                className="btn-close"
                aria-label="Close"
                onClick={onClose}
              ></button>
            </div>

            {/* Body */}
            <div className="modal-body p-4">{children}</div>

            {/* Footer */}
            {footer && (
              <div className="modal-footer border-top px-4 py-3 bg-light">
                {footer}
              </div>
            )}
          </div>
        </div>
      </div>
      <div className="modal-backdrop fade show"></div>
    </>
  );
};

export default Modal;
