import React from 'react';

export const Pagination = ({
  currentPage = 1,
  totalPages = 1,
  onPageChange,
  totalItems = null,
}) => {
  if (totalPages <= 1) return null;

  const pages = [];
  for (let i = 1; i <= totalPages; i++) {
    // Show first, last, and window around current page
    if (i === 1 || i === totalPages || (i >= currentPage - 1 && i <= currentPage + 1)) {
      pages.push(i);
    } else if (pages[pages.length - 1] !== '...') {
      pages.push('...');
    }
  }

  return (
    <div className="d-flex flex-column flex-sm-row justify-content-between align-items-center gap-2 p-3 border-top bg-light small">
      {totalItems !== null && (
        <span className="text-muted">
          Showing Page <strong>{currentPage}</strong> of <strong>{totalPages}</strong> ({totalItems} total records)
        </span>
      )}

      <nav aria-label="Table navigation" className="ms-auto">
        <ul className="pagination pagination-sm mb-0">
          <li className={`page-item ${currentPage === 1 ? 'disabled' : ''}`}>
            <button
              className="page-link"
              onClick={() => onPageChange(currentPage - 1)}
              disabled={currentPage === 1}
              aria-label="Previous"
            >
              <i className="bi bi-chevron-left"></i>
            </button>
          </li>

          {pages.map((p, idx) => (
            <li
              key={idx}
              className={`page-item ${p === currentPage ? 'active' : ''} ${p === '...' ? 'disabled' : ''}`}
            >
              {p === '...' ? (
                <span className="page-link">...</span>
              ) : (
                <button className="page-link" onClick={() => onPageChange(p)}>
                  {p}
                </button>
              )}
            </li>
          ))}

          <li className={`page-item ${currentPage === totalPages ? 'disabled' : ''}`}>
            <button
              className="page-link"
              onClick={() => onPageChange(currentPage + 1)}
              disabled={currentPage === totalPages}
              aria-label="Next"
            >
              <i className="bi bi-chevron-right"></i>
            </button>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Pagination;
