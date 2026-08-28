import React from 'react';

export const Table = ({
  columns = [],
  data = [],
  loading = false,
  emptyMessage = 'No records found in database.',
  keyExtractor = (item, idx) => item.id || idx,
  className = '',
}) => {
  return (
    <div className="table-responsive">
      <table className={`table table-hover align-middle mb-0 ${className}`}>
        <thead className="table-light">
          <tr>
            {columns.map((col, idx) => (
              <th
                key={idx}
                scope="col"
                className={`py-3 px-3 text-secondary text-uppercase fw-bold small ${col.className || ''}`}
                style={{ fontSize: '11px', letterSpacing: '0.5px' }}
              >
                {col.header}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {loading ? (
            <tr>
              <td colSpan={columns.length} className="text-center py-5">
                <div className="spinner-border spinner-border-sm text-primary me-2" role="status"></div>
                <span className="text-muted small">Loading records...</span>
              </td>
            </tr>
          ) : data.length === 0 ? (
            <tr>
              <td colSpan={columns.length} className="text-center py-5 text-muted small">
                <i className="bi bi-inbox fs-3 d-block mb-2 text-secondary opacity-50"></i>
                {emptyMessage}
              </td>
            </tr>
          ) : (
            data.map((item, rowIdx) => (
              <tr key={keyExtractor(item, rowIdx)}>
                {columns.map((col, colIdx) => (
                  <td key={colIdx} className={`py-3 px-3 ${col.cellClassName || ''}`}>
                    {col.render ? col.render(item, rowIdx) : item[col.accessor]}
                  </td>
                ))}
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
};

export default Table;
