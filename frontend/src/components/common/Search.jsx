import React from 'react';

export const Search = ({
  value = '',
  onChange,
  placeholder = 'Search records...',
  className = '',
}) => {
  return (
    <div className={`input-group ${className}`} style={{ maxWidth: '320px' }}>
      <span className="input-group-text bg-white border-end-0 text-muted">
        <i className="bi bi-search"></i>
      </span>
      <input
        type="text"
        className="form-control border-start-0 ps-0"
        placeholder={placeholder}
        value={value}
        onChange={(e) => onChange(e.target.value)}
      />
      {value && (
        <button
          className="btn btn-outline-secondary border-start-0 bg-white text-muted"
          type="button"
          onClick={() => onChange('')}
          aria-label="Clear search"
        >
          <i className="bi bi-x"></i>
        </button>
      )}
    </div>
  );
};

export default Search;
