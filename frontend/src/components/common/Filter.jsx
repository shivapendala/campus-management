import React from 'react';

export const Filter = ({
  options = [],
  value = '',
  onChange,
  label = 'All',
  className = '',
}) => {
  return (
    <div className={`d-flex align-items-center gap-2 ${className}`}>
      <select
        className="form-select form-select-sm"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        style={{ width: 'auto', minWidth: '140px' }}
      >
        <option value="">{label}</option>
        {options.map((opt, idx) => (
          <option key={idx} value={opt.value || opt}>
            {opt.label || opt}
          </option>
        ))}
      </select>
    </div>
  );
};

export default Filter;
