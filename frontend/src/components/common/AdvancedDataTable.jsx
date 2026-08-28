import React, { useState, useMemo } from 'react';
import Pagination from './Pagination';
import Search from './Search';

const AdvancedDataTable = ({
  columns = [],
  data = [],
  searchPlaceholder = 'Search records...',
  pageSize = 10,
  keyField = 'id',
  onRowClick = null,
  actions = null,
  emptyMessage = 'No records found matching query.'
}) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [sortField, setSortField] = useState(null);
  const [sortOrder, setSortOrder] = useState('asc'); // 'asc' or 'desc'
  const [currentPage, setCurrentPage] = useState(1);

  const handleSort = (fieldKey) => {
    if (sortField === fieldKey) {
      setSortOrder(sortOrder === 'asc' ? 'desc' : 'asc');
    } else {
      setSortField(fieldKey);
      setSortOrder('asc');
    }
  };

  // Filter
  const filteredData = useMemo(() => {
    if (!searchTerm) return data;
    const lower = searchTerm.toLowerCase();
    return data.filter((row) =>
      columns.some((col) => {
        const val = row[col.key];
        return val !== null && val !== undefined && String(val).toLowerCase().includes(lower);
      })
    );
  }, [data, searchTerm, columns]);

  // Sort
  const sortedData = useMemo(() => {
    if (!sortField) return filteredData;
    return [...filteredData].sort((a, b) => {
      let valA = a[sortField];
      let valB = b[sortField];
      if (valA === undefined || valA === null) valA = '';
      if (valB === undefined || valB === null) valB = '';

      if (typeof valA === 'number' && typeof valB === 'number') {
        return sortOrder === 'asc' ? valA - valB : valB - valA;
      }
      return sortOrder === 'asc'
        ? String(valA).localeCompare(String(valB))
        : String(valB).localeCompare(String(valA));
    });
  }, [filteredData, sortField, sortOrder]);

  // Paginate
  const totalPages = Math.ceil(sortedData.length / pageSize) || 1;
  const paginatedData = useMemo(() => {
    const start = (currentPage - 1) * pageSize;
    return sortedData.slice(start, start + pageSize);
  }, [sortedData, currentPage, pageSize]);

  return (
    <div className="advanced-data-table-wrapper">
      <div className="d-flex justify-content-between align-items-center mb-3 flex-wrap gap-2">
        <div style={{ maxWidth: '360px', width: '100%' }}>
          <Search
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value);
              setCurrentPage(1);
            }}
            placeholder={searchPlaceholder}
          />
        </div>
        <div className="d-flex align-items-center gap-2 text-muted small">
          <span>Showing {sortedData.length} records</span>
        </div>
      </div>

      <div className="table-responsive bg-white rounded shadow-sm border">
        <table className="table table-hover align-middle mb-0">
          <thead className="table-light">
            <tr>
              {columns.map((col) => (
                <th
                  key={col.key}
                  onClick={() => col.sortable !== false && handleSort(col.key)}
                  style={{ cursor: col.sortable !== false ? 'pointer' : 'default', userSelect: 'none' }}
                  className="py-3"
                >
                  <div className="d-flex align-items-center gap-1">
                    <span>{col.label}</span>
                    {col.sortable !== false && sortField === col.key && (
                      <i className={`bi bi-arrow-${sortOrder === 'asc' ? 'up' : 'down'} text-primary small`}></i>
                    )}
                  </div>
                </th>
              ))}
              {actions && <th className="text-end py-3">Actions</th>}
            </tr>
          </thead>
          <tbody>
            {paginatedData.length === 0 ? (
              <tr>
                <td colSpan={columns.length + (actions ? 1 : 0)} className="text-center py-5 text-muted">
                  <i className="bi bi-inbox fs-2 d-block mb-2 text-secondary"></i>
                  {emptyMessage}
                </td>
              </tr>
            ) : (
              paginatedData.map((row, rIdx) => (
                <tr
                  key={row[keyField] || rIdx}
                  onClick={() => onRowClick && onRowClick(row)}
                  style={{ cursor: onRowClick ? 'pointer' : 'default' }}
                >
                  {columns.map((col) => (
                    <td key={col.key}>
                      {col.render ? col.render(row[col.key], row) : (row[col.key] !== null && row[col.key] !== undefined ? String(row[col.key]) : '-')}
                    </td>
                  ))}
                  {actions && (
                    <td className="text-end" onClick={(e) => e.stopPropagation()}>
                      {actions(row)}
                    </td>
                  )}
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>

      {totalPages > 1 && (
        <div className="d-flex justify-content-between align-items-center mt-3 flex-wrap gap-2">
          <span className="small text-muted">
            Page {currentPage} of {totalPages}
          </span>
          <Pagination
            currentPage={currentPage}
            totalPages={totalPages}
            onPageChange={(page) => setCurrentPage(page)}
          />
        </div>
      )}
    </div>
  );
};

export default AdvancedDataTable;
