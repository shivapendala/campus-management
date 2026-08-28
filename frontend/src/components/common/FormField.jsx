import React from 'react';

export const FormField = ({
  label,
  name,
  type = 'text',
  value,
  onChange,
  error = '',
  placeholder = '',
  required = false,
  options = [], // for select type
  rows = 3, // for textarea type
  helpText = '',
  disabled = false,
  className = '',
}) => {
  return (
    <div className={`mb-3 ${className}`}>
      {label && (
        <label className="form-label small fw-semibold text-secondary mb-1">
          {label} {required && <span className="text-danger">*</span>}
        </label>
      )}

      {type === 'select' ? (
        <select
          name={name}
          value={value}
          onChange={onChange}
          disabled={disabled}
          required={required}
          className={`form-select ${error ? 'is-invalid' : ''}`}
        >
          {placeholder && <option value="">{placeholder}</option>}
          {options.map((opt, idx) => (
            <option key={idx} value={opt.value !== undefined ? opt.value : opt}>
              {opt.label !== undefined ? opt.label : opt}
            </option>
          ))}
        </select>
      ) : type === 'textarea' ? (
        <textarea
          name={name}
          value={value}
          onChange={onChange}
          rows={rows}
          placeholder={placeholder}
          disabled={disabled}
          required={required}
          className={`form-control ${error ? 'is-invalid' : ''}`}
        ></textarea>
      ) : (
        <input
          type={type}
          name={name}
          value={value}
          onChange={onChange}
          placeholder={placeholder}
          disabled={disabled}
          required={required}
          className={`form-control ${error ? 'is-invalid' : ''}`}
        />
      )}

      {helpText && !error && <small className="text-muted d-block mt-1">{helpText}</small>}
      {error && <div className="invalid-feedback d-block small">{error}</div>}
    </div>
  );
};

export default FormField;
